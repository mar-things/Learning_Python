import numpy as np 
import re 

book = open('Task_text.txt',encoding='utf-8')
text_book = book.read()

#Question 1

number_of_capital_The = re.findall(r'The',text_book)
number_of_capital_the = re.findall(r'the',text_book)
the_total = number_of_capital_The + number_of_capital_the
print("The_count: ",len(the_total))

#Question 2

number_of_capital_I = re.findall(r'I',text_book)
print("I_count: ",len(number_of_capital_I))

#Question 3
def sum(arr):
    sum = 0 
    for i in arr:
        sum = sum + i 
    return(sum)

List_of_numbers = re.findall(r'[\d]+',text_book)
array_of_numbers = [eval(i)for i in List_of_numbers]
total_sum = sum(array_of_numbers)
print("Total sum: ",total_sum)


#Question 4

number_of_capital_The = re.findall(r'The',text_book)
number_of_capital_the = re.findall(r'the',text_book)
the_total = number_of_capital_The + number_of_capital_the
print("The_count: ",len(the_total))

#Question 5