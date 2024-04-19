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

    # Do we have to just use input() thing here?
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
        return jsonify({"result": result}), status

    def get_patient(self, patient_id):
        result = self.patient_db.select_patient(patient_id)
        if result == None:
            return jsonify({"message": "an error occured"}), 400
        else:
            return jsonify({"patient": result}), 200

    def update_patient(self, patient_id):
        response = self.patient_db.update_patient(patient_id, request.get_json())
        if response == None:
            return jsonify({"message": "an error occured"}), 400
        else:
            return jsonify({"message": "patient updated successfully"}), 200

    def delete_patient(self, patient_id):
        response = self.patient_db.delete_patient(patient_id)
        return "something"

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
