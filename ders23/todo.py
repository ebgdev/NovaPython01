from datetime import datetime, timedelta
from icecream import ic

all_events = {}  # Stores events with (start_time, end_time) as keys
events_by_day = {}  # Stores events grouped by date (YYYY-MM-DD)

while True:
    print("\nWelcome to the To-Do List Program.")
    print("1. See all events")
    print("2. See events for a specific day")
    print("3. Add a new event")
    print("4. Delete an event")
    print("5. Edit event details")
    print("6. Exit the program")

    in_value = input("Choose your option: ")

    if in_value == "1":
        if not all_events:
            print("No events scheduled.")
        else:
            print("\nAll Events:")
            for (start_time, end_time), event_info in all_events.items():
                print(f"Event Name: {event_info['name']}")
                print(f"Event Description: {event_info['description']}")
                print(f"Start Time: {start_time}")
                print(f"End Time: {end_time}")
                print("-----------------------------")

    elif in_value == "2":
        date_query = input("Enter the date (YYYY-MM-DD) to see events: ")

        if date_query in events_by_day:
            print(f"\nEvents on {date_query}:")
            for event in events_by_day[date_query]:
                print(f"Event Name: {event['name']}")
                print(f"Event Description: {event['description']}")
                print(f"Start Time: {event['start_time']}")
                print(f"End Time: {event['end_time']}")
                print("-----------------------------")
        else:
            print("No events found on this date.")

    elif in_value == "3":
        event_name = input("Enter the event name: ")
        event_description = input("Enter the event description: ")
        get_time = input("Enter the event start date & time (YYYY-MM-DD-HH-MM-SS): ")

        time_parts = get_time.split("-")
        if len(time_parts) != 6 or not all(part.isdigit() for part in time_parts):
            print("❌ Invalid format. Use YYYY-MM-DD-HH-MM-SS.")
            continue

        year, month, day, hour, minute, second = map(int, time_parts)
        if not (
            datetime.now().year <= year <= 2050
            and 1 <= month <= 12
            and 1 <= day <= 31
            and 0 <= hour < 24
            and 0 <= minute < 60
            and 0 <= second < 60
        ):
            print(
                "❌ Invalid date values. Check Year, month, day, hour, minute, and second."
            )
            continue

        event_duration = input("Enter event duration (in hours): ")
        if not event_duration.isdigit() or int(event_duration) <= 0:
            print("❌ Duration must be a positive integer.")
            continue

        event_start_time = datetime(year, month, day, hour, minute, second)
        event_end_time = event_start_time + timedelta(hours=int(event_duration))
        event_date = event_start_time.strftime("%Y-%m-%d")
        # ic(event_start_time, event_end_time, event_date)

        conflict = None
        for existing_start, existing_end in all_events.keys():
            if not (
                event_end_time <= existing_start or event_start_time >= existing_end
            ):
                conflict = (existing_start, existing_end)
                break

        if conflict:
            print(
                f"⚠️ Conflict: You already have an event '{all_events[conflict]['name']}' at this time."
            )
            replace = (
                input("Do you want to replace the existing event? (yes/no): ")
                .strip()
                .lower()
            )
            if replace != "yes":
                print("❌ Event not added due to conflict.")
                continue
            del all_events[conflict]

        all_events[(event_start_time, event_end_time)] = {
            "name": event_name,
            "description": event_description,
        }
        events_by_day.setdefault(event_date, []).append(
            {
                "name": event_name,
                "description": event_description,
                "start_time": event_start_time,
                "end_time": event_end_time,
            }
        )
        ic(all_events)
        ic(events_by_day)
        print("✅ Event added successfully.")

    elif in_value == "4":
        event_to_delete = input("Enter the event name to delete: ")
        found = False
        for key in list(all_events):
            if all_events[key]["name"] == event_to_delete:
                del all_events[key]
                event_date = key[0].strftime("%Y-%m-%d")

        # Remove event from events_by_day
        if event_date in events_by_day:
            updated_events = []
            for event in events_by_day[event_date]:
                if event["name"] != event_to_delete:
                    updated_events.append(event)
            events_by_day[event_date] = updated_events

            print("✅ Event deleted successfully.")
            break

        else:
            print("❌ Event not found.")

    elif in_value == "5":
        event_to_edit = input("Enter the event name to edit: ")
        for key, event_info in all_events.items():
            if event_info["name"] == event_to_edit:
                new_name = (
                    input("Enter the new name (leave blank to keep the same): ")
                    or event_info["name"]
                )
                new_description = (
                    input("Enter the new description (leave blank to keep the same): ")
                    or event_info["description"]
                )
                all_events[key]["name"] = new_name
                all_events[key]["description"] = new_description
                for event in events_by_day[key[0].strftime("%Y-%m-%d")]:
                    ic(events_by_day[key[0].strftime("%Y-%m-%d")])
                    if event["name"] == event_to_edit:
                        event["name"] = new_name
                        event["description"] = new_description
                print("✅ Event updated successfully.")
                break
        else:
            print("❌ Event not found.")

    elif in_value == "6":
        print("Bye!")
        break

    else:
        print("Invalid option. Please try again.")


# -------------------------------------------------------------

# note : why we do use setdefault() method


# events_by_day = {}  # Empty dictionary

# event_date = "2025-03-10"

# # Trying to append directly without checking if the key exists
# events_by_day[event_date].append(
#     {
#         "name": "Meeting",
#         "description": "Project discussion",
#         "start_time": "2025-03-10 10:00:00",
#         "end_time": "2025-03-10 11:00:00",
#     }
# )


# output : KeyError

# ------------------------------

# but the perferd way is :

# events_by_day = {}

# event_date = "2025-03-10"

# # Using setdefault to avoid the KeyError
# events_by_day.setdefault(event_date, []).append(
#     {
#         "name": "Meeting",
#         "description": "Project discussion",
#         "start_time": "2025-03-10 10:00:00",
#         "end_time": "2025-03-10 11:00:00",
#     }
# )

# print(events_by_day)

# # output:

# {
#     "2025-03-10": [
#         {
#             "name": "Meeting",
#             "description": "Project discussion",
#             "start_time": "2025-03-10 10:00:00",
#             "end_time": "2025-03-10 11:00:00",
#         }
#     ]
# }


# ----------------------------------------------------------

# events_by_day = {
#     "2025-03-04": [
#         {
#             "name": "Meeting",
#             "description": "Project discussion",
#             "start_time": datetime(2025, 3, 4, 10, 0, 0),
#             "end_time": datetime(2025, 3, 4, 11, 0, 0),
#             # ...
#         }
#     ]
# }


# events_by_day[key[0].strftime("%Y-%m-%d")] --> events_by_day["2025-03-04"]


# -----------------------------------------------

# the general shape of the data we store as 2 dicts:

# all_events = {
#     (datetime(2025, 3, 4, 10, 0, 0), datetime(2025, 3, 4, 11, 0, 0)): {
#         "name": "Meeting",
#         "description": "Project discussion",
#     }
# }
# events_by_day = {
#     "2025-03-04": [
#         {
#             "name": "Meeting",
#             "description": "Project discussion",
#             "start_time": datetime(2025, 3, 4, 10, 0, 0),
#             "end_time": datetime(2025, 3, 4, 11, 0, 0),
#         }
#     ]
# }
