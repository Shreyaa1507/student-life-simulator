# Student Life Simulator

A Python student life simulation project.

## Run

```bash
python3 student_life_simulator/main.py
```

## Study Habit File Format

Workshop files should start with `Workshops`, then use:

```text
time, collaboration, complete
```

Lecture files should start with `Lectures`, then use:

```text
time focused, distraction, distraction
```

## Grades

The final grade is calculated from attendance and learning:

```text
AF: fewer than 10 attendance points
HD: 3000 or more learning points
D: 2500 or more learning points
CR: 2000 or more learning points
P: 1500 or more learning points
F: below 1500 learning points
```

## Campus Map File Format

Campus map files use:

```text
.
# 
R
```

Unknown symbols are treated as `#`.

Use `search(campus_map, current_position)` to find a room from a starting row
and column position.

## Daily Activities File Format

Daily activity files use:

```text
hours:24
sleeping:6-8
studying:3-6
```

Use `generate_day(activities)` to create a random schedule string.

## Okta Verification

`Student.attend(activity)` uses a simulated verification code before applying
activity gains. Every third successful verification asks for the code twice.
