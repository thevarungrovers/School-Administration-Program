# entering data in csv file
import csv

def write_csv(info_added): # w+ - write mode # name of file # for new line # a- append mode
    with open('student_info.csv', 'a',newline='')as csv_file: # variable holding file object
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0: # to check whether file is empty or not
            writer.writerow(["First_name", "Last_name", "Class", "Age", "Mobile_no", "E-mail"])
        
        writer.writerow(info_added)


# input 

condition = True

while (condition):
    stu = input('Enter student information in the format First_name Last_name Class Age Mobile_no E-mail : ')
    # stu_name = input('Name: ')
    # stu_age = int(input('Age: '))
    # stu_class = int(input('Class: '))
    # print('Entered info: ' + stu_name,str(stu_age),str(stu_class)) # printing entered data

    print('You entered : '+ stu) # printing entered data

    #split to create list
    entered_info = stu.split(' ')
    print(entered_info)

    # function call - add info
    write_csv(entered_info)

    addstu = input('Do you want to add new student info ? Type - yes/no: ')
    if addstu == 'yes' or addstu == 'YES':
        condition = True
    elif addstu == 'no' or addstu == 'NO':
        condition = False
    else:
        print('Please enter a valid info !!')

