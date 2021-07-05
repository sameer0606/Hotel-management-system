import  random
import sys
free1_rooms = list(range(1,101))
free2_rooms = list(range(1,101))
free3_rooms = list(range(1,101))
free4_rooms = list(range(1,101))
free5_rooms = list(range(1,101))

booked_free1_rooms = []
booked_free2_rooms = []
booked_free3_rooms = []
booked_free4_rooms = []
booked_free5_rooms = []

floor1_details = {}
floor2_details = {}
floor3_details = {}
floor4_details = {}
floor5_details = {}

def Checkin():
    user = input("Enter free_room and floor number for booking room: ")
    if user == "free_room1":
        user1 = input("Enter book to continue: ")
        if user1 == "book":
            name, phone_no, dob, password = input("Enter your name phone_no D.O.B password respectively: ").split()
            alloted_room = random.choice(free1_rooms)
            booked_free1_rooms.append(alloted_room)
            floor1_details.update({f"Room no{alloted_room}": (name, phone_no, dob, password)})
            print(f"Allotted room: R_1_{alloted_room}")
            print(f"table R_1_{alloted_room}")
        else:
            print("Please enter a valid input")
    elif user == "free_room2":
        user1 = input("Enter book to continue: ")
        if user1 == "book":
            name, phone_no, dob, password = input("Enter your name phone_no D.O.B password respectively: ").split()
            alloted_room = random.choice(free2_rooms)
            booked_free2_rooms.append(alloted_room)
            floor2_details.update({f"Room no{alloted_room}": (name, phone_no, dob, password)})
            print(f"Allotted room: R_2_{alloted_room}")
            print(f"table R_2_{alloted_room}")
        else:
            print("Please enter a valid input")
    elif user == "free_room3":
        user1 = input("Enter book to continue: ")
        if user1 == "book":
            name, phone_no, dob, password = input("Enter your name phone_no D.O.B password respectively: ").split()
            alloted_room = random.choice(free3_rooms)
            booked_free3_rooms.append(alloted_room)
            floor3_details.update({f"Room no{alloted_room}": (name, phone_no, dob, password)})
            print(f"Allotted room: R_3_{alloted_room}")
            print(f"table R_3_{alloted_room}")
        else:
            print("Please enter a valid input")
    elif user == "free_room4":
        user1 = input("Enter book to continue: ")
        if user1 == "book":
            name, phone_no, dob, password = input("Enter your name phone_no D.O.B password respectively: ").split()
            alloted_room = random.choice(free4_rooms)
            booked_free4_rooms.append(alloted_room)
            floor4_details.update({f"Room no{alloted_room}": (name, phone_no, dob, password)})
            print(f"Allotted room: R_4_{alloted_room}")
            print(f"table R_4_{alloted_room}")
        else:
            print("Please enter a valid input")
    elif user == "free_room5":
        user1 = input("Enter book to continue: ")
        if user1 == "book":
            name, phone_no, dob, password = input("Enter your name phone_no D.O.B password respectively: ").split()
            alloted_room = random.choice(free5_rooms)
            booked_free5_rooms.append(alloted_room)
            floor5_details.update({f"Room no{alloted_room}": (name, phone_no, dob, password)})
            print(f"Allotted room: R_5_{alloted_room}")
            print(f"table R_5_{alloted_room}")
        else:
            print("Please enter a valid input")
    else:
        print("Please enter a valid input")

def CheckOut():
    user_floor = int(input("Enter your floor number: "))
    user_room_num = int(input("Enter your room number: "))
    if user_floor == 1:

        if user_room_num in booked_free1_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor1_details.get(f"Room no{user_room_num}"):
                floor1_details.pop(f"Room no{user_room_num}")
                print("You have successfully Checked out")

    if user_floor == 2:

        if user_room_num in booked_free2_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor2_details.get(f"Room no{user_room_num}"):
                floor2_details.pop(f"Room no{user_room_num}")
                print("You have successfully Checked out")

        else:
            print("Please enter a valid input")
    if user_floor == 3:

        if user_room_num in booked_free3_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor3_details.get(f"Room no{user_room_num}"):
                floor3_details.pop(f"Room no{user_room_num}")
                print("You have successfully Checked out")

        else:
            print("Please enter a valid input")

    if user_floor == 4:

        if user_room_num in booked_free4_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor4_details.get(f"Room no{user_room_num}"):
                floor4_details.pop(f"Room no{user_room_num}")
                print("You have successfully Checked out")
        else:
            print("Please enter a valid input")
    if user_floor == 5:
        if user_room_num in booked_free5_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor5_details.get(f"Room no{user_room_num}"):
                floor5_details.pop(f"Room no{user_room_num}")
                print("You have successfully Checked out")
        else:
            print("Please enter a valid input")
    else:
        print("Please enter a valid input")

def book_meal():
    user_floor = int(input("Enter your floor number: "))
    user_room_num = int(input("Enter your room number: "))
    if user_floor == 1:

        if user_room_num in booked_free1_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor1_details.get(f"Room no{user_room_num}"):
                food = input("What you want eat: ").split()
                print(f"{food}: Your food will be delivered in 30 minutes")

    if user_floor == 2:

        if user_room_num in booked_free2_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor2_details.get(f"Room no{user_room_num}"):
                food = input("What you want eat: ").split()
                print(f"{food}: Your food will be delivered in 30 minutes")

        else:
            print("Please enter a valid input")
    if user_floor == 3:

        if user_room_num in booked_free3_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor3_details.get(f"Room no{user_room_num}"):
                food = input("What you want eat: ").split()
                print(f"{food}: Your food will be delivered in 30 minutes")
        else:
            print("Please enter a valid input")

    if user_floor == 4:

        if user_room_num in booked_free4_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor4_details.get(f"Room no{user_room_num}"):
                food = input("What you want eat: ").split()
                print(f"{food}: Your food will be delivered in 30 minutes")
        else:
            print("Please enter a valid input")
    if user_floor == 5:
        if user_room_num in booked_free5_rooms:
            name, phoneno, dob, password = input("Enter your details: ").split()
            if (name, phoneno, dob, password) == floor5_details.get(f"Room no{user_room_num}"):
                food = input("What you want eat: ").split()
                print(f"{food}: Your food will be delivered in 30 minutes")
        else:
            print("Please enter a valid input")
    else:
        print("Please enter a valid input")




print("------**** WELCOME TO BEING ARTIFEX HOTEL MANAGEMENT SYSTEM ****------")
while(True):
    print("1. Enter 1 for Check in")
    print("2. Enter 2 for Check out")
    print("3. Enter 3 in order to book meal")
    print("4. Enter ok for Exit")
    user = input("Enter your option: ")
    if user == "1":
        Checkin()
    elif user == "ok":
        sys.exit("thanks for using being artifex hotel management system")
    elif user=="2":
        CheckOut()
    elif user== "3":
        book_meal()
    else:
        print("Please enter a valid option")