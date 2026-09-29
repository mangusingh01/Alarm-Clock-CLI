# Project Alarm CLI

A simple Python command-line alarm clock application. It lets users add multiple alarms, view active alarms, and delete alarms from the terminal.

This project uses only Python's built-in modules. No UI, database, or external packages are required.

## Features

- Add multiple alarms
- View all active alarms
- Delete an alarm by number
- Alarm clock starts automatically when the app opens
- Ring with a terminal message and system beep
- Store alarms in memory while the program is running

## Requirements

- Python 3.8 or higher

## Project Structure

```text
Project-Alarm-CLI/
├── alarm_clock.py
└── README.md
```

## Setup

Open a terminal and move into the project folder:

```bash
cd Project-Alarm-CLI
```

Check that Python is installed:

```bash
python3 --version
```

Run the application:

```bash
python3 alarm_clock.py
```

On Windows, you may need to use:

```bash
python alarm_clock.py
```

## How To Use

After starting the application, you will see this menu:

```text
=== CLI Alarm Clock ===
1. Add alarm
2. View alarms
3. Delete alarm
4. Exit
```

Choose an option by entering its number.

### Add an Alarm

Use option `1` and enter the alarm time in 24-hour `HH:MM` format.

Examples:

```text
07:30
13:45
22:10
```

### View Alarms

Use option `2` to see all alarms currently added.

### Delete an Alarm

Use option `3`, then enter the alarm number shown in the active alarms list.

### Exit

Use option `4` to exit the application.

## Notes

- Alarms are stored only while the program is running.
- If the program is closed, all alarms are cleared.
- The app uses 24-hour time format.
- An alarm rings the next time the current system time matches the alarm time.

## Example

```text
=== CLI Alarm Clock ===
1. Add alarm
2. View alarms
3. Delete alarm
4. Exit
Choose an option: 1
Enter alarm time in 24-hour HH:MM format: 07:30
Alarm added for 07:30.

=== CLI Alarm Clock ===
1. Add alarm
2. View alarms
3. Delete alarm
4. Exit
Choose an option:

==============================
Alarm ringing for 07:30!
Wake up!
==============================
All alarms have rung.
```

## Areas of Improvement

- Add support for alarms on future dates, such as `2026-10-05 07:30`.
- Save alarms to a local file so they are not lost when the app closes.
- Add a snooze option when an alarm rings.
- Allow custom labels or messages for each alarm.
- Support recurring alarms, such as daily or weekday alarms.
- Add 12-hour time format support, such as `07:30 AM`.
- Improve the alarm sound beyond the terminal beep.
