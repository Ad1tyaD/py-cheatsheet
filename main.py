#this is a python cheatsheet
#version:20220622
#Creator:Ad1tya

#Divison functions
def division():
    try_again = "Y"

    while try_again== "Y":
        print("\nWhat operation would you like to perform?\n"
              "\t 1. Simple integer division \n"
              "\t 2. Find remainder \n"
              "\t 3. Integer division without decimals \n\n"
              "Enter desired number to proceed \n"
              "Enter 0 to go back to main menu \n")
        choice = int(input("Your choice: "))

        if choice == 0:
            break

        numerator = int(input("What number you want to divide: "))
        denominator = int(input("Which number do you want to divide it by: "))

        if choice == 1:
            answer = numerator/denominator
            syntax = "answer = numerator/denominator"
        elif choice == 2:
            answer = numerator % denominator
            syntax = "answer = numerator%denominator"
        elif choice == 3:
            answer = numerator // denominator
            syntax = "answer = numerator//denominator"
        else:
            break

        print("--------------------------")
        print(f"Your answer is: {answer}")
        print("--------------------------")
        print(f"The code syntax is:\n{syntax}")
        print("--------------------------\n")

        try_again = input("\nDo you want to try again? (Y/N): ")


#String operations
def strings():
    try_again = "Y"

    while try_again == "Y":
        print("\nWhat operation would you like to perform?\n"
              "\t 1. String concatenation \n"
              "\t 2. Find string length \n"
              "\t 3. Count occurrence of substring\n"
              "Enter desired number to proceed \n"
              "Enter 0 to go back to main menu\n")

        choice = int(input("Your choice: "))

        if choice == 0:
            break

        first_string = input("Enter a string: ")

        if choice == 1:
            second_string = input("Enter second string: ")
            answer = first_string + second_string
            syntax = "answer = first_string + second_string"
        elif choice == 2:
            answer = len(first_string)
            syntax = "answer = len(first_string)"
        elif choice == 3:
            second_string = input("Enter the substring you want to count occurrence for:")
            answer = first_string.count(second_string, 0, len(first_string))
            syntax = "answer = first_string.count(second_string, 0, len(first_string))\n" \
                     "Alternatively you can also use\n" \
                     "answer = first_string.count(second_string)"
        else:
            break
        print("--------------------------")
        print(f"Your answer is: {answer}")
        print("--------------------------")
        print(f"The code syntax is:\n{syntax}")
        print("--------------------------\n")
        try_again = input("\nDo you want to try again? (Y/N): ")



#Main page
user_name = input("Please enter your name: ")
print(f"Hi \'{user_name}\'")
print("Welcome to the python cheatsheet! \n"
      "The purpose of this cheatsheet is to help you remember python syntax and code in you early learning phase.\n"
      "Happy coding...\n\n")

repeat_again = "Y"

while(repeat_again == "Y"):
    print("What would you like to try today?\n"
          "\t 1.Division \n"
          "\t 2.String Operation \n"
          "\t Enter 0 to exit")
    your_choice = int(input("Your choice: "))
    if your_choice == 1:
        division()
    elif your_choice == 2:
        strings()
    else:
        print("Exiting...")
        break

    repeat_again = input("\nWould you like to see menu again? (Y/N): ")

print(f"\nThank you for trying our python cheatsheet!\nBye {user_name}")