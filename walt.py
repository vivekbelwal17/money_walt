#setting up the wallet balance 
wallet_balance =0.0
transaction_history=[]
 
print("welcome to the personal wallet system!\n")
while True:
    print("\n"+"_"*20)
    print("1. add Income"
        "\n2.add Expences"
        "\n3. view balance & history"
        "\n0.exit"
        "\n"+"_"*20)
    choice = input("Enter your choice (0-3): ")
    if choice == "1":
        ammount  = float(input("Enter the ammount to add : ₹"))
        wallet_balance= wallet_balance + ammount
        
        #
        transaction_history.append({"type": "Income", "amount": ammount})
        print(f"success!₹{ammount} added to your wallet.")
        
    elif choice == "2":
        ammount = float(input("Enter The expence ammount: ₹"))
        if ammount >wallet_balance:
            print("Insufficient balance! Transaction failed.")
        else:
            wallet_balance = wallet_balance -ammount
            transaction_history.append({"type":"Expense", "amount": ammount})
            print(f"success!₹{ammount} deducted from your wallet.")
            
    elif choice == "3":
        print("\n" + "*" * 10 + " wallet status " + "*" * 10)
        print(f"Current balance: ₹{wallet_balance}")
        print("Transaction history:")
        
        if len(transaction_history) == 0:
            print("No transactions yet.")
        else:
           for t in transaction_history:
                print(f" - {t['type']}: ₹{t['amount']}")
                
    elif choice =="0":
        print(f"clossing the wallet.your final balance is ₹{wallet_balance}. Namastae!")
        break 
    else:
        print("Invalid choice please enter a valid number (0-3).")