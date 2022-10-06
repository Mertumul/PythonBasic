print(""" 
*****************************************************
USER LOGIN PROGRAM
*****************************************************
""")

sys_username = "karen"
sys_password = "sunshine"
right_of_entry = 3
while True:
    toexit = input("Press 'q' to exit")
    if (toexit == 'q'):
        break

    else:
        if (right_of_entry > 0):
            username = input("please enter your username:")
            password = input("please enter your password:")
            if (username == sys_username and password == sys_password):
                print("Login Succesfull..")
                break

            elif (username != sys_username and password == sys_password):
                print("invalid username")
            elif (username == sys_username and password != sys_password):
                print("invalid password")
            else:
                print("invalid username and password")
            right_of_entry -= 1

        else:
            print("Your login has expired")
            break
