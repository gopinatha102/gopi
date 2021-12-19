from Bankclass import *
print("Welcome to ", Bank.Bank_Name)
print("*" * 30)
print("  *************  Choice ************* ")
print("*" * 10, "0----------- Display  Account", "*" * 10)
print("*" * 10, "1------------add new account", "*" * 10)
print("*" * 10, "2------------Deposit Amount", "*" * 10)
print("*" * 10, "3------------Withdraw Amount", "*" * 10)
print("*" * 10, "4------------Display All Account details : ", "*" * 10)
print("*" * 10, "5------------Interst_calcuation ", "*" * 10)
print("*" * 10, "5------------Continue ", "*" * 10)
print("*" * 10, "6 ---------- Quit the program", "*" * 10)

while True:
    print("*" * 30)
    option = int(input("Enter the specified Number in operation: "))
    print("*" * 30)
    if option == 0:
        obj.display_Account_Details()
        obj.bank_details()
    elif option == 1:
        print("*" * 30)
        print("Welcome to New account Creating")
        print("*" * 30)
        n = int(input("Enter The number of New account Creating:"))
        for i in range(n):
            obj = Bank()
            name = input("Enter The New Account Name")
            account_no = int(input("Enter The account Number :"))
            amt = float(input("Enter The account amount"))
            #obj.add_new_account(name, account_no, amt)
            obj.add_new_account(name, account_no, amt)
            l.append(obj)

    elif option == 2:
        print("*" * 30)
        print("\tDeposit Mode")
        obj.deposit_mode_selection()

    elif option == 3:
        print("*" * 30)
        print("\t Withdraw Mode ")
        obj.withdraw_mode_selection()

    elif option == 4:
        obj.display_all_account_details()

    elif option == 5:
        years = float(input("Enter the No Years :"))
        rate = float(input("Enter the rate of interst"))
        obj.interst_calcuation(years, rate)

    elif option == 6:
        continue

    elif option == 7:
        break

    else:
        print("correct option ")

print("*"*30)
print("Thank you from visiting Banking Application")
print("*"*30)


