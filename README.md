# OS Laboratory Activity 3

## Multilevel Queue and Real-Time CPU Scheduling

## Student Information

- **Name:** Candice S. Guinoo
- **Course and Section:** BS Computer Applications | B186
- **Instructor:** Maria Fe P. Bahinting
- **Date Submitted:** November 9, 2026

## I. Introduction

This activity focuses on implementing Multilevel Queue (MLQ), Rate Monotonic Scheduling (RMS), and Earliest Deadline First (EDF) using Python. These algorithms help manage processes and tasks based on their priorities and scheduling requirements.

## II. Objectives

- Implement Multilevel Queue Scheduling using Round Robin and FCFS.
- Implement Rate Monotonic Scheduling.
- Implement Earliest Deadline First Scheduling.
- Generate Gantt charts to show the execution order.
- Calculate CPU utilization and analyze deadline compliance.
- Use GitHub to manage and submit the project.

## III. Scheduling Algorithms

### 1. Multilevel Queue (MLQ)

MLQ separates processes into different queues based on their type. Queue 1 uses Round Robin with a time quantum of 2 ms, while Queue 2 uses First Come First Serve (FCFS).

Queue 1 has a higher priority than Queue 2.

### 2. Rate Monotonic Scheduling (RMS)

RMS is a fixed-priority scheduling algorithm. The task with the shorter period gets a higher priority.

### 3. Earliest Deadline First (EDF)

EDF is a dynamic-priority scheduling algorithm. The task with the earliest absolute deadline gets the CPU first.

## IV. Program Implementation

The project contains three Python programs:

- `multilevel_queue/mlq.py` – Implements Multilevel Queue Scheduling.
- `real_time_scheduling/rms.py` – Implements Rate Monotonic Scheduling.
- `real_time_scheduling/edf.py` – Implements Earliest Deadline First Scheduling.

The programs use Python to simulate scheduling and display Gantt charts and scheduling results.



lculate CPU utilization and check if tasks meet their deadlines. Overall, this activity helped me understand how scheduling algorithms manage processes and tasks in an operating system.
