from datetime import datetime
from threading import Event, Lock, Thread
import time


TIME_FORMAT = "%H:%M"
CHECK_INTERVAL_SECONDS = 1


def show_menu():
    print("\n=== CLI Alarm Clock ===")
    print("1. Add alarm")
    print("2. View alarms")
    print("3. Delete alarm")
    print("4. Exit")


def is_valid_time(alarm_time):
    try:
        datetime.strptime(alarm_time, TIME_FORMAT)
        return True
    except ValueError:
        return False


def add_alarm(alarms, alarm_lock):
    alarm_time = input("Enter alarm time in 24-hour HH:MM format: ").strip()

    if not is_valid_time(alarm_time):
        print("Invalid time. Please use HH:MM format, for example 07:30 or 21:15.")
        return

    with alarm_lock:
        if alarm_time in alarms:
            print(f"Alarm for {alarm_time} already exists.")
            return

        alarms.append(alarm_time)
        alarms.sort()

    print(f"Alarm added for {alarm_time}.")


def view_alarms(alarms, alarm_lock):
    with alarm_lock:
        alarm_list = alarms.copy()

    if not alarm_list:
        print("No alarms set.")
        return

    print("\nActive alarms:")
    for index, alarm_time in enumerate(alarm_list, start=1):
        print(f"{index}. {alarm_time}")


def delete_alarm(alarms, alarm_lock):
    with alarm_lock:
        alarm_list = alarms.copy()

    if not alarm_list:
        print("No alarms to delete.")
        return

    view_alarms(alarms, alarm_lock)
    selected_alarm = input("Enter alarm number to delete: ").strip()

    if not selected_alarm.isdigit():
        print("Please enter a valid alarm number.")
        return

    alarm_index = int(selected_alarm) - 1
    if alarm_index < 0 or alarm_index >= len(alarm_list):
        print("Alarm number is out of range.")
        return

    selected_time = alarm_list[alarm_index]

    with alarm_lock:
        if selected_time not in alarms:
            print("That alarm is no longer available.")
            return

        alarms.remove(selected_time)

    print(f"Deleted alarm for {selected_time}.")


def ring_alarm(alarm_time):
    print("\n" + "=" * 30)
    print(f"Alarm ringing for {alarm_time}!")
    print("Wake up!")
    print("\a" * 3)
    print("=" * 30)


def alarm_monitor(alarms, alarm_lock, stop_event):
    while not stop_event.is_set():
        current_time = datetime.now().strftime(TIME_FORMAT)
        alarm_to_ring = None
        remaining_alarms = []

        with alarm_lock:
            if current_time in alarms:
                alarm_to_ring = current_time
                alarms.remove(current_time)
                remaining_alarms = alarms.copy()

        if alarm_to_ring:
            ring_alarm(alarm_to_ring)

            if remaining_alarms:
                print(f"Remaining alarms: {', '.join(remaining_alarms)}")
            else:
                print("All alarms have rung.")

            time.sleep(60)
        else:
            time.sleep(CHECK_INTERVAL_SECONDS)


def main():
    alarms = []
    alarm_lock = Lock()
    stop_event = Event()
    alarm_thread = Thread(
        target=alarm_monitor,
        args=(alarms, alarm_lock, stop_event),
        daemon=True,
    )
    alarm_thread.start()

    print("Alarm clock is running. Add alarms from the menu.")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_alarm(alarms, alarm_lock)
        elif choice == "2":
            view_alarms(alarms, alarm_lock)
        elif choice == "3":
            delete_alarm(alarms, alarm_lock)
        elif choice == "4":
            stop_event.set()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
