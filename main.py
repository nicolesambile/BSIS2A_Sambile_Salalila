"""
main.py
CLI app for managing student records.
Uses sorting and searching algorithms from algorithms.py
"""

from algorithms import bubble_sort_nbs, quick_sort_nbs, binary_search_by_id_nbs
from collections import deque

# In-memory data storage
students_nbs = []
action_queue_nbs = deque(maxlen=10)  # store recent actions
SORT_ALGOS_nbs = {"1": bubble_sort_nbs, "2": quick_sort_nbs}


def display_students_nbs(data_nbs):
    """Display the list of students in a table format."""
    if not data_nbs:
        print("\nNo students found.\n")
        return
    print("\nID\tName\t\tGrade")
    print("-" * 30)
    for s_nbs in data_nbs:
        print(f"{s_nbs['id']}\t{s_nbs['name']}\t\t{s_nbs['grade']}")
    print()


def add_student_nbs():
    """Add a new student record."""
    sid_nbs = input("Enter student ID: ").strip()
    name_nbs = input("Enter student name: ").strip()
    grade_nbs = float(input("Enter grade: "))

    students_nbs.append({"id": sid_nbs, "name": name_nbs, "grade": grade_nbs})
    action_queue_nbs.append(f"Added student {name_nbs} (ID: {sid_nbs})")

    print("Student added successfully.\n")


def edit_student_nbs():
    """Edit an existing student's information."""
    sid_nbs = input("Enter ID of student to edit: ").strip()
    sorted_by_id_nbs = sorted(students_nbs, key=lambda x: x["id"])
    idx_nbs = binary_search_by_id_nbs(sorted_by_id_nbs, sid_nbs)

    if idx_nbs == -1:
        print("Student not found.\n")
        return

    for s_nbs in students_nbs:
        if s_nbs["id"] == sid_nbs:
            s_nbs["name"] = input("Enter new name: ").strip() or s_nbs["name"]
            new_grade_nbs = input("Enter new grade (leave blank to keep current): ").strip()
            if new_grade_nbs:
                s_nbs["grade"] = float(new_grade_nbs)
            action_queue_nbs.append(f"Edited student {sid_nbs}")
            print("Student updated successfully.\n")
            return


def delete_student_nbs():
    """Delete a student by ID."""
    sid_nbs = input("Enter ID of student to delete: ").strip()
    for s_nbs in students_nbs:
        if s_nbs["id"] == sid_nbs:
            students_nbs.remove(s_nbs)
            action_queue_nbs.append(f"Deleted student {sid_nbs}")
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")


def sort_students_nbs():
    """Sort the students by name or grade using Bubble Sort or Quick Sort."""
    if not students_nbs:
        print("No students to sort.\n")
        return

    print("Sort by: 1) Name  2) Grade")
    sort_key_choice_nbs = input("Choose option: ").strip()
    key_nbs = (lambda s: s["name"]) if sort_key_choice_nbs == "1" else (lambda s: s["grade"])

    print("Choose algorithm: 1) Bubble Sort  2) Quick Sort")
    algo_choice_nbs = input("Enter choice: ").strip()
    algo_nbs = SORT_ALGOS_nbs.get(algo_choice_nbs, bubble_sort_nbs)

    reverse_nbs = input("Reverse order? (y/n): ").lower().startswith("y")

    sorted_list_nbs = algo_nbs(students_nbs, key_nbs, reverse_nbs)
    display_students_nbs(sorted_list_nbs)

    action_queue_nbs.append(
        f"Sorted students by {'name' if sort_key_choice_nbs == '1' else 'grade'} using {algo_nbs.__name__}"
    )


def search_student_nbs():
    """Search for a student by ID using binary search."""
    if not students_nbs:
        print("No students in the list.\n")
        return

    target_id_nbs = input("Enter student ID to search: ").strip()
    sorted_by_id_nbs = sorted(students_nbs, key=lambda s: s["id"])
    idx_nbs = binary_search_by_id_nbs(sorted_by_id_nbs, target_id_nbs)

    if idx_nbs != -1:
        print("\n Student found:")
        s_nbs = sorted_by_id_nbs[idx_nbs]
        print(f"ID: {s_nbs['id']}  |  Name: {s_nbs['name']}  |  Grade: {s_nbs['grade']}\n")
    else:
        print("Student not found.\n")

    action_queue_nbs.append(f"Searched for student ID {target_id_nbs}")


def show_recent_actions_nbs():
    """Display the most recent actions."""
    print("\nRecent actions:")
    if not action_queue_nbs:
        print("No actions yet.\n")
    else:
        for act_nbs in list(action_queue_nbs)[::-1]:
            print(f"- {act_nbs}")
    print()


def main_menu_nbs():
    """Main CLI menu loop."""
    while True:
        print("""
==============================
   STUDENT RECORDS SYSTEM - CC104 (CLI)
==============================
1. Add Student
2. Edit Student
3. Delete Student
4. Sort Students (by name/grade)
5. Search Student by ID
6. Show Recent Actions
7. List All Students (unsorted)
0. Exit
""")
        choice_nbs = input("Enter choice: ").strip()
        if choice_nbs == "1":
            add_student_nbs()
        elif choice_nbs == "2":
            edit_student_nbs()
        elif choice_nbs == "3":
            delete_student_nbs()
        elif choice_nbs == "4":
            sort_students_nbs()
        elif choice_nbs == "5":
            search_student_nbs()
        elif choice_nbs == "6":
            show_recent_actions_nbs()
        elif choice_nbs == "7":
            display_students_nbs(students_nbs)
        elif choice_nbs == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu_nbs()
