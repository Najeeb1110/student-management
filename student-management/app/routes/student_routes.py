from flask import Blueprint, request, jsonify
from app.services.student_service import StudentService

student_routes = Blueprint("student_routes", __name__)

@student_routes.route("/students", methods=["POST"])
def add_student():
    data = request.json
    response = StudentService.create_student(data["name"], data["age"], data["email"])
    return jsonify(response), 201

@student_routes.route("/students", methods=["GET"])
def get_students():
    students = StudentService.get_all_students()
    return jsonify(students), 200

@student_routes.route("/students/<email>", methods=["GET"])
def get_student(email):
    student = StudentService.get_student_by_email(email)
    if student:
        return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

@student_routes.route("/students/<email>", methods=["DELETE"])
def delete_student(email):
    result = StudentService.delete_student(email)
    if result.deleted_count:
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"message": "Student not found"}), 404
