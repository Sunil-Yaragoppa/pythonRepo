def swap_case(s):
    modified_string = ""
    for letter in s:
        if letter.islower():
            modified_string += letter.upper()
        elif letter.isupper():
            modified_string += letter.lower()
        else:
            modified_string += letter

    return modified_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)