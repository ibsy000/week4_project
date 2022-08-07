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

        add_rent = input("""
Do you have any additional rental income from laundry services, storage fees, or
other miscellaneous rental income?

Please respond with "yes" or "no"\n
""").lower().strip()
        os.system("cls")


        while add_rent not in {'yes', 'no'}:

            add_rent = input('I\'m sorry that is not a valid response...\nPlease respond with "yes" or "no"\n')
            os.system("cls")
            

        if add_rent == 'yes':
            os.system("cls")

            laundry = self.user_input('laundry', 'services')
            os.system("cls")
            
            storage = self.user_input('storage', 'fees')
            os.system("cls")
            
            misc = self.user_input('misc. rental', 'income')
            os.system("cls")
            
            self.rent_income = sum([rent, laundry, storage, misc])

        elif add_rent == 'no':
            os.system("cls")

        self.rent_income = rent
        print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly rental income is: ${self.rent_income:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
            """)



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
\tYour total monthly rental expenses is: ${self.rent_exp:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                """)



    def cash_flow(self):
        
        print("You're almost done! Let's calculate your cash flow...\n")
        time.sleep(3)

        cf_monthly = self.rent_income - self.rent_exp
        rent_cashflow = cf_monthly * 12

        print(f"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\tYour total monthly cashflow is: ${cf_monthly:.2f}
\tYour total annual cashflow is: ${rent_cashflow:.2f}
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
        """)
        


    def coc_return(self):

        print("You've made it to the final step! Now let's go over your rental property investments.\n")

        down_pymt = self.user_input('down payment', 'initial')


    def edit():
        pass
    
    def user_input(self, first_value, frequency = 'monthly', sec_value = 'amount'):
    # I started to realize I'm typing the same input over and over again, I decided
    # to make a method to call the inputs instead and insert the two parameters
    # that change with each question... let's see how it goes
        
        question = input(f"How much is your {frequency} {first_value} {sec_value}?\n")
        question = int(question)

        return question


def main():
    
    os.system("cls")

    calculate = ROI()

    calculate.intro()

    calculate.income()

    calculate.expenses()

    calculate.cash_flow()

    calculate.coc_return()

main()