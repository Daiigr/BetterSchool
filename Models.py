from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)

    password = db.Column(db.String(50), nullable=False) # this needs to be hashed in the future
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_email = db.Column(db.String(100), unique=True, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Class(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    instructor_name = db.Column(db.String(100), nullable=False)
    class_schedule = db.Column(db.String(200), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Assessment(db.Model):
    __tablename__ = 'assessments'
    assessment_id = db.Column(db.Integer, primary_key=True)
    assessment_name = db.Column(db.String(100), nullable=False)
    assessment_type = db.Column(db.String(50), nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)
    weightage = db.Column(db.DECIMAL(3,2), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class StudentClass(db.Model):
    __tablename__ = 'student_classes'
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), primary_key=True)

    student = db.relationship('Student', backref=db.backref('student_classes', lazy=True))
    cls = db.relationship('Class', backref=db.backref('student_classes', lazy=True))

class ClassAssessment(db.Model):
    __tablename__ = 'class_assessments'
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.assessment_id'), primary_key=True)

    cls = db.relationship('Class', backref=db.backref('class_assessments', lazy=True))
    assessment = db.relationship('Assessment', backref=db.backref('class_assessments', lazy=True))