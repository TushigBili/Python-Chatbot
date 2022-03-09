"""
This program is a chatbot for room service
By Tushig and Tsegi
"""

#import module to validate the time
import datetime

#Dictionary with the current guests and their room
guests = {'101':'Tushig', '102':'Tsegi', '103':'Stephen Curry', '104':'Damian Lillard'}

#Dictionaries with the menu
starters = {'101':'Chicken Nuggets', '102':'Bacon Rings', '103':'Chinese Dumplings'} 
main_courses = {'201':'BBQ Steak', '202':'Pepperoni Pizza','203':'Pork Chop'} 
desserts = {'301':'Vanilla Ice Cream', '302':'Chocolate Cake', '303':'Strawberry Cake'}

#Guest name and room
name = None
room = None

#Dictionary with the customer's order
order = {}

#check if the room has been booked
while room not in guests.keys():
    room = input('Please, enter your room number: ')
    #check if room exists
    if room in guests.keys():
        name = input('Please, enter your name: ')
        #Check if the room and guest name match
        if guests[room] != name:
            print ('Your name does not match our records.')
            room = None
    else:
        print (f'Room {room} has not been booked.')

#Print starters
print ()
print ('Starters menu')
print ('-------------')
for code, food in starters.items():
    print (code, '->', food)

#Add a blank line
print()

#Select starters
starter = None
#validate the starter
while starter not in starters.keys():
    starter = input ('Please, enter the starter code: ')
    if starter not in starters:
        print('Wrong starter code.')
    else:
        order[starter] = starters[starter]

#Print main courses
print ()
print ('Main courses menu')
print ('-----------------')
for code, food in main_courses.items():
    print (code, '->', food)

#Add a blank line
print()

#Select main course
main_course = None
#validate the starter
while main_course not in main_courses.keys():
    main_course = input ('Please, enter the starter code: ')
    if main_course not in main_courses:
        print('Wrong main course code.')
    else:
        order[main_course] = main_courses[main_course]

#Print desserts
print ()
print ('Desserts menu')
print ('-------------')
for code, food in desserts.items():
    print (code, '->', food)

#Add a blank line
print()

#Select desserts
dessert = None
#validate the dessert
while dessert not in desserts.keys():
    dessert = input ('Please, enter the starter code: ')
    if dessert not in desserts:
        print('Wrong dessert code.')
    else:
        order[dessert] = desserts[dessert]

#Validate the delivery time
validtime = False
timeformat = "%H:%M"
while not validtime:
    delivery_time = input("Please, enter delivery time (hh:mm): ")
    try:
        validtime = datetime.datetime.strptime(delivery_time, timeformat)
    except ValueError:
       print ('Time format hh:mm')

#Print the order:
print ()
print ('Your order')
print ('----------')
for code, food in order.items():
    print (code, '->', food)

print('Delivery time:', delivery_time)

#Confirm the order
place_order = ''

while place_order.lower() not in ('yes', 'no'):
    place_order = input ('Would you like to place your order (yes/no)? ')

print ()
if place_order == 'yes':
    print ('Your order is being processed')
else:
    print ('Your order has been cancelled')

print ('Thank you for choosing us!')
