# College Attendance Analyzer

## 1. Project Overview

The **College Attendance Analyzer** is a Python-based project developed to manage, calculate, and analyze student attendance records.

The project reads attendance data from a CSV file, calculates attendance percentages, identifies students who are below the minimum attendance requirement of 75%, and displays subject-wise average attendance.

It also uses graphical representations such as bar charts and pie charts to make attendance analysis easier to understand.

## 2. Objectives

The main objectives of this project are:

- To calculate student attendance percentages.
- To identify students with attendance below 75%.
- To display eligible and shortage lists.
- To calculate subject-wise average attendance.
- To represent attendance data using charts.
- To validate attendance records and handle incorrect data.

## 3. Features

The main features of the College Attendance Analyzer are:

- **Attendance Percentage:** Calculates the attendance percentage of each student.
- **Shortage List:** Identifies students whose attendance is below 75%.
- **Eligibility Checking:** Displays students who meet the minimum attendance requirement.
- **Subject-wise Average:** Calculates the average attendance for each subject.
- **Bar Chart:** Displays subject-wise average attendance using a bar chart.
- **Pie Chart:** Shows the distribution of subject-wise average attendance.
- **Input Validation:** Checks incorrect or invalid attendance records.
- **CSV File Handling:** Reads attendance records directly from a CSV file.

## 4. Technologies Used

The following technologies and Python libraries are used in this project:

### Python

Python is the main programming language used to develop the project.

### Pandas

Pandas is used for reading, managing, filtering, and analyzing attendance data stored in the CSV file.

### Matplotlib

Matplotlib is used to create graphical representations of attendance data, including bar charts and pie charts.

### CSV (Comma-Separated Values)

A CSV file is used to store student attendance records in tabular format.

## 5. Requirements and Installation

To run this project, the following are required:

- Python 3
- Pandas library
- Matplotlib library
- Visual Studio Code (or any Python-supported editor)

### Install Required Libraries

Open the terminal and execute the following commands:

```bash
py -m pip install pandas
```

```bash
py -m pip install matplotlib
```

## 6. Project Structure

The project contains the following files:

```text
College_Attendance_Analyzer/
│
├── attendance_analyzer.py
├── attendance.csv
├── README.md
├── SUMMARY.md
│
├── 01_Attendance_Percentage.png
├── 02_Shortage_List.png
├── 03_Invalid_Input.png
├── 04_Subject_Wise_Average.png
├── 05_Bar_Chart.png
└── 06_Pie_Chart.png
```

**File Description:**

- `attendance_analyzer.py` – Contains the main Python program.
- `attendance.csv` – Stores student attendance records.
- `README.md` – Provides project information and instructions.
- `SUMMARY.md` – Contains the project implementation summary, test cases, and screenshot references.
- `.png` files – Contain screenshots of the project outputs.

## 7. How to Run the Project

Follow these steps to run the project:

1. Install Python on your computer.
2. Install the Pandas and Matplotlib libraries.
3. Open the project folder in Visual Studio Code.
4. Make sure `attendance.csv` and `attendance_analyzer.py` are in the same folder.
5. Open the terminal in Visual Studio Code.
6. Execute the following command:

```bash
py attendance_analyzer.py
```

7. The Attendance Analyzer menu will appear in the terminal.
8. Enter your preferred menu option to view the required result.

## 8. Attendance Calculation Formula

The project calculates attendance percentage using the following formula:

**Attendance Percentage = (Classes Attended / Classes Held) × 100**

For example:

- Classes Held = 40
- Classes Attended = 36

Attendance Percentage:

(36 / 40) × 100 = 90%

The minimum attendance requirement is **75%**.

- Attendance below 75%: Shortage
- Attendance equal to or above 75%: Eligible

## 9. Menu Options Explained

The project provides the following menu options:

| Option | Function |
|---|---|
| 1 | Attendance Percentage |
| 2 | Shortage List |
| 3 | Subject-wise Average |
| 4 | Bar Chart |
| 5 | Pie Chart |
| 6 | Exit |

**Option 1 – Attendance Percentage:** Displays the attendance percentage of each student.

**Option 2 – Shortage List:** Displays students below 75% attendance and identifies eligible students.

**Option 3 – Subject-wise Average:** Calculates the average attendance percentage for each subject.

**Option 4 – Bar Chart:** Displays subject-wise average attendance in a bar chart.

**Option 5 – Pie Chart:** Displays subject-wise average attendance in a pie chart.

**Option 6 – Exit:** Closes the program.

## 10. Input Validation

Input validation is used to ensure that attendance records contain valid data.

The program checks:

- Whether classes held and classes attended are numeric.
- Whether the number of classes held is greater than zero.
- Whether attended classes are not negative.
- Whether attended classes are not greater than classes held.

Invalid records are skipped so that incorrect data does not affect the attendance analysis.

## 11. Conclusion

The College Attendance Analyzer is a Python-based project that makes attendance calculation and analysis easier.

It demonstrates the practical use of Python, Pandas, CSV file handling, data validation, and Matplotlib.

The project helps identify attendance shortages, calculate subject-wise averages, and visualize attendance information through charts.
