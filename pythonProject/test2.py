
l=list()
class Bank:
    Bank_Name = "SBI Bank"
    Bank_Address = "Bangalore"
    Bank_IFSC_Code = "SBI49000"
    #amount = 0

    # noinspection PyShadowingNames
    def __init__(self,name,address,account_no,phonno,amt=0):
        self.name=name
        self.address=address
        self.account_no = account_no
        self.phonno=phonno
        self.amount=amt

    def Account_Detials(self):
        print("Name of New Account ", self.name)
        print("Address of New account Holder", self.address)
        print("New Account Number ", self.account_no)
        print("Phone Number of New Account Holder ", self.phonno)
        print("Total Balance Account is  ", self.amount)

    # noinspection PyShadowingNames
    def New_Account(self, name, address, account_no, phonno,amt=0):
        self.name = name
        self.address = address
        self.phonno = phonno
        self.account_no=account_no
        self.amount=amt

        print("Name of New Account ",self.name)
        print("Address of New account Holder",self.address)
        print("New Account Number ", self.account_no)
        print("Phone Number of New Account Holder ",self.phonno)
        print("Balance of account is",Bank.amount)
        for i in range(len(l)):
            print(l[i].name, l[i].address, l[i].account_no, l[i].phonno,l[i].amount)

    def Display(self):
        print("Name of New Account ", self.name)
        print("Address of New account Holder", self.address)
        print("New Account Number ", self.account_no)
        print("Phone Number of New Account Holder ", self.phonno)
        print("Balance of account is", self.amount)

    # noinspection PyShadowingNames
    def Deposit(self, amt):
        self.amount = self.amount + amt
        print("Balance in your Account is ", self.amount)
        return self.amount

    # noinspection PyShadowingNames
    def change_account_no(self,account_no):
        self.account_no = account_no
        print("after Changing account Number ")

    # noinspection PyShadowingNames
    def display_change_phoneno(self):
        for i in range(len(l)):
            print(l[i].name, l[i].address, l[i].account_no, l[i].phonno)

print("***********************Welcome Bank Application **************************")
print("*********************** Welcome SBI BANK        **************************")
print("  *************  Choice ************* ")
print("0---------------for default Account")
print("1------------for Add New Account")
print("2------------Deposit Amount")
print("3------------Withdraw Amount")
print("4------------Balance Details  ")
print("5------------Check Deposit")
print("6------------DD Deposit")
print("7------------Bank Details Check")
print("8------------Withdraw Check Amount")
print("9------------Withdraw DD Amount")
print("10-----------Interst Calculation")
print("11----------- Account Details")
print("12 --------------Quit the program")
print("Enter other keys program continues")

while True:
    option = int(input("Enter the options::"))
    obj = Bank(name="Gopi",address="srinivaspur",account_no="64057521691", phonno=9964474302,amt=0)
    l.append(obj)
    if option == 0:
            print("*" * 30)
            obj.Account_Detials()
            print(" Thank you choosing SBI Bank")

    elif option == 1:
        print("*" * 30)
        n=int(input("Enter The Number of New account create:"))
        for i in range(n):
            name = input("Enter the New Account Create:")
            address = input("Enter the New Account Create are Address:")
            account_no = int(input("Enter the Account Number "))
            phonno = int(input("Enter the New Account Create Phone Number:"))
            amt=int(input("Enter the Amount "))
            obj=Bank(name,address,account_no,phonno,amt)
            #obj.New_Account(name,address,account_no,phonno)
            l.append(obj)
        for l2 in l:
            print("*" * 30)
            print("name is {} address {} account {} phono {} Balance  {}".format(l2.name,l2.address,l2.account_no,l2.phonno,l2.amount))

    elif option == 2:
        print("*" * 30)
        print("\tDeposit Mode")
        print("*" * 30)
        count_no_obj = len(l)
        for i in range(count_no_obj-1):
            name = input("Enter Depositor  Name :")
            print("*" * 30)
            print("\t",l[i].name)
            if l[i].name == name:
                print("*" * 30)
                amt = int(input("Enter the Deposit  amount:"))
                l[i].amount = l[i].amount+amt
                print("adding amount  is ", l[i].amount)
            else:
                print("Name not matched ")
        obj.Display()

    elif option == 3:
        print("*"*30)
        print("\tWithdraw Mode")
        print("*" * 30)
        count_no_obj = len(l)
        print(count_no_obj)
        for i in range(count_no_obj-1):
            name = input("Enter Withdraw Account Name :")
            print("*" * 30)
            print("\t", l[i].name)
            if l[i].name == name:
                # if l[i].name in name:
                print("*" * 30)
                amt = int(input("Enter the amount:"))
                l[i].amount = l[i].amount-amt
                print("After withdraw Balance  ", l[i].amount)
            else:
                print("Name not matched ")

    elif option == 4:
        print("*"*30)
        obj.Balance_Check()

    elif option == 5:
        print("*"*30)
        check_no = int(input("Enter The Check Number:"))
        check_amount = float(input("Enter The check Amount:"))
        obj.Check_Deposit(check_no, check_amount)

    elif option == 6:
        print("*" * 30)
        Dd_no = int(input("Enter The DD Number:"))
        Dd_amount = float(input("Enter The DD Amount:"))
        obj.DD_Deposit(Dd_no, Dd_amount)

    elif option == 7:
        print("*" * 30)
        obj.Bank_Details()

    elif option == 8:
        print("*" * 30)
        check_no=int(input("Enter the Check Number"))
        check_amount=float(input("Enter The Check Amount"))

        obj.Withdraw_check_Amount(check_no,check_amount)

    elif option == 9:
        print("*" * 30)
        dd_no = int(input("Enter the DD Number"))
        dd_amount = float(input("Enter The DD Amount"))
        obj.Withdraw_DD_Amount(dd_no, dd_amount)

    elif option == 10:
        print("*" * 30)
        rate=float(input("Enter the Rate of Interst"))
        years=int(input("Enter the Number of Years "))
        obj.Interst_calcuation(rate,years)

    elif option == 11:
        print("*" * 30)
        obj.Display()

    elif option == 12:
        print("*" * 44)
        break
        quit()
    elif option == 13:
        print("*" * 30)
        obj.Display_Account_Details()

    elif option == 14:
        print("*" * 30)
        print("Changing phone Number in account :")
        count_no_obj=len(l)
        for i in range(count_no_obj):
            name=input("Enter the Name :")
            print("*" * 30)
            print(l[i].name)
            if l[i].name == name:
            #if l[i].name in name:
                print("*" * 30)
                phonno=int(input("Enter the changing phono Number:"))
                l[i].phonno=phonno
                print("Changed phoneno is this ",l[i].phonno)
            else:
                print("Name not matched ")
        obj.display_change_phoneno()

    else:
        print("*"* 30)
        print("Enter to continue press other the keys  ")
        print("*" * 30)
        continue

print("Thank you from visiting Banking Application")
print("********************************************")