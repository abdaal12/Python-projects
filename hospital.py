class Patient:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")
        print("Appointments:")
        for appointment in self.appointments:
            print(f"- {appointment}")
class Appointment:
    def __init__(self, date, time, doctor):
        self.date = date
        self.time = time
        self.doctor = doctor

    def __str__(self):
        return f"{self.date} at {self.time} with Dr. {self.doctor}"
class Billing:
    def generate_bill(self, patient, services):
        total_cost = sum(services.values())
        print(f"Patient: {patient.name}")
        print("Services received:")
        for service, cost in services.items():
            print(f"- {service}: ${cost}")
        print(f"Total Amount: ${total_cost}")
# Creating a patient
patient1 = Patient("John Doe", 30, "Male", "123-456-7890")

# Adding appointments
appointment1 = Appointment("2023-12-25", "10:00 AM", "Smith")
patient1.add_appointment(appointment1)

# Displaying patient information
patient1.display_info()

# Generating a bill
billing = Billing()
services = {"Consultation": 50, "Tests": 100, "Medication": 80}
billing.generate_bill(patient1, services)
