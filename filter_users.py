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


if __name__ == "__main__":
    try:
        print("Enter quit to exit the program.")
        while True:
            filter_option = input(
                "What would you like to filter by name, age or email?: "
            ).strip().lower()

            if filter_option == "name":
                name_to_search = input("Enter a name to filter users: ").strip()
                filtered_users = filter_users_by_name(name_to_search)
            elif filter_option == "age":
                while True:
                    user_age = input("Enter an age to filter users: ").strip()
                    d = type(user_age)
                    if not user_age.isdigit():
                        print("Please enter a valid age.")
                        continue
                    break
                filtered_users = filter_users_by_age(int(user_age))

            elif filter_option == "email":
                while True:
                    user_email = input("Enter an email to filter users: ").strip()
                    if "@" not in user_email or not user_email.endswith(".com"):
                        print("Please enter a valid email.")
                        continue
                    break
                filtered_users = filter_users_by_email(user_email)
            elif filter_option == "quit":
                break
            else:
                print("Filtering by that option is not yet supported.")
                continue

            if not filtered_users:
                print("No users found.")
    except (ValueError, TypeError) as error:
        print(f"Unexpected error: {error}")
