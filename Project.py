class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("Your balance is 50000")
    def withdrawal(self, amount):
        new_amount = 50000 - amount
        print(new_amount)
    def main():
        Cardnumber=input("insert your card number:-")
        pinnumber=input("Enter your pin number:-")
        new_user= Atm(Cardnumber, pinnumber)
        print("Choose your activity")
        print("1.Balance Enquiry 2.Withdrawal")
        activity = int(input("enter activity number :- "))
         if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")
if __name__ == "__main__":
    main()
   

    
     
