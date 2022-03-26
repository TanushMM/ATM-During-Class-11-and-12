# Banking Management

from random import randint
import time
import mysql.connector as db
con=db.connect(host="localhost",user="root",passwd="tanushtgc2004",database="atm")
cur=con.cursor()

def randomnumber(n):
    rangestart = 10**(n-1)
    rangeend = (10**n)-1
    return randint(rangestart, rangeend)


def transaction():
    print("Transaction")
    acc1 = input("Enter Your Account Number: ")
    cur.execute("select * from sss where accno =" + acc1 + "")
    data = cur.fetchall()
    accno = None
    for i in data:
        accno = i[0]
    if accno == acc1:
        for j in (0,3):
            pd = input("Enter The Password: ")
            cur.execute("select * from sss where accno = '"+acc1+"' and pin = " + pd + "")
            data = cur.fetchall()
            pwd = None
            for i in data:
                pwd = i[1]
            if pwd == pd:
                acc2 = input("Enter the Reciever's Account Number: ")
                cur.execute("select * from sss where accno =" + acc2 + "")
                data = cur.fetchall()
                accno = None
                for i in data:
                    accno = i[0]
                if accno == acc2:
                    cur.execute("select * from sss where accno =" + acc1 + "")
                    data = cur.fetchall()
                    accno1 = None
                    for i in data:
                        accno1,pwd1,balance1 = i[0],i[1],i[2]
                    transamount = input("Enter The Amount To Transfer: ")
                    if int(transamount) < 25000:
                        bal_sub_1 = int(balance1) - int(transamount)
                        cur.execute("update sss set balance = '" +str(bal_sub_1)+ "' where accno = '" +acc1+ "' and pin = '" +pd+ "' ")
                        cur.execute("commit")
                        cur.execute("select * from sss where accno =" + acc2 + "")
                        data = cur.fetchall()
                        accno2 = None
                        for i in data:
                            accno2, pwd2, balance2 = i[0], i[1], i[2]
                        bal_add_2 = int(balance2) + int(transamount)
                        cur.execute("update sss set balance = '"+str(bal_add_2)+"' where accno = '"+acc2+"' ")
                        cur.execute("commit")
                        print("Processing Transaction...")
                        time.sleep(4)
                        print("Transaction Successful...")
                        time.sleep(2)
                        print("Balance In Your Account After Transaction: ",bal_sub_1)
                        print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18
                        time.sleep(2)
                        break
                    else:
                        printd("Transaction Amount Greater Than 25000. ")
                else:
                    print("Reciever's Account NUmber Not Found In Database. ")
            else:
                print("Wrong Password ! ")
    else:
        print("Account Number Not Found In Database. ")


def createacc():
    print("""
------------------Welcome To OTA Banking Service------------------""")  # 25 + 21 + 21
    print("Create Account ")
    name = str(input("Enter Your Name Without Any Spaces And Special Symbols (Initials After Full Name): "))
    age = input("Enter Your Age: ")
    date = input("Enter Your Date of Birth (Only Date): ")
    month = input("Enter Your Month Of Birth (Only Month): ")
    year = input("Enter Your Year Of birth (Only Year): ")
    phonenumber = input("Enter Your Phone Number: ")
    accno = str(randomnumber(16))
    for j in (0,3):
        pin = input("Enter a Pin (Only 4 digits) (Only Numbers): ")
        if len(pin) == 4:
            print("Processing Your Request")
            time.sleep(5)
            print("Deposit a Minimum Of Rs. 1000 to Start An Account. ")
            balance = input("Enter The Amount You Have Decided To Deposit: ")
            print("Insert The Money In The Slot ")
            print("""
    Inserted The Money (Type 'I')
    """)
            comm = input("To Do: ")
            if comm.upper() == "I":
                print("Calculating Money")
                time.sleep(4)
                print("Creating An Account, Please Wait For A Moment...")
                time.sleep(4)
                cur.execute("insert into sss values ('"+accno+"','"+pin+"','"+balance+"','"+name+"','"+age+"','"+date+"','"+month+"','"+year+"','"+phonenumber+"')")
                cur.execute("commit")
                print("Account Created Successfully...")
                print("Name: ",name)
                print("Age: ",age)
                print("Date Of Birth (D.O.B): ",date,".",month,".",year)
                print("Allotted Account Number: ",accno)
                print("Pin (Pin will not be shown): ****")
                print("Balance: ",balance)
                break
            else:
                print("Command Error....")
        elif len(pin) < 4:
            print("Pin Is Shorter Than 4 Digits")
        elif len(pin) > 4:
            print("Pin Is Longer Than 4 Digits")
        else:
            print("Something Went Wrong!!!")
    time.sleep(2)
    print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18

