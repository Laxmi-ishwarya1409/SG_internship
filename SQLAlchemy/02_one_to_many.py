# ONE TO MANY
from sqlalchemy import Integer,String, Column, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///student_course"

engine = create_engine(db_url,echo=True)

Session = sessionmaker(bind=engine)
session =Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,nullable=False,primary_key=True)
    name = Column(String,nullable=False)

    courses = relationship("Course",back_populates="students")

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer,nullable=False,primary_key=True)
    name = Column(String,nullable=False)
    student_id = Column(Integer,ForeignKey("students.id"))

    students = relationship("Student",back_populates="courses")

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    

def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

Base.metadata.create_all(engine)

# student1 =Student(name="Ishwarya")
# student2 = Student(name="Pranav")

# student1.courses = [
#     Course(name="Python"),
#     Course(name="SQLalchemy")
#     ]

# student2.courses = [
#     Course(name="Python"),
#     Course(name="SQLalchemy"),
#     Course(name="JAVA")
# ]

# session.add_all([student1,student2])
# session.commit()


course = session.query(Course).filter_by(name="Python").first()
if course:
    print(f"Course name : {course.name}")

else:
    print("Course Not Found")




student = session.query(Student).filter_by(name="Ishwarya").first()
if student:
    print(f"Courses of {student.name}:")
    for course in student.courses:
        print(f"{course.name}")

else:
    print("Student Not Found")


# List all students in a particular course

course = session.query(Course).filter_by(name="Python").first()
if course:
    print(f"Students enrolled in {course.name}:")
    print(course.students.name)

else:
    print("Not found")