from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

from Models import Student, Assessment, Class, StudentClass, ClassAssessment


from databaseController import DatabaseController as dbController
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://daniel:password@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key_here"

jwt = JWTManager(app)
db = SQLAlchemy(app)


dbController.update_tables(app, db)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    user = Student.query.filter_by(email=email).first()
    if user and password == "1234":  # Replace with actual password validation
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token})
    return jsonify({"message": "Invalid email or password"}), 401
    
        # Create a student

@app.route("/students", methods=["POST"])
@jwt_required
def create_student():
    data = request.get_json()
    new_student = Student(name=data["name"], email=data["email"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added", "student": new_student.as_dict()}), 201
    
    # Get all students
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify({"students": [student.as_dict() for student in students]})
    

    # Get a specific student by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify({"student": student.as_dict()})
    
    # Update a student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    student.name = data["name"]
    student.email = data["email"]
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student updated", "student": student.as_dict()})
    
    # Delete a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})
    
    # Create a class
    
    # Get all classes
@app.route("/classes", methods=["GET"])
def get_classes():
    data = request.get_json()
    classes = Class.query.all()
    return jsonify({"classes": [class_.as_dict() for class_ in classes]})

if __name__ == "__main__":
    app.run(debug=True)