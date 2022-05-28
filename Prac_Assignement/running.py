
import sort_functions
try:
    user_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', 'end']

    staycation_booking_details_dict = [
        {"customer_name": "Bill", "package_name": "Package I", "cost": 200, "pax": 20},
            {"customer_name": "Amos", "package_name": "Package J", "cost": 100, "pax": 30},
                {"customer_name": "Tan", "package_name": "Package H", "cost": 50, "pax": 7},
                    {"customer_name": "Beverly", "package_name": "Package C", "cost": 900, "pax": 3},
                        {"customer_name": "Theresa", "package_name": "Package E", "cost": 300, "pax": 29},
                            {"customer_name": "Ellen", "package_name": "Package B", "cost": 200, "pax": 17},
                                {"customer_name": "Hollow", "package_name": "Package A", "cost": 190, "pax": 23},
                                    {"customer_name": "Jill", "package_name": "Package G", "cost": 400, "pax": 28},
                                        {"customer_name": "Jane", "package_name": "Package F", "cost": 700, "pax": 10},
                                            {"customer_name": "Koen", "package_name": "PackageD", "cost": 100, "pax": 36}
                                        ]


    begin_menu= input('Press y to start.').lower()
    if begin_menu == 'y':
        while True:
            print("1. Display all records")
            print("2. Sort record by Customer Name using Bubble sort")
            print("3. Sort record by Package Name using Selection sort")
            print("4. Sort record by Package Cost using Insertion sort")
            print("5. Search record by Customer Name using Linear Search and update record")
            print("6. Search record by Package Name using Binary Search and update record")
            print("7. List records range from $X to $Y. e.g $100-200")
            print("8. Exit Application")
            choice = input("Enter choice: ").lower()

            if choice == "1":
                print('Printing all Staycation Record Displays')
                for i in staycation_booking_details_dict:
                    print("Customer name:", i["customer_name"], end=" ")
                    print("Package name:", i["package_name"], end=" ")
                    print("Pax number:", i["pax"], end=" ")
                    print("Cost:", i["cost"])
            elif choice == "2":
                bubble_sort_opts= input('Enter which BubbleSort Option You Would Like \n'
                      '1: Bubble Sort \n'
                      '2: Optimised Bubble Sort \n'
                      '3: Recursive Bubble Sort \n'
                                        )

                if bubble_sort_opts == "1":
                    print('Staycation booking will now be sorted using Bubble Sort')
                    sort_functions.bubbleSort(staycation_booking_details_dict)
                elif bubble_sort_opts =="2":
                    print('Staycation booking will now be sorted using Optimized Bubble Sort')
                    sort_functions.bubbleSort_optimized(staycation_booking_details_dict)
                elif bubble_sort_opts =="3":
                    print('Staycation booking will now be sorted using Recursive Bubble Sort')
                    sort_functions.bubbleSortRecursive(staycation_booking_details_dict)
                else:
                    print('Invalid options')
            elif choice == "3":
                sort_functions.selection_sort(staycation_booking_details_dict)
            elif choice == "4":
                sort_functions.insertion_sort(staycation_booking_details_dict)

            elif choice == "5":
                cust_name_to_search = input('Enter the customer name you wish to update: ').title()
                re_enter_name =''
                cust_val_update = sort_functions.linear_search(staycation_booking_details_dict,cust_name_to_search)

                #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                customer_name_list=[]
                for cust_name in staycation_booking_details_dict:
                    name = cust_name["customer_name"]
                    customer_name_list += [(name)]
                print('customer_name_list',customer_name_list)
                print('cust_name_search; ',cust_name_to_search)
                print('cust_val_update: ',cust_val_update)



                if cust_val_update == False:
                    print('Name entered does not exists. Check the record and try again')
                    pass
                #if cust name entered and is in list this will update cust name record
                elif (cust_val_update in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict

                    new_cust_name= input('Customer name in Staycation Record. Enter the new cust name. New name will override old name: ').title()

                    if new_cust_name not in customer_name_list:
                        #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                        #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                        while new_cust_name not in customer_name_list:
                            print('New Customer Name {} Accepted #3'.format(new_cust_name))
                            print('cust_val_update #3',cust_val_update)
                            sort_functions.shellSort(staycation_booking_details_dict)
                            for i in staycation_booking_details_dict:
                                cust_val_update["customer_name"] = new_cust_name

                                print('Staycation_Dict_Updated #3?: ',i["customer_name"])
                                sort_functions.shellSort(staycation_booking_details_dict)

                            break
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

                        #
                        #
                        # #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                        # #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                        # while new_cust_name not in customer_name_list:
                        #     print('New Customer Name {} Accepted #3'.format(new_cust_name))
                        #     print('cust_val_update #3',cust_val_update)
                        #     sort_functions.shellSort(staycation_booking_details_dict)
                        #     for i in staycation_booking_details_dict:
                        #         cust_val_update["customer_name"] = new_cust_name
                        #         print('Staycation_Dict_Updated #3?: ',i["customer_name"])
                        #     break


                    # print('staycation_booking_details_dict #1',staycation_booking_details_dict)
                    # print('cust_name_to_search',cust_name_to_search)

                else:
                    print('Err Occured')


            elif choice == "6":
                sort_functions.selection_sort(staycation_booking_details_dict)
                pack_name_search = input("Which Package Name would you to search using Binary Search and update record?: ")
                recordToUpdatePack = sort_functions.binary_search(staycation_booking_details_dict,pack_name_search)

                #code to store only cust names in a list for comparison MAY BE REMOVED/MODIFIED TO FIT QUES REQUIREMENTS
                pack_name_list=[]
                for i in staycation_booking_details_dict:
                    pack_name = i["package_name"]
                    pack_name_list.append(i)
                print('customer_name_list',pack_name_list)
                print('cust_name_search; ',pack_name_search)
                print('cust_val_update: ',recordToUpdatePack)

                if recordToUpdatePack == -1:
                    print('Pack Name entered does not exists. Check the record and try again')
                    pass
                #if cust name entered and is in list this will update cust name record
                elif (recordToUpdatePack in staycation_booking_details_dict): #1 in cause one is just a name and one is the entire dict

                    new_pack_name= input('Pack name in Staycation Record. Enter the new cust name. New name will override old name: ')

                    #assume that the new name user wants to update to cannot be in the list, prevent duplicate records
                    while new_pack_name in pack_name_list:
                        new_pack_name= input('New Pack Name already exsits. Enter a new name that does not exisst: ')


                    while new_pack_name not in pack_name_list:
                        print('New Pack Name {} Accepted #2'.format(new_pack_name))
                        print('pack_val_update #2',recordToUpdatePack)
                        sort_functions.pancakeSort(staycation_booking_details_dict)
                        for i in staycation_booking_details_dict:
                            recordToUpdatePack["package_name"] = new_pack_name
                            print('Staycation_Dict_Updated #2?: ',i["package_name"])
                        break

                    #codes if var 'cust_name_to_search' is in cust_list BUT var 'new_cust_name' is NOT in customer_list
                    #if new_cust_name is not in customer_list, means that var new_cust_name is unique and can be acceptted.
                    while new_pack_name not in pack_name_list:
                        print('New Package Name {} Accepted #3'.format(new_pack_name))
                        print('Pack_val_update #3',recordToUpdatePack)
                        sort_functions.heapSort(staycation_booking_details_dict)
                        for i in staycation_booking_details_dict:
                            recordToUpdatePack["package_name"] = new_pack_name
                            print('Staycation_Dict_Updated #3?: ',i["package_name"])
                        break


                    # print('staycation_booking_details_dict #1',staycation_booking_details_dict)
                    # print('cust_name_to_search',cust_name_to_search)

                else:
                    print('Err Occured')

                if recordToUpdatePack == -1:
                    print("Package Name not found!!!")

                else:
                    New_pack = input("Enter the New Name For Package: ")
                    recordToUpdatePack["package_name"] = New_pack


                # pack_name_to_search = input('Enter the Package Name you wish to search: ')
                # print('Package Name will be sorted using Pancake Sort.')
                # sort_functions.pancakeSort(staycation_booking_details_dict,len(staycation_booking_details_dict))
                #
                #
                # pack_val_update = sort_functions.binary_search(staycation_booking_details_dict,pack_name_to_search)
                #
                # if pack_val_update == False:
                #     print('The Package You Are Searching For Does Not Exist.')
                # else:
                #     update_pack_name = input('Enter new Package name. Warning: This will Overide Previous Package Name').title()
                #
                #     for dup in staycation_booking_details_dict:
                #         if update_pack_name in dup["package_name"]:
                #             dup_warning = input('New Package name exists. Do you wish to Override Existing Package Name? y-yes, n-no')
                #             if dup_warning == 'y':
                #                 pack_val_update["package_name"]= update_pack_name
                #                 break
                #             else:
                #                 print('Update Package Name Failed.')
                #                 break

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
                print('You have entered Exit Application')
                order = False
                break
            elif choice != user_inputs:
                print('Please enter from 1 to 8. Type end to quit')

    else:
        print('Goodbye')
except IOError:
    print('Error')


