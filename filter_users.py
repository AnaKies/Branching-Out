import json


def filter_users_by_name(name):
    """
    Filters users bei their names.
    :param name: Name of the user
    :return: List of filtered users with the same name
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_by_name = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users_by_name:
        print(user)
    return filtered_users_by_name


def filter_users_by_age(age):
    """
    Filters users bei their names.
    :param age: Age of the user
    :return: List of filtered users with the same age
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_by_age = [user for user in users if user["age"] == age]

    for user in filtered_users_by_age:
        print(user)
    return filtered_users_by_age


def filter_users_by_email(email):
    """
    Filters users bei their names.
    :param email: Email of the user
    :return: List of filtered users with the same email
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_by_email = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users_by_email:
        print(user)
    return filtered_users_by_email


def handle_name():
    """
    Gets user input for the name, validates it and filters the user's name.
    :return: List of filtered users with the same name
    """
    while True:
        user_name = input("Enter a name to filter users: ").strip()

        if user_name.lower() == "quit":
            return user_name

        if not user_name.isalpha():
            print("Please enter a valid name.")
            continue
        break
    return filter_users_by_name(user_name)


def handle_age():
    """
    Gets user input for the age, validates it and filters the user's age.
    :return: List of filtered users with the same age
    """
    while True:
        user_age = input("Enter an age to filter users: ").strip()

        if user_age.lower() == "quit":
            return user_age

        if not user_age.isdigit():
            print("Please enter a valid age.")
            continue
        break
    return filter_users_by_age(int(user_age))


def handle_email():
    """
    Gets user input for the email, validates it and filters the user's email.
    :return: List of filtered users with the same email
    """
    while True:
        user_email = input("Enter an email to filter users: ").strip()

        if user_email.lower() == "quit":
            return user_email

        if "@" not in user_email or not user_email.endswith(".com"):
            print("Please enter a valid email with @ and '.com' ending.")
            continue
        # split at the first @
        name, domain = user_email.split("@", 1)

        if not name:
            print("Please enter a valid email with name part.")
            continue

        if "." not in domain:
            print("Please enter a valid email with dot in domain part.")
            continue

        domain_name = domain.split(".")[0]
        if not domain_name:
            print("Please enter a valid email with domain name.")
            continue
        break

    return filter_users_by_email(user_email)


if __name__ == "__main__":
    try:
        print("Enter quit to exit the program.")

        commands = {
            "name": handle_name,
            "age": handle_age,
            "email": handle_email
        }
        while True:
            filter_option = input("What would you like to filter by name, "
                                  "age or email?: ").strip().lower()

            if filter_option.lower() == "quit":
                break

            action = commands.get(filter_option)

            if not action:
                print("Filtering by that option is not yet supported.")
                continue

            filtered_users = action()
            if filtered_users == "quit":
                break

            if not filtered_users:
                print("No users found.")
    except (ValueError, TypeError) as error:
        print(f"Unexpected error: {error}")
