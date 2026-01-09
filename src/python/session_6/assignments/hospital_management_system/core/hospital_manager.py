from model import Hospital, Department, Patient, StaffMember


class HospitalManager:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital

    def add_department(self, department: Department):
        self.hospital.add_department(department)

    def add_patient_to_department(self, department_name: str, patient: Patient):
        for dept in self.hospital.departments:
            if dept.name == department_name:
                dept.add_patient(patient)
                return

        print(f"Department '{department_name}' not found.")

    def add_staff_to_department(self, department_name: str, staff_member: StaffMember):
        for dept in self.hospital.departments:
            if dept.name == department_name:
                dept.add_staff(staff_member)
                return

        print(f"Department '{department_name}' not found.")

    def view_hospital_info(self):
        hospital_info = (
            f"Hospital Name: {self.hospital.name}, Location: {self.hospital.location}\n"
        )

        hospital_info += "Departments:\n"

        for dept in self.hospital.departments:
            hospital_info += f" - {dept.name} (Patients: {len(dept.patients)}, Staff: {len(dept.staff)})\n"
        return hospital_info
