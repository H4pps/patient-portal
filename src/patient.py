"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import config
from api_controller import PatientAPIController

import datetime
import uuid
import time

class Patient:
    def __init__(self, name: str, gender: str, age: int):
        self.patient_id = str(uuid.uuid4())
        self.patient_name = name
        self.patient_age = age
        if gender not in config.GENDERS:
            raise Exception()
        self.patient_gender = gender
        self.patient_checkin = datetime.datetime.now()
        self.patient_checkout = None
        self.patient_ward = None
        self.patient_room = None

    def updateRoomAndWard(self, room, ward):
        if room in config.ROOM_NUMBERS and ward in config.WARD_NUMBERS and (room // 10) == ward:
            self.patient_room = room
            self.patient_ward = ward
        else:
            raise Exception()
        
    def commitPatient(self, controller):
        result = controller.patient_db.insert_patient(self.__dict__)
        if result == None:
            print("Error occured while adding the patient into patient_db")
        else:
            print("Success")
  
# newPatient = Patient("Vasyok", "Male", 20)
API_Controller = PatientAPIController()
time.sleep(3)
newPatient = Patient("Vasyok", "Male", 14)
newPatient.commitPatient(API_Controller)