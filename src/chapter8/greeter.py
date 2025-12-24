def greet_user(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = greet_user(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    repeat = input("Would you like to enter another name? (yes/no) ")
    if repeat.lower() == 'no':
        break
