# Define the function for calculating the total price for a green package.
def green_package(base_price, additional_price, data):
    total_price = round(base_price + additional_price*(data - 2), 2)
    return total_price


# Define the function for calculating the total price for a blue package.
def blue_package(base_price, additional_price, data):
    total_price = round(base_price + additional_price*(data - 4), 2)
    return total_price


# Define the function for calculating the total price for a purple package.
def purple_package(base_price, additional_price, data):
    total_price = round(base_price + additional_price*(data - 0), 2)
    return total_price


# Define the function for inputting a valid package name.
def input_valid_name():
    package_name = input("Which plan would you like? (green, blue, purple)").strip().lower()
    while package_name != "green" and package_name != "blue" and package_name != "purple":
        print("Sorry, that is not a valid package name.")
        package_name = input("Please enter a valid package name:").lower().strip()
    return package_name


# Define the function for inputting a valid number of GBs used.
def input_valid_data():
    data = float(input("Enter GBs used this month:"))
    while data < 0:
        print("Sorry, that is not a valid number for GBs.")
        data = float(input("Please enter a valid number of GBs used this month."))
    return data


# Define the main function based on the user's inputs.
def main():
    print("This program determines how much a customer owes their mobile phone provider based on their subscription.")
    package_name = input_valid_name()
    data = input_valid_data()
    if package_name == "green":
        base_price = 49.99
        additional_price = 15
        total_price = green_package(base_price, additional_price, data)
        coupon = input("Do you have a coupon?(yes/no)").strip().lower()
        if package_name == "green" and coupon == "yes" and total_price > 75:
            total_price = 75
            print("The total price of your monthly bill is:", total_price)
        if package_name == "green" and coupon == "no":
            total_price = green_package(base_price, additional_price, data)
            print("The total price of your monthly bill is:", total_price)
    elif package_name == "blue":
        base_price = 70
        additional_price = 10
        if data - 4 < 0:
            data = 4
        total_price = blue_package(base_price, additional_price, data)
        print("The total price of your monthly bill is:", total_price)
    elif package_name == "purple":
        base_price = 99.95
        additional_price = 0
        total_price = purple_package(base_price, additional_price, data)
        print("The total price of you monthly bill is:", total_price)
    else:
        print("Sorry, you entered an invalid package.")


# Call the main function.
main()
