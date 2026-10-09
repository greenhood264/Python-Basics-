import json 
import random
import string 
from pathlib import Path 


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file found")
    except Exception as err:
        print(f"An Exception Occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def Createaccount(self):
        info = {
            "name": input("Enter your name :- "),
            "age" : int(input("Enter your age :- ")),
            "email": input("Enter your email :- "),
            "pin": int(input("Enter your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)

            Bank.__update()
        
    def depositmoney(self):
        accnumber = input("Please Enter your account number ")
        pin = int(input("Please Enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        
        else:
            amount = int(input("How much you want to depoit "))
            if amount  > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")
    

    def withdrawmoney(self):
        accnumber = input("Please Enter your account number ")
        pin = int(input("Please Enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        
        else:
            amount = int(input("How much you want to withdraw "))
            if userdata[0]['balance']  < amount:
                print("Sorry you dont have that much money")
              
            else:
                
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully ")


    def showdetails(self):

        accnumber = input("Please Enter your account number ")
        pin = int(input("Please Enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your Information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Please Enter your account number ")
        pin = int(input("Please Enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such user found ")
        
        else:
            print("You cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("Please Enter new name or press enter : "),
                "email":input("Please Enter your new Email or press enter to skip :"),
                "pin": input("Please Enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def Delete(self):
        accnumber = input("Please Enter your account number ")
        pin = int(input("Please Enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such data exist ")
        else:
            check = input("Press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()

            

user = Bank()
print("Press 1 for Creating an account")
print("Press 2 for Deposititing the money in the bank ")
print("Press 3 for Withdrawing the money ")
print("Press 4 for Details ")
print("Press 5 for Updating the details")
print("Press 6 for Deleting your account")

check = int(input("Please enter your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()