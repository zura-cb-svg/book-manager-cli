def get_valid_year():
    while True:
        try:
            year = int(input("Year: "))
            return year
        except ValueError:
            print("Please enter a valid number!")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() != "":
            return value
        print("This field cannot be empty!")