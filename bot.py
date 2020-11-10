print('Hello! My name is Bilal.')
print('I was created in 2020.')
print('Please, remind me your name.')
your_name = input() # reading a name
# another way to print 
#  print('What a great name you have, {}'. format(your_name)) 
# another way to print
#  print('What a great name you have, ',your_name) 
print('What a great name you have, '+ your_name) 
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " , age ," that's a good time to start programming!" )
