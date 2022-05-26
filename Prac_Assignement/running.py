
import sort_functions
try:
    user_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', 'end']

    staycation_booking_details_dict = [
        {"customer_name": "Bill", "package_name": "Sentosa", "cost": 200, "pax": 20},
            {"customer_name": "Amos", "package_name": "Riverside", "cost": 100, "pax": 30},
                {"customer_name": "Tan", "package_name": "Sea", "cost": 50, "pax": 7},
                    {"customer_name": "Beverly", "package_name": "Wind", "cost": 900, "pax": 3},
                        {"customer_name": "Theresa", "package_name": "Rock", "cost": 300, "pax": 29},
                            {"customer_name": "Ellen", "package_name": "Fire", "cost": 200, "pax": 17},
                                {"customer_name": "Hollow", "package_name": "Air", "cost": 190, "pax": 23},
                                    {"customer_name": "Jill", "package_name": "Ocean", "cost": 400, "pax": 28},
                                        {"customer_name": "Jane", "package_name": "Atlantic", "cost": 700, "pax": 10},
                                            {"customer_name": "Koen", "package_name": "Towers", "cost": 100, "pax": 36}
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
                cust_val_update = sort_functions.linear_search(staycation_booking_details_dict,cust_name_to_search)

                customer_list=[]
                for i in staycation_booking_details_dict:
                    customer_name= i["customer_name"]
                    customer_list.append(customer_name)

                print('Cust_list:',customer_list)
                print('Cust_val_update: ',cust_val_update)
                print(staycation_booking_details_dict)

                while (cust_val_update not in customer_list) and (cust_val_update not in staycation_booking_details_dict):
                    print('This person does not exists')
                    cust_val_update = input('Enter new name')
                    if cust_val_update in customer_list or cust_val_update in staycation_booking_details_dict:

                        print('custvalupdate',cust_val_update)
                        print('cust_lists',customer_list)
                        print('staycation_dict: ',staycation_booking_details_dict)


                while (cust_val_update in staycation_booking_details_dict) or (cust_val_update in customer_list):
                    #2
                    print('Chosen name will be overridded..')
                    cust_val_update = input('Enter neww name: ')
                    print('New name saved \n'
                          'Printing new name list')

                    print('custvalupdate',cust_val_update)
                    print('cust_lists',customer_list)
                    print('staycation_dict #2: ',staycation_booking_details_dict)


                    cust_name_to_search["customer_name"]= cust_val_update
                    print('custvalupdate',cust_val_update)
                    print('cust_lists',customer_list)
                    print('staycation_dict #2: ',staycation_booking_details_dict)



                if cust_val_update not in customer_list and (cust_val_update not in staycation_booking_details_dict):
                    #3

                    cust_name_to_search["customer_name"]= cust_val_update
                    print('Sucss')
                    sort_functions.shellSort(staycation_booking_details_dict)
                    for i in staycation_booking_details_dict:
                        print(i["customer_name"])


            elif choice == "6":
                pack_name_to_search = input('Enter the Package Name you wish to search: ')
                binary_sort_algo_options = input('You are about to perform Binary Search. The Package Name Needs to be sorted first. Choose your preffered sorting algorithm \n'
                                                    '1: Bubble Sort \n'
                                                    '2: Optimised Bubble Sort \n'
                                                    '3: Recursive Bubble Sort \n'
                                                    '4: Pancake Sort \n'
                                                 )
                if binary_sort_algo_options == "1":
                    print('Staycation booking will now be sorted using Bubble Sort')
                    sort_functions.bubbleSort(staycation_booking_details_dict)
                elif binary_sort_algo_options == "2":
                    print('Staycation booking will now be sorted using Optimized Bubble Sort')
                    sort_functions.bubbleSort_optimized(staycation_booking_details_dict)
                elif binary_sort_algo_options =="3":
                    print('Staycation booking will now be sorted using Recursive Bubble Sort')
                    sort_functions.bubbleSortRecursive(staycation_booking_details_dict)
                elif binary_sort_algo_options == "4":
                    print('Staycation booking will now be sorted using Pancake Sort')
                    sort_functions.pancakeSort(staycation_booking_details_dict,len(staycation_booking_details_dict))
                else:
                    print('Please choose from option 1 to 4')

                pack_val_update = sort_functions.binary_search(staycation_booking_details_dict,pack_name_to_search)

                if pack_val_update == False:
                    print('The Package You Are Searching For Does Not Exist.')
                else:
                    update_pack_name = input('Enter new Package name. Warning: This will Overide Previous Package Name').title()

                    for dup in staycation_booking_details_dict:
                        if update_pack_name in dup["package_name"]:
                            dup_warning = input('New Package name exists. Do you wish to Override Existing Package Name? y-yes, n-no')
                            if dup_warning == 'y':
                                pack_val_update["package_name"]= update_pack_name
                                break
                            else:
                                print('Update Package Name Failed.')
                                break

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

