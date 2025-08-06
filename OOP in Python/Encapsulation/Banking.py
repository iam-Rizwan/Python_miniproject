class ATM:
    def __init__(self, client, balance=30000000):
        self.__client = client      
        self.__balance = balance    

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful! New Balance: {self.__balance}")
        else:
            print("Insufficient Balance!")

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit successful! New Balance: {self.__balance}")

    def check_balance(self):
        print(f"Your Current Balance: {self.__balance}")

valid_client=["Rizwan"]

print("----------- Welcome to ATM Service -----------")
name = input("Enter your name: ")

if name in valid_client:
    print(f"\t Hello  {name}!")
    atm = ATM(client=name)
    while True:
        print("\nChoose an option:")
        print("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Thank you for using our ATM service!")
            break
        else:
            print("Invalid choice! Please try again.")
        break
