grade = {
    ("John", "Maths"): 4,
    ("Alice", "Biology"): 4,
    ("Eve", "Physics"): 3.5,
    ("Bobby", "English"): 5,
    ("Donald", "Music"): 5
}

john_maths = grade[("John", "Maths")]
print("John Maths Grade is", john_maths)

grade[("Bob", "Math")] = 2
print(grade)

keys = list(grade.keys())

student, subject = keys[0]
print(student, "'s grade in", subject ,"is", john_maths)