def withdraw():

    print("""
---------------------Welcome To OTA Bank ATM---------------------""")  # 25 + 21 + 21
    print("Withdrawl Money")
    accin = input("Enter The Account Number: ")
    cur.execute("select * from sss where accno =" + accin + "")
    data = cur.fetchall()
    accno = None
    for i in data:
        accno = i[0]
    if accno == accin:
        for j in (0,3):
            pd = input("Enter The Password: ")
            cur.execute("select * from sss where accno = '"+accin+"' and pin = " + pd + "")
            data = cur.fetchall()
            pwd = None
            for i in data:
                pwd = i[1]
            if pwd == pd:
                amount = int(input("Enter The Amount To Withdraw: "))
                if amount < 25000:
                    cur.execute("select * from sss where accno =" + accin + "")
                    data = cur.fetchall()
                    accno = None
                    for i in data:
                        balance = i[2]
                    if amount < int(balance):
                        pd = input("Enter The Password: ")
                        cur.execute("select * from sss where accno = " + accin + "")
                        data = cur.fetchall()
                        pwd = None
                        for i in data:
                            pwd = i[1]
                        if pwd == pd:
                            updateamount = str(int(balance) - amount)
                            cur.execute(
                                "UPDATE sss set balance = '" + updateamount + "' where accno = '" + accin + "'")
                            cur.execute("commit")
                            print("Precessing Transaction ")
                            print("Counting Cash")
                            time.sleep(4)
                            print("Collect The Card Then The Cash")
                            print("Balance = ", updateamount)
                            x = False
                            time.sleep(2.5)
                            break
                        else:
                            print("The Password you have entered now is incorrect. ")
                            y = False
                    elif amount > int(balance):
                        print("Withdrawl Amount More Tha Your Account Balance")
                    elif int(balance) - amount == 0:
                        print(
                            "Proceeding Transaction moght zer0-out your account balance, This Transaction cannot be Performed. ")
                elif amount > 25000:
                    print("Withdrawl more than 25000 is not available contact your Bank Brance to know More.")
                elif amount == 0:
                    print("The user using this ATM dosn't have brain, how can 0 amount be withdrawn")
                    print("0 Amount Can't be withdrawn")
            else:
                print("Password Mistake")
    else:
        print("Account Number Not Found In Database")

    print("------------------Thanks For Using OTA Bank ATM------------------")  # 31 + 18 + 18


def accinfo():
    print("""
------------------Welcome To OTA Banking Service------------------""")  # 25 + 21 + 21
    print("Account Information")
    accin = input("Enter The Account Number: ")
    cur.execute("select * from sss where accno =" + accin + "")
    data = cur.fetchall()
    accno = None
    for i in data:
        accno = i[0]
    if accno == accin:
        for j in (0,3):
            pd = input("Enter The Password: ")
            cur.execute("select * from sss where accno = '"+accin+"' and pin = " + pd + "")
            data = cur.fetchall()
            pwd = None
            for i in data:
                accno, pwd, balance, name, ph = i[0], i[1], i[2], i[3], i[8]
            if pwd == pd:
                print("""
------------------------Account Information------------------------ 
""")  # 24 + 19 + 24
                print("Account Number: ", accno)
                print("Name: ",name )
                print("Phone Number: ", ph)
                print("Balance: ", balance)
                time.sleep(2.5)
                break
            else:
                print("Password Entered Now is Incorrect")
    else:
        print("Account Number Is Not Found In Database")
    print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18

def deposit():
    print("""
------------------Welcome To OTA Banking Service------------------""")  # 25 + 21 + 21
    print("Deposit Money")
    accin = input("Enter The Account Number: ")
    cur.execute("select * from sss where accno =" + accin + "")
    data = cur.fetchall()
    accno = None
    for i in data:
        accno = i[0]
    if accno == accin:
        for j in (0,3):
            pd = input("Enter The Password: ")
            cur.execute("select * from sss where accno = '"+accin+"' and pin =  '"+pd+"'")
            dataa = cur.fetchall()
            pwd = None
            for i in dataa:
                accno, pwd, balance = i[0], i[1], i[2]
            if pwd == pd:
                amount = input("Enter The Amount To Deposit ")
                print("Insert The Money In The Slot ")
                print("""
Inserted The Money (Type 'I')
    """)
                comm = input("To Do: ")
                if comm.upper() == "I":
                    print("Calculating Money ")
                    time.sleep(4)
                    print("Balance Before Depositing Money: ",balance)
                    print("Deposit Amount: ",amount)
                    bal = str(int(balance) + int(amount))
                    cur.execute("update sss set balance = '"+bal+"' where accno = '"+accin+"'")
                    cur.execute("commit")
                    print("Balance After Depositing Money: ",bal)
                    time.sleep(2.5)
                    break
                else:
                    print("Command Error....")
            else:
                print("Password Error....")
    else:
        print("Account Number Not Found In Database. ")
    print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18


