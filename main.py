# input 

condition = True

while (condition):
    stu = input('Enter student information in the format First_name Last_name Class Age Mobile_no E-mail : ')
    # stu_name = input('Name: ')
    # stu_age = int(input('Age: '))
    # stu_class = int(input('Class: '))
    # print('Entered info: ' + stu_name,str(stu_age),str(stu_class)) # printing entered data

    print('You entered : '+ stu) # printing entered data

    addstu = input('Do you want to add new student info ? Type - yes/no: ')
    if addstu == 'yes' or addstu == 'YES':
        condition = True
    elif addstu == 'no' or addstu == 'NO':
        condition = False
    else:
        print('Please enter a valid info !!')

