# OPTION 1 2 3 4 REQUIRES ADMIN USE
# LOOK AT OPT 5 AND 6 SUB MENU FOR ADMIN USAGE
#CHANGES TO OPT 6 NOT DONE -30/6/2022

import sort_functions
try:
    user_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', 'end']

    staycation_booking_details_dict = [
        {"customer_name": "Bill", "package_name": "Fire", "cost": 15, "pax": 10},
            {"customer_name": "Amos", "package_name": "Air", "cost": 20, "pax": 5},
                {"customer_name": "Tan", "package_name": "Water", "cost": 10, "pax": 4},
                    {"customer_name": "Beverly", "package_name": "Earth", "cost": 9, "pax": 3},
                        {"customer_name": "Theresa", "package_name": "Lava", "cost": 5, "pax": 1},
                            {"customer_name": "Ellen", "package_name": "Sea", "cost": 20, "pax": 2},
                                {"customer_name": "Hollow", "package_name": "Mountain", "cost": 15, "pax": 10},
                                    {"customer_name": "Jill", "package_name": "Zoo", "cost": 10, "pax": 15},
                                        {"customer_name": "Jane", "package_name": "Desert", "cost": 11, "pax": 4},
                                            {"customer_name": "Koen", "package_name": "Oceania", "cost": 12, "pax": 4}
                                        ]


    begin_menu= input('Press y to start.').lower()
    if begin_menu == 'y':
        while True:
            print("1. Display all records (Requires Admin)")
            print("2. Sort record by Customer Name using Bubble sort (Requires Admin)")
            print("3. Sort record by Package Name using Selection sort (Requires Admin)")
            print("4. Sort record by Package Cost using Insertion sort (Requires Admin)")
            print("5. Search record by Customer Name using Linear Search and update record")
            print("6. Search record by Package Name using Binary Search and update record")
            print("7. List records range from $X to $Y. e.g $100-200")
            print("X. Exit Application")
            print('Note that some options require Admin Use')
            choice = input("Enter choice: ").lower()

            if choice == "1":

                admin_only_warning= input('This option is only for admins.\n'
                                          'Are you an Admin Y/N ?: ').upper()
                if admin_only_warning == "Y":
                    passwd_stored = sort_functions.encrypt('Gay', 4)
                    user_enter_passwd = input('Enter passwd: ')
                    user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                    attempt =0

                    while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                        print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                        user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                        attempt +=1

                        if attempt == 4:
                            sort_functions.admin_pass_countdown()
                            print('')

                            break

                    if (passwd_stored == user_enter_passwd_encrypt):
                        print('Printing Staycation Record')
                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost:", i["cost"])



            elif choice == "2":

                admin_only_warning= input('This option is only for admins.\n'
                                          'Are you an Admin Y/N ?: ').upper()
                if admin_only_warning == "Y":
                    passwd_stored = sort_functions.encrypt('Gay', 4)
                    user_enter_passwd = input('Enter passwd: ')
                    user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                    attempt =0

                    while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                        print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                        user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                        attempt +=1

                        if attempt == 4:
                            sort_functions.admin_pass_countdown()
                            print('')
                            break

                    if (passwd_stored == user_enter_passwd_encrypt):

                        bubble_sort_opts= input('Enter which BubbleSort Option You Would Like \n'
                              '1: Bubble Sort \n'
                              '2: Optimised Bubble Sort \n')

                        if bubble_sort_opts == "1":
                            order_input = input('Would you like the display in Ascending or Descending Order?'
                                                'A: Ascending'
                                                'D: Descending'
                                                'input choice: ').upper()
                            if order_input == "A":
                                print('Staycation booking will now be sorted using Bubble Sort in Ascending Order.')
                                sort_functions.bubbleSort(staycation_booking_details_dict)
                                for i in staycation_booking_details_dict:
                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost:", i["cost"])
                            elif order_input == "D":
                                print('Staycation booking will now be sorted using Bubble Sort in Descending Order.')
                                sort_functions.bubbleSort_reverse(staycation_booking_details_dict)
                                for i in staycation_booking_details_dict:
                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost:", i["cost"])
                            else:
                                print('Invalid Input')
                                print()

                        elif bubble_sort_opts =="2":
                            order_input = input('Would you like the display in Ascending or Descending Order?'
                                                'A: Ascending'
                                                'D: Descending'
                                                'input choice: ').upper()
                            if order_input == "A":
                                print('Staycation booking will now be sorted using Optimized Bubble Sort in Ascending Order')
                                sort_functions.bubbleSort_optimized(staycation_booking_details_dict)

                                for i in staycation_booking_details_dict:
                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost:", i["cost"])
                                print('')

                            elif order_input == "D":
                                print('Staycation booking will now be sorted using Optimized Bubble Sort in Descending Order')
                                sort_functions.bubbleSort_optimized_reverse(staycation_booking_details_dict)

                                for i in staycation_booking_details_dict:
                                    print("Customer name:", i["customer_name"], end=" ")
                                    print("Package name:", i["package_name"], end=" ")
                                    print("Pax number:", i["pax"], end=" ")
                                    print("Cost:", i["cost"])
                                print('')
                        else:
                            print('Invalid options')

            elif choice == "3":

                admin_only_warning= input('This option is only for admins.\n'
                                          'Are you an Admin Y/N ?: ').upper()

                if admin_only_warning == "Y":
                    passwd_stored = sort_functions.encrypt('Gay', 4)
                    user_enter_passwd = input('Enter passwd: ')
                    user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                    attempt =0

                    while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                        print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                        user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                        attempt +=1

                        if attempt == 4:

                            sort_functions.admin_pass_countdown()
                            print('')
                            break

                    if (passwd_stored == user_enter_passwd_encrypt):

                        order_input = input('Would you like the display in Ascending or Descending Order?'
                                                'A: Ascending'
                                                'D: Descending'
                                                'input choice: ').upper()

                        if order_input == "A":
                            print('Staycation booking will now be sorted using Selection Sort in Ascending Order')
                            sort_functions.selection_sort(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost:", i["cost"])
                            print('')

                        elif order_input == "D":
                            print('Staycation booking will now be sorted using Optimized Bubble Sort in Descending Order')
                            sort_functions.selection_sort_reverse(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost:", i["cost"])
                            print('')


            elif choice == "4":

                admin_only_warning= input('This option is only for admins.\n'
                                          'Are you an Admin Y/N ?: ').upper()
                if admin_only_warning == "Y":
                    passwd_stored = sort_functions.encrypt('Gay', 4)
                    user_enter_passwd = input('Enter passwd: ')
                    user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                    attempt =0

                    while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                        print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                        user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                        attempt +=1

                        if attempt == 4:
                            sort_functions.admin_pass_countdown()
                            print('')
                            break

                    if (passwd_stored == user_enter_passwd_encrypt):
                        order_input = input('Would you like the display in Ascending or Descending Order?'
                                                'A: Ascending'
                                                'D: Descending'
                                                'input choice: ').upper()
                        if order_input == "A":
                            print('Staycation booking will now be sorted using Insertion Sort in Aescending Order')
                            sort_functions.insertion_sort(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost:", i["cost"])
                            print('')

                        elif order_input == "D":
                            print('Staycation booking will now be sorted using Optimized Bubble Sort in Descending Order')
                            sort_functions.insertion_sort_reverse(staycation_booking_details_dict)

                            for i in staycation_booking_details_dict:
                                print("Customer name:", i["customer_name"], end=" ")
                                print("Package name:", i["package_name"], end=" ")
                                print("Pax number:", i["pax"], end=" ")
                                print("Cost:", i["cost"])
                            print('')

#---------------------------------------------------------------------------------------------------------------------------------------------



            elif choice == "5":
                cust_name_to_search = input('Enter the customer name you wish to update: ').title()
                # re_enter_name =''
                cust_val_update = sort_functions.linear_search(staycation_booking_details_dict,cust_name_to_search)


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

                print('customer_name_list',customer_name_list)
                print('cust_name_search; ',cust_name_to_search)
                print('cust_val_update: ',cust_val_update)

                print('Customer {} currently has the {} Package. Total Cost: S$ {}'.format(cust_name_to_search, current_cust_package_name, cust_cost_update))

                #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                customer_package_name_list_5 = []
                for cust_pack_name_5 in staycation_booking_details_dict:
                    pack_name_5 = cust_pack_name_5["package_name"]
                    customer_package_name_list_5 += [(pack_name_5)]
                print('package_name_list',customer_package_name_list_5)


                if cust_val_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                    print('Name entered does not exists. Check the record and try again')
                    continue

                #if cust name entered and is in list this will update cust name record
                elif (cust_val_update in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict
                    update_choices = input('What wanna change\n'
                                           '1.Cust name\n'
                                           '2.Packname\n'
                                           '3.Cost (Restricted For Admins Only)\n'
                                           '4.Pax'                                           
                                           'Choice: ')

                    if update_choices == "1":

                        new_cust_name= input('Customer name in Staycation Record. Enter the new cust name. New name will override old name: ').title()

                        if new_cust_name not in customer_name_list:
                            #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                            #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                            print('New Customer Name {} Accepted #3'.format(new_cust_name))
                            print('cust_val_update #3',cust_val_update)
                            sort_functions.shellSort(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                cust_val_update["customer_name"] = new_cust_name

                                print('Staycation_Dict_Updated #3?: ',i["customer_name"])
                                sort_functions.shellSort(staycation_booking_details_dict)

                        else:
                            #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                            while new_cust_name in customer_name_list:
                                new_cust_name= input('New Customer Name already exsits. Enter a new name that does not exisst: ').title()
                                while new_cust_name not in customer_name_list:
                                    print('New Customer Name {} Accepted #2'.format(new_cust_name))
                                    print('cust_val_update #2',cust_val_update)
                                    sort_functions.shellSort(staycation_booking_details_dict)
                                    for i in staycation_booking_details_dict:
                                        cust_val_update["customer_name"] = new_cust_name

                                        print('Staycation_Dict_Updated #2?: ',i["customer_name"])
                                        sort_functions.shellSort(staycation_booking_details_dict)
                                    break

                    elif update_choices == "2": #NOTE FOR PACKAGE NAME ITS THE OPPOSITE OF UPDATE CUST NAME. SUCCESSFUL CHANGE ONLY HAPPPENDS IF PACK NAME CUST ENTERS EXSISTS IN THE PACK NAME LIST
                        new_cust_pack_name= input('Customer name in Staycation record. Enter new package name. Warning new name will override old name: ').title()
                        new_cust_pack_name_update= sort_functions.linear_search_pack_name_5(staycation_booking_details_dict,new_cust_pack_name)
                        print('jsiwhsiwhswh' ,new_cust_pack_name_update)

                        if new_cust_pack_name_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                            print('Name entered does not exists. Check the record and try again')
                            pass

                        elif new_cust_pack_name in customer_package_name_list_5:

                            #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                            #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                            while new_cust_pack_name in customer_package_name_list_5:
                                print('New Package Name {} Accepted #3'.format(new_cust_pack_name))

                                # sort_functions.shellSort(staycation_booking_details_dict)

                                pack_name_update = new_cust_pack_name_update["package_name"]
                                print('gaysyysysys', pack_name_update)

                                cost_update = new_cust_pack_name_update["cost"]
                                print(cost_update)


                                print('efrr', new_cust_pack_name_update)
                                print('ednjenj', cust_val_update)


                                for i in staycation_booking_details_dict:
                                    cust_val_update["package_name"] = pack_name_update

                                    # print('new cust_val_update: ',cust_val_update["package_name"])

                                    cust_val_update["cost"] = cost_update

                                    print("Customer name:", i["customer_name"], end=" ")

                                    print("Package name:", i["package_name"], end=" ")

                                    print("Pax number:", i["pax"], end=" ")

                                    print("Cost:", i["cost"])
                                break

                        else:
                            #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                            while new_cust_pack_name not in customer_package_name_list_5:
                                new_cust_pack_name= input('Entered Package Name does not exsits. Enter a new name that exisst: ').title()
                                while new_cust_pack_name in customer_package_name_list_5:

                                    print('New Package Name {} Accepted #2'.format(new_cust_pack_name))

                                    # sort_functions.shellSort(staycation_booking_details_dict)

                                    pack_name_update = new_cust_pack_name_update["package_name"]
                                    print('gaysyysysys #3', pack_name_update)

                                    pax_num_update = new_cust_pack_name_update["pax"] =+ 1
                                    print('wnjdnwjdnj #3',pax_num_update)

                                    cost_update = new_cust_pack_name_update["cost"]
                                    print('mekdek #3 ',cost_update)


                                    break

                    elif update_choices == "3":

                            admin_only_warning= input('This option is only for admins.\n'
                                                      'Are you an Admin Y/N ?: ').upper()
                            if admin_only_warning == "Y":
                                passwd_stored = sort_functions.encrypt('Gay', 4)
                                user_enter_passwd = input('Enter passwd: ')
                                user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                                attempt =0

                                while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                                    print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                                    user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                                    attempt +=1

                                    if attempt == 4:
                                        sort_functions.admin_pass_countdown()

                                        break

                                if (passwd_stored == user_enter_passwd_encrypt):
                                        print('You are about to change the cost for {} Package'.format(current_cust_package_name))
                                        new_cost = int(input('Enter new cost: S$ '))


                                        for i in staycation_booking_details_dict:
                                            # new_cust_pack_name_update["pax"] = pax_num_update
                                            cust_val_update["cost"] = new_cost

                                            # print('new cust_val_update: ',cust_val_update["package_name"])

                                            print("Customer name:", i["customer_name"], end=" ")
                                            print("Package name:", i["package_name"], end=" ")
                                            print("Pax number:", i["pax"], end=" ")
                                            print("Cost:", i["cost"])

                            elif admin_only_warning == "N":
                                print('This page is only for Admins. Please try again and select a differnt option.')
                                print()
                                break
                            else:
                                print("Invalid Option. Please try again: ")
                                print()

                    elif update_choices == "4":
                        print('')
                        print('You are about to change the current pax for {} Package. Current pax {}.'.format(cust_val_update["package_name"],cust_val_update["pax"]))
                        new_pax = int(input('Enter new pax: '))
                        cust_val_update["pax"] = new_pax

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost:", i["cost"])

                else:
                    print('Err Occured')





#---------------------------------------------------------------------------------------------------------------------------------------------

            #
            # elif choice == "6":
            #     sort_functions.selection_sort(staycation_booking_details_dict)
            #     pack_name_search = input("Which Package Name would you to search using Binary Search and update record?: ").title()
            #     recordToUpdatePack = sort_functions.binary_search(staycation_booking_details_dict,pack_name_search)
            #
            #     #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
            #     customer_name_list_6=[]
            #     for cust_name_6 in staycation_booking_details_dict:
            #         name_6 = cust_name_6["customer_name"]
            #         customer_name_list_6 += [(name_6)]
            #     print('customer_name_list_6',customer_name_list_6)
            #     print('pack_name_search; ',pack_name_search)
            #     print('cust_val_update: ',recordToUpdatePack)
            #
            #     #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
            #     customer_package_name_list_6 = []
            #     for cust_pack_name_6 in staycation_booking_details_dict:
            #         pack_name_6 = cust_pack_name_6["package_name"]
            #         customer_package_name_list_6 += [(pack_name_6)]
            #     print('package_name_list',customer_package_name_list_6)
            #
            #
            #     if recordToUpdatePack == -1: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
            #         print('Package Name entered does not exists. Check the record and try again')
            #         pass
            #
            #     #if cust name entered and is in list this will update cust name record
            #     elif (recordToUpdatePack in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict
            #         update_choices = input('What wanna change\n'
            #                                '1.Cust name\n'
            #                                '2.Packname\n'
            #                                'Choce: ')
            #
            #         if update_choices == "1":
            #             new_cust_name_6= input('Package name in Staycation Record. Enter the new customer name. New name will override old name: ').title()
            #
            #             if new_cust_name_6 not in customer_name_list_6:
            #                 #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
            #                 #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
            #                 while new_cust_name_6 not in customer_name_list_6:
            #                     print('New Customer Name {} Accepted #3'.format(new_cust_name_6))
            #                     print('rectoupdatepack #3',recordToUpdatePack)
            #                     sort_functions.bubbleSort_optimized(staycation_booking_details_dict)
            #                     for i in staycation_booking_details_dict:
            #                         recordToUpdatePack["customer_name"] = new_cust_name_6
            #
            #                         print('Staycation_Dict_Updated #3?: ',i["customer_name"], end=" ")
            #                         print('Staycation_Dict_Updated #3?: ',i["package_name"])
            #                         sort_functions.bubbleSort_optimized(staycation_booking_details_dict)
            #
            #                     break
            #
            #             else:
            #                 #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
            #                 while new_cust_name_6 in customer_name_list_6:
            #                     new_cust_name_6= input('New Customer Name already exsits. Enter a new name that does not exisst: ').title()
            #                     while new_cust_name_6 not in customer_name_list_6:
            #                         print('New Customer Name {} Accepted #2'.format(new_cust_name_6))
            #                         print('cust_val_update #2',recordToUpdatePack)
            #                         sort_functions.shellSort(staycation_booking_details_dict)
            #                         for i in staycation_booking_details_dict:
            #                             recordToUpdatePack["customer_name"] = new_cust_name_6
            #
            #                             print('Staycation_Dict_Updated #2?: ',i["customer_name"], end= " ")
            #                             print('Staycation_Dict_Updated #2?: ',i["package_name"])
            #                             sort_functions.shellSort(staycation_booking_details_dict)
            #
            #                         break
            #
            #
            #         elif update_choices == "2": #NOTE FOR PACKAGE NAME ITS THE OPPOSITE OF UPDATE CUST NAME. SUCCESSFUL CHANGE ONLY HAPPPENDS IF PACK NAME CUST ENTERS EXSISTS IN THE PACK NAME LIST
            #             sort_functions.selection_sort(staycation_booking_details_dict)
            #             new_cust_pack_name_6= input('Customer name in Staycation record. Enter new package name. Warning new name will override old name: ').title()
            #             new_cust_pack_name_update_6= sort_functions.binary_search(staycation_booking_details_dict,new_cust_pack_name_6)
            #             print('jsiwhsiwhswh' ,new_cust_pack_name_update_6)
            #
            #             if new_cust_pack_name_update_6 == -1: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
            #                 print('Name entered does not exists. Check the record and try again')
            #                 pass
            #
            #             elif new_cust_pack_name_6 in customer_package_name_list_6:
            #
            #                 #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
            #                 #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
            #
            #                 while new_cust_pack_name_6 in customer_package_name_list_6:
            #                     print('New Package Name {} Accepted #3'.format(new_cust_pack_name_6))
            #
            #                     # sort_functions.shellSort(staycation_booking_details_dict)
            #
            #                     pack_name_update_6 = new_cust_pack_name_update_6["package_name"]
            #                     print('gaysyysysys', pack_name_update_6)
            #
            #                     pax_num_update_6 = new_cust_pack_name_update_6["pax"] + 1
            #                     print('wnjdnwjdnj',pax_num_update_6)
            #
            #                     cost_update_6 = new_cust_pack_name_update_6["cost"]
            #                     print('mekdek ',cost_update_6)
            #
            #                     for i in staycation_booking_details_dict:
            #                         new_cust_pack_name_update_6["pax"] = pax_num_update_6
            #                         recordToUpdatePack["package_name"] = pack_name_update_6
            #                         recordToUpdatePack["pax"] = pax_num_update_6
            #                         recordToUpdatePack["cost"] = cost_update_6
            #
            #                     # print('new cust_val_update: ',cust_val_update["package_name"])
            #
            #                         print("Customer name:", i["customer_name"], end=" ")
            #                         print("Package name:", i["package_name"], end=" ")
            #                         print("Pax number:", i["pax"], end=" ")
            #                         print("Cost:", i["cost"])
            #
            #                     break


#-------------------------------------------------------------------------------------------------------------



            elif choice == "6":
                sort_functions.selection_sort(staycation_booking_details_dict)
                pack_name_to_search = input('Enter the Pack name you wish to update: ').title()
                # re_enter_name =''
                cust_val_update_using_pack_name = sort_functions.binary_search(staycation_booking_details_dict,pack_name_to_search)


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

                print('customer_name_list',customer_name_list_6)
                print('packaege_name_search; ',pack_name_to_search)
                print('cust_val_update customer rec that has the pack_nmae_to_search: ',cust_val_update_using_pack_name)

                print('Customer {} currently has the {} Package. Total Cost: S$ {}'.format(pack_name_to_search, current_cust_package_name_6, cust_cost_update_6))

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
                    update_choices = input('What wanna change\n'
                                           '1.Cust name\n'
                                           '2.Packname\n'
                                           '3.Cost (Restricted For Admins Only)\n'
                                           '4.Pax'                                           
                                           'Choice: ')

                    if update_choices == "1":

                        new_cust_name_6= input('Customer name in Staycation Record. Enter the new cust name. New name will override old name: ').title()

                        if new_cust_name_6 not in customer_name_list_6:
                            #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                            #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                            print('New Customer Name {} Accepted #3'.format(new_cust_name_6))
                            print('cust_val_update #3',cust_val_update_using_pack_name)
                            sort_functions.shellSort(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                cust_val_update_using_pack_name["customer_name"] = new_cust_name_6

                                print('Staycation_Dict_Updated #3?: ',i["customer_name"])
                                sort_functions.shellSort(staycation_booking_details_dict)

                        else:
                            #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                            while new_cust_name_6 in customer_name_list_6:
                                new_cust_name_6= input('New Customer Name already exsits. Enter a new name that does not exisst: ').title()
                                while new_cust_name_6 not in customer_name_list_6:
                                    print('New Customer Name {} Accepted #2'.format(new_cust_name_6))
                                    print('cust_val_update #2',cust_val_update_using_pack_name)
                                    sort_functions.shellSort(staycation_booking_details_dict)
                                    for i in staycation_booking_details_dict:
                                        cust_val_update_using_pack_name["customer_name"] = new_cust_name_6

                                        print('Staycation_Dict_Updated #2?: ',i["customer_name"])
                                        sort_functions.shellSort(staycation_booking_details_dict)
                                    break


                    elif update_choices == "2": #NOTE FOR PACKAGE NAME ITS THE OPPOSITE OF UPDATE CUST NAME. SUCCESSFUL CHANGE ONLY HAPPPENDS IF PACK NAME CUST ENTERS EXSISTS IN THE PACK NAME LIST
                        new_cust_pack_name= input('Customer name in Staycation record. Enter new package name. Warning new name will override old name: ').title()
                        new_cust_pack_name_update= sort_functions.linear_search_pack_name_5(staycation_booking_details_dict,new_cust_pack_name)
                        print('jsiwhsiwhswh' ,new_cust_pack_name_update)

                        if new_cust_pack_name_update == False: #FOR UPDTAE CHOICES 2, TRY IMPLEMENT THIS
                            print('Name entered does not exists. Check the record and try again')
                            pass

                        elif new_cust_pack_name in customer_package_name_list_5:

                            #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                            #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                            while new_cust_pack_name in customer_package_name_list_5:
                                print('New Package Name {} Accepted #3'.format(new_cust_pack_name))

                                # sort_functions.shellSort(staycation_booking_details_dict)

                                pack_name_update = new_cust_pack_name_update["package_name"]
                                print('gaysyysysys', pack_name_update)

                                cost_update = new_cust_pack_name_update["cost"]
                                print(cost_update)


                                print('efrr', new_cust_pack_name_update)
                                print('ednjenj', cust_val_update)


                                for i in staycation_booking_details_dict:
                                    cust_val_update["package_name"] = pack_name_update

                                    # print('new cust_val_update: ',cust_val_update["package_name"])

                                    cust_val_update["cost"] = cost_update

                                    print("Customer name:", i["customer_name"], end=" ")

                                    print("Package name:", i["package_name"], end=" ")

                                    print("Pax number:", i["pax"], end=" ")

                                    print("Cost:", i["cost"])
                                break

                        else:
                            #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                            while new_cust_pack_name not in customer_package_name_list_5:
                                new_cust_pack_name= input('Entered Package Name does not exsits. Enter a new name that exisst: ').title()
                                while new_cust_pack_name in customer_package_name_list_5:

                                    print('New Package Name {} Accepted #2'.format(new_cust_pack_name))

                                    # sort_functions.shellSort(staycation_booking_details_dict)

                                    pack_name_update = new_cust_pack_name_update["package_name"]
                                    print('gaysyysysys #3', pack_name_update)

                                    pax_num_update = new_cust_pack_name_update["pax"] =+ 1
                                    print('wnjdnwjdnj #3',pax_num_update)

                                    cost_update = new_cust_pack_name_update["cost"]
                                    print('mekdek #3 ',cost_update)


                                    break

                    elif update_choices == "3":

                            admin_only_warning= input('This option is only for admins.\n'
                                                      'Are you an Admin Y/N ?: ').upper()
                            if admin_only_warning == "Y":
                                passwd_stored = sort_functions.encrypt('Gay', 4)
                                user_enter_passwd = input('Enter passwd: ')
                                user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
                                attempt =0

                                while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
                                    print('Incorect passwd. try again. Attemot number {}'.format(attempt))
                                    user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
                                    attempt +=1

                                    if attempt == 4:
                                        sort_functions.admin_pass_countdown()

                                        break

                                if (passwd_stored == user_enter_passwd_encrypt):
                                        print('You are about to change the cost for {} Package'.format(current_cust_package_name))
                                        new_cost = int(input('Enter new cost: S$ '))


                                        for i in staycation_booking_details_dict:
                                            # new_cust_pack_name_update["pax"] = pax_num_update
                                            cust_val_update["cost"] = new_cost

                                            # print('new cust_val_update: ',cust_val_update["package_name"])

                                            print("Customer name:", i["customer_name"], end=" ")
                                            print("Package name:", i["package_name"], end=" ")
                                            print("Pax number:", i["pax"], end=" ")
                                            print("Cost:", i["cost"])

                            elif admin_only_warning == "N":
                                print('This page is only for Admins. Please try again and select a differnt option.')
                                print()
                                break
                            else:
                                print("Invalid Option. Please try again: ")
                                print()

                    elif update_choices == "4":
                        print('')
                        print('You are about to change the current pax for {} Package. Current pax {}.'.format(cust_val_update["package_name"],cust_val_update["pax"]))
                        new_pax = int(input('Enter new pax: '))
                        cust_val_update["pax"] = new_pax

                        for i in staycation_booking_details_dict:
                            print("Customer name:", i["customer_name"], end=" ")
                            print("Package name:", i["package_name"], end=" ")
                            print("Pax number:", i["pax"], end=" ")
                            print("Cost:", i["cost"])

                else:
                    print('Err Occured')

#---------------------------------------------------------------------------------------------------------------------------------------------


            elif choice == "7":
                while True:
                    try:
                        r1 = int(input('Low'))
                        r2 =int(input("high"))
                        break
                    except:
                        print('Enter a number')
                user_range_sort_opt = input('You are about to perform Range Selection. Would you like to sort the result? y/n').lower()
                if user_range_sort_opt == 'y':
                    asnd_ran= sort_functions.val_ran(r1,r2)
                    sort_functions.heapSort(asnd_ran)
                    for i in asnd_ran:
                        print("Customer name:", i["customer_name"], end=" ")
                        print("Package name:", i["package_name"], end=" ")
                        print("Pax number:", i["pax"], end=" ")
                        print("Cost:", i["cost"])
                elif user_range_sort_opt == 'n':
                    asnd_ran = sort_functions.val_ran(r1,r2)
                    for i in asnd_ran:
                        print("Customer name:", i["customer_name"], end=" ")
                        print("Package name:", i["package_name"], end=" ")
                        print("Pax number:", i["pax"], end=" ")
                        print("Cost:", i["cost"])
                else:
                    print('Invalid Opt')

            elif choice == "end":

                sort_functions.shutdown()
                order = False

                break
            elif choice != user_inputs:
                print('Please enter from 1 to 8. Type end to quit')

    else:
        print('Goodbye')
except IOError:
    print('Error')


