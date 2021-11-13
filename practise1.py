# programme will tell your age.
print("_________________________________________________________________________")
try:
    user_age_year = int(input("Please provide your Current Age or Year of Birth: \n"))
    user_age_future = int(input("In which year's age you want to know: \n"))
    current_year = 2021
except Exception as e:
    print(" Your Error is ", e)
# writing conditions:
else:
    if user_age_future >= 2022:
        if user_age_year <= 120:
            print(f"So your age will be {user_age_year + (user_age_future - current_year)} on {user_age_future}")
        elif (user_age_year > 120) and (user_age_year < 1900):
            print(f"You are too old Sir. Don't fool me I am smarter than you.")
        elif (user_age_year >= 1900) and (user_age_year < 2022):
            print(f"So your age will be {user_age_future - user_age_year} on {user_age_future}")
        elif user_age_year >= 2022:
            print("You not yet born bro how can you access your mobile from ..... ")
    elif user_age_future <= 2021:
        print("Please provide future year after 2021")
    else:
        print("Some thing Went Wrong")
finally:
    print("_________________________________________________________________________")
    exit()
