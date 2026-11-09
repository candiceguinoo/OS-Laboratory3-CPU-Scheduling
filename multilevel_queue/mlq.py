# Multilevel Queue Scheduling
# Queue 1: Interactive (Round Robin, Quantum = 2 ms)
# Queue 2: Batch (First Come First Serve)

from collections import deque

processes = [
    {"pid": "P1", "arrival": 0, "burst": 5, "queue": 1},
    {"pid": "P2", "arrival": 1, "burst": 4, "queue": 1},
    {"pid": "P3", "arrival": 0, "burst": 6, "queue": 2},
    {"pid": "P4", "arrival": 2, "burst": 3, "queue": 2},
    {"pid": "P5", "arrival": 3, "burst": 2, "queue": 1},
]

quantum = 2

remaining = {p["pid"]: p["burst"] for p in processes}
completion = {}
gantt = []
ready_q1 = deque()
ready_q2 = []
time = 0
completed = 0

while completed < len(processes):
    for p in processes:
        if p["arrival"] == time:
            if p["queue"] == 1:
                ready_q1.append(p["pid"])
            else:
                ready_q2.append(p["pid"])

    if ready_q1:
        pid = ready_q1.popleft()
        run_time = min(quantum, remaining[pid])

        gantt.append((pid, time, time + run_time))
        time += run_time
        remaining[pid] -= run_time

        for p in processes:
            if p["arrival"] > time - run_time and p["arrival"] <= time:
                if p["queue"] == 1 and p["pid"] not in ready_q1 and p["pid"] != pid:
                    if remaining[p["pid"]] > 0:
                        ready_q1.append(p["pid"])
                elif p["queue"] == 2 and p["pid"] not in ready_q2:
                    if remaining[p["pid"]] > 0:
                        ready_q2.append(p["pid"])

        if remaining[pid] > 0:
            ready_q1.append(pid)
        else:
            completion[pid] = time
            completed += 1

    elif ready_q2:
        pid = ready_q2.pop(0)
        run_time = remaining[pid]

        # Check for higher-priority Queue 1 arrivals
        next_q1 = [
            p["arrival"] for p in processes
            if p["queue"] == 1
            and p["arrival"] > time
            and remaining[p["pid"]] > 0
        ]

        if next_q1 and min(next_q1) < time + run_time:
            run_time = min(next_q1) - time

        gantt.append((pid, time, time + run_time))
        time += run_time
        remaining[pid] -= run_time

        if remaining[pid] > 0:
            ready_q2.insert(0, pid)
        else:
            completion[pid] = time
            completed += 1
    else:
        time += 1

print("MULTILEVEL QUEUE SCHEDULING")
print("\nGantt Chart:")
for pid, start, end in gantt:
    print(f"| {pid} ({start}-{end}) ", end="")
print("|")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    pid = p["pid"]
    ct = completion[pid]
    tat = ct - p["arrival"]
    wt = tat - p["burst"]
    print(f"{pid}\t{p['arrival']}\t{p['burst']}\t{ct}\t{tat}\t{wt}")