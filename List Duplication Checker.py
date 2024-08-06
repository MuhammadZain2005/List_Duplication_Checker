"""
LIST DUPLICATE CHECKER : Basic Program

Difficulty : 3/10

Comments : No comments , very easy
"""


def remove_duplicates(lst):
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


def get_user_input(data_type):
    while True:
        user_input = input(f"Add {data_type} to be checked if duplicated (comma separated) > ")
        try:
            if data_type == "numbers":
                user_input_list = list(map(int, user_input.split(',')))
            else:
                user_input_list = list(map(str.strip, user_input.split(',')))
            return user_input_list
        except ValueError:
            print(f"Invalid input. Please enter a valid list of {data_type}.")


def main():
    print("Welcome to the List Duplicate Checker!")
    data_type_choice = input("Do you want to check duplicates in (1) Numbers or (2) Strings? Enter 1 or 2: ")

    if data_type_choice == '1':
        data_type = "numbers"
    elif data_type_choice == '2':
        data_type = "strings"
    else:
        print("Invalid choice. Please restart the program and enter 1 or 2.")
        return

    user_input_list = get_user_input(data_type)
    result = remove_duplicates(user_input_list)

    sort_choice = input("Do you want to sort the result? (y/n): ").lower()
    if sort_choice == 'y':
        result.sort()

    print("The list without duplicates is:", result)


if __name__ == "__main__":
    main()
