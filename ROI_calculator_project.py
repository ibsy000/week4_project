import os
import time

# Here we assume that we have a client coming to us asking for an automated 
# Rental Property Calculator. Our client's name is Brandon from a company called 
# "Bigger Pockets". Below, you will find a video of what Brandon usually does to 
# calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming 
# create a program that will calculate the Return on Investment(ROI) for a rental 
# property.

class ROI:
    

    def __init__(self, rent_income = 0, rent_exp = 0, rent_cashflow = 0, rent_coc_return = 0):

        self.rent_income = rent_income
        self.rent_exp = rent_exp
        self.rent_cashflow = rent_cashflow
        self.rent_coc_return = rent_coc_return

   
    def intro(self):
        
        print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Welcome and thank you for using ROI (Return On Investment) Calculator for your
rental property.

To start, let's take a look at your sources of rental income. 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)


    def income(self):
        # I went back through here and changed all the inputs to make it shorter
        # and less redundant 

        print("For your response please only use numbers and exclude any special characters ($ . , etc.)\n")

        rent = self.user_input('rental', 'income')
        self.rent_income = rent
        os.system("cls")
        
        while True:

            add_rent = input("""
Do you have any additional rental income from laundry services, storage fees, or
other miscellaneous rental income?

Please respond with "yes" or "no"\n
""")
            add_rent = add_rent.lower().strip()
            # os.system("cls")

            if add_rent == 'yes':
                os.system("cls")

                laundry = self.user_input('laundry', 'services')
                self.rent_income += laundry
                os.system("cls")
                
                storage = self.user_input('storage', 'fees')
                self.rent_income += storage
                os.system("cls")
                
                misc = self.user_input('misc. rental', 'income')
                self.rent_income += misc
                os.system("cls")

                print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental income is ${self.rent_income:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)

                break

            elif add_rent == 'no':
                os.system("cls")

                print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental income is ${self.rent_income:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)

                break

            else:
                print("I'm sorry that is not a valid response...")

    def expenses(self):
        
        print("You're doing great! Now let's take a look at your monthly rental expenses.\n")

        # mortgage = input("How much is your monthly mortgage?\n")
        # mortgage = int(mortgage)

        # this is when I realized I need a method to ask the question over and over
        mortgage = self.user_input('mortgage', 'amount')
        self.rent_exp += mortgage
        os.system("cls")

        taxes = self.user_input('tax', 'amount')
        self.rent_exp += taxes
        os.system("cls")

        
        


    def cash_flow(self):
        pass


    def coc_return(self):
        pass


    def edit():
        pass
    
    # I started to realize I'm typing the same input over and over again, I decided
    # to make a method to call the inputs instead and insert the two parameters
    # that change with each question... let's see how it goes
    def user_input(self, first_value, sec_value):
        
        question = input(f"How much is your monthly {first_value} {sec_value}?\n")
        question = int(question)

        return question


def main():
    
    os.system("cls")

    calculate = ROI()

    calculate.intro()

    calculate.income()

    calculate.expenses()

main()