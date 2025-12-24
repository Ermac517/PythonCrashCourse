def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet('willie', 'dog')
describe_pet(pet_name='whiskers', animal_type='cat')
describe_pet(pet_name='buddy', animal_type='dog')
describe_pet('max')  # Uses default animal_type 'dog'