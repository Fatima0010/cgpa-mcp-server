import os
from fastmcp import FastMCP

from tools import (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_semester_gpa_from_marks,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    get_horizon_credit_hours,
    plan_target_cgpa,
    save_report,
)

mcp = FastMCP("cgpa")

# Task 1: share every tool
mcp.tool(marks_to_grade_points)
mcp.tool(calculate_semester_gpa)
mcp.tool(calculate_semester_gpa_from_marks)
mcp.tool(calculate_new_cgpa)
mcp.tool(required_gpa_for_target)
mcp.tool(get_semester_courses)
mcp.tool(get_remaining_credit_hours)
mcp.tool(get_horizon_credit_hours)
mcp.tool(plan_target_cgpa)
mcp.tool(save_report)

if __name__ == "__main__":
    # locally: http://127.0.0.1:8000/mcp
    # on Render: set HOST=0.0.0.0 (Render gives the PORT itself)
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="http", host=host, port=port)
