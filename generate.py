import csv, random

departments = ["Computer Science", "Cyber Security", "Software Engineering",
               "Information Technology", "Business Admin"]
levels = [100, 200, 300, 400]

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Student_ID", "Department", "Level",
                "Attendance_Percentage", "Average_Exam_Score"])
    for i in range(1, 51):
        w.writerow([
            f"STU{i:03d}",
            random.choice(departments),
            random.choice(levels),
            random.randint(40, 100),
            round(random.uniform(30, 95), 1),
        ])