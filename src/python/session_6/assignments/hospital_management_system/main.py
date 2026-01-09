from core import HospitalManager
from model import Hospital, Department, Patient, StaffMember


def main():
    hospital = Hospital("El Salam Hospital", "123 XYZ St")

    hospital_manager = HospitalManager(hospital)

    cardiology_dept = Department("Cardiology")
    neurology_dept = Department("Neurology")

    hospital_manager.add_department(cardiology_dept)
    hospital_manager.add_department(neurology_dept)

    patient1 = Patient("John Doe", 45, "Heart Disease")
    patient2 = Patient("Jane Smith", 38, "Migraine")

    hospital_manager.add_patient_to_department("Cardiology", patient1)
    hospital_manager.add_patient_to_department("Neurology", patient2)

    staff_member_1 = StaffMember("Dr. George", 35, "Cardiologist")
    staff_member_2 = StaffMember("Dr. Samuel", 48, "Neurologist")

    hospital_manager.add_staff_to_department("Cardiology", staff_member_1)
    hospital_manager.add_staff_to_department("Neurology", staff_member_2)

    print()
    print(hospital_manager.view_hospital_info())


if __name__ == "__main__":
    main()
