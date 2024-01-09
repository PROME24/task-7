from print_line import print_line


def cash_out(db: dict):
    try:
        cash_out_taka = float(input("Enter amount: "))
        get_available_balance = db.get("balance")

        if (get_available_balance >= cash_out_taka):
            db.update({
                "balance": get_available_balance - cash_out_taka
            })
            print_line("cash out Successfully .")
        else:
            print_line("Insufficient balance")
    except:
        print_line("\nInvalid amount\n")
        return cash_out(db)