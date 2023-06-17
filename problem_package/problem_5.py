"""Name, Age, Comment Program"""
first_name = input('Enter First Name: ')
#if first_name == "":
  #  print('Name cannot be empty')
   # exit()

last_name = input('Enter Last Name: ')
#if last_name == "":
  #  print('Name cannot be empty')
   # exit()
age = int(input('Enter your age: '))

if first_name != '' and last_name != '':
    if age < 0:
        print('Age cannot be negative number')
    elif age < 18:
        print('Your name is', last_name, first_name, 'and your age is', age, 'you are underage')
    elif 18 <= age < 65:
        print('Your name is', last_name, first_name, 'and your age is', age, 'you are a youth')
    elif age >= 65:
        print('Your name is', last_name, first_name, 'and your age is', age, 'you are old')
elif first_name == '' and last_name == '':
    print('Both First name and Last name are empty')
elif first_name == '':
    print('First name cannot be empty')
elif last_name == '':
    print('Last name cannot be empty')

