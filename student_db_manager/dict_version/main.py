import logic
import textwrap


def executeUserCommand(studentList,userChoice):
    match userChoice:
        case "1":
            print("\nAdding student...\n")
            studentName=input("please enter student name: ")
            studentEmail=input("please enter student email id: ")

            logic.add_student(studentList,studentName,studentEmail)
            print("\nstudent Added")
        case "2":
            displayAllStudents(studentList)
        case "3":
            studentId=input("please enter student id: ")
            print("\n", end="") 
            studentData=logic.get_student_data(studentList,studentId)
            for key,value in studentData.items():
                 print(f"{key} :{value}")
        case "4":
             studentId=input("please enter student id: ")
             print("\n", end="") 
             logic.delete_student(studentList,studentId)
     
            


def displayAllStudents(studentList):
    
    print("\n") 
 
    for s in studentList:
        for key,value in s.items():
            print(f"{key} :{value}")
        print("\n", end="") # Prints \n and stops there. No extra jump.       
    print("__________________________________________________")




def main():
    studentList=logic.load_data()
    while True:
       

       
        print(textwrap.dedent("""
                 1.Add student
                 2.View All
                 3.Search by ID
                 4.Delete Student 
                 5.Exit            
               """))

        userChoice=input("enter choice: ")

        executeUserCommand(studentList,userChoice)
        if userChoice=="5":
            break
        
        


main() 