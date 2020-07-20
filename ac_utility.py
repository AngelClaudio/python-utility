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


def get_roots(a, b, c):
    '''
    Quadratic equation root calculator
    '''
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    
    return({'x1' : x_1, 'x2' : x_2})
