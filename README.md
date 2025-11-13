# Student Records CLI (CC104)

A simple Python CLI app demonstrating core Data Structures and Algorithms:

- List and Dictionary for in-memory storage
- Queue to track pending actions/logs
- Bubble Sort and Quick Sort for sorting by name or grade
- Binary Search for searching by student ID

## Requirements

- Python 3.9+

## Installation

No external dependencies are required. Optionally, create and activate a virtual environment.

## Run

```
python main.py
```

## Features

- Add / Edit / Delete students
- Display sorted list by name or grade
- Choose algorithm: Bubble Sort or Quick Sort
- Search student by ID (binary search on ID-sorted list)
- Queue to review and process recent actions

## Data Model

Each student is a dictionary:

```
{
  "id": str,
  "name": str,
  "grade": float
}
```

All data is kept in-memory for this exercise.
