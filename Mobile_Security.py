#Mobile Security

class Mobile_Security:

    def __init__(self , owner):

        self.owner = owner 
        self.__password = 1234
        self.__status = "Locked"

    def unlock(self):

        password = input("Enter Password:")

        if password == self.__password:
            self.__status = "Unlocked"
            print("Mobile Unlocked successfully!")
        else:
            print("Wrong password.")

    def lock(self):
        self.__status = "Locked"
        print("Mobile Locked successfully!!")

    def change_password(self):

        if old == self.__password:
           new = input("Enter New password:")
           self.__password = new
           print("Password changed Successfully.")
        else:
            print("Incorrect Old Password.")

    def display(self):

        print("\n=====Mobile Details=====")
        print("Owner :" , self.owner)
        print("Status :" , self.__status)
        print("==========================")

owner = input("Enter Mobile Owner Name:")

mobile = Mobile(Owner)

while True:

  print("\n====Menu====")
  print("1.Unlock Mobile")
  print("2.Lock Mobile")
  print("3.Change Password")
  print("4.Mobile Status")
  print("5.Exit")

  choice = input("Enter choice :")

  if choice == 1:
      mobile.unlock()

  elif choice == 2:
      mobile.lock()

  elif choice == 3:
      mobile.change_password()

  elif choice == 4:
      mobile.display()

  elif choice == 5:
      print("Thank you!!")
      break
    
  else:
      print("Invaild choice.")
      
    
 




        
