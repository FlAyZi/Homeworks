'''Create a Python class representing a Hospital account with methods to schedule visit
and remove schedule'''


class HospitalAccount:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.schedule = []

    def schedule_visit(self, date, time):
        appointment = {"date": date, "time": time}
        self.schedule.append(appointment)
        print(f"Visit scheduled for {self.patient_name} on {date} at {time}.")

    def remove_schedule(self, date, time):
        appointment = {"date": date, "time": time}
        if appointment in self.schedule:
            self.schedule.remove(appointment)

    def view_schedule(self):
        if self.schedule:
            for appointment in self.schedule:
                print(f"Date: {appointment['date']}, Time: {appointment['time']}")
