"""
algorithms.py

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

Student = Dict[str, Any]


def bubble_sort(items: List[Student], key: Callable[[Student], Any], reverse: bool = False) -> List[Student]:
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            a = key(arr[j])
            b = key(arr[j + 1])
            if (a > b and not reverse) or (a < b and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(items: List[Student], key: Callable[[Student], Any], reverse: bool = False) -> List[Student]:
    arr = items.copy()

    def _qs(lst: List[Student]) -> List[Student]:
        if len(lst) <= 1:
            return lst
        pivot = key(lst[len(lst) // 2])
        less = [x for x in lst if key(x) < pivot]
        equal = [x for x in lst if key(x) == pivot]
        greater = [x for x in lst if key(x) > pivot]
        sorted_less = _qs(less)
        sorted_greater = _qs(greater)
        result = sorted_less + equal + sorted_greater
        return result if not reverse else list(reversed(result))

    return _qs(arr)


def binary_search_by_id(sorted_students: List[Student], target_id: str) -> int:
    """
    Perform binary search on a list of students sorted ascending by 'id'.
    Returns the index of the found student, or -1 if not found.
    """
    low = 0
    high = len(sorted_students) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = str(sorted_students[mid]["id"])  # ensure comparable as string
        if mid_id == target_id:
            return mid
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
