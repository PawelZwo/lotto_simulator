from random import randint, shuffle


def get_users_number():
    while True:
        try:
            user_picked_numbers = int(input("Pick a number from 1 to 49: "))
            break
        except ValueError:
            print("It's not a number! Pick a number.")
    return user_picked_numbers


def create_users_numbers_list():
    user_picked_numbers = []
    while len(user_picked_numbers) < 6:
        number = get_users_number()
        while number > 49:
            print("It has to be a number between 1 and 49! \n")
            number = get_users_number()
            break
        if number not in user_picked_numbers and 0 < number <= 49:
            user_picked_numbers.append(number)
    return sorted(user_picked_numbers)


def pc_secret_numbers():
    secret_numbers = list(range(1, 49))
    shuffle(secret_numbers)
    secret_numbers = secret_numbers[:6]
    return sorted(secret_numbers)


def lotto():
    print(
        "Hello, there! Let's try your luck in LOTTO. Pick six numbers and let's find out, if you won the grand prize!\n"
    )
    list_from_user = create_users_numbers_list()
    print("\nYou chose: " + ", ".join(str(number) for number in list_from_user) + ".")
    list_from_pc = pc_secret_numbers()
    print("I chose: " + ", ".join(str(number) for number in list_from_pc) + ".")
    hits = 0
    for number in list_from_user:
        if number in list_from_pc:
            hits += 1
    print(f"\nYou got {hits} {'number' if hits == 1 else 'numbers'} of them right!")


lotto()
