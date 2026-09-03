student = input("Are you a student? Yes or No: ") == "Yes" or "yes"
age = int(input("How old are you?: "))
membership = input("Do you have a membership? Yes or No: ") == "Yes" or "yes"

if student == "Yes" or "yes" and membership == "Yes" or "yes":
    print("You are eligible for the discount.")
elif age >=60 and membership == "Yes" or "yes":
    print("You are eligible for the discount.")
else: print("You are not eligible for the discount.")
