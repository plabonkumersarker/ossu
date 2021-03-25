# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:30:03 2021

@author: Plabon kumer sarker
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary/12
portion_saved_monthly = monthly_salary * portion_saved
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings*(0.04/12)) + portion_saved_monthly
    months = months + 1 
    if months % 6 == 0:
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
        monthly_salary = annual_salary/12
        portion_saved_monthly = monthly_salary * portion_saved
    
print("Number of months: ", months)