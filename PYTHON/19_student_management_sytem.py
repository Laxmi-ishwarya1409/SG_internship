class Student:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber
        self.__marks = []


    def add_mark(self,mark):
        try:
            if 0 <= mark <=  100:
                self.__marks.append(mark)
            else:
                raise ValueError("Mark should be between 0 and 100")
        except ValueError as ve:
            print(f"error: {ve}")

    def get_name(self):
        return self.name
    
    def get_average(self):
        try:
            if not self.__marks:
                return 0
            else:
                return sum(self.__marks)/len(self.__marks)
        except Exception as e:
            print(f"Error calculating average: {e}")
        
    def display_info(self):
        try:
            print(f"Name: {self.name}, Roll No: {self.rollnumber}, Marks {self.__marks}")
        except Exception as e:
            print(f"Error displaying student info: {e}")

    def calculate_avg(self):
        try:
            avg = self.get_average()
            if avg >= 90:
                return "A"
            elif avg >= 70:
                return "B"
            elif avg >= 50:
                return "C"
            elif avg >= 30:
                return "D"
            else:
                return "Fail"
        except Exception as e:
            print(f"Error calculating grade: {e}")

    def print_result(self):
        print(f"{self.get_name()} | Avg: {self.get_average():.2f} | Grade: {self.calculate_avg()}")


class GraduateStudent(Student):
    def calculate_avg(self):
        avg = self.get_average()
        if avg >= 85:
            return "Distinction"
        elif avg >= 60:
            return "Merit"
        elif avg >= 40:
            return "Pass"
        else:
            return "Fail"
        


s1 = Student("ish", 101)
s1.add_mark(78)
s1.add_mark(92)
s1.add_mark(90)
s1.add_mark(69)
s1.add_mark(-10) 
s1.add_mark(105)  
s1.display_info()
print("Grade:", s1.calculate_avg())
# s1.display_info()
s1.print_result()

s2 = GraduateStudent("Ishwarya", 202)
s2.add_mark(88)
s2.add_mark(91)
s2.display_info()
print("Grade:", s2.calculate_avg())
print("Graduate Grade:", s2.calculate_avg())

# students = [Student("ish", 101), GraduateStudent("Ishwarya", 202)]

# students[0].add_mark(78)
# students[0].add_mark(92)

# students[1].add_mark(88)
# students[1].add_mark(91)

# for s in students:
#     s.print_result()  