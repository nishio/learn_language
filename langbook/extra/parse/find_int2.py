def find_int(string):
    result = ""
    is_found = False
    for char in string:
        print 'char=%r, result=%r, is_found=%r' % (char, result, is_found)
        if char in '0123456789':
            result += char
            is_found = True
        elif is_found:
            return result

    return ''


print find_int("ab12cd")
