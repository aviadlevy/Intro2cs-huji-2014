##########################################################################
# FILE: ex4.py
# WRITER: Aviad Levy
# EXERCISE : intro2cs ex4 2013-2014
# Description
#
#live_like_a_king - Find the maximal expenses you may expend
#during your lifetime
#bubble_sort_2nd_value - sort a list of tuples using bubble sort algorithm
#choosing_retirement_home - Find the most expensive retirement
#house one can afford.
#get_value_key - returns a function that calculates the new value of a house
#choose_retirement_home_opponents - Find the best retiremnt house
#that is affordable and fun
##########################################################################

#  Implement the following functions according the description in ex4

def live_like_a_king(salary, save, pre_retire_growth_rates,
                  post_retire_growth_rates, epsilon):
    """ Find the maximal expenses you may expend during your lifetime  

    A function that calculates what is the maximal annual expenses you may
    expend each year and not enter into debts
    You may Calculate it using binary search or using arithmetics
    Specify in your README in which method you've implemnted the function

    Args:  
    -salary: the amount of money you make each year-a non negative float.
    -save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    -pre_retire_growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -post_retire_growth_rates: a list of annual growth percentages
    on investments while you are retired. a list of floats larger
    than or equal to -100. In case of empty list return None
    - epsilon: an upper bound on the money must remain in the account
    on the last year of retirement. A float larger than 0

    Returns the maximal expenses value you found (such that the amount of
    money left in your account will be positive but smaller than epsilon)

    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""

    #check for proper values
    if salary < 0 or save < 0 or save > 100 or epsilon <= 0:
        return
    if len(post_retire_growth_rates) == 0:
        return
    if len(pre_retire_growth_rates) == 0 or \
       salary == 0 or save == 0:
        return 0
    #check for proper values inside pre_retire_growth_rates list
    growCounter = 0
    while growCounter < len(pre_retire_growth_rates):
        if float(pre_retire_growth_rates[growCounter]) < -100:
            return
        growCounter += 1
    #check for proper values inside post_retire_growth_rates list
    growCounter = 0
    while growCounter < len(post_retire_growth_rates):
        if float(post_retire_growth_rates[growCounter]) < -100:
            return
        growCounter += 1
        
    retireFund = salary*save*0.01   #the value of the 1st year
    varPension = [retireFund]       #enter the value to the list
    counter = 1
    #calculate the value of the rest years to the list
    while counter < len(pre_retire_growth_rates):
        varPension.append(retireFund*(1+(float(pre_retire_growth_rates[counter])
                                         *0.01))+salary*save*0.01)
        retireFund = varPension[counter]
        counter += 1
    
    savings = varPension[-1]  #savings equal to the last year pre retire
    #value that increase on the 1st year post retire:
    growthVal = 1+post_retire_growth_rates[0]*0.01
    #define high and low values for the binary search
    expensesHi = savings*growthVal
    expensesLo = 0
    if savings <= 0:
        return 0
    #binary search
    while expensesHi > expensesLo:
        expenses = (expensesHi + expensesLo) / 2
        retireList = []
        #the value of the 1st year:
        postRetire = savings*(1+post_retire_growth_rates[0]*0.01)-expenses
        retireList = [postRetire]  #enter the value to the list
        counter = 1
        #calculate the value of the rest years to the list
        while counter < len(post_retire_growth_rates):
            retireList.append(postRetire*(1+(float(
                post_retire_growth_rates[counter])*0.01))-expenses)
            postRetire = retireList[counter]
            counter += 1
        #checking for the binary search high value
        if retireList[-1] < 0:
            expensesHi = expenses
        #checking for the binary search low value
        elif retireList[-1] > epsilon:
            expensesLo = expenses
        #if no higher then ep and not lower then 0, we found it!
        else: return expenses
    


def bubble_sort_2nd_value(tuple_list):
    """sort a list of tuples using bubble sort algorithm

    Args:
    tuples_list - a list of tuples, where each tuple is composed of a string
    value and a float value - ('house_1',103.4)

    Return: a NEW list that is sorted by the 2nd value of the tuple,
    the numerical one. The sorting direction should be from the lowest to the
    largest. sort should be stable (if values are equal, use original order)

    You can assume that the input is correct."""

    from copy import deepcopy
    newList = deepcopy(tuple_list)
    #create a list with only the values of the numbers
    newListNum = []
    for index in range(len(tuple_list)):
        newListNum.append(tuple_list[index][1])
    #do the bubble sort
    index = 0
    while index < len(newListNum):
        index1 = 0
        while index1 < (len(newList)-index-1):
            if newListNum[index1] > newListNum[index1+1]:
                newList[index1+1],newList[index1] = \
                newList[index1],newList[index1+1]
                newListNum[index1+1],newListNum[index1] = \
                newListNum[index1],newListNum[index1+1]
            index1 += 1
        index += 1
    return newList


def choosing_retirement_home(savings,growth_rates,retirement_houses):
    """Find the most expensive retirement house one can afford.

    Find the most expensive, but affordable, retiremnt house.
    Implemnt the function using binary search

    Args:
    -savings: the initial amount of money in your savings account.
    -growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -retirement_houses: a list of tuples of retirement_houses, where
    the first value is a string - the name of the house and the
    second is the annual rent of it - nonnegative float.

    Return: a string - the name of the chosen retirement house
    Return None if can't afford any house.

    You need to test the legality of savings and growth_rates
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""

    #check for proper values
    growCounter = 0
    while growCounter < len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1
    growCounter = 0
    while growCounter < len(retirement_houses):
        if float(retirement_houses[growCounter][1]) < 0:
            return
        growCounter += 1
    if len(retirement_houses) == 0 or len(growth_rates) == 0:
        return
    #create sorted list of retirement houses
    sortRetireHome = bubble_sort_2nd_value(retirement_houses)
    #do the binary search
    expensesHi = len(sortRetireHome)
    expensesLo = 0
    houseName = ''
    while expensesHi >= expensesLo:
        expenses = int((expensesHi + expensesLo) / 2)
        houseName = sortRetireHome[expenses][0]
        retireList = []
        #the value of the 1st year:
        postRetire = savings*(1+growth_rates[0]*0.01)-retirement_houses[expenses][1]
        retireList = [postRetire]  #enter the value to the list
        counter = 1
        #check and enter the value of the rest years to the list
        while counter < len(growth_rates):
            retireList.append(postRetire*(1+(float(
                growth_rates[counter])*0.01))-retirement_houses[expenses][1])
            postRetire = retireList[counter]
            counter += 1
        #checking for the binary search high value
        if retireList[-1] < 0:
            if expensesHi == expenses:
                return
            expensesHi = expenses
        #checking for the binary search low value
        elif retireList[-1] > 0:
            if expensesLo == expenses:
                return houseName
            expensesLo = expenses
    
   

