# user will provide a number and a range of number you have to check if the number is divisor of any number of the range
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
try:
    no_student = int(input("How many Student you have: \n"))
    min_no_apple = int(input("Minimum No of apple you can provide: \n"))
    max_no_apple = int(input("Maximum No of apple you can provide: \n"))
except Exception as e:
    print(e)
else:
    if min_no_apple < max_no_apple:
        for apple_count in range(min_no_apple, (max_no_apple + 1)):
            if apple_count < no_student:
                print(f"{apple_count} is Less Number of apple you provided. Can't donate Everyone equally")
            else:
                if apple_count % no_student == 0:
                    print(
                        f"Every Student Can get Equally if No of Apple is {apple_count} and both "
                        f"will get {apple_count / no_student} apples")
                else:
                    print(f"If you Provide {apple_count} no of apple i can't divide equally.")
    elif min_no_apple >= max_no_apple:
        print("You set minimum range greater than or equal to maximum range. ")
    else:
        print("Some thing Went Wrong.")

finally:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
