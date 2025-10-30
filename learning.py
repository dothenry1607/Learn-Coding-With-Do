import random 

def bank_num_rand():
    x = f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"
    return x

class bank:
    def __init__(self):
        pass 

    def account_system(self):
        question = input("Do you want to login or open an account? (1 for login, 2 for open): ")
        if question == "1":
            bank_number = input("Enter your bank number(including dash because im suck: ")
            with open('bank_number.txt', 'r') as f :
                content = f.read()
                if bank_number in content:
                    self.bank_number = bank_number
                    print("Login Success.") 
                else:
                    print("Invalid bank number.")            
        elif question == "2":
            while True:
                bank_num = bank_num_rand()
                with open('bank_number.txt', 'r') as f :
                    content = f.read()
                    if bank_num in content:
                        pass
                    else:
                        break
            open(f"{bank_num}.txt", 'x') 
            with open("bank_number.txt", 'a') as f:
                f.write(f"{bank_num}\n")            
            self.bank_number = bank_num
            print("account created.")
        else:
            print("Invalid input")
    
    def deposit(self, money):
        self.money = f"${money}"
        with open(f"{self.bank_number}.txt", 'w') as f:
            f.write(str(money))
        print(f"You added {self.money} into your bank account.")
    
    def balance(self):
        with open(f"{self.bank_number}.txt", 'r')  as f:
            x = f.read()
            return x 


    


do = bank()





        

