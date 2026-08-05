class BankAccount:

  def __init__(self, name, acc_no, balance):
    self.name = name
    self.acc_no = acc_no
    self.__balance = balance

  def deposit(self):
        amount = float(input("Enter Deposit Amount : "))
        self.__balance += amount
        print("Amount Deposited Successfully.")

  def withdraw(self):
        amount = float(input("Enter Withdraw Amount : "))
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

  def check_balance(self):
        print("Current Balance :", self.__balance)

  def display(self):
        print("\nAccount Holder :", self.name)
        print("Account Number :", self.acc_no)
        print("Balance :", self.__balance)


name = input("Enter Account Holder Name : ")
acc_no = input("Enter Account Number : ")
balance = float(input("Enter Opening Balance : "))

obj = BankAccount(name, acc_no, balance)

while True:

    print("\n----- MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        obj.deposit()

    elif choice == "2":
        obj.withdraw()

    elif choice == "3":
        obj.check_balance()

    elif choice == "4":
        obj.display()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
