from print_line import print_line


def user_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except:
        print_line("Enter valid input")
        return user_choice()