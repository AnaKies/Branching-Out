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


def validate_user_age_input(age_of_user):
    """
    Validates user age input.
    Displays an error message if users' age is invalid.
    :return: Validated age of the user
    """
    while True:
        if not age_of_user.isdigit():
            print("Please enter a valid age.")
            continue
        break
    return age_of_user


def validate_user_email_input(email_of_user):
    """
    Validates user email input.
    Displays an error message if users' email is invalid.
    :return: Validated email of the user
    """
    while True:
        if "@" not in email_of_user or not email_of_user.endswith(".com"):
            print("Please enter a valid email.")
            continue
        break
    return email_of_user


def validate_user_name(name_of_user):
    """
    Validates username input.
    Displays an error message if the user's name is invalid.
    :param name_of_user: Raw name input
    :return: Validated name
    """
    while True:
        if not name_of_user.isalpha():
            print("Please enter a valid name.")
            continue
        break
    return name_of_user


if __name__ == "__main__":
    try:
        print("Enter quit to exit the program.")

        while True:
            filter_option = input("What would you like to filter by name, "
                                  "age or email?: ").strip().lower()

            if filter_option == "name":
                user_name = input("Enter a name to filter users: ").strip()
                valid_name = validate_user_name(user_name)
                filtered_users = filter_users_by_name(valid_name)
            elif filter_option == "age":
                user_age = input("Enter an age to filter users: ").strip()
                valid_age = validate_user_age_input(user_age)
                filtered_users = filter_users_by_age(int(valid_age))
            elif filter_option == "email":
                user_email = input("Enter an email to filter users: ").strip()
                valid_email = validate_user_email_input(user_email)
                filtered_users = filter_users_by_email(valid_email)
            elif filter_option == "quit":
                break
            else:
                print("Filtering by that option is not yet supported.")
                continue

            if not filtered_users:
                print("No users found.")
    except (ValueError, TypeError) as error:
        print(f"Unexpected error: {error}")
