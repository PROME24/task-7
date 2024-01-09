from print_line import print_line


def send_mony(db: dict):
    try:
        user_send_taka = float(input("Enter amount: "))
        get_available_balance = db.get("balance")

        if (get_available_balance >= user_send_taka):
            db.update({
                "balance": get_available_balance - user_send_taka
            })
            print_line("send money Successfully .")
        else:
            print_line("Insufficient balance")
    except:
        print_line("\nInvalid amount\n")
        return send_mony(db)