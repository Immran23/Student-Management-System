students = []

# load file data (program start time)
def load_students():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                students.append({"name": name, "marks": int(marks)})
    except:
        pass

# save file data
def save_students():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['marks']}\n")

# add student
def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    students.append({"name": name, "marks": marks})
    save_students()
    print("✅ Student added")

# show students
def show_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(s["name"], s["marks"])

# search student
def search_student():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print("Found:", s["name"], s["marks"])
            return
    print("❌ Student not found")

# delete student
def delete_student():
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_students()
            print("🗑 Student deleted")
            return
    print("❌ Student not found")

# average marks
def average_marks():
    if not students:
        print("No data")
    else:
        total = sum(s["marks"] for s in students)
        avg = total / len(students)
        print("📊 Average marks:", avg)

# load existing data
load_students()

# menu
while True:
    print("\n1.Add Student")
    print("2.Show Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Average Marks")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        average_marks()
    elif choice == "6":
        break
