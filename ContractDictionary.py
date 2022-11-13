Userinfos = []
first = {"Fullname": "Joshua", "Age": "18", "Course": "Bscoe","Gender": "Male","Address": "Taytay","Number": "0912312312"}
second = {"Fullname": "Roi", "Age": "22", "Course": "Bsece","Gender": "Male","Address": "Bicol","Number": "09121231123"}
third = {"Fullname": "Bev", "Age": "18", "Course": "Bscoe","Gender": "Female","Address": "Jalajala","Number": "09121231123"}
fourth = {"Fullname": "Josep", "Age": "18", "Course": "Bscoe","Gender": "Male","Address": "Caloocan","Number": "09121231123"}

Userinfos.append(first)
Userinfos.append(second)
Userinfos.append(third)
Userinfos.append(fourth)

def menu():
    print("\n+++++++++++++++++++ME-N-U+++++++++++++++++++"
          "\n\t1 -> Add an Contact"
          "\n\t2 -> Search a Contact"
          "\n\t3 -> View All Contacts"
          "\n\t4 -> Exit")


def add():
    try:
        user = {"Fullname": input("\n\t\tEnter User Full Name: ").capitalize(), "Age": input("\t\tEnter User Age: "),"Course": input("\t\tEnter User Course: ").capitalize(), "Gender": input("\t\tEnter User Gender: ").capitalize(),"Address": input("\t\tEnter User Address: ").capitalize(), "Number": input("\t\tEnter User Mobile Number: : ")}
    except:
        print("Invalid Input!!!")
    else:
        Userinfos.append(user)

def search():
    contact = 0
    try:
        keySearch = str(input("\n\t\tWhat do key you want to find? (Fullname/Age/Course/Gender/Address/Number): ")).capitalize()
        varsearch = str(input("\t\tEnter the value: ")).capitalize()
    except:
        print("Invalid Input!!!")
    else:
        for i in range(len(Userinfos)):
            currentuser = Userinfos[i]
            if varsearch == currentuser[keySearch]:
                contact += 1
                print("\t\t----------------------------------------------")
                print("\n\n\t\tFullname: ", currentuser["Fullname"])
                print("\t\tAge: ", currentuser["Age"])
                print("\t\tCourse: ", currentuser["Course"])
                print("\t\tGender: ", currentuser["Gender"])
                print("\t\tAddress: ", currentuser["Address"])
                print("\t\tMobile Number: ", currentuser["Number"])
                print("\t\t----------------------------------------------")
        print("\n\t\tThe total number of matched contact is", contact)

def view():
    num = 0
    for i in range(len(Userinfos)):
        num += 1
        currentuser = Userinfos[i]
        print("\n\n\t\tFullname: ",currentuser["Fullname"])
        print("\t\t----------------------------------------------")
        print("\t\tAge: ",currentuser["Age"])
        print("\t\tCourse: ",currentuser["Course"])
        print("\t\tGender: ",currentuser["Gender"])
        print("\t\tAddress: ",currentuser["Address"])
        print("\t\tMobile Number: ",currentuser["Number"])
        print("\t\t----------------------------------------------")
        print("\n\t\tThe total number of contacs is", num)

ans = "Y"
while ans == "Y":
    menu()
    try:
        choice = int(input("\n\tInput your choice: "))
    except ValueError:
        print("\n\tInvalid Input! Try Again!")
    else:
        if choice == 1:
            add()
        elif choice == 2:
            search()
        elif choice == 3:
            view()
        elif choice == 4:
            print("\n\n\t Thank you for using me!")
            break
        else:
            print("\t\tInput Error! Try Again!")

        ans = input("\n\tWould you like to go back to Menu (y) or Exit (n): ").upper()