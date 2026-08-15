#AUTHOR:      Bradley, Sarah
#UNIT 1:      CMSC315 Data Structures and Analysis
#PURPOSE:     object-oriented programming principles
#DATE:        15Aug2026
#LAST UPDATED:15Aug2026

""""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Athlete:
    activity_type = "Exercise"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name, "Age:", self.age)


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Runner(Athlete):
    sport = "Running"

    def __init__(self, name, age, weekly_miles):
        super().__init__(name, age)
        self.weekly_miles = weekly_miles
        self.runs = []

    def add_run(self, distance):
        self.runs.append(distance)

    # TODO 6: student created extension
    def total_runs(self):
        return len(self.runs)

    def display_info(self):
        print("Name:", self.name, "Age:", self.age,
              "Weekly Miles:", self.weekly_miles, "Runs:", self.runs)

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    runner1 = Runner("Sarah", 26, 25)
    runner2 = Runner("Juan", 28, 15)

    print(Runner.sport)
    print(runner1.sport)

    runner1.favorite_run = "Trail"

    print(runner1.__dict__)
    print(runner2.__dict__)
    print(Runner.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    runner = Runner("Millie", 3, 7)
    runner.add_run(3)
    runner.add_run(5)

    shallow = copy(runner)
    deep = deepcopy(runner)

    runner.add_run(10)

#shallow copy = shares run
#deep copy = seperate runs

    print("Original:", runner.runs)
    print("shallow copy", shallow.runs)
    print("deep copy:", deep.runs)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    athlete = Athlete("Joey", 28)
    athlete.display_info()

    print("\nTODO: Create and test your child object")
    runner = Runner("Dave", 32, 20)
    runner.add_run(3)
    runner.add_run(5)
    runner.display_info()

    print("Total runs:", runner.total_runs())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()