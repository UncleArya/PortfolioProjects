from morse_code import MORSE

# Constants
IS_RUNNING = True


def convert_user_string():
    """
    While True, prompts the user to enter a string to be converted into Morse Code.
    """

    user_input = input("Enter the text to be converted: ")

    clean_user_input = user_input.lower()  # convert to lower case for dictionary lookup

    if check_user_string(clean_user_input):
        print(f"'{user_input}' in Morse Code is:")
        for char in clean_user_input:
            if char == " ":
                print(" ")
            else:
                print(MORSE[char])

    # ask user if they want to convert another string
    convert_another()


def check_user_string(user_string):
    """Checks if any characters in the user provided string contain invalid characters that cannot be converted.

    Args:
        user_string (str) -> str

    Returns:
        bool: returns True or False
    """
    user_string_without_spaces = user_string.replace(" ", "")  # remove spaces from the character check

    if user_string_without_spaces.isalnum():
        return True
    else:
        print("Characters must be alphanumeric only")
        return False


def convert_another():
    """
    Requests input from user. If anything other than "N" is entered, the program continues.
    """
    global IS_RUNNING
    user_answer = input("Convert another string to Morse Code? (Y/N) ").lower()
    if user_answer == "n":
        print("Goodbye.")
        IS_RUNNING = False
    elif user_answer != "y" and user_answer != "n":
        print("Enter a 'Y' to convert another string or an 'N' to quit")
        convert_another()


# Program execution
print("Welcome to Arya's Morse Code Converter!")

while IS_RUNNING:
    convert_user_string()
