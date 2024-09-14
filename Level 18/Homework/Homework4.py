def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


age = get_positive_integer("Enter your age: ")
driving_experience = get_positive_integer("Enter your years of driving experience: ")


if age < 18:
    
    eligibility = "You cant obtain a driver's license because you are under 18."

elif driving_experience < 1:

    eligibility = "You cant a driver's license because you need at least 1 year of driving experience."

else:
    eligibility = "You can obtain a driver's license."

print(eligibility)