__author__ = 'Jay Edwards'
"""This program implements Luhn's algorithm to verify the validity of a credit card number"""


def check():
    even_nums = 0  # Number's in the even position.
    odd_nums = 0  # Number's in the odd position.
    odd_length = 0  # The amount of number's in the odd position
    credit_card = str(input("Insert your god damn credit card number(Between 8 to 19 digits):"))  # credit card number
    card_numbers = []  # individual numbers in the credit card number

    for n in credit_card:  # For each number in the credit card number
        if n.isdigit():
            card_numbers.append(int(n))  # Takes each number and add them to the list

    if 8 < len(card_numbers) < 19:  # checks if the amount of numbers meets the requirements
        for n in card_numbers:
            if (card_numbers.index(n)) % 2 != 0:
                odd_nums += (n * 2)
                odd_length += 1
            else:
                even_nums += n

        if odd_length == (len(card_numbers)/2) or ((len(card_numbers)/2)-1) or((len(card_numbers)/2)+1):
            sum_var = odd_nums + even_nums

            print("number equals " + str(sum_var))
            if sum_var % 10 != 0:
                print("Number is invalid")
            else:
                print("Number is valid. now leave maggot")
    else:
        print("Number is too long or short")

check()
