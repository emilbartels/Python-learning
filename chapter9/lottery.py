#Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list 
# and print a message saying that any ticket matching these 4 numbers 
# or letters wins a prize.”

from random import choice
lotterynumbers = (1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f")

print("If your ticket matches these 4 letters and numbers wins a prize")

x = 1
while x < 5:
    print(choice(lotterynumbers))
    x = x +1

