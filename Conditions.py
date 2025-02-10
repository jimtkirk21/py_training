#name = input('Enter your name: ')
#if name == 'Adam':
#    print ('Hello Boss!')
#    print ('Welcome back; it is nice to see you again!')
#else:
#    print ('Who the hell are you?')

#first  = input('Enter first: ')
#second = input ('Enter second: ')
#if first < second:
#    print (f'{first} comes before {second}.')
#else:
#    print (f'{second} comes before {first}.')


#name = input('Enter your name: ')
#if name == 'Adam':
#    print ('Hello Boss!')
#    print ('Welcome back; it is nice to see you again!')
#elif name == 'John Doe':
#    print(f'That is very secretive name, {name}!')
#else:
#    print ('Who the hell are you?')

#first  = input('Enter first: ')
#second = input ('Enter second: ')
#if first < second:
#    print (f'{first} comes before {second}.')
#elif second < first:
#    print (f'{second} comes before {first}.')
#else:
#    print (f'{first} and {second} are the same')

my_name = 'Adam'
my_company = 'Concorde'
name = input('Enter your name: ')
company = input('Enter your company: ')
if name == my_name and company == my_company:
    print ('You must be me!')
elif name == my_name:
    print (f'Greate name, {my_name} but the {company} is terrible place!')
elif company == my_company:
    print (f'Hello {name}, welcome to {my_company}!')
else:
    print (f'Hello {name} I do not know you and the {company}!')