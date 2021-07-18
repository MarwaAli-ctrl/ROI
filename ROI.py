#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ROI:
    def __init__(self):
        pass


    def income(self):
        self.income = int(input('What is your income for the property? '))
        print(f"Your income is {self.income}")
        self.expenses() 

    def expenses(self):
        self.expenses = []
        repairs = float(input('Enter the monthly cost of your Tax '))
        self.expenses.append(tax)
        tax = float(input('Enter the monthly cost of your Repairs '))
        self.expenses.append(tax)
        manager = float(input('Enter the monthly cost of your Property Manager '))
        self.expenses.append(manager)
        vacancy = float(input('Enter the monthly cost of your Vacancy expenses '))
        self.expenses.append(vacancy)
        mortgage = float(input('Enter the monthly cost of your Mortgage expenses '))
        self.expenses.append(mortgage)
        print(self.expenses)
        self.expenses = sum(self.expenses)
        print(self.expenses)
        self.cashflow()  

    def cashflow(self):
        self.cash = self.income - self.expenses
        print(f'Your monthly cash flow is: ${self.cash}')
        self.cash_on_cash()

        

    def cash_on_cash(self):
        self.coc = []
        dp = int(input("What was your down payment for the property? "))
        self.coc.append(dp)
        cc = int(input("What was closing costs for this beast? "))
        self.coc.append(cc)
        print(f'The total cost is: {self.TotalInvestment}!')
        self.Annual_cashflow = int(self.cash) * 12
        print(f" Your Annual Cashflow is : {self.Annual_cashflow}!")
        self.cash_on_cash_ROI = self.Annual_cashflow / self.TotalInvestment
        print(f'Here is your Cash on cash ROI:\n {self.cash_on_cash_ROI}%')
        end = input("Type 'yes' to find the cash on cash ROI of another property, or you can exit! ")
        if end == 'yes': 
            roi.income()
        
        elif end == 'exit':
            exit
        else:
            exit


roi = ReturnOnInvestment()

while True:
    user_input = input("Hello, to Marwa's ROI calculater, type 'start' to begin, or 'exit' to leave ")
    if user_input == 'start':
        roi.income()
    if user_input == 'no':
        exit
    else:
        print("goodbye!")


# In[ ]:




