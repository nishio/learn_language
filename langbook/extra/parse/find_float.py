def find_float(string):
    result = ''
    state = 0
    for char in string:
        print 'state=%r, char=%r, result=%r' % (state, char, result)
        if state == 0:
            if char in '0123456789':
                result += char
                state = 1
        elif state == 1:
            if char == '.':
                result += char
                state = 2
            elif char in '0123456789':
                result += char
            else:
                result = ''
                state = 0
        elif state == 2:
            if char in '0123456789':
                result += char
                state = 3
            else:
                result = ''
                state = 0
        elif state == 3:
            if char in '0123456789':
                result += char
            else:
                return result


print find_float("a0b12.c34.56d")
