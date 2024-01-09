from print_line import print_line


def payment(db: dict):
    try:
        user_payment = float(input("Enter amount: "))
        get_available_balance = db.get("balance")

        if (get_available_balance >= user_payment):
            db.update({
                "balance": get_available_balance - user_payment
            })
            print_line("payment Successfully .")
        else:
            print_line("Insufficient balance")
    except:
        print_line("\nInvalid amount\n")
        return payment(db)