def deleteacc():
    print("""
------------------Welcome To OTA Banking Service------------------""")  # 25 + 21 + 21
    print("Delete Account")
    accin = input("Enter The Account Number That You Wanted To Delete: ")
    cur.execute("select * from sss where accno = '"+accin+"'")
    data = cur.fetchall()
    accno = None
    for i in data:
        accno = i[0]
    if accin == accno:
        for j in (0,3):
            pin = input("Enter The Pin: ")
            phonenumber = input("Enter the Registered Phone Number: ")
            cur.execute("select * from sss where accno = '"+accin+"' and pin = '"+pin+"'")
            data = cur.fetchall()
            pwd = None
            for i in data:
                pwd = i[1]
            if pwd == pin:
                print("""
Delete Account  (Type 'Y')
Mind Changed    (Type 'N')
            """)
                comm = input("Confirmation: ")
                if comm.upper() == "Y":
                    print("Processing request.... Takes A Few Seconds...")
                    time.sleep(4)
                    cur.execute("delete from sss where accno = '"+accin+"' and pin = '"+pin+"' and phonenumber = '"+phonenumber+"' ")
                    cur.execute("commit")
                    print("Calculating Balance Amount. ")
                    time.sleep(1)
                    print("Counting....")
                    time.sleep(2.5)
                    print("Your Account with Acc No:",accin, "Has Been Deleted, Please Collect your Balance Money In Cash Now. ")
                    print("Thanks for Having Account In Our Bank...")
                    print("Please Let Us Know If There Are Any Flaws In Our Online Banking Service")
                    print("""
            https://www.gaajubankingservice.in
                           (OR)
        https://www.gaajubankingservice.in/queries
            """)
                    time.sleep(2)
                    break
                elif comm.upper() == "N":
                    print("You Have Canceled The Deletion Of The Account. ")
                else:
                    print("Confirmation Error....")
            else:
                print("Wrong PIN Entered....")
    else:
        print("Account Number Not Found In Database. ")

    print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18



# Project By Tanush, Adithyanarayanan, Koushik
# Modules Used Are: Time Module (import time), Random Module (from random import randint)
# Connectors Used: MySQL Connector (import mysql.connector as db)
# Brain Used: Tanush's Brain, Adithyanarayanan's Brain, Kowshic's Brain
# Books Used: Computer Science With Python Class 12 By: Sumitha Arora
# Website Used: https://www.python.org , https://www.w3schools.com/pthon
# YouTube Videos used: https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=20839s
# Time Taken To Learn Extra Things: 2.5 weeks
# Time Taken To Code: 1.5 weeks

# Program Starts Here

var = True
while var:
    print("""
-----------------Welcome To OTA Banking Service-----------------""")  # 32 + 17 + 17
    print("""
1. Transaction (Account To Account)    (Type 'T' or 1)
2. Create Account                      (Type 'C' or 2)
3. Withdraw Money                      (Type 'W' or 3)
4. Account Information                 (Type 'A' or 4)
5. Deposit Money                       (Type 'D' or 5)
6. Delete Account                      (Type 'X' or 6)
7. Exit                                (Type 'E' or 7)      
""")
    comm = input("To Do: ")
    if comm.upper() == "T" or comm == "1":
        transaction()
    elif comm.upper() == "C" or comm == "2":
        createacc()
    elif comm.upper() == "W" or comm == "3":
        withdraw()
    elif comm.upper() == "A" or comm == "4":
        accinfo()
    elif comm.upper() == "D" or comm == "5":
        deposit()
    elif comm.upper() == "X" or comm == "6":
        deleteacc()
    elif comm.upper() == "E" or comm == "7" :
        print("--------------Thanks For Using OTA Banking Service--------------")  # 31 + 18 + 18
        var = False
    else:
        print("Command Error.... ")
