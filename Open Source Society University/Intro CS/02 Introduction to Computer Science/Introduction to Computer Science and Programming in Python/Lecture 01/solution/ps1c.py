# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:49:10 2021

@author: Plabon kumer sarker
"""

annual_salary = float(input("Enter the starting salary: "))
portion_saved = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary/12
portion_saved_monthly = monthly_salary * portion_saved
current_savings = 0
months = 36

epsilon = 100
low = 0.0
high = 1.0
guess = (low + high) / 2.0
num_guesses = 0
notPossible = False

while(abs(current_savings - portion_down_payment) > epsilon):
    if(guess == 1.0):
        notPossible = True
        break
    a_salary = annual_salary
    m_salary = annual_salary/12
    num_guesses += 1
    month = 0
    current_savings = 0
    while(month < months):
        current_savings += (current_savings *portion_saved/12) + (guess * m_salary)
        month += 1
        if((month % 6) == 0):
            a_salary += a_salary * semi_annual_raise
            m_salary = a_salary / 12
            
    if(abs(current_savings - portion_down_payment) > epsilon):
        if(current_savings < portion_down_payment):
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        
if(notPossible):
    print("It is not possible to pay down in 3 years.")
else:
    print("Best savings rate: ", "{:.4f}".format(guess))
    print("Steps in bisection search: ", num_guesses)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
