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
        os.system("cls")
        
        while True:

            add_rent = input("""
Do you have any additional rental income from laundry services, storage fees, or
other miscellaneous rental income?

Please respond with "yes" or "no"\n
""").lower().strip()

            if add_rent not in {'yes', 'no'}:

                print("I'm sorry that is not a valid response...")
                os.system("cls")
                
            elif add_rent == 'yes':
                os.system("cls")

                laundry = self.user_input('laundry', 'services')
                os.system("cls")
                
                storage = self.user_input('storage', 'fees')
                os.system("cls")
                
                misc = self.user_input('misc. rental', 'income')
                os.system("cls")
                
                self.rent_income = sum([rent, laundry, storage, misc])
# ***********FIGURE OUT HOW TO NOT HAVE TO TYPE THIS TWICE************
                print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental income is ${self.rent_income:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)
                break

            elif add_rent == 'no':
                os.system("cls")
# ***********FIGURE OUT HOW TO NOT HAVE TO TYPE THIS TWICE************
                print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental income is ${self.rent_income:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)
                break

    def expenses(self):
        
        print("You're doing great! Now let's take a look at your monthly rental expenses.\n")

        # mortgage = input("How much is your monthly mortgage?\n")
        # mortgage = int(mortgage)

        # this is when I realized I need a method to ask the question over and over
        mortgage = self.user_input('mortgage')
        # self.rent_exp += mortgage  <----- I had this after each input....
        os.system("cls")

        taxes = self.user_input('tax')
        os.system("cls")

        insurance = self.user_input('insurance')
        os.system("cls")

        hoa = self.user_input('HOA', 'fees')
        os.system("cls")
        
        lawn_snow = self.user_input('lawn/snow', 'service(s)')
        os.system("cls")

        vacancy = self.user_input('vacancy')
        os.system("cls")

        repairs = self.user_input('repair')
        os.system("cls")

        cap_ex = self.user_input('capital expenditure')
        os.system("cls")

        prop_mgm = self.user_input('property management', 'expense')
        os.system("cls")

        # I realized I kept adding to self.rent_exp over and over again after
        # each question so I tested if I could get the sum of all the inputs
        # I tried first to get the sum of a set, but that didn't work so I 
        # changed it to a list and it worked!
        self.rent_exp = sum([mortgage, taxes, insurance, hoa, lawn_snow, vacancy, repairs, cap_ex, prop_mgm])

        print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental expenses is ${self.rent_exp:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)

    def cash_flow(self):
        pass


    def coc_return(self):
        pass


    def edit():
        pass
    
    # I started to realize I'm typing the same input over and over again, I decided
    # to make a method to call the inputs instead and insert the two parameters
    # that change with each question... let's see how it goes
    def user_input(self, first_value, sec_value = 'amount'):
        
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