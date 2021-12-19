class Bank:
    Bank_Name = "SBI"
    Bank_Address = "Bangalore"
    Bank_IFCS_Code = "SBI00049"

    def __init__(self) -> object:
        """

        :rtype: object
        """
        self.dd_no = 0
        self.check_no = 0
        self.name = "Gopi"
        self.account_no = 650
        self.balance = 1000

    def add_new_account(self, name, account_no, amt):
        self.name = name
        self.account_no = account_no
        self.balance = amt
        obj.display_Account_Details()

    def deposit(self):
        len_obj = len(l)
        print(len_obj)
        name = input("Enter the Deposit Name:")
        account_no = int(input("Enter the Deposit account"))
        for i in range(len_obj):
            print(l[i].name, l[i].account_no, l[i].balance)
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the deposit amount"))
                l[i].balance += amt
                print("Balance of after ", l[i].balance)

    def check_deposit(self, check_no):
        self.check_no = check_no
        name = input("Enter the Deposit Name:")
        account_no = int(input("Enter the Deposit account"))
        len_obj = len(l)
        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the deposit amount"))
                l[i].balance += amt
                print("Balance of after ", l[i].balance)

        print("Check No ", self.check_no)
        print("After Cheek Deposit Account Details")
        obj.bank_details()
        obj.display_Account_Details()

    def dd_deposit(self, dd_no):
        self.dd_no = dd_no
        name = input("Enter the Deposit Name:")
        account_no = int(input("Enter the Deposit account"))
        len_obj = len(l)
        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the deposit amount"))
                l[i].balance += amt
                print("After Cheek Deposit Account Details", l[i].balance)

        print("Check No ", self.dd_no)
        obj.bank_details()
        obj.display_Account_Details()

    def display_Account_Details(self):
        print("Account Holder Name ", self.name)
        print("Account Number is ", self.account_no)
        print("Account Balance is ", self.balance)
        print("*" * 30)

    @classmethod
    def bank_details(cls):
        print("*" * 30)
        print("Bank Name is ", Bank.Bank_Name)
        print("Bank Place is ", Bank.Bank_Address)
        print("Bank IFCS code is", Bank.Bank_IFCS_Code)
        print("*" * 30)

    @staticmethod
    def display_all_account_details():
        for l2 in l:
            print("name\t account No\t balance\t")
            print(l2.name, "\t", l2.account_no, "\t\t", l2.balance)

    @staticmethod
    def interst_calcuation(years, rate):
        name = input("Enter the Deposit Name:")
        account_no = int(input("Enter the Deposit account"))
        len_obj = len(l)
        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                interst = (l[i].balance * rate * years) / 100
                l[i].balance += interst
                print("Balance of after ", l[i].balance)

    def deposit_mode_selection(self):
        print("1-----cash Deposit \n2-------check Deposit \n3-----dd Deposit\n")
        option = int(input('Enter the Deposit mode :'))
        if option == 1:
            obj.deposit()

        elif option == 2:
            check_no = int(input("Enter the check no:"))

            if check_no not in l_cc_no:
                l_cc_no.append(check_no)
                obj.check_deposit(check_no)


        elif option == 3:
            dd_no = int(input("Enter the dd no:"))

            if dd_no not in l_dd:
                l_cc_no.append(dd_no)
                obj.dd_deposit(dd_no)




    def withdraw(self):
        print("*" * 30)
        name = input("Enter the Withdraw Name:")
        account_no = int(input("Enter the Withdraw account"))
        len_obj = len(l)
        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the withdraw amount"))
                if l[i].balance > amt:
                    l[i].balance -= amt
        print("After Cheek Withdraw Account Details")
        # obj.bank_details()
        # obj.display_Account_Details()

    def check_withdraw(self, check_withdraw_no):
        self.check_withdraw_no = check_withdraw_no
        name = input("Enter the Withdraw Name:")
        account_no = int(input("Enter the Withdraw account"))
        len_obj = len(l)

        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the withdraw amount"))
                if l[i].balance > amt:
                    l[i].balance -= amt
                    print("After Cheek withdraw Account Details", l[i].balance)

                else:
                    print("insufficient balance in you account")
        print("Check No ", self.check_no)

        # obj.display_all_account_details()

    def dd_withdraw(self, dd_withdraw_no):
        self.dd_withdraw_no = dd_withdraw_no
        name = input("Enter the Withdraw Name:")
        account_no = int(input("Enter the Withdraw account"))
        len_obj = len(l)

        for i in range(len_obj):
            if (l[i].name == name) and (l[i].account_no == account_no):
                amt = float(input("Enter the withdraw amount"))
                if l[i].balance > amt:
                    l[i].balance -= amt
                    print("After DD withdraw Account Details", l[i].balance)

                else:
                    print("insufficient balance in you account")
        print("Check No ", self.dd_withdraw_no)

        obj.display_all_account_details()

    def withdraw_mode_selection(self):
        print("1-----cash withdraw \n2-------check withdraw \n3-----dd withdraw \n")
        option1 = int(input('Enter the withdraw mode :'))
        if option1 == 1:
            obj.withdraw()

        elif option1 == 2:
            check_withdraw_no = int(input("Enter the withdraw check no:"))

            if check_withdraw_no not in withdraw_check_no:
                withdraw_check_no.append(check_withdraw_no)
                obj.check_withdraw(check_withdraw_no)

        elif option1 == 3:
            dd_withdraw_no = int(input("Enter the withdraw  dd no:"))

            if dd_withdraw_no not in withdraw_dd_no:
                withdraw_dd_no.append(dd_withdraw_no)
                obj.dd_withdraw(dd_withdraw_no)
l = list()
l3 = dict()
l_dd = list()
l_cc_no = []
withdraw_check_no = []
withdraw_dd_no = []
obj=Bank()
l.append(obj)
len_obj = len(l)