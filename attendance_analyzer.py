
import pandas as pd
import matplotlib.pyplot as plt

MIN_ATTENDANCE = 75

# College Attendance Analyzer
print("===== COLLEGE ATTENDANCE ANALYZER =====")

# Read attendance data from CSV
df = pd.read_csv("attendance.csv")

# Validate attendance records
valid_rows = []

for index, row in df.iterrows():

    held = pd.to_numeric(row["Classes_Held"], errors="coerce")
    attended = pd.to_numeric(row["Classes_Attended"], errors="coerce")

    if pd.isna(held) or pd.isna(attended) or held <= 0 or attended < 0:
        print(f"Row {index + 1} invalid: Incorrect data. Row skipped.")
        continue

    if attended > held:
        print(
            f"Row {index + 1} invalid: attended "
            f"({attended:g}) cannot exceed held "
            f"({held:g}). Row skipped."
        )
        continue

    valid_rows.append({
        "Name": row["Name"],
        "Subject": row["Subject"],
        "Classes_Held": held,
        "Classes_Attended": attended
    })

df = pd.DataFrame(valid_rows)

if df.empty:
    print("No valid attendance records found.")

else:

    # Calculate attendance percentage
    df["Percentage"] = (
        df["Classes_Attended"] / df["Classes_Held"]
    ) * 100

    while True:

        print("\n===== MENU =====")
        print("1. Attendance Percentage")
        print("2. Shortage List")
        print("3. Subject-wise Average")
        print("4. Bar Chart")
        print("5. Pie Chart")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Option 1: Attendance percentage
        if choice == "1":

            print("\nAttendance Percentage:")

            for index, row in df.iterrows():
                print(f"{row['Name']}: {row['Percentage']:.2f}%")

        # Option 2: Shortage list
        elif choice == "2":

            below_75 = df[df["Percentage"] < MIN_ATTENDANCE]

            if below_75.empty:
                print("No student below 75%.")
            else:
                print("\nStudents below 75%:")
                for index, row in below_75.iterrows():
                    print(f"{row['Name']}: {row['Percentage']:.2f}%")

            eligible = df[df["Percentage"] >= MIN_ATTENDANCE]

            for index, row in eligible.iterrows():
                print(
                    f"{row['Name']} ({row['Percentage']:.2f}%) "
                    "is eligible."
                )

        # Option 3: Subject-wise average
        elif choice == "3":

            subject_average = df.groupby("Subject")["Percentage"].mean()

            print("\nSubject-wise Average Attendance:")
            print(subject_average)

        # Option 4: Bar chart
        elif choice == "4":

            subject_average = df.groupby("Subject")["Percentage"].mean()

            subject_average.plot(kind="bar", figsize=(8, 5))

            plt.title("Subject-wise Average Attendance")
            plt.xlabel("Subjects")
            plt.ylabel("Attendance Percentage")
            plt.ylim(0, 100)
            plt.tight_layout()
            plt.show()

        # Option 5: Pie chart
        elif choice == "5":

            subject_average = df.groupby("Subject")["Percentage"].mean()

            plt.figure(figsize=(7, 7))

            plt.pie(
                subject_average,
                labels=subject_average.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Subject-wise Attendance Distribution")
            plt.tight_layout()
            plt.show()

        # Option 6: Exit
        elif choice == "6":
            print("Thank you for using Attendance Analyzer!")
            break

        else:
            print("Invalid choice! Please enter 1 to 6.")
