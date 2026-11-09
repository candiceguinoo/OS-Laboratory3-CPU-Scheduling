# Earliest Deadline First (EDF) Scheduling

tasks = [
    {"name": "T1", "execution": 1, "period": 4, "deadline": 4},
    {"name": "T2", "execution": 1, "period": 5, "deadline": 5},
    {"name": "T3", "execution": 2, "period": 10, "deadline": 10},
]

simulation_time = 20

jobs = []

for task in tasks:
    release = 0

    while release < simulation_time:
        jobs.append({
            "task": task["name"],
            "release": release,
            "remaining": task["execution"],
            "deadline": release + task["deadline"]
        })
        release += task["period"]

time = 0
gantt = []
missed_deadlines = []

while time < simulation_time:
    ready_jobs = [
        job for job in jobs
        if job["release"] <= time
        and job["remaining"] > 0
    ]

    if ready_jobs:
        # Earliest absolute deadline gets highest priority
        current = min(
            ready_jobs,
            key=lambda job: (
                job["deadline"],
                job["release"],
                job["task"]
            )
        )

        gantt.append((current["task"], time, time + 1))
        current["remaining"] -= 1

    else:
        gantt.append(("IDLE", time, time + 1))

    time += 1

# Check deadline compliance
for job in jobs:
    if job["remaining"] > 0 and job["deadline"] <= simulation_time:
        missed_deadlines.append(job)

# Calculate CPU utilization
total_execution = sum(
    task["execution"] * (simulation_time // task["period"])
    for task in tasks
)

utilization = (total_execution / simulation_time) * 100

print("EARLIEST DEADLINE FIRST SCHEDULING")
print("\nGantt Chart:")

for task, start, end in gantt:
    print(f"| {task} ({start}-{end}) ", end="")
print("|")

print(f"\nSimulation Time: {simulation_time} ms")
print(f"CPU Utilization: {utilization:.2f}%")

print("\nDeadline Analysis:")

if not missed_deadlines:
    print("All task instances met their deadlines.")
else:
    for job in missed_deadlines:
        print(
            f"{job['task']} missed deadline at {job['deadline']} ms"
        )