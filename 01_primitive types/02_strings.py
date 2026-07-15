##

course = "Python Programming"
message = """
Hi Deep,
I hope you are doing well. I am writing to you regarding the Python Programming course that you recently enrolled in. I wanted to check in and see how you are finding the course so far.
I hope you are enjoying the course and finding it helpful. If you have any questions or need any assistance, please don't hesitate to reach out to me. I am here to help you succeed in your learning journey.
Best regards,
John Doe
"""

print(len(course))  # 18

print(course[0])  # P
print(course[-1])  # g

print(course[0:3])  # Pyt
print(course[0:])  # Python Programming
print(course[:3])  # Pyt
print(course[:])  # Python Programming

# escape sequences
course = "Python \"Programming\""
print(course)  # Python "Programming"

# formatting strings
first = "Deep"
last = "Vadukiya"
full = f"{len(first)} {last}"  # f-string
print(full)  # Deep Vadukiya

# string methods
print(course.upper())  # "PYTHON PROGRAMMING"
print(course.lower())  # "python programming"
print(course.title())  # "Python Programming"
print(course.strip())
# .strip() "Python Programming" remoes whitespace from the beginning and end of the string
print(course.find("thon"))  # 2
print(course.replace("thon", "thon Programming"))  # "Python Programming"
print("Python" in course)  # True
print("Python" not in course)  # False
