import sort_functions
import sys
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

# while True:
#     gay= input('Search')
#     hay2= input('Search again')
#     if hay2 == "n":
#         break
#     else:
#         print()



def encrypt(text,s):
    result =''
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char)+ s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
# text = "Gay"
# s = 4
#
# print("Plain Text : " + text)
# print("Shift pattern : " + str(s))
# print("Cipher: " + encrypt(text,s))
# non_plain_encrypt = encrypt(text,s)
# print(non_plain_encrypt)
# user_txt= input('shit')
# user_txt_encypt= encrypt(user_txt,s)
# print(user_txt_encypt)
#
# if non_plain_encrypt == user_txt_encypt:
#     print('Access Granted')


# passwd =''
# attempt = 0
# while (non_plain_encrypt != user_txt_encypt) and (attempt < 3):
#     passwd = ()
#     attempt = attempt + 1
#     print('dwqsq',non_plain_encrypt)
#     print('mdwmkw3', user_txt_encypt)
#     print ('No that is not correct. Try again.')
#
#     if attempt == 3:
#         print ('Sorry you have reached maximum number of attempts')
#         break
#
#     if (non_plain_encrypt == user_txt_encypt):
#         print('Access Granted!')


# passwd_stored = sort_functions.encrypt('Gay', 4)
# user_enter_passwd = input('Enter passwd: ')
# user_enter_passwd_encrypt = sort_functions.encrypt(user_enter_passwd, 4)
# attempt =0
#
# while (passwd_stored != user_enter_passwd_encrypt) and (attempt < 4):
#     print('Incorect passwd. try again. Attemot number {}'.format(attempt))
#     user_enter_passwd_encrypt = sort_functions.encrypt((input('Enter passwd again')), 4)
#     attempt +=1
#
#
#
#     if attempt == 4:
#         print('Max reacned')
#         break
#
#     if (passwd_stored == user_enter_passwd_encrypt):
#         print('Access')
