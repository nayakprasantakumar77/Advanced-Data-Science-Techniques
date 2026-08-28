print("HOSPITAL APPOINTMENT SYSTEM")
name= input("Enter patient name: ")
requested= input("Enter requested departments: ")
requested= requested.split(",")
requested= [x.strip() for x  in requested]
available= {"Cardiology", "Neurology","ENT","Orthopedics"}
previous={"ENT","Dermatology"}
emergency= {"Cardiology", "Neurology"}
requested_set= set(requested)
common= requested_set & available
unavailable= requested_set-available
visited= requested_set & previous
emergency_dept= requested_set & emergency
if len(requested)!= len(requested_set):
    duplicate= "Yes"
else:
    duplicate= "No"
if emergency_dept:
    recommended= list(emergency_dept)[0]
elif common:
    recommended= list(common)[0]
else: 
    recommended= "General Medicine"
if common:
    status= "Appointment Confirmed"
else:
    status= "Appointment Not Available"

print("FINAL REPORT")
print("Patient:", name)
print("Requested Departments:", requested_set)
print("Available Departments:", common if common else "None")
print("Unavailable Departments:", unavailable if unavailable else "None")
print("Previously Visited:", visited if visited else "None")
print("Emergency Departments:", emergency_dept if emergency_dept else "None")
print("Duplicate Request:", duplicate)
print("Recommended Department:", recommended)
print("Appointment Status:", status)