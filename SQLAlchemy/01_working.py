from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker
import random

db_url = "sqlite:///working.db"
engine = create_engine(db_url,echo=True)

Session = sessionmaker(bind=engine)
session=Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=False)
    branch = Column(String(20),nullable=False)


    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', branch='{self.branch}')>"


Base.metadata.create_all(bind=engine)



student1 = Student(name="Ishwarya",branch="CSE")
student2 = Student(name="Pranav",branch="CSE")
student3 = Student(name="Laxmi Ishwarya",branch="CSE")


session.add(student1)
session.add_all([student2,student3])
session.commit()


students = session.query(Student).all()
for student in students:
    print(f"{student.id}: {student.name} - {student.branch}")



student = students[0]
print(student)
print(student.id)
print(student.name)
print(student.branch)


students_names = session.query(Student.name).all()
for student in students_names:
    print(student)


first_student = session.query(Student).first()
print(first_student)


filter_by_result = session.query(Student).filter_by(branch="CSE").all()
# print(filter_by_result)
for student in filter_by_result:
    print(student.name)


update_record = session.query(Student).filter_by(id=1).one_or_none()
print(update_record.name)
update_record.name= "Gopathi"
print(update_record.name)
session.commit()


delete_record = session.query(Student).filter_by(id=6).one_or_none()
# session.delete(delete_record)
session.commit()




# adding random data to the database
names = ["vicky","lucky","mani","cherry","kanna","deepu","nishi"]
branch = [3,6,15,11,10]
for i in range(10):
    student=Student(name=random.choice(names),branch=random.choice(branch))

    session.add(student)
    session.commit()



student_order_by = session.query(Student).order_by(Student.name).all()
print(student_order_by)


student_orderby = session.query(Student).order_by(Student.branch.desc()).all()
for student in student_orderby:

    print(f"{student.id} | {student.name} | {student.branch}")



limit_students = session.query(Student).order_by(Student.name).limit(5).all()
print(limit_students)


filter_student = session.query(Student).filter(Student.branch>10)
for student in filter_student:
    print(student)


group_by_student = session.query(Student).group_by(Student.name).all()
print(group_by_student)


groupby_students = session.query(Student.name,func.count(Student.id)).group_by(Student.branch).all()
print(groupby_students)