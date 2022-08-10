#SNIPPET CODE FOR INTRODUCTION
def intro():
    print("Welcome to quiz game!!!")
    playing = input("Do you ready to play? ")
    if playing.lower() != "yes":
        print("OK BYE")
        quit()
    print("Let's begin!!!")
#SNIPPET CODE FOR QUESTIONS
def questions():
    mark=0
    question1 = input("What is the abrevation of CISC? ")
    if question1.lower() == str("complex instruction set computer"):
      print("CORRECT")
      mark=mark+1
    else:
     print("WRONG")
    question2 = input("What is the abrevation of FIFO? ")
    if question2.lower() == str("first in first out"):
     print("CORRECT")
     mark=mark+1
    else:
     print("WRONG")
    question3 = input("What is the abrevation of DNS ? ")
    if question3.lower() == str("domain name system"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question4 = input("What is the abrevation of DOS? ")
    if question4.lower() == str("denial of service") or question4.lower() == str("disk operating system"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question5 = input("What is the abrevation of FPS? ")
    if question5.lower() == str("frames per second"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question6 = input("What is the abrevation of FORTRAN? ")
    if question6.lower() == str("formula translation"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question7 = input("What is the abrevation of GIF? ")
    if question7.lower() == str("graphical interchange format"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question8 = input("What is the abrevation of HFS? ")
    if question8.lower() == str("hierarchical file system"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question9 = input("What is the abrevation of IDE? ")
    if question9.lower() == str("integrated development environment"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    question10 = input("What is the abrevation of ISR? ")
    if question10.lower() == str("interrupt service routine"):
     print("CORRECT")
     mark += 1
    else:
     print("WRONG")
    print("You got " + str(mark)+" Questions correct")
    print("You got " + str((mark/ 10)*100)+"%.")
def main():
    intro()
    questions()
main()
