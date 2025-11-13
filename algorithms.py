"""
algorithms_nbs.py

Contains sorting and searching algorithms used by the CLI app.
- Bubble Sort
- Quick Sort
- Binary Search (by ID)

All algorithms operate on lists of dictionaries representing students with keys:
- id: str
- name: str
- grade: float or int
"""

from typing import List, Dict, Callable, Any

Student_nbs = Dict[str, Any]


def bubble_sort_nbs(items_nbs: List[Student_nbs], key_nbs: Callable[[Student_nbs], Any], reverse_nbs: bool = False) -> List[Student_nbs]:
    """
    Sorts a list of students using the Bubble Sort algorithm.
    Can sort ascending or descending based on reverse_nbs flag.
    """
    arr_nbs = items_nbs.copy()
    n_nbs = len(arr_nbs)

    for i_nbs in range(n_nbs):
        swapped_nbs = False
        for j_nbs in range(0, n_nbs - i_nbs - 1):
            a_nbs = key_nbs(arr_nbs[j_nbs])
            b_nbs = key_nbs(arr_nbs[j_nbs + 1])
            if (a_nbs > b_nbs and not reverse_nbs) or (a_nbs < b_nbs and reverse_nbs):
                arr_nbs[j_nbs], arr_nbs[j_nbs + 1] = arr_nbs[j_nbs + 1], arr_nbs[j_nbs]
                swapped_nbs = True
        if not swapped_nbs:
            break

    return arr_nbs


def quick_sort_nbs(items_nbs: List[Student_nbs], key_nbs: Callable[[Student_nbs], Any], reverse_nbs: bool = False) -> List[Student_nbs]:
    """
    Sorts a list of students using the Quick Sort algorithm.
    Can sort ascending or descending based on reverse_nbs flag.
    """
    arr_nbs = items_nbs.copy()

    def _qs_nbs(lst_nbs: List[Student_nbs]) -> List[Student_nbs]:
        if len(lst_nbs) <= 1:
            return lst_nbs

        pivot_nbs = key_nbs(lst_nbs[len(lst_nbs) // 2])
        less_nbs = [x_nbs for x_nbs in lst_nbs if key_nbs(x_nbs) < pivot_nbs]
        equal_nbs = [x_nbs for x_nbs in lst_nbs if key_nbs(x_nbs) == pivot_nbs]
        greater_nbs = [x_nbs for x_nbs in lst_nbs if key_nbs(x_nbs) > pivot_nbs]

        sorted_less_nbs = _qs_nbs(less_nbs)
        sorted_greater_nbs = _qs_nbs(greater_nbs)
        result_nbs = sorted_less_nbs + equal_nbs + sorted_greater_nbs

        return result_nbs if not reverse_nbs else list(reversed(result_nbs))

    return _qs_nbs(arr_nbs)


def binary_search_by_id_nbs(sorted_students_nbs: List[Student_nbs], target_id_nbs: str) -> int:
    """
    Perform binary search on a list of students sorted ascending by 'id'.
    Returns the index of the found student, or -1 if not found.
    """
    low_nbs = 0
    high_nbs = len(sorted_students_nbs) - 1

    while low_nbs <= high_nbs:
        mid_nbs = (low_nbs + high_nbs) // 2
        mid_id_nbs = str(sorted_students_nbs[mid_nbs]["id"])  # ensure comparable as string

        if mid_id_nbs == str(target_id_nbs):
            return mid_nbs
        elif mid_id_nbs < str(target_id_nbs):
            low_nbs = mid_nbs + 1
        else:
            high_nbs = mid_nbs - 1

    return -1
