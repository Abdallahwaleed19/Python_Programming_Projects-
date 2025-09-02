class Patient:
    def __init__(self, name , aliemet):
        self.name = name
        self.aliment = aliemet

    def recieve_diagonse(self , diagonse):
        return f"The patient {self.name} recicve {diagonse}"


class Appointment:
    def __init__(self, name, patient_name_list , doctors_name_list , time):
        if patient_name_list:
            self.name = name
            self.patients = [Patient(name , "stomache") for name in patient_name_list]
        if doctors_name_list:
            self.name  = name
            self.doctors = [Doctor(name , "stomache") for name in doctors_name_list]
            
        self.time = time

    def add_patient(self, patient):
        self.patients.append(patient)
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    def get_details(self):
        print(f"Appointment {self.name} , Patient List : {[patient.name for patient in self.patients]} , Doctor List : {[doctor.name for doctor in self.doctors]} , time {self.time}")


class Doctor :
    def __init__(self , name  , specialty):
        self.name  = name 
        self.specialty=  specialty
    def diagonse_patient (self , patient):
        return f"{patient.recieve_diagonse(self.specialty)}"
    

Appointment1 = Appointment("Appointment1" , ["Ahemd" , "Ali"] , ["Abdallah" , "sara"] , "5:00 pm")
Appointment1.add_patient(Patient("Mona" , "Stomache"))
Appointment1.add_doctor(Doctor("Mahmoud" , "Stomacheace Speciallity"))

patient1 = Patient("Ahmed" , "Stomache")
print(patient1.recieve_diagonse("stomcahe"))

doctor1 = Doctor("Abdallah" , "Stomacheace Speciallity")
print(doctor1.diagonse_patient(patient1))
Appointment1.get_details()

