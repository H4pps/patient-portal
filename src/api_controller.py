"""Patient API Controller"""

from flask import Flask, request, jsonify
from patient_db import PatientDB


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """
    
    def create_patient(self):
        result = self.patient_db.insert_patient(request.get_json())
        status = 200
        if result == None:
            status = 400
            return jsonify({"result": None}), status
        
        return jsonify({"result": result[0]}), status

    def get_patients(self):
        result = self.patient_db.select_all_patients()
        status = 200
        if result == None:
            status = 400

        if request.args.get("search_name") != None:
            for i in range(len(result) - 1,  -1, -1):
                if (result[i]["patient_name"] != request.args.get("search_name")):
                    del result[i]

        return jsonify({"result": result}), status
    
    # Error 500 if the patient is not in the database
    def get_patient(self, patient_id):
        result = self.patient_db.select_patient(patient_id)
        status = 200
        if result == None:
            status = 400

        return jsonify({"result": result}), status

    def update_patient(self, patient_id):
        result = self.patient_db.update_patient(patient_id, request.get_json())
        status = 200
        if result == None:
            status = 400
        
        return jsonify({"result": result}), status

    def delete_patient(self, patient_id):
        result = self.patient_db.delete_patient(patient_id)
        status = 200
        if result == None:
            status = 400

        return jsonify({"result": result}), status

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
