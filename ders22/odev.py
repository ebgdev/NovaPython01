from datetime import datetime, timedelta
from icecream import ic

all_events = {}  # Stores events with (start_time, end_time) as keys
events_by_day = {}  # Stores events grouped by date (YYYY-MM-DD)

while True:
    print("\nWelcome to the To-Do List Program.")
    print("1. See all events")
    print("2. See events for a specific day")
    print("3. Exit the program")
    print("4. Add a new event")

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
        print("Bye!")
        break

    elif in_value == "4":
        event_name = input("Enter the event name: ")
        event_description = input("Enter the event description: ")
        get_time = input("Enter the event start date & time (YYYY-MM-DD-HH-MM-SS): ")

        # Validate date format
        time_parts = get_time.split("-")
        if len(time_parts) != 6 or not all(part.isdigit() for part in time_parts):
            print("❌ Invalid format. Use YYYY-MM-DD-HH-MM-SS.")
            continue

        year, month, day, hour, minute, second = map(int, time_parts)

        # Ensure valid date values
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

        # Validate duration
        if not event_duration.isdigit() or int(event_duration) <= 0:
            print("❌ Duration must be a positive integer.")
            continue

        # Convert inputs to datetime and timedelta
        event_start_time = datetime(year, month, day, hour, minute, second)
        event_end_time = event_start_time + timedelta(hours=int(event_duration))
        event_date = event_start_time.strftime("%Y-%m-%d")  # Extract date (YYYY-MM-DD)

        # Check for time conflicts
        conflict = False
        for existing_start, existing_end in all_events.keys():
            # Check if the event overlaps with an existing event's time range
            if not (
                event_end_time <= existing_start or event_start_time >= existing_end
            ):
                conflict = True
                print(
                    f"⚠️ Conflict: You already have an event '{all_events[(existing_start, existing_end)]['name']}' at this time."
                )
                break

        if not conflict:
            all_events[(event_start_time, event_end_time)] = {
                "name": event_name,
                "description": event_description,
            }

            # Store the event in the day-based dictionary
            if event_date not in events_by_day:
                events_by_day[event_date] = []

            events_by_day[event_date].append(
                {
                    "name": event_name,
                    "description": event_description,
                    "start_time": event_start_time,
                    "end_time": event_end_time,
                }
            )

            print("✅ Event added successfully.")
        else:
            print("❌ Event not added due to conflict.")

    else:
        print("Invalid option. Please try again.")
