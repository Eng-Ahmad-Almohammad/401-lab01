appetizers=['Wings','Cookies', 'Spring Rolls'] 

entrees= ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden' ]

desserts= ['Ice Cream', 'Cake', 'Pie']

drinks= ['Coffee', 'Tea', 'Unicorn Tears']

all_items = ['Wings','Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To get a summary any time, type "summary" **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

print()




print('Appetizers')
print('----------')
for i in appetizers:
    print(i)


print()

print('Entrees')
print('----------')
for i in entrees:
    print(i)

print()


print('Desserts')
print('----------')
for i in desserts:
    print(i)

print()

print('Drinks')
print('----------')
for i in drinks:
    print(i)

print()


print('***********************************') 
print('** What would you like to order? **') 
print('***********************************') 

orders=[]


while True:
    user_input = input('>')
    if (user_input=='quit'):
        break
    elif (user_input == 'summary'):
        if (len(orders)==0):
            print ('There is no order yet')
        else:
            for i in orders:
                print(f'** {orders.count(i)} order of {i} **')
    else:
        if (user_input in all_items):
                orders.append(user_input)
                if(orders.count(user_input)>1):
                    repetition = orders.count(user_input)
                    print(f'** {repetition} order of {user_input} have been added to your meal **')
                else:
                    print(f'** 1 order of {user_input} have been added to your meal **')
        else:
            print('Sorry your order is not found!!')



