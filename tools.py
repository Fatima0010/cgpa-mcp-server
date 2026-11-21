from typing import List


def marks_to_grade_points(marks: int) -> float | str:
    """ tool when the student needs the corresponding grade points. """
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"

    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa(
    grade_points: list[float],
    credit_hours: list[float]
) -> float | str:
    """ tool when the student provides grade points and credit hours and wants the semester GPA. """
    if len(grade_points) != len(credit_hours):
        return "Error: grade points and credit hours must have the same length"

    if len(grade_points) == 0:
        return "Error: at least one course is required"

    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than 0"

    total_quality_points = sum(
        gp * ch for gp, ch in zip(grade_points, credit_hours)
    )

    total_credit_hours = sum(credit_hours)

    return round(total_quality_points / total_credit_hours, 2)

def calculate_semester_gpa_from_marks(
    semester: int,
    marks: list[int]
) -> float | str:
    """
    Calculate a complete semester GPA from the student's marks.

    The marks must be provided in the same order as the graded courses
    returned by the COURSES dictionary for that semester.

    MD-001 and MD-002, if present, are excluded because they are
    non-credit pass/fail courses.
    """
    if semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    courses = [
        (code, name, credits)
        for code, name, credits in COURSES[semester]
        if code not in ("MD-001", "MD-002")
    ]

    if len(marks) != len(courses):
        return (
            f"Error: Semester {semester} requires marks for "
            f"{len(courses)} graded courses, but {len(marks)} were provided."
        )

    grade_points = []

    for mark in marks:
        grade_point = marks_to_grade_points(mark)

        if isinstance(grade_point, str):
            return grade_point

        grade_points.append(grade_point)

    credit_hours = [credits for _, _, credits in courses]

    return calculate_semester_gpa(
        grade_points,
        credit_hours
    )



def calculate_new_cgpa(
    current_cgpa: float,
    completed_credit_hours: float,
    semester_gpa: float,
    semester_credit_hours: float
) -> float | str:
    """ tool when the student wants to know their projected CGPA after completing one more semester. """
    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"

    if semester_gpa < 0 or semester_gpa > 4:
        return "Error: semester GPA must be between 0 and 4"

    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"

    if semester_credit_hours <= 0:
        return "Error: semester credit hours must be greater than 0"

    new_cgpa = (
        current_cgpa * completed_credit_hours
        + semester_gpa * semester_credit_hours
    ) / (completed_credit_hours + semester_credit_hours)

    return round(new_cgpa, 2)


def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float
) -> float | str:
    """ tool when the student wants to know what average GPA they need over their remaining credit hours to reach a target CGPA. """
    if target_cgpa < 0 or target_cgpa > 4:
        return "Error: target CGPA must be between 0 and 4"

    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"

    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"

    if remaining_credit_hours <= 0:
        return "Error: remaining credit hours must be greater than 0"

    required_gpa = (
        target_cgpa * (completed_credit_hours + remaining_credit_hours)
        - current_cgpa * completed_credit_hours
    ) / remaining_credit_hours

    return round(required_gpa, 2)


COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}


def get_semester_courses(semester: int) -> str:
    """ tool when the student asks which courses they have in a particular semester or needs the credit hours for those courses. """
    if semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    courses = COURSES[semester]

    lines = []

    for code, name, credits in courses:
        lines.append(f"{code}: {name} ({credits} credit hours)")

    total_credits = sum(credits for _, _, credits in courses)

    return "\n".join(lines) + f"\nTotal graded credit hours: {total_credits}"


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """ tool when the student wants to know how many graded credit hours remain after completing a particular semester."""
    if current_semester < 0 or current_semester > 8:
        return "Error: semester must be between 0 and 8"

    total_remaining = 0.0

    for semester in range(current_semester + 1, 9):
        total_remaining += sum(
            credits for _, _, credits in COURSES[semester]
        )

    return total_remaining

def get_horizon_credit_hours(start_semester: int, number_of_semesters: int) -> float | str:
    """ tool when the student wants a target-CGPA plan across multiple upcoming semesters and the total graded credit hours for that specific semester horizon are needed. """
    if start_semester < 1 or start_semester > 8:
        return "Error: start semester must be between 1 and 8"

    if number_of_semesters < 1:
        return "Error: number of semesters must be at least 1"

    end_semester = start_semester + number_of_semesters - 1

    if end_semester > 8:
        return "Error: semester horizon goes beyond semester 8"

    total_credit_hours = 0.0

    for semester in range(start_semester, end_semester + 1):
        total_credit_hours += sum(
            credits for _, _, credits in COURSES[semester]
        )

    return total_credit_hours

def plan_target_cgpa(
    current_semester: int,
    current_cgpa: float,
    completed_credit_hours: float,
    target_cgpa: float
) -> str:
    """ tool when a student wants to know what average GPA they need to reach a target CGPA by graduation. The tool checks the current
    semester first, then progressively wider semester horizons until the target becomes achievable or all remaining semesters are checked."""
    if current_semester < 1 or current_semester > 8:
        return "Error: current semester must be between 1 and 8"

    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"

    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"

    if target_cgpa < 0 or target_cgpa > 4:
        return "Error: target CGPA must be between 0 and 4"

    results = []

    for number_of_semesters in range(1, 9 - current_semester + 1):

        remaining_credit_hours = get_horizon_credit_hours(
            current_semester,
            number_of_semesters
        )

        required_gpa = required_gpa_for_target(
            target_cgpa,
            current_cgpa,
            completed_credit_hours,
            remaining_credit_hours
        )

        if isinstance(required_gpa, str):
            return required_gpa

        end_semester = current_semester + number_of_semesters - 1

        if number_of_semesters == 1:
            horizon = f"Semester {current_semester}"
        else:
            horizon = f"Semesters {current_semester}-{end_semester}"

        results.append(
            f"{horizon}: {remaining_credit_hours} credit hours, "
            f"required GPA {required_gpa}"
        )

        if required_gpa <= 4.0:
            return (
                "\n".join(results)
                + f"\nAchievable horizon: {horizon}"
            )

    return (
        "\n".join(results)
        + "\nThe target cannot be reached by graduation "
          "within a maximum GPA of 4.0."
    )







def save_report(filename: str, content: str) -> str:
    """ tool only when the student explicitly wants to save a useful GPA, CGPA, or target-planning report. """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Report saved successfully as {filename}"

    except Exception as e:
        return f"Error: could not save report: {e}"