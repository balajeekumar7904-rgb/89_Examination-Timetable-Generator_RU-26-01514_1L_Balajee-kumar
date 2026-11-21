# Import datetime to handle dates, weekdays, and date validation,
# and timedelta to increment dates by one day at a time.
from datetime import datetime, timedelta


def parse_date(date_str):
    """Validates a date string in DD-MM-YYYY format.

    Returns a datetime object if valid, or None if invalid.
    """
    try:
        # Remove extra spaces and attempt to parse using Day-Month-Year format
        return datetime.strptime(date_str.strip(), "%d-%m-%Y")
    except ValueError:
        # Triggered if the date doesn't match DD-MM-YYYY or isn't a real calendar date (e.g., 32-10-2026)
        return None


def generate_timetable(subjects, start_date_str, holiday_strs):
    """Validates inputs, schedules exams while skipping Sundays and holidays,

    and prints the final examination timetable.
    """

    # --- STEP 1: Validate the Subjects List ---
    # Check if the list of subjects is empty
    if not subjects:
        print("At least one subject is required.")
        return

    # Use a set to keep track of subjects we have already seen to catch duplicates
    seen_subjects = set()
    for sub in subjects:
        if sub in seen_subjects:
            print(f"Duplicate subject: {sub}.")
            return
        seen_subjects.add(sub)

    # --- STEP 2: Validate the Start Date ---
    current_date = parse_date(start_date_str)
    if current_date is None:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    # --- STEP 3: Validate Optional Holiday Dates ---
    # Store valid holiday dates in a set for fast lookup
    holidays = set()
    for h_str in holiday_strs:
        h_date = parse_date(h_str)
        if h_date is None:
            print("Invalid date. Please enter the date as DD-MM-YYYY.")
            return
        # .date() extracts just the Year-Month-Day part without the time
        holidays.add(h_date.date())

    # --- STEP 4: Schedule Exams Using Lists and Dictionaries ---
    # Initialize an empty list to store dictionary entries for each exam
    timetable = []

    for subject in subjects:
        # Keep moving forward one day while the current date is either:
        # 1. A Sunday (in Python's datetime, Monday=0 ... Sunday=6)
        # 2. Listed in the holidays set
        while current_date.weekday() == 6 or current_date.date() in holidays:
            current_date += timedelta(days=1)

        # Create a dictionary for the current subject's exam schedule
        entry = {
            "subject": subject,
            "date": current_date.strftime(
                "%d-%m-%Y"
            ),  # Format date back to DD-MM-YYYY string
            "day": current_date.strftime(
                "%A"
            ),  # Get full weekday name (e.g., Monday)
        }

        # Add the dictionary entry to the timetable list
        timetable.append(entry)

        # Advance to the next calendar day for the next subject in the list
        current_date += timedelta(days=1)

    # --- STEP 5: Display the Generated Date Sheet ---
    for item in timetable:
        print(f"{item['subject']} : {item['date']} ({item['day']})")


def main():
    """Main function to take user inputs from the console and run the generator."""

    # Read comma-separated subjects, split them into a list, and strip extra whitespace
    raw_subjects = input("Enter subjects (comma-separated): ").strip()
    if raw_subjects.lower() == "none" or not raw_subjects:
        subjects = []
    else:
        subjects = [s.strip() for s in raw_subjects.split(",") if s.strip()]

    # Read the start date string from the user
    start_date = input("Enter start date (DD-MM-YYYY): ").strip()

    # Read comma-separated holidays; treat 'none' or empty input as no holidays
    raw_holidays = input("Enter holidays (comma-separated, or 'none'): ").strip()
    if raw_holidays.lower() == "none" or not raw_holidays:
        holidays = []
    else:
        holidays = [h.strip() for h in raw_holidays.split(",") if h.strip()]

    print("\n--- Examination Date Sheet ---")
    # Call the timetable generator with the cleaned inputs
    generate_timetable(subjects, start_date, holidays)


# Standard Python boilerplate to ensure main() runs only when the script is executed directly
if __name__ == "__main__":
    main()