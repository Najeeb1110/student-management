from app.repositories.student_repository import StudentRepository
from app.models.student import Student

class StudentService:
    @staticmethod
    def create_student(name, age, email):
        student = Student(name, age, email)
        StudentRepository.add_student(student)
        return {"message": "Student added successfully"}

    @staticmethod
    def get_all_students():
        return StudentRepository.get_students()
    
    @staticmethod
    def get_student_by_email(email):
        return StudentRepository.get_student(email)

    @staticmethod
    def delete_student(email):
        return StudentRepository.delete_student(email)
