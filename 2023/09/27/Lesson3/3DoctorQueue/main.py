import time
import resources

# Pre-Requisites:
resources.load() # Testing the resources plugin to see if its working

patients = {
    0 : {"Name": "Jimmy", "Priority": False, "Doctor": "Dr. Smith"},
    1 : {"Name": "Sarah", "Priority": True, "Doctor": "Dr. Smith"},
    2 : {"Name": "Bob", "Priority": False, "Doctor": "Dr. Joe"},
    3 : {"Name": "Dan", "Priority": False, "Doctor": "Dr. Joe"},
}

resources.test() # Asking user whether they are testing the program or not



