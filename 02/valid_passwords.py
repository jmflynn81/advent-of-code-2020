from collections import Counter


def get_passwords():
    with open('passwords') as f:
        passwords = f.read().splitlines()
    return passwords


def split_password(password_string):
    policy, password = password_string.split(':')
    nums, letter = policy.split()
    low, high = nums.split('-')
    return {
        "low" : int(low), 
        "high": int(high),
        "letter": letter,
        "password": password.strip()
    }


def check_for_letters(password):
    if password['letter'] in password['password']:
        all_items = dict(Counter(password['password']))
        if all_items[password['letter']] >= password['low'] and all_items[password['letter']] <= password['high']:
            return True        
    return False


def check_letter_position(password):
    if password['letter'] in password['password']:
        high = False
        low = False
        if password['password'][password['low']-1] == password['letter']:
            low = True
        if password['password'][password['high']-1] == password['letter']:
            high = True
        if high and low:
            return False
        elif high or low:
            return True            
    return False


password_strings = get_passwords()
formatted_passwords = [
    split_password(password_string)
    for password_string in password_strings
]

good = 0
bad = 0
for password in formatted_passwords:
    if check_letter_position(password):
        print(f"Good password: {password['password']}, Letter: {password['letter']}, Low: {password['low']}, High: {password['high']}")
        good += 1
    else:
        print(f"Bad password: {password['password']}, Letter: {password['letter']}, Low: {password['low']}, High: {password['high']}")
        bad += 1

print(f"Good: {good}")
print(f"Bad: {bad}")

