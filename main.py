#
class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
    
  # display their information
  def display_info(self):
    print("Name: " + self.name)
    print("Age: " + str(self.age))
    print("Grade: " + str(self.grade))
    print()

#Create at least two instances of the Student class with different attributes
student1 = Student("leo", 15, "A")
student2 = Student("John", 16, "A")

student1.display_info()
student2.display_info()
