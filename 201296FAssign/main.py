#Nmame: Surya Moorthy S/O Sathia Moorthy
#Admin Number: 201296F
#Group: IT2653-03

import basic_sorts_searches_functions,advanced_sorts_functions,additional_functions

def main():
    user_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', 'end']

    staycation_booking_details_dict = [
        {"customer_name": "Bill", "package_name": "Dc", "cost": 15, "pax": 10},
            {"customer_name": "Amos", "package_name": "Air", "cost": 21, "pax": 5},
                {"customer_name": "Tan", "package_name": "Water", "cost": 17, "pax": 4},
                    {"customer_name": "Beverly", "package_name": "Earth", "cost": 9, "pax": 3},
                        {"customer_name": "Theresa", "package_name": "Lava", "cost": 5, "pax": 1},
                            {"customer_name": "Ellen", "package_name": "Sea", "cost": 27, "pax": 2},
                                {"customer_name": "Hollow", "package_name": "Mountain", "cost": 19, "pax": 10},
                                    {"customer_name": "Jill", "package_name": "Zoo", "cost": 10, "pax": 15},
                                        {"customer_name": "Jane", "package_name": "Desert", "cost": 11, "pax": 4},
                                            {"customer_name": "Koen", "package_name": "Oceania", "cost": 12, "pax": 4}
                                        ]


    admin_only_warning= input('This option is only for admins.\n'
                              'Are you an Admin Y/N ?: ').upper()
    if admin_only_warning == "Y":
        shift_val= 10
        passwd_stored = additional_functions.encrypt('Windows10', shift_val)   #note changin num parameter to 26 will return back plaintext
        user_enter_passwd = input('Enter passwd: ')
        user_enter_passwd_encrypt = additional_functions.encrypt(user_enter_passwd, shift_val)
        attempt =0
        max_attempt = 3
        remaining_attempt = max_attempt
        while (passwd_stored != user_enter_passwd_encrypt) and (attempt < max_attempt):
            print('Incorect passwd. try again. Remaining Attempts {}'.format(remaining_attempt))
            user_enter_passwd_encrypt = additional_functions.encrypt((input('Enter passwd again')), shift_val)
            attempt +=1
            remaining_attempt = max_attempt - attempt
            if attempt == max_attempt:
                print('')
                print('Maximum attempts reached. Re-run the program again')

                break

        if (passwd_stored == user_enter_passwd_encrypt):
            print('Access Granted')
            print('')
            while True:
                print("1. Display all records")
                print("2. Sort record by Customer Name using Bubble sort")
                print("3. Sort record by Package Name using Selection sort")
                print("4. Sort record by Package Cost using Insertion sort")
                print("5. Search record by Customer Name using Linear Search and update record")
                print("6. Search record by Package Name using Binary Search and update record")
                print("7. List records range from $X to $Y. e.g $100-200")
                print("X. Exit Application")
                choice = input("Enter choice: ").lower()

                if choice == "1":
                    print('Printing Staycation Record')
                    for i in staycation_booking_details_dict:
                        print("Customer name:", i["customer_name"], end=" ")
                        print("Package name:", i["package_name"], end=" ")
                        print("Pax number:", i["pax"], end=" ")
                        print("Cost SGD:", i["cost"])
                    print('')

                elif choice == "2":
                    opt2_acceptable_choice = ['BS','OBS']
                    bubble_sort_opts= input('Enter which BubbleSort Option You Would Like \n'
                          'BS: Bubble Sort \n'
                          'OBS: Optimised Bubble Sort \n'
                          'Input Choice: ').upper()

                    while bubble_sort_opts =='' or bubble_sort_opts not in opt2_acceptable_choice:
                        bubble_sort_opts_retry = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                        if bubble_sort_opts_retry in opt2_acceptable_choice:
                            bubble_sort_opts = bubble_sort_opts_retry

                            print()


                    if bubble_sort_opts == "BS":
                        order_input_BS_opt2 = ['A','D']

                        order_input = input('Would you like the display in Ascending or Descending Order?\n'
                                            'A: Ascending\n'
                                            'D: Descending\n'
                                            'input choice: ').upper()


                        while order_input =='' or order_input not in order_input_BS_opt2:
                            order_input_retry_opt2 = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                            if order_input_retry_opt2 in order_input_BS_opt2:
                                order_input = order_input_retry_opt2

                                print()



                        if order_input == "A":

                            basic_sorts_searches_functions.bubbleSort(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            print('')

                        elif order_input == "D":

                            basic_sorts_searches_functions.bubbleSort_reverse(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            print('')

                        else:
                            print('Invalid Input')
                            print()

                    elif bubble_sort_opts =="OBS":
                        opt2_acceptable_choice_OBS = ['A','D']
                        order_input_OBS_opt2 = input('Would you like the display in Ascending or Descending Order?\n'
                                            'A: Ascending\n'
                                            'D: Descending\n'
                                            'input choice: ').upper()


                        while order_input_OBS_opt2 =='' or order_input_OBS_opt2 not in opt2_acceptable_choice_OBS:
                            order_input_retry_OBS_opt2 = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                            if order_input_retry_OBS_opt2 in opt2_acceptable_choice_OBS:
                                order_input_OBS_opt2 = order_input_retry_OBS_opt2

                                print()


                        if order_input_OBS_opt2 == "A":

                            basic_sorts_searches_functions.bubbleSort_optimized(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            print('')

                        elif order_input_OBS_opt2 == "D":

                            basic_sorts_searches_functions.bubbleSort_optimized_reverse(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            print('')

                    else:
                        print('Invalid options')


                elif choice == "3":
                    opt3_acceptable_choice = ['A','D']
                    order_input_opt3 = input('Would you like the display in Ascending or Descending Order?\n'
                                            'A: Ascending\n'
                                            'D: Descending\n'
                                            'input choice: ').upper()

                    while order_input_opt3 =='' or order_input_opt3 not in opt3_acceptable_choice:
                        order_input_retry_opt3 = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                        if order_input_retry_opt3 in opt3_acceptable_choice:
                            order_input_opt3 = order_input_retry_opt3

                            print()



                    if order_input_opt3 == "A":

                        basic_sorts_searches_functions.selection_sort(staycation_booking_details_dict)

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost SGD:", i["cost"])
                        print('')

                    elif order_input_opt3 == "D":

                        basic_sorts_searches_functions.selection_sort_reverse(staycation_booking_details_dict)

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost SGD:", i["cost"])
                        print('')


                elif choice == "4":
                    opt4_acceptable_choice =['A','D','R']
                    order_input = input('Would you like the display in Ascending or Descending Order?\n'
                                            'A: Ascending\n'
                                            'D: Descending\n'
                                            'R: Recursion Ascending\n'
                                            'input choice: ').upper()

                    while order_input =='' or order_input not in opt4_acceptable_choice:
                        order_input_retry = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                        if order_input_retry in opt4_acceptable_choice:
                            order_input = order_input_retry

                            print()

                    if order_input == "A":

                        basic_sorts_searches_functions.insertion_sort(staycation_booking_details_dict)
                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost SGD:", i["cost"])
                        print('')

                    elif order_input == "D":
                        basic_sorts_searches_functions.insertion_sort_reverse(staycation_booking_details_dict)

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost SGD:", i["cost"])
                        print('')

                    elif order_input == "R":
                        advanced_sorts_functions.insertionSortRecursive(staycation_booking_details_dict, len(staycation_booking_details_dict))
                        print('Package Name will now be sorted using Insertion Sort Recursive')
                        print('')

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost SGD:", i["cost"])
                        print('')

    #---------------------------------------------------------------------------------------------------------------------------------------------
                elif choice == "5":
                    cust_name_to_search = input('Enter the customer name you wish to update: ').title()
                    # re_enter_name =''
                    cust_val_update = basic_sorts_searches_functions.linear_search_cust_name(staycation_booking_details_dict,cust_name_to_search)


                    if cust_val_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                        print('Name entered does not exists. Check the record and try again')
                        print('')
                        continue

                    #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                    customer_name_list=[]
                    for cust_name in staycation_booking_details_dict:
                        name = cust_name["customer_name"]
                        customer_name_list += [(name)]


                    current_cust_package_name= cust_val_update["package_name"]
                    cust_cost_update = cust_val_update["pax"] * cust_val_update["cost"]


                    print('Customer {} currently has the {} Package. Total Cost: S$ {}'.format(cust_name_to_search, current_cust_package_name, cust_cost_update))

                    #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                    customer_package_name_list_5 = []
                    for cust_pack_name_5 in staycation_booking_details_dict:
                        pack_name_5 = cust_pack_name_5["package_name"]
                        customer_package_name_list_5 += [(pack_name_5)]



                    if cust_val_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                        print('Name entered does not exists. Check the record and try again')
                        continue

                    #if cust name entered and is in list this will update cust name record
                    elif (cust_val_update in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict
                        update_choices = input('What would you like to change\n'
                                               '1.Customer name\n'
                                               '2.Package name\n'
                                               '3.Cost \n'
                                               '4.Pax\n'                                           
                                               'Choice: ')

                        if update_choices == "1":

                            new_cust_name= input('Customer name in Staycation Record. Enter the new customer name. New name will override old name: ').title()

                            if new_cust_name not in customer_name_list:
                                #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                                #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                                print('New Customer Name {} Accepted'.format(new_cust_name))
                                print('Customer Name will now be sorted using Shell Sort')
                                print('')
                                cust_val_update["customer_name"] = new_cust_name
                                advanced_sorts_functions.shellSort(staycation_booking_details_dict)
                                for i in staycation_booking_details_dict:

                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost SGD:", i["cost"])

                            else:
                                #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                                while new_cust_name in customer_name_list:
                                    new_cust_name= input('New Customer Name already exists. Enter a new name that does not exist: ').title()
                                    while new_cust_name not in customer_name_list:
                                        print('New Customer Name {} Accepted'.format(new_cust_name))
                                        cust_val_update["customer_name"] = new_cust_name
                                        advanced_sorts_functions.pancakeSort(staycation_booking_details_dict)
                                        print('Package Name will be sorted using Pancake Sort')
                                        print('')

                                        for i in staycation_booking_details_dict:

                                            print("Customer name:", i["customer_name"], end=" ")
                                            print("Package name:", i["package_name"], end=" ")
                                            print("Pax number:", i["pax"], end=" ")
                                            print("Cost SGD:", i["cost"])

                                            advanced_sorts_functions.pancakeSort(staycation_booking_details_dict)
                                        break

                        elif update_choices == "2": #NOTE FOR PACKAGE NAME ITS THE OPPOSITE OF UPDATE CUST NAME. SUCCESSFUL CHANGE ONLY HAPPPENDS IF PACK NAME CUST ENTERS EXSISTS IN THE PACK NAME LIST
                            new_cust_pack_name= input('Customer name in Staycation record. Enter new package name. Warning new name will override old name: ').title()
                            new_cust_pack_name_update= basic_sorts_searches_functions.linear_search_pack_name(staycation_booking_details_dict,new_cust_pack_name)


                            if new_cust_pack_name_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                                print('Name entered does not exists. Check the record and try again')
                                pass

                            elif new_cust_pack_name in customer_package_name_list_5:

                                #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                                #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                                while new_cust_pack_name in customer_package_name_list_5:
                                    print('New Package Name {} Accepted'.format(new_cust_pack_name))

                                    pack_name_update = new_cust_pack_name_update["package_name"]

                                    cost_update = new_cust_pack_name_update["cost"]

                                    print('Package Name will be sorted using Gnome Sort')

                                    cust_val_update["package_name"] = pack_name_update
                                    cust_val_update["cost"] = cost_update
                                    advanced_sorts_functions.gnomeSort(staycation_booking_details_dict)
                                    for i in staycation_booking_details_dict:

                                        # print('new cust_val_update: ',cust_val_update["package_name"])

                                        print("Customer name:", i["customer_name"], end=" ")

                                        print("Package name:", i["package_name"], end=" ")

                                        print("Pax number:", i["pax"], end=" ")

                                        print("Cost SGD:", i["cost"])

                                        advanced_sorts_functions.gnomeSort(staycation_booking_details_dict)
                                    break


                        elif update_choices == "3":

                            print('You are about to change the cost for {} Package'.format(current_cust_package_name))

                            while True:
                                try:
                                    new_cost = int(input('Enter new cost: S$ '))
                                    break
                                except:
                                    print('Please Enter Only Numbers and do not enter Blanks.')
                                    print()

                            cust_records_cost_affected_5 = []

                            for i in staycation_booking_details_dict:

                                if cust_val_update["package_name"] in i["package_name"]:

                                    cust_records_cost_affected_5 += [i]

                                    for new in cust_records_cost_affected_5:

                                        new["cost"] = new_cost     #update the cost in array of all dup_packages

                            advanced_sorts_functions.combSort(staycation_booking_details_dict)

                            #Codes to ensure that any other duplicate package cost will also change
                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])

                            print()

                        elif update_choices == "4":
                            print('')
                            print('You are about to change the current pax for {} Package. Current pax {}.'.format(cust_val_update["package_name"],cust_val_update["pax"]))
                            while True:
                                try:
                                    new_pax = int(input('Enter new pax: '))
                                    break
                                except:
                                    print('Please Enter Only Numbers and do not enter Blanks.')
                                    print()

                            cust_val_update["pax"] = new_pax
                            advanced_sorts_functions.oddEvenSort(staycation_booking_details_dict, len(staycation_booking_details_dict))
                            for i in staycation_booking_details_dict:

                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])

                    else:
                        print('Error has Occured')

    #---------------------------------------------------------------------------------------------------------------------------------------------

                elif choice == "6":
                    advanced_sorts_functions.cocktailSort(staycation_booking_details_dict)
                    pack_name_to_search = input('Enter the Pack name you wish to update: ').title()
                    # re_enter_name =''
                    cust_val_update_using_pack_name = basic_sorts_searches_functions.binary_search(staycation_booking_details_dict,pack_name_to_search)


                    if cust_val_update_using_pack_name == -1: #Binary search return -1
                        print('Package Name entered does not exists. Check the record and try again')
                        print('')
                        continue

                    #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                    customer_name_list_6=[]
                    for cust_name_using_packname in staycation_booking_details_dict:
                        name_6 = cust_name_using_packname["customer_name"]
                        customer_name_list_6 += [(name_6)]

                    current_cust_package_name_6= cust_val_update_using_pack_name["package_name"]
                    cust_cost_update_6 = cust_val_update_using_pack_name["pax"] * cust_val_update_using_pack_name["cost"]

                    cust_having_searched_pack = cust_val_update_using_pack_name["customer_name"]

                    pack_cost_per_pax_6 = cust_val_update_using_pack_name["cost"]


                    print('{} Package currently belongs to Customer {}. Package Cost Per Pax: S$ {}'.format(pack_name_to_search, cust_having_searched_pack, pack_cost_per_pax_6))

                    #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                    customer_package_name_list_6 = []
                    for cust_pack_name_6 in staycation_booking_details_dict:
                        pack_name_6 = cust_pack_name_6["package_name"]
                        customer_package_name_list_6 += [(pack_name_6)]
                    print('package_name_list',customer_package_name_list_6)


                    if cust_val_update_using_pack_name == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                        print('Name entered does not exists. Check the record and try again')
                        continue

                    #if cust name entered and is in list this will update cust name record
                    elif (cust_val_update_using_pack_name in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict
                        update_choices = input('What would you like to change\n'
                                               '1.Customer name\n'
                                               '2.Package Name\n'
                                               '3.Cost\n'
                                               '4.Pax\n'                                           
                                               'Choice: ')

                        if update_choices == "1":

                            new_cust_name_6= input('Package name in Staycation Record. Enter the new Customer Name. New name will override old name: ').title()

                            if new_cust_name_6 not in customer_name_list_6:

                                #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                                #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                                print('New Customer Name {} Accepted'.format(new_cust_name_6))

                                print('Customer Name will now be sorted using Pancake Sort')
                                print('')
                                cust_val_update_using_pack_name["customer_name"] = new_cust_name_6
                                advanced_sorts_functions.pancakeSort(staycation_booking_details_dict)
                                for i in staycation_booking_details_dict:


                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost SGD:", i["cost"])


                            else:
                                #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                                while new_cust_name_6 in customer_name_list_6:
                                    new_cust_name_6= input('New Customer Name already exists. Enter a new name that does not exist: ').title()
                                    while new_cust_name_6 not in customer_name_list_6:
                                        print('New Customer Name {} Accepted'.format(new_cust_name_6))
                                        print('Customer Name will now be sorted using Shell Sort')
                                        print('')
                                        cust_val_update_using_pack_name["customer_name"] = new_cust_name_6
                                        advanced_sorts_functions.shellSort(staycation_booking_details_dict)
                                        for i in staycation_booking_details_dict:

                                            print("Customer name:", i["customer_name"], end=" ")
                                            print("Package name:", i["package_name"], end=" ")
                                            print("Pax number:", i["pax"], end=" ")
                                            print("Cost SGD:", i["cost"])

                                        break


                        elif update_choices == "2": #NOTE FOR PACKAGE NAME ITS THE OPPOSITE OF UPDATE CUST NAME. SUCCESSFUL CHANGE ONLY HAPPPENDS IF PACK NAME CUST ENTERS EXSISTS IN THE PACK NAME LIST
                            new_cust_pack_name_6= input('Customer name in Staycation record. Enter new package name. Warning new name will override old name: ').title()
                            new_cust_pack_name_update_6= basic_sorts_searches_functions.linear_search_pack_name(staycation_booking_details_dict,new_cust_pack_name_6)

                            if new_cust_pack_name_update_6 == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                                print('Name entered does not exists. Check the record and try again')
                                pass

                            elif new_cust_pack_name_6 in customer_package_name_list_6:

                                #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                                #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                                while new_cust_pack_name_6 in customer_package_name_list_6:
                                    print('New Package Name {} Accepted'.format(new_cust_pack_name_6))

                                    pack_name_update = new_cust_pack_name_update_6["package_name"]

                                    cost_update = new_cust_pack_name_update_6["cost"]
                                    print('Package Name will be sorted using Cocktail Sort')
                                    print('')
                                    cust_val_update_using_pack_name["package_name"] = pack_name_update

                                    cust_val_update_using_pack_name["cost"] = cost_update
                                    advanced_sorts_functions.cocktailSort(staycation_booking_details_dict)
                                    for i in staycation_booking_details_dict:
                                        print("Customer name:", i["customer_name"], end=" ")
                                        print("Package name:", i["package_name"], end=" ")
                                        print("Pax number:", i["pax"], end=" ")
                                        print("Cost SGD:", i["cost"])


                                    break

                            else:
                                #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                                while new_cust_pack_name_6 not in customer_package_name_list_6:
                                    new_cust_pack_name_6= input('Entered Package Name does not exsits. Enter a new name that exisst: ').title()
                                    while new_cust_pack_name_6 in customer_package_name_list_6:

                                        print('New Package Name {} Accepted.'.format(new_cust_pack_name_6))

                                        # sort_functions.shellSort(staycation_booking_details_dict)

                                        pack_name_update = new_cust_pack_name_update_6["package_name"]

                                        pax_num_update = new_cust_pack_name_update_6["pax"] =+ 1

                                        cost_update = new_cust_pack_name_update_6["cost"]

                                        break

                        elif update_choices == "3":
                            print('You are about to change the cost for {} Package'.format(current_cust_package_name_6))

                            while True:
                                try:
                                    new_cost = int(input('Enter new cost: S$ '))
                                    print()
                                    break
                                except:
                                    print('Please Enter Only Numbers and do not enter Blanks.')
                                    print()

                            #Codes to ensure that any other duplicate package cost will also change
                            cust_records_cost_affected = []
                            for i in staycation_booking_details_dict:
                                if cust_val_update_using_pack_name["package_name"] in i["package_name"]:

                                    cust_records_cost_affected += [i]

                                    for new in cust_records_cost_affected:

                                        new["cost"] = new_cost     #update the cost in array of all duppackages
                            advanced_sorts_functions.combSort(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            print()

                        elif update_choices == "4":
                            print('')
                            print('You are about to change the current pax for {} Package. Current pax {}.'.format(cust_val_update_using_pack_name["package_name"],cust_val_update_using_pack_name["pax"]))
                            while True:
                                try:
                                    new_pax = int(input('Enter new pax: '))
                                    break
                                except:
                                    print('Please Enter Only Numbers and do not enter Blanks.')
                                    print()

                            cust_val_update_using_pack_name["pax"] = new_pax
                            print('Pax number will be sorted using OddEven Sort')
                            print('')
                            advanced_sorts_functions.oddEvenSort(staycation_booking_details_dict, len(staycation_booking_details_dict))
                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])

                    else:
                        print('Error Occured')

    #---------------------------------------------------------------------------------------------------------------------------------------------


                elif choice == "7":
                    while True:
                        try:

                            r1 = int(input('Minimum Range Value: S$'))

                            r2 =int(input("Maximum Range Value: S$"))
                            input_validation= basic_sorts_searches_functions.val_ran_validation( r1 , r2 )
                            if input_validation == False:
                                break
                        except:
                            print('Please Enter Only Numbers and do not enter Blanks.')
                            print()

                    user_range_sort_opt_accepable_opts = ['A', 'D']
                    user_range_sort_opt = input('You are about to perform Range Selection. Would you like to sort the Results in Ascending or Descending Order?\n'
                                                'A: Ascending\n'
                                                'D: Descending\n'
                                                'Enter your choice: ').upper()

                    while user_range_sort_opt =='' or user_range_sort_opt not in user_range_sort_opt_accepable_opts:
                        user_range_sort_opt_retry = input('Please Do Not Enter Nothing. Ensure that if you have entered an option. Check to see if it is an acceptable value: ').upper()
                        if user_range_sort_opt_retry in user_range_sort_opt_accepable_opts:
                            user_range_sort_opt = user_range_sort_opt_retry

                            print()

                    if user_range_sort_opt in user_range_sort_opt_accepable_opts:

                        if user_range_sort_opt == 'A':
                            print('Range Search Result will be sorted using Heap Sort (Ascending)')
                            print('')
                            asnd_ran= basic_sorts_searches_functions.val_ran(r1,r2)
                            advanced_sorts_functions.heapSort(asnd_ran)
                            for i in asnd_ran:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                                advanced_sorts_functions.heapSort(asnd_ran)


                        elif user_range_sort_opt == 'D':
                            print('Range Search Result will be sorted using Heap Sort (Descending)')
                            asnd_ran = basic_sorts_searches_functions.val_ran(r1,r2)
                            advanced_sorts_functions.heapSort_reverse(asnd_ran)
                            for i in asnd_ran:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost SGD:", i["cost"])
                            continue


# sort_functions.cocktailSort(staycation_booking_details_dict)
                elif choice == "x":


                    break
                elif choice != user_inputs:
                    print('Please enter from 1 to 8. Type X to quit')

    else:
        print('This system is only for Admins. Please check the Word Document for password.\n'
              'Note that the password is case-sensitive')



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Keyboard error detected. System will shutdown')
    except ValueError:
        print('Value Error has occured. System will now shutdown')

    except RuntimeError:
        print('Runtime error has occured. We hope this error does not happen. System will now shutdown')

    except:
        print('An unexpected error has occured. Please restart the programme and try again')


