import { expect, it, vi } from "vitest";

import {
  verifyNoTokenOwnedProcesses,
  type ProcessIdentityObservation,
  type ProcessOwnershipHost,
  type ProcessTableEntry,
} from "./ProcessOwnership.js";
import { ProcessOwnershipEvidenceOwner } from "./ProcessOwnershipEvidence.js";

const worker: ProcessTableEntry = {
  pid: 225534,
  parentPid: 2,
  processGroupId: 0,
  state: "I",
  command: "kworker/u12:2-events_power_efficient",
};

const native = (
  options: {
    readonly kernel?: boolean;
    readonly generation?: string;
    readonly parentPid?: number;
    readonly processGroupId?: number;
  } = {},
): ProcessIdentityObservation => ({
  state: "readable",
  identity: options.generation ?? "linux-starttime:123456",
  ...(options.kernel === false ? {} : { kernelThread: true }),
  lifecycle: { state: "observed", lifecycle: "non-zombie" },
  relation: {
    state: "observed",
    parentPid: options.parentPid ?? 2,
    processGroupId: options.processGroupId ?? 0,
  },
});

const makeFixture = (
  first: ProcessIdentityObservation,
  second: ProcessIdentityObservation = first,
  options: { readonly platform?: "linux" | "darwin" } = {},
) => {
  let observationCalls = 0;
  const runTokens = vi.fn(async (members: readonly ProcessTableEntry[]) =>
    new Map(
      members.map(({ pid }) => [
        pid,
        {
          state: "unavailable" as const,
          reason: "ESRCH: no user environment for kernel task",
        },
      ]),
    ),
  );
  const signalGroup = vi.fn();
  const host: ProcessOwnershipHost = {
    platform: options.platform ?? "linux",
    listProcesses: async () => [worker],
    environment: async () => {
      throw new Error("ESRCH");
    },
    runTokens,
    processIdentities: async (members) => {
      const observation = ++observationCalls === 1 ? first : second;
      return new Map(members.map(({ pid }) => [pid, observation]));
    },
    signalGroup,
  };
  return {
    runTokens,
    signalGroup,
    verify: () =>
      verifyNoTokenOwnedProcesses(
        "rea-owned-capture",
        host,
        undefined,
        {
          leaderPid: 100,
          processGroupId: 100,
          evidenceOwner: new ProcessOwnershipEvidenceOwner(),
        },
      ),
  };
};

it("does not confuse independently spawned Linux kworkers with owned children", async () => {
  const fixture = makeFixture(native());
  await expect(fixture.verify()).resolves.toEqual({
    cleaned: true,
    signaled: false,
  });
  expect(fixture.runTokens).not.toHaveBeenCalled();
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});

it("keeps a userspace process named kworker fail-closed without PF_KTHREAD", async () => {
  const fixture = makeFixture(native({ kernel: false }));
  await expect(fixture.verify()).resolves.toMatchObject({
    cleaned: false,
    reason: expect.stringContaining("process ownership token could not be read"),
  });
  expect(fixture.runTokens).toHaveBeenCalled();
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});

it("requires the same native start generation on both kthread reads", async () => {
  const fixture = makeFixture(
    native({ generation: "linux-starttime:1" }),
    native({ generation: "linux-starttime:2" }),
  );
  await expect(fixture.verify()).resolves.toMatchObject({
    cleaned: false,
  });
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});

it("requires PF_KTHREAD to remain observed on the second read", async () => {
  const fixture = makeFixture(native(), native({ kernel: false }));
  await expect(fixture.verify()).resolves.toMatchObject({
    cleaned: false,
  });
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});

it("does not trust PF_KTHREAD without the native kthreadd parent and group", async () => {
  const fixture = makeFixture(
    native({ parentPid: 100, processGroupId: 100 }),
  );
  await expect(fixture.verify()).resolves.toMatchObject({
    cleaned: false,
  });
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});

it("does not apply Linux native proof to a non-Linux process host", async () => {
  const fixture = makeFixture(native(), native(), { platform: "darwin" });
  await expect(fixture.verify()).resolves.toMatchObject({
    cleaned: false,
  });
  expect(fixture.signalGroup).not.toHaveBeenCalled();
});
