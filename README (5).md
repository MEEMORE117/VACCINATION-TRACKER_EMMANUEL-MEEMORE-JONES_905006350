# Vaccination Tracker

**Module:** PROG211 Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Student:** Emmanuel Meemore Jones | **Student ID:** 905006350
**Lecturer:** Amandus Benjamin Coker
**Domain:** Health

## Overview

The Vaccination Tracker is a Python program that records patients, the vaccines available, and which patient received which dose on which date. It solves a real health problem: clinics need a simple way to check who is vaccinated and whether a vaccine course is complete.

## How the Solution Aligns with DPG Standards

| DPG Principle | How this project meets it |
|---|---|
| **Open-source** | The full source code is published in this public GitHub repository. |
| **Inclusive and accessible** | Output is plain, readable text that works in any terminal or screen reader. The program runs offline on basic hardware with no external libraries. |
| **Privacy-respecting** | Only non-sensitive data is stored: patient ID, first name and age. No phone numbers, addresses, national IDs or medical histories are collected. |
| **Modular and reusable** | Each class has a single job, and the functions accept any registry dictionary, so the code can be reused or extended. |

## Program Structure

### Classes

- **Patient**: attributes `patient_id`, `name`, `age`
- **Vaccine**: attributes `vaccine_name`, `doses_required`
- **VaccinationRecord**: links a `Patient` to a `Vaccine` with `date_given` and `dose_number`

### Data Structures

- A **dictionary** (`patient_registry`) stores `Patient` objects using the unique patient ID as the key.
- A **tuple** (`APPROVED_VACCINES`) holds the fixed list of approved vaccines.

### Methods

| Type | Method | Purpose |
|---|---|---|
| Instance | `Patient.update_age()` | Updates one patient's age after validation |
| Instance | `Vaccine.is_course_complete()` | Checks whether enough doses were received |
| Class | `Patient.get_total_patients()` | Returns how many patients have been created |
| Class | `Vaccine.is_approved()` | Checks a vaccine against the approved tuple |
| Static | `Patient.is_valid_age()` | Validates that an age is between 0 and 120 |

### Functions

- `add_patient(registry, patient)` adds a patient to the dictionary.
- `display_all_patients(registry)` loops through the dictionary and prints every patient.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python main.py
```

## Example Usage (Sample Output)

```
Added patient: Aminata
Added patient: Mohamed
--- Registered Patients ---
ID: P001 | Name: Aminata | Age: 25
ID: P002 | Name: Mohamed | Age: 30
--- Vaccines ---
Vaccine: COVID-19 | Doses required: 2
Vaccine: Measles | Doses required: 1
--- Vaccination Records ---
Aminata received COVID-19 (dose 1 of 2) on 2026-10-01
Aminata received COVID-19 (dose 2 of 2) on 2026-10-29
Mohamed received Measles (dose 1 of 1) on 2026-10-05
--- Methods Demo ---
Total patients: 2
Updated Mohamed's age to 31
Invalid age: -5
Valid age 40? True
Course complete after 1 dose? False
Course complete after 2 doses? True
Is Polio approved? True
Is Mumps approved? False
Approved vaccines: COVID-19, Measles, Polio
```

## Source Code

- `main.py`: all classes, functions and the demo program
