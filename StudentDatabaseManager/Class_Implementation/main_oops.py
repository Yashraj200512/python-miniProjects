import logic_oops
import textwrap


def executeUserCommand(student_list,user_choice):
    match user_choice:
        case "1":
            print("\nAdding student...\n")
            student_name=input("please enter student name: ")
            student_email=input("please enter student email id: ")

            logic_oops.add_student(student_list,student_name,student_email)
            print("\nstudent Added")
        case "2":
            displayAllStudents(student_list)
        case "3":
            student_id=int(input("please enter student id: "))
            print("\n", end="") 
            student_data=logic_oops.get_student_data(student_list,student_id)
            print(student_data)
                 
        case "4":
             student_id=int(input("please enter student id: "))
             print("\n", end="") 
             logic_oops.delete_student(student_list,student_id)
     
            


def displayAllStudents(student_list):
    
    print("\n") 
 
    for s in student_list:
        print(s)      
    print("__________________________________________________")




def main():
    student_list=logic_oops.load_data()
    while True:
       

       
        print(textwrap.dedent("""
                 1.Add student
                 2.View All
                 3.Search by ID
                 4.Delete Student 
                 5.Exit            
               """))

        user_choice=input("enter choice: ")
        if user_choice=="5":
            break
        executeUserCommand(student_list,user_choice)
      
        
        


main() 