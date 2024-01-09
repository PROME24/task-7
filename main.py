from command import command
from user_choice import user_choice
from helpline import helpline
from my_account import my_account
from paybill import pay_bill
from cash_out import cash_out
from payment import payment
from send_mony import send_mony 

def main():
    isQuit = False
    [account_details, db] = my_account()
    while (not isQuit):
        command()
        choice = user_choice()
        if (choice == 1):
            send_mony(db())
        elif (choice == 2):
            payment(db())
        elif (choice == 3):
            cash_out(db())
        elif (choice == 4):
            pay_bill(db())
        elif (choice == 5):
            account_details()
        elif (choice == 6):
            helpline()
        elif (choice == 7):
            isQuit = True


main()