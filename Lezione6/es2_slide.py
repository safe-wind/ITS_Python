# 1. Write a class called Student with the attributes name (str) and
# studyProgram (str)
# 2. Create three instances. One for yourself, one for your left neighbour and one
# for our right neighbour.
# 3. Add a method printInfo that prints the name and studyProgram of a
# Student. Test your method on the objects!
# 4. Modify the code and add age and gender to the attributes. Modify your
# printing methods respectively too.

class Student:

    def __init__(self, name:str, study_program:str, age:int, gender:str) -> None:
        self.name = name
        self.study_program  = study_program
        self.age = age
        self.gender = gender

    def printInfo(self) -> None:
        print(f"Name: {self.name}\nStudy program: {self.study_program}\nAge: {self.age}\nGender: {self.gender}")

    def printAge(self) -> None:
        print(f"Age: {self.age}")

    def printCourse(self) -> None:
        print(f"Course: {self.study_program}")




st1 = Student("molowiz", "arte", 25, "m")
st2 = Student("filowiz", "fisica", 27, "m" )
st3 = Student("esu", "data", 26, "m")

st1.printInfo()
print()
st2.printInfo()
print()
st3.printInfo()

