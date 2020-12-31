#Functions with inputs


def format_name(f_name, l_name):
    print(f"Your first name is {formated_f_name} and last name is {formated_l_name}")

formated_f_name = input("What is your first name? ").title()
formated_l_name = input("What is your last name? ").title()

format_name(f_name = formated_f_name , l_name = formated_l_name )

