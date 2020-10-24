import json


# blacklistHard:
# Same as the blacklistEasy condition, except
# we used a five-billion-word dictionary created using the
# algorithm outlined by Weir et al. [25]. For this condition, we
# trained Weir et al.’s algorithm on the MySpace, RockYou,
# and inflection lists. Both training and testing were conducted
# case-insensitively, increasing the strength of the blacklist.

# comprehensive8:
# “Password must have at
# least 8 characters including an uppercase and lowercase
# letter, a symbol, and a digit. It may not contain a dictionary
# word.” We performed the same dictionary check as in dictionary8.

# basic16:
# Participants were given the email scenario and
# the composition policy “Password must have at least 16
# characters.”

def create_eng_dict():
    word_dict = set()
    with open("/usr/share/dict/words", "r") as words:
        lines = words.readlines()
        for line in lines:
            word_dict.add(line.strip())
    return word_dict
    

def in_dict(word, word_dict):
    word = word.lower()
    for size in range(4, len(word) + 1):
        for j in range(0, len(word) - size + 1):
            sliced = word[j:j + size]
            if sliced in word_dict:
                print(sliced)
                return True
    return False
    

def is_valid_length(password, length):
    return len(password) >= length
    

def has_special_characters(password):
    letters = set(r"!@#$%^&*()_-+=[]{}|:<>,.?/")
    for char in password:
        if char in letters:
            return True
    return False


def has_lower_upper(password):
    return not (password == password.upper() or password == password.lower())

def has_digit(password):
    return sum([ch.isdigit() for ch in password]) > 0

def create_name_set(filename):
    names = set()
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:     
            names.add((line.split()[0]).lower())
    return names


def main():

    english_dict = create_eng_dict()
    password = input("Enter Password: ")

    # Create name set
    names = set()
    names = names.union(create_name_set("dist.all.last"))
    names = names.union(create_name_set("dist.female.first"))
    names = names.union(create_name_set("dist.male.first"))

    common_passwords = create_name_set("10-million-password-list-top-1000000.txt")
    
    # Check if there is an english word or name
    not_eng_word = not in_dict(password, english_dict)
    not_name = not in_dict(password, names)
    not_common_pass = password not in common_passwords

    # Check if there is a number
    has_number = has_digit(password)
    
    # Check if there is a special character in the password
    special_characters = has_special_characters(password)

    # Check the password length
    valid_length = is_valid_length(password, 8)

    # Check if the password has an upper and lower case
    has_diff_case = has_lower_upper(password)

    over16 = is_valid_length(password, 16)
    
    print(not_eng_word, not_name, special_characters, valid_length, has_diff_case, not_common_pass, over16)

    if (not_eng_word and not_name and special_characters and valid_length and has_diff_case and not_common_pass and has_number) or over16:
        print("strong")
    else:
        print("weak")
    
if __name__ == "__main__":
    main()