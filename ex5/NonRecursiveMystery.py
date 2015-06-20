__author__ = 'Aviad Levy'
def mystery_computation(number):
    '''a function that get a number and return
    the summarize of all the number who are the
    factors (divisors) of the number'''
    ONE = 1
    TWO = 2
    result = 0
    #loop goes over all the numbers (except the number itself)
    if number == TWO:
        return ONE
    for index in range(ONE,number - ONE):
        #if is divisor, summarize
        if number % index == 0:
            result += index
    return result
