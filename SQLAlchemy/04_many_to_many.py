# MANY TO MANY
from sqlalchemy import Column,Integer,String, ForeignKey,Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

student_course_table = Table(
    "student_course_association_table",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"),primary_key=True),
    Column("course_id",ForeignKey("courses.id"),primary_key=True)
)
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,primary_key=True)
    name = Column(String)

    courses = relationship("Course",secondary=student_course_table,back_populates="students")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    
    students = relationship("Student",secondary=student_course_table,back_populates="courses")


engine = create_engine("sqlite:///many_many.db")
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session=Session()


student1 = Student(name="Ishwarya")
student2 = Student(name = "Pranav")

course1 = Course(name = "Python")
course2 = Course(name="SQLAlchemy")
course3 = Course(name = "JAVA")

student1.courses = [course1,course2]
student2.courses = [course1,course3]

session.add_all([student1,student2,course1,course2,course3])
session.commit()

all_students = session.query(Student).all()
for s in all_students:
    print(f"{s.name}")
    for c in s.courses:
        print(f"{c.name}")


student = session.query(Student).filter_by(name="Ishwarya").first()

for c in student.courses:
    if c.name == "Python":
        student.courses.remove(c)
        session.commit()
        print(f"removed course {c} from {student.name}")
        break
    else:
        print("Not Found")
