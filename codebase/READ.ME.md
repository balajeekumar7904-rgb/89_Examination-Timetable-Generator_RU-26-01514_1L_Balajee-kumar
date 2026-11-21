# 📅 Examination Timetable Generator

A Python command-line application that automatically generates an examination date sheet from a list of subjects. It schedules exams sequentially from a chosen start date while automatically skipping **Sundays** and **custom holidays**.

## ✨ Features

- **Subject Validation:** Prevents empty subject lists and catches duplicate subject names.
- **Strict Date Parsing:** Validates that all dates follow the `DD-MM-YYYY` format and correspond to real calendar dates.
- **Automatic Day Skipping:** Automatically skips Sundays (`weekday() == 6`) and any user-defined holidays.
- **Readable Date Sheet Output:** Displays each scheduled subject alongside its formatted date and weekday name.
- **Zero External Dependencies:** Uses only Python's built-in `datetime` module.

## 🛠️ Prerequisites

- **Python 3.6+** installed on your machine.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Run the Script
Replace `main.py` with your actual script filename if different:
```bash
python main.py
```

## 💻 Usage Example

When you run the script, follow the interactive prompts in your terminal:

### Input
```text
Enter subjects (comma-separated): Mathematics, Physics, Computer Science, English
Enter start date (DD-MM-YYYY): 27-11-2026
Enter holidays (comma-separated, or 'none'): 30-11-2026
```

### Output
```text
--- Examination Date Sheet ---
Mathematics : 27-11-2026 (Friday)
Physics : 28-11-2026 (Saturday)
Computer Science : 01-12-2026 (Tuesday)
English : 02-12-2026 (Wednesday)
```
> **Note:** `29-11-2026` is skipped automatically because it falls on a Sunday, and `30-11-2026` is skipped because it was entered as a holiday.

## ⚠️ Input Validation & Error Messages

The script validates all inputs before generating the timetable and stops if an issue is detected:

| Condition | Error Message |
| :--- | :--- |
| Empty subject list or `none` | `At least one subject is required.` |
| Repeated subject name | `Duplicate subject: <Subject>.` |
| Invalid date format or non-existent date | `Invalid date. Please enter the date as DD-MM-YYYY.` |

## 📂 Project Structure

```text
├── main.py        # Main Python script containing validation and scheduling logic
└── README.md      # Project documentation
```

