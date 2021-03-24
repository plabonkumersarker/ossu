# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:28:17 2021

@author: Plabon kumer Sarker
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary/12
portion_saved_monthly = monthly_salary * portion_saved
current_savings = 0
months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings*(0.04/12)) + portion_saved_monthly
    months = months + 1
    
print("Number of months: ", months)