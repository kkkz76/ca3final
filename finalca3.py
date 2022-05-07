from tabulate import tabulate
import datetime



# Dictionary Variables.............


swimmers = {'Mgmg': {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[],'Time':[],"Meet":[]}}
total_record_swimmers_real={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status': []}



record_swimmers_temp ={}


record_swimmers_real = {}
# record_swimmers_real_table= {'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}


#register_status
reg_status_true = "active"
reg_status_false = "inactive"

#post status
post_status_true ="posted"
post_status_false ="unposted"

# function
#input_validation_function
def check_name(check_reg_name):
    
    if check_reg_name.isalpha():
        return True
    else:
        return False

#check date function
def check_date(check_reg_date):

    year,month,day = check_reg_date.split('/')
    #check input_validation_for age
    
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return False

#check gender

def check_gender(check_reg_gender):
    
    if check_reg_gender == '1':
        return ['Male']
    elif check_reg_gender == '2':
        return ['Female']
    elif check_reg_gender == '3':
        return ['Others']
    else:
        return False


# check register swimmers
def registered_swimmers():
    register_swimmers_table={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}
    for x in swimmers.values():
        
        for a in x['Name']:
            register_swimmers_table['Name'].append(a)

        for a in x['Age']:
            register_swimmers_table['Age'].append(a)

        for a in x['Gender']:
            register_swimmers_table['Gender'].append(a)

        for a in x['Status']:
            register_swimmers_table['Status'].append(a)

        for a in x['Event']:
            register_swimmers_table['Event'].append(a)
                    
        for a in x['Time']:
            register_swimmers_table['Time'].append(a)
                    
        for a in x['Meet']:
            register_swimmers_table['Meet'].append(a)
                
    print("\n\n\n"+ tabulate(register_swimmers_table, headers='keys'))            
    main_program = True   

# check recorded swimmers
def recorded_swimmers():
    record_swimmers_temp_table ={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status':[]}
    for temp_swimmer in record_swimmers_temp.values():

        for b in temp_swimmer['Name']:
            record_swimmers_temp_table['Name'].append(b)

        for b in temp_swimmer['Age']:
            record_swimmers_temp_table['Age'].append(b)

        for b in temp_swimmer['Gender']:
            record_swimmers_temp_table['Gender'].append(b)

        for b in temp_swimmer['Status']:
            record_swimmers_temp_table['Status'].append(b)

        for b in temp_swimmer['Event']:
            record_swimmers_temp_table['Event'].append(b)
                    
        for b in temp_swimmer['Time']:
            record_swimmers_temp_table['Time'].append(b)
                    
        for b in temp_swimmer['Meet']:
            record_swimmers_temp_table['Meet'].append(b)
                        
        for b in temp_swimmer['Post_Status']:
            record_swimmers_temp_table['Post_Status'].append(b)
                

    print("\n\n\n"+ tabulate(record_swimmers_temp_table, headers='keys'))            
        


#Main Program.........

#For Registering.....................

main_program = True
while main_program == True:
    user_choice = input("\n\n\nFor register press 1\nFor record swimmer time press 2\nFor search individual press 3\nTo display unposted press 4\nTo execute program press 5\nEnter Your option:")
    if user_choice == '5':
        main_program = False
    if user_choice == 'apple':        
       registered_swimmers()
    if user_choice == 'banana':        
       recorded_swimmers()       
    if user_choice == '1':

        input_loop = True
    
        while input_loop == True:

            reg_name  = input("Enter name:")

            #check input_validation_for name  
            check_name(reg_name)                                 
            while check_name(reg_name) == False:
                print("Only allow alphabets for name")
                reg_name  = input("Enter name:")
                check_name(reg_name)



            if reg_name in swimmers and [reg_status_false] == swimmers[reg_name]['Status']:
                swimmers[reg_name]['Status'] = [reg_status_true]
                print("This username is now active")
                input_loop = True

            elif reg_name in swimmers and [reg_status_true] == swimmers[reg_name]['Status']:
                print("This user is already active")
                input_loop = True
            else:
                input_loop = False
                swimmers[reg_name]={}
                swimmers[reg_name]['Name']=[reg_name]

                reg_dob= input("Enter data of birth in format yy/mm/dd:")

                #check input_validation_for dateTime  
                check_date(reg_dob)
                while check_date(reg_dob) == False:
                    print("Input date is not valid..")
                    reg_dob= input("Enter data of birth in format yy/mm/dd:")
                    check_date(reg_dob)
                swimmers[reg_name]['Age']=[reg_dob] 


                reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                check_gender(reg_gen)
                while check_gender(reg_gen) == False:
                    reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                    check_gender(reg_gen)
                    
                swimmers[reg_name]['Gender']=check_gender(reg_gen)

            
                swimmers[reg_name]['Status']=[reg_status_true]
                swimmers[reg_name]['Event']=[None]
                swimmers[reg_name]['Time']=[None]
                swimmers[reg_name]['Meet']=[None]


                print("Register Successful and now active")

               
        registered_swimmers() #table for register

#...........................Record Swimmers..........................
    elif user_choice == '2':
        record_name = input('Enter player name to record(must be registered):')

        if record_name in swimmers:

            record_event_type =input("Choose the event type\nPress 1 for Freestyle\nPress 2 for Backstroke\nPress 3 for Breaststroke\nPress 4 for Butterfly\nPress 5 for individual Medley\nEnter your type:")

            if record_event_type == '1':
                record_event_type_detail = "Freestyle"
                record_event_meter= input('Choose between meter 50,100,200,400,800,1500:')
            elif record_event_type == '2':
                record_event_type_detail = "Backstroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '3':
                record_event_type_detail = "Breaststroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '4':
                record_event_type_detail = "Butterfly"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '5':
                record_event_type_detail = "individual Medley"
                record_event_meter= input('Choose between meter 100,200,400:')
            else:
                print("invaild input")
                main_program = True

            record_time=input("Enter time to record(eg.01:11:00):")
            record_meet=input("Enter the name of competition:")


            # if record_event_type_detail in record_swimmer_real[record_name]['Event'] and record_time in record_swimmer_real[record_name]['Time'] and record_meet in record_swimmer_real[record_name]['Meet']:
            #         print("You can not add same record twice")
            #         main_program = True

            if 1 == 1:

    #......................................Check Already Record and Register swimmer............................            
                if record_name in list(swimmers.keys()) and ((record_name in list(record_swimmers_temp.keys()) or record_name in list(record_swimmers_real.keys()) or record_name in list(record_swimmers_real.keys()) and record_name in list(record_swimmers_temp.keys()))):
                    print('1')
                    if record_name in list(record_swimmers_temp.keys()) and record_name not in list(record_swimmers_real.keys()):
                        print('1.1')
                        record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                        record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                        record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                        record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                        record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                        record_swimmers_temp[record_name]['Time'].append(record_time)
                        record_swimmers_temp[record_name]['Meet'].append(record_meet)
                        record_swimmers_temp[record_name]['Post_Status'].append(post_status_false)

                    elif record_name in list(record_swimmers_real.keys()) and record_name not in list(record_swimmers_temp.keys()): 
                        print('1.2')
                        if record_swimmers_temp == {}:
                            print('1.2.1')  
                            # print(list(record_swimmers_real.keys()))
                            record_swimmers_temp[record_name]={}
                            record_swimmers_temp[record_name]['Name']=[record_name]
                            record_swimmers_temp[record_name]['Age']=[swimmers[record_name]['Age'][0]]
                            record_swimmers_temp[record_name]['Gender']=[swimmers[record_name]['Gender'][0]]
                            record_swimmers_temp[record_name]['Status']=[swimmers[record_name]['Status'][0]]
                            record_swimmers_temp[record_name]['Event']=[record_event_type_detail]
                            record_swimmers_temp[record_name]['Time']=[record_time]
                            record_swimmers_temp[record_name]['Meet']=[record_meet]
                            record_swimmers_temp[record_name]['Post_Status']=[post_status_false]
                        else:
                            print('1.2.2')
                            record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                            record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                            record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                            record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                            record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                            record_swimmers_temp[record_name]['Time'].append(record_time)
                            record_swimmers_temp[record_name]['Meet'].append(record_meet)
                            record_swimmers_temp[record_name]['Post_Status'].append(post_status_false)


                    elif record_name in list(record_swimmers_real.keys()) and record_name in list(record_swimmers_temp.keys()):
                            print('1.3')
                            record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                            record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                            record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                            record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                            record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                            record_swimmers_temp[record_name]['Time'].append(record_time)
                            record_swimmers_temp[record_name]['Meet'].append(record_meet)
                            record_swimmers_temp[record_name]['Post_Status'].append(post_status_false) 



            #......................................Check Register swimmer but not Record............................  
                elif record_name in list(swimmers.keys()) and record_name not in list(record_swimmers_temp.keys()):
                    print('2')
                    record_swimmers_temp[record_name]={}
                    record_swimmers_temp[record_name]['Name']=[record_name]
                    record_swimmers_temp[record_name]['Age']=[swimmers[record_name]['Age'][0]]
                    record_swimmers_temp[record_name]['Gender']=[swimmers[record_name]['Gender'][0]]
                    record_swimmers_temp[record_name]['Status']=[swimmers[record_name]['Status'][0]]
                    record_swimmers_temp[record_name]['Event']=[record_event_type_detail]
                    record_swimmers_temp[record_name]['Time']=[record_time]
                    record_swimmers_temp[record_name]['Meet']=[record_meet]
                    record_swimmers_temp[record_name]['Post_Status']=[post_status_false]


                recorded_swimmers()
                print(record_swimmers_temp)
                # ....................................posted_unposted..........................................

                check_post_status_input = input("Do you want to post all the unposted data(y/n):")
                if check_post_status_input == 'y':
                    real_keys_Temp_append = []
                    real_values_Temp_append = []
                    for real_swimmer_keys,real_swimmer_values in record_swimmers_temp.items():

                        real_keys_Temp_append.append(real_swimmer_keys)       #=>['alex', 'Mgmg']
                        real_values_Temp_append.append(real_swimmer_values)   #[{'Name': ['alex'], 'Age': ['2022/2/2'], 'Gender': ['Male'], 'Status': ['active'], 'Event': ['Backstroke'], 'Time': ['2'], 'Meet': ['2'], 'Post_Status': ['unposted']}, {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'], 'Status': ['active'], 'Event': ['Backstroke'], 'Time': ['4'], 'Meet': ['4'], 'Post_Status': ['unposted']}]

                    
                    
                    for c in real_keys_Temp_append: # =>mgmg
                        # record_swimmers_real[c]={}  # {'mgmg':{....}}
                        
                        record_swimmers_real[c]=total_record_swimmers_real
                        print(record_swimmers_real[c])


                        for e in record_swimmers_temp.values():
                    
                            for f in e['Name']:
                                total_record_swimmers_real['Name'].append(f)

                            for f in e['Age']:
                                total_record_swimmers_real['Age'].append(f)

                            for f in e['Gender']:
                                total_record_swimmers_real['Gender'].append(f)

                            for f in e['Status']:
                                total_record_swimmers_real['Status'].append(f)

                            for f in e['Event']:
                                total_record_swimmers_real['Event'].append(f)
                                        
                            for f in e['Time']:
                                total_record_swimmers_real['Time'].append(f)
                                        
                            for f in e['Meet']:
                                total_record_swimmers_real['Meet'].append(f)

                            for f in e['Post_Status']:
                                total_record_swimmers_real['Post_Status'].append(post_status_true)
                                    
                        
                    record_swimmers_temp.clear()
                    print(record_swimmers_temp)
                    print(record_swimmers_real)
                    main_program = True      
                else:
                    print(record_swimmers_temp)
                    print(record_swimmers_real)
                    main_program = True



                

        else:
            print("no user found")
            main_program = True

# ....................................Total Swimmer Detail.................................            
    