def get_value_key(value = 0):
    """returns a function that calculates the new value of a house


    #Args:
    -value: the value added per opponent - a float - the default value is 0

    This function returns a function that accepts triple containing
    (house ,anntual rent,number of opponents) and returns the new value of
    this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    #create a nested func that get a tuple
    def calc_new_house(houseTuple):
        #calculate the new value of the house
        house = houseTuple[1] + value * houseTuple[2]
        #the nested func returns the new house value
        return house
    #the func return the nested func
    return calc_new_house


def choose_retirement_home_opponents(budget,key,retirement_houses):
    """ Find the best retiremnt house that is affordable and fun

    A function that returns the best retiremnt house to live in such that:
    the house is affordable and
    his value (annual_rent+value*opponents) is the highest

    Args:
    -annual_budget: positive float. The amount of money you can
    expand per year.
    -key: a function of the type returned by get_value_key
    -retirement_houses: a list of houses (tuples), where  the first value
    is a string - the name of the house,
    the second is the annual rent on it - a non negative float, and the third
    is the number of battleship opponents the home hosts - non negative int
    
    Returns the name of the retirement home which provides the best value and
    which is affordable.

    You need to test the legality of annual_budget,
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""
    #check for prope value
    if budget < 0 or len(retirement_houses) == 0:
        return
    retirementSafe = -1
    nameOfTheHouse = False
    for index in range(len(retirement_houses)):
        #check key value for all retirement house
        keyValue = key(retirement_houses[index])
        #check if affordable
        if budget >= retirement_houses[index][1]:
            retirementValue = keyValue
            #check who's the highest
            if retirementValue > retirementSafe:
                retirementSafe = retirementValue
                nameOfTheHouse = retirement_houses[index][0]
    #check if name entered
    if nameOfTheHouse:
        return nameOfTheHouse
    #if no name entered (no house is affordable) return None
    else:
        return
