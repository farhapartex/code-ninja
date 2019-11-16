def swap_case(str):
    new_str = ""
    for ch in str:
        if ch.isalpha():
            if ch.isupper():
                new_str += ch.lower()
            elif ch.islower():
                new_str += ch.upper()
        else:
            new_str += ch
    return new_str

if __name__ == "__main__":
    str = input()
    print(swap_case(str))