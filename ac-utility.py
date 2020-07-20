def is_factor(a, b):
    ''' 
        Check if a is a factor of b
        '''
    if b % a == 0:
        return True

    else:
        return False


def get_celsius(f):
    '''
        Converts fahrenheit temperature to celsius.
        '''
    return((f - 32) * (5 / 9))


def get_fahrenheit(c):
    '''
        Converts celsius to fahrenheit.
        '''
    return(c * (9 / 5) + 32)