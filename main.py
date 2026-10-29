"""
Vaccination Tracker - PROG211 OOP1 Assignment
Domain: Health

DPG Standards:
- Open-source: published on GitHub.
- Privacy-respecting: stores only an ID, first name and age.
  No sensitive personal or medical data is collected.
- Modular and reusable: separate classes for Patient, Vaccine and
  VaccinationRecord; functions accept any registry dictionary.
- Inclusive and accessible: plain-text, readable output; runs offline
  on basic hardware with no extra libraries.
"""
# ===== CLASSES =====

class Patient:
    total_patients = 0  # class attribute shared by all patients

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        Patient.total_patients += 1

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age}")

    # Instance method: works on one specific patient
    def update_age(self, new_age):
        if Patient.is_valid_age(new_age):
            self.age = new_age
            print(f"Updated {self.name}'s age to {self.age}")
        else:
            print(f"Invalid age: {new_age}")

    # Class method: works on the class as a whole
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # Static method: a helper that needs neither self nor cls
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120


class Vaccine:
    # Tuple: fixed list of approved vaccines that should not change
    APPROVED_VACCINES = ("COVID-19", "Measles", "Polio")

    def __init__(self, vaccine_name, doses_required):
        self.vaccine_name = vaccine_name
        self.doses_required = doses_required

    def display_info(self):
        print(f"Vaccine: {self.vaccine_name} | Doses required: {self.doses_required}")

    # Instance method
    def is_course_complete(self, doses_received):
        return doses_received >= self.doses_required

    # Class method
    @classmethod
    def is_approved(cls, name):
        return name in cls.APPROVED_VACCINES


class VaccinationRecord:
    def __init__(self, patient, vaccine, date_given, dose_number):
        self.patient = patient
        self.vaccine = vaccine
        self.date_given = date_given
        self.dose_number = dose_number

    def display_info(self):
        print(f"{self.patient.name} received {self.vaccine.vaccine_name} "
              f"(dose {self.dose_number} of {self.vaccine.doses_required}) "
              f"on {self.date_given}")


# ===== FUNCTIONS =====

def add_patient(registry, patient):
    registry[patient.patient_id] = patient
    print(f"Added patient: {patient.name}")


def display_all_patients(registry):
    print("--- Registered Patients ---")
    for patient_id, patient in registry.items():
        patient.display_info()


# ===== PROGRAM =====

patient_registry = {}

p1 = Patient("P001", "Aminata", 25)
p2 = Patient("P002", "Mohamed", 30)

add_patient(patient_registry, p1)
add_patient(patient_registry, p2)

display_all_patients(patient_registry)

v1 = Vaccine("COVID-19", 2)
v2 = Vaccine("Measles", 1)

print("--- Vaccines ---")
v1.display_info()
v2.display_info()

print("--- Vaccination Records ---")
r1 = VaccinationRecord(p1, v1, "2026-10-01", 1)
r2 = VaccinationRecord(p1, v1, "2026-10-29", 2)
r3 = VaccinationRecord(p2, v2, "2026-10-05", 1)

r1.display_info()
r2.display_info()
r3.display_info()

print("--- Methods Demo ---")
print("Total patients:", Patient.get_total_patients())
p2.update_age(31)
p2.update_age(-5)
print("Valid age 40?", Patient.is_valid_age(40))
print("Course complete after 1 dose?", v1.is_course_complete(1))
print("Course complete after 2 doses?", v1.is_course_complete(2))
print("Is Polio approved?", Vaccine.is_approved("Polio"))
print("Is Mumps approved?", Vaccine.is_approved("Mumps"))
print("Approved vaccines:", ", ".join(Vaccine.APPROVED_VACCINES))