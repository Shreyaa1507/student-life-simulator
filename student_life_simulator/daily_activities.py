import random


def generate_activities(filepath):
    """Read daily activity ranges from a file."""
    activities = {}

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("hours:"):
                parts = line.split(":")
                activities["hours"] = int(parts[1])
            else:
                parts = line.split(":")
                activity_name = parts[0]
                hours_range = parts[1].split("-")
                min_hours = int(hours_range[0])
                max_hours = int(hours_range[1])

                activities[activity_name] = [min_hours, max_hours]

    return activities


def generate_day(activities):
    """Generate a random day schedule from activity ranges."""
    def add_activities(current_hours, schedule):
        if current_hours >= activities["hours"]:
            return schedule

        activity_names = []

        for key in activities:
            if key != "hours":
                activity_names.append(key)

        random_index = random.randint(0, len(activity_names) - 1)
        chosen_activity = activity_names[random_index]

        min_time = activities[chosen_activity][0]
        max_time = activities[chosen_activity][1]
        random_time = random.randint(min_time, max_time)

        activity_str = chosen_activity + " " + str(random_time) + "hrs"

        if schedule == "":
            new_schedule = activity_str
        else:
            new_schedule = schedule + " -> " + activity_str

        return add_activities(current_hours + random_time, new_schedule)

    return add_activities(0, "")
