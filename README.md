# Contact Book Using Dictionaries

**Veda Technology — Python Programming Track · Level 1 · Task 10 (Day 10)**

A command-line contact book where users can **add, search, update, and delete** contact information. Built in pure Python using dictionaries (key-value data management).

## Features
- Full CRUD: Create, Read (view/search), Update, Delete
- Phone number used as the unique dictionary key
- Duplicate-entry validation
- Input validation (10-digit phone, basic email format, non-empty name)
- Search by phone (exact) or name (partial, case-insensitive)
- Delete confirmation prompt
- Pre-loaded sample contact data
- Simple numbered menu

## Requirements
- Python 3.6+ (no external libraries)

## How to Run
```bash
python contact_book.py
```

## Menu
```
1. Add contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
```

## Data Structure
```python
contacts = {
    "9876543210": {"name": "Aarav Sharma", "email": "aarav@example.com", "city": "Bhopal"},
}
```
Key = phone number (unique) · Value = nested dictionary of contact details.

## Sample Run
```
Choose an option (1-6): 1
Enter phone number (10 digits): 9876543210
Duplicate entry: 9876543210 already belongs to Aarav Sharma.
```

## Approach
1. Chose a dictionary keyed by phone number so lookups, duplicate checks, updates and deletes are O(1).
2. Wrote one function per CRUD operation and a dispatch dictionary (`ACTIONS`) to map menu choices to functions.
3. Added validation before any change to the data.

## Possible Improvements
- Save/load contacts to a JSON file for persistence
- Sort/filter by city
- Export contacts to CSV

## Author
Nabila — Veda Technology Intern