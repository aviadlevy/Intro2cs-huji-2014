#############################################################
# FILE: ex3.py
# WRITER: Aviad Levy
# EXERCISE : intro2cs ex3 2013-2014
# Description
#############################################################



#  Implement the following function according the description in ex3




def constant_pension(salary, save, growth_rate, years):
    
    if salary<0 or (save<0 and save>100) or growth_rate<-100 or years<0:
        return
    else:
        retireFund = salary*save*0.01
        consPension = [retireFund]
        counter = 1
        while counter<years:
            consPension.append(retireFund*(1+growth_rate*0.01)+salary*save*0.01)
            retireFund = consPension[counter]
            counter += 1
        return consPension
##    """ calculate retirement fund assuming constant pesnion
##
##    A function that calculates the value of a retirement fund in each year
##    based on the worker salary, savings, working years and assuming constant
##    growthRate of the fund
##
##    Args:
##    - salary: the amount of money you earn each year,
##           a non negative float.
##    - save: the percent of your salary to save in the investment account
##            each working year -  a non negative float between 0 and 100
##    - growth_rate: the annual percent increase/decrease in your investment
##           account, a float larger than or equal to -100 (minus 100)
##    - years: number of years to work - non negative int
##
##    return: a list whose values are the size of your retirement account at
##      the end of each year.
##
##    In case of bad input: values are out of range
##    returns None
##
##    You can assume that the types of the input arguments are correct. """
##




def variable_pension(salary, save, growth_rates):

    if salary<0 or (save<0 and save>100):
        return
    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1

    retireFund = salary*save*0.01
    varPension = [retireFund]
    counter = 1
    while counter<len(growth_rates):
        varPension.append(retireFund*(1+(float(growth_rates[counter])*0.01))
                          +salary*save*0.01)
        retireFund = varPension[counter]
        counter += 1
    return varPension
    
##    """ calculate retirement fund assuming variable_pension
##
##    A function that calculates the value of a retirement fund in each year
##    based on the worker salary, savings,  and a list of growthRates values.
##    Number of working years is as the length of growthRats
##
##    Args:
##    - salary: the amount of money you earn each year, a non negative float.
##    - save: the percent of your salary to save in the investment account
##    each working year -  a non negative float between 0 and 100
##    - growth_rates: a list of annual growth percentages in your investment
##    account - a list of floats larger than or equal to -100. The length of 
##    the list defines the number of years you plan to work.
##
##    return: a list whose values are the size of your retirement account at
##    the end of each year.
##
##    In case of bad input: values are out of range
##    returns None
##
##    You can assume that the types of the input arguments are correct. """
    



def choose_best_fund(salary,save,funds_file):

    if salary<0 or (save<0 and save>100):
        return
    f = open(funds_file, 'r')
    lines = f.readlines()
    f.close()
    lineNum = 0
    
    fundNameList = []
    bigFundIndex = -1
    fundValueSafe = [0]
    while lineNum < len(lines):
        newGrowthList = []    
        counterName = 1
        fundName = ''
        while counterName < len(lines[lineNum]):
            if lines[lineNum][counterName] == ',':
                break
            fundName += str(lines[lineNum][counterName])
            counterName += 1
        fundNameList.append(fundName)
        counterName += 1
        newGrowthList = ((lines[lineNum].partition(','))[2])
        newGrowthList = newGrowthList[:-1]
        newGrowthList = newGrowthList.split(',')
        fundValue = variable_pension(salary, save, newGrowthList)
        newVal = float(fundValue[-1])
        oldVal = float(fundValueSafe[-1])
        if newVal > oldVal:
            bigFundIndex = lineNum
            fundValueSafe = list(fundValue)
        lineNum +=1
    bigFund = (fundNameList[bigFundIndex], fundValueSafe[-1])
    return bigFund
##    """find the best fund to invest in
##
##    A function that calculates the best fund to invest money in from a list
##    of funds in a file.
##
##    Args:
##    - salary: the amount of money you earn each year, a non negative float.
##    - save: the percent of your salary to save in the investment account
##    each working year -  a non negative float between 0 and 100
##    - funds_file: A string -a path to a file that lists the different funds
##    that you may choose to invest in
##    format of the file:
##    #nameOfFund0,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##    #nameOfFund1,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##    #nameOfFund2,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##
##
##    return: a tuple, where its first value is the name of the best fund to
##    invest in assuming such an annual deposition, and the seocnd value in the
##    tuple is the value of the pension fund in its end assuming we choose the
##    best fund.
##
##    In case of bad input: values are out of range
##    returns None
##
##    Note that for this specific exercise you may assume a correct form
##    of the file. If an error accourd (File not exist, wrong type inside
##    the file - Let python print its error and exit (Will happen
##    automatically)
##
##    You may also assume that the lists of growthRates have the same length
##    and that the types of the inputs arguments are correct. """
    


def growth_in_year(growth_rates,year):

    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1
    if growCounter < year+1:
        return
    return float(growth_rates[year])
##    """return the growth value in a given year
##
##    Args:
##    - growth_rates: a list of annual growth percentages in your investment
##    account - a list of floats larger than or equal to -100.
##    -year: the index in the list we are intersted in
##    a int between 0 and the size of growthRates
##
##    return: a float with the value of growthRates in the specified year or
##    None in case of a year not in the list
##
##    You can assume that the types of the input arguments are correct."""
    

    

  


def inflation_growth_rates(growth_rates,inflation_factors):
    
    newGrowthRates = []
    for index in range(len(growth_rates)):
        if inflation_factors[index] == 0:
            newGrwothRates.append(growth_rates[index])
        else:
            newGrowthRates.append(100*((100+growth_rates[index])/ \
                                      (100+inflation_factors[index])-1))
    return newGrowthRates

##    """ Calculate the adjusted growth list given inflation
##
##
##    A function that return a new list with a adjusted growth rates due to
##    the inflation. inflation should be adjusted for all years there is both
##    inflation factor and growth factor.
##    inflation is defined as 100*((100+g)/(100+i)-1)
##    where g is growth in that year and i is the inflation.
##
##    Args:
##    - growth_rates: a list of annual growth percentages in your investment
##    account - a list of floats larger than or equal to -100. 
##    -inflation_factors: the annual inflation in percents.
##    a list of floats larger than (BUT NOT EQUAL) to -100 .
##    The list may have different size from growth_rates.
##
##    returns a NEW list with the same length as growth_rates but during the
##    inflation years the rates are adjusted.
##    In case of bad input: values are out of range returns None
##
##    You can assume that the types of the input arguments are correct."""
##    



#def post_retirement(savings, growth_rates, expenses):
##    """ calculates the account status after retirement
##
##    A function that calculates the account status after retirement, assuming
##    constant expenses and no income
##    Args:
##    -savings: the initial amount of money in your savings account.
##    A float larger than 0
##    - growth_rates: a list of annual growth percentages in your investment
##    account - a list of floats larger than or equal to -100.
##    -expenses: the amount of money you plan to spend each year during
##    retirement. A non negative float
##
##    return: a list of your retirement account value at the end of each year.
##
##    Note in case of a negative balance - the growth rate will change into
##    rate on the debt
##    In case of bad input: values are out of range returns None
##
##    You can assume that the types of the input arguments are correct."""
##    
##
