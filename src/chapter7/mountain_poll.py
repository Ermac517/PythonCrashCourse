responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could climb any mountain in the world, which would it be? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Mountain Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain}.")