def find_int(string):
    result = ""
    is_found = False
    for char in string:
        if char in '0123456789':
            result += char
            is_found = True
        elif is_found:
            return result

    return ''


print find_int("int x = 1234;")
