student_data = [
  {
          "ID": 1,
          "Name": "Alice",
          "Age": 20,
          "Major": "Computer Science",
          "GPA": 3.7
  },
  {
          "ID": 2,
          "Name": "Bob",
          "Age": 21,
          "Major": "Engineering",
          "GPA": 3.9
  }
    ]
# Function to get a student by ID
def get_student_by_id(data, student_id):
  for student in data:
    if student["ID"] == student_id:
       return student
  return None
# Function to get all students
def get_all_students(data):
  return data
# Function to get students by major
def get_students_by_major(data, major):
  students = [student for student in data if student["Major"] == major]
  return students
# Function to add a new student
def add_student(data, name, age, major, gpa):
  new_student = {
          "ID": len(data) + 1,
          "Name": name,
          "Age": age,
          "Major": major,
          "GPA": gpa
      }
  data.append(new_student)
  return new_student
 # Function to find common majors in two student data lists
def find_common_majors(data1, data2):
   majors1 = set(student["Major"] for student in data1)
   majors2 = set(student["Major"] for student in data2)
   common_majors = majors1.intersection(majors2)
   return common_majors
# Function to delete a student by ID
def delete_student_by_id(data, student_id):
  for student in data:
     if student["ID"] == student_id:
        data.remove(student)
        return True
  return False
# Function to calculate the average GPA of all students
def calculate_average_gpa(data):
  total_gpa = sum(student["GPA"] for student in data)
  average_gpa = total_gpa / len(data)
  return average_gpa
# Function to get top performers by GPA
def get_top_performers(data, num_top):
  sorted_students = sorted(data, key=lambda x: x["GPA"], reverse=True)
  top_performers = [(student["Name"]) for student in sorted_students[:num_top]]
  return top_performers
# Main menu loop
while True:
  print("""
1. Get Student by ID
2. Get All Students
3. Get Students by Major
4. Add Student
5. Find Common Majors
6. Delete Student
7. Calculate Average GPA
8. Get Top Performers
9. Exit
- - - - - - - - - - - - - - -""")
  choice = input("Enter your choice (1-9): ")
  if choice == "1":
   student_id = int(input("Enter the student's ID: "))
   student = get_student_by_id(student_data, student_id)
   if student:
      print("Student information:")
      for key, value in student.items():
       print(f"{key}: {value}")
   else:
      print("Student not found.")

  elif choice == "2":
   all_students = get_all_students(student_data)
   print("All students:")
   for student in all_students:
      print(student)

  elif choice == "3":
    major = input("Enter the major: ")
    students = get_students_by_major(student_data, major)
    if students:
     print(f"Students in {major}:")
     for student in students:
        print(student)
    else:
      print(f"No students found in {major}.")
  elif choice == "4":
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    major = input("Enter the student's major: ")
    gpa = float(input("Enter the student's GPA: "))
    new_student = add_student(student_data, name, age, major, gpa)
    print(f"New student added with ID {new_student['ID']}")
  elif choice == "5":
  # Assuming you have another student data list, data2
   common_majors = find_common_majors(student_data, data2)
   print("Common majors:", common_majors)
  elif choice == "6":
    student_id = int(input("Enter the student's ID to delete: "))
    if delete_student_by_id(student_data, student_id):
      print("Student deleted.")
    else:
       print("Student not found.")
  elif choice == "7":
    average_gpa = calculate_average_gpa(student_data)
    print(f"Average GPA of all students: {average_gpa:.2f}")
  elif choice == "8":
    num_top = int(input("Enter the number of top performers to retrieve: "))
    top_performers = get_top_performers(student_data, num_top)
    print(f"Top {num_top} performers by GPA:")
    for student in top_performers:
      print(student)
  elif choice == "9":
    print("Exiting the program.")
    break
  else:
   print("Invalid choice. Please enter a number from 1 to 9.")
