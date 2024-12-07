import os

operation_status="Successful Operation"
defined_input="Enter file name: "
#Write function
def write(file_name):
    try:
        with open(file_name,'w') as file:
            write_text=input("Enter text to Write: ")
            file.write(write_text)
    except PermissionError:
        print("Unable to creat File!")
    else:
        print(operation_status)

#Append Function
def append(file_name):
    try:
        with open(file_name,'a')as file:
            user_input=input("Enter text to Append: ")
            file.write(user_input)
    except PermissionError:
        print("No such file found!")
    except OSError as e:
        print(f"An os error occured {e}")
    else:
        print(operation_status)

#Read Function
def read(file_name):
    try:
        with open(file_name,'r')as file:
            print(file.read())
    except FileNotFoundError:
        print("No file found!")
    except PermissionError:
        print("Permission Error")
    else: 
        print(operation_status)

#Rename Function

def file_opeation(file_name):
    if os.path.exists(file_name):
        new_name=input("Enter new file name: ")
        try:
            os.rename(file_name, new_name)
            print(f"{file_name} renamed to {new_name}")
        except PermissionError:
            print("Permission denied!")
        except OSError as e:
            print(f"OS error encountered {e}")
    else:
        print("no such file found!")

            

print("Welcome to Text Editor using Python")
while True:
    user_choice=int(input("1-> write, 2-> append, 3-> read, 4-> rename file, 5-> exit program: "))
    match(user_choice):
        case 1:
            file_name=input(defined_input)
            write(file_name)
        
        case 2:
            file_name=input(defined_input)
            append(file_name)
        
        case 3: 
            file_name=input(defined_input)
            read(file_name)

        case 4:
            file_name=input(defined_input)
            file_opeation(file_name)
        case 5:
            break