############################################################################
# FILE: ex3.py
# WRITER: Aviad Levy
# EXERCISE : intro2cs ex3 2013-2014
#
# Description:
#
# constant_pension: calculate retirement fund assuming constant pesnion
# variable_pension: calculate retirement fund assuming variable pension
# choose_best_fund: find the best fund to invest in
# growth_in_year: return the growth value in a given year
# inflation_growth_rates: calculate the adjusted growth list given inflation
# post_retirement: calculates the account status after retirement
############################################################################



def constant_pension(salary, save, growth_rate, years):

    #check for proper values
    if salary<0 or save<0 or save>100 or growth_rate<-100 or years<0:
        return
    #if no year entered return empty list
    elif years == 0:
        consPension = []
        return consPension
    
    else:
        retireFund = salary*save*0.01   #the value for the 1st year
        consPension = [retireFund]      #enter the value to the list

        counter = 1
        #check and enter the value of the rest years to the list
        while counter<years:
            consPension.append(retireFund*(1+growth_rate*0.01)+salary*save*0.01)
            retireFund = consPension[counter]
            counter += 1
        return consPension




def variable_pension(salary, save, growth_rates):

    #check for proper values
    if salary<0 or save<0 or save>100:
        return
    #if no year entered (growth_rates is empty) return empty list
    if len(growth_rates) == 0:
        retireList = []
        return retireList    
    #check for proper values inside growth_rates list
    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1

    retireFund = salary*save*0.01   #the value of the 1st year
    varPension = [retireFund]       #enter the value to the list

    counter = 1
    #check and enter the value of the rest years to the list
    while counter<len(growth_rates):
        varPension.append(retireFund*(1+(float(growth_rates[counter])*0.01))
                          +salary*save*0.01)
        retireFund = varPension[counter]
        counter += 1
    return varPension
    



def choose_best_fund(salary,save,funds_file):

    #check for proper values
    if salary<0 or save<0 or save>100:
        return

    #open the file and read the lines
    f = open(funds_file, 'r')
    lines = f.readlines()
    f.close()

    lineNum = 0
    fundNameList = []
    bigFundIndex = -1       #remeber the line of the biggest fund
    fundValueSafe = [0]     #save the biggest fund line
    while lineNum < len(lines):   #loop over all lines in file
        newGrowthList = []  #list the gets the line and "convert" it to list
        counterName = 1     #lines[lineNum][0] is '#' so we start at 1
        fundName = ''       #string that will "read" the fund name

        while counterName < len(lines[lineNum]): #loop over one line at a time

            #stop when we "meet" the 1st ','
            if lines[lineNum][counterName] == ',':
                break
            #fundName gets the fund name
            fundName += str(lines[lineNum][counterName])
            counterName += 1
        
        fundNameList.append(fundName)  #enter the name to a list of names
        counterName += 1

        #get the rest of the list:
        #i used partition[2] to get the second half of the line after the ','
        newGrowthList = ((lines[lineNum].partition(','))[2])
        newGrowthList = newGrowthList[:-1]    #delete '\n' from the end of line
        newGrowthList = newGrowthList.split(',')  #remove all ','

        #send the newGrowthList with salary and save provided
        #to variable_pension
        fundValue = variable_pension(salary, save, newGrowthList)
        
        newVal = float(fundValue[-1])   #last year value of the fund we checked
        oldVal = float(fundValueSafe[-1]) #last year value of the biggest fund
        if newVal > oldVal:            #check if new is bigger
            bigFundIndex = lineNum     #remember biggest line
            fundValueSafe = list(fundValue)  #keep the new biggest fund list
        lineNum +=1
    #creat tuple of the name and last year value of the biggest we kept
    bigFund = (fundNameList[bigFundIndex], fundValueSafe[-1])
    return bigFund
    


def growth_in_year(growth_rates,year):
    #check for proper value
    if year<0:
        return
    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1
    #check if year is on list
    if growCounter < year+1:
        return
    #return the growth rates in the spesific year
    return float(growth_rates[year])

  


def inflation_growth_rates(growth_rates,inflation_factors):

    newGrowthRates = []
    #check if we got any infilation factors.
    #if not return growth rates as it is
    if len(inflation_factors) == 0:
        return growth_rates

    #check for proper values
    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1
        
    growCounter = 0
    while growCounter<len(inflation_factors):
        if float(inflation_factors[growCounter]) <= -100:
            return
        growCounter += 1

    #loop that run over the infilation factors and add the new value
    #to the new list.
    for index in range(len(inflation_factors)):
        #if infilation factors list is bigger than the growth rates list,
        #return the new list when we calculate every value in growth list.
        if index == len(growth_rates):
            return newGrowthRates
        newGrowthRates.append(float(100*((100+growth_rates[index])/ \
                                  (100+inflation_factors[index])-1)))
    
    index += 1
    #run over the rest values of growth rates & add them without change
    for index1 in range(index,len(growth_rates)):
        newGrowthRates.append(float(growth_rates[index1]))
    return newGrowthRates




def post_retirement(savings, growth_rates, expenses):

    #check for proper values
    if savings<=0 or expenses<0:
        return
    growCounter = 0
    while growCounter<len(growth_rates):
        if float(growth_rates[growCounter]) < -100:
            return
        growCounter += 1

    #if no year entered (growth_rates is empty) return empty list
    if len(growth_rates) == 0:
        retireList = []
        return retireList
    
    retireList = []
    #the value of the 1st year:
    postRetire = savings*(1+growth_rates[0]*0.01)-expenses
    retireList = [postRetire]  #enter the value to the list

    counter = 1
    #check and enter the value of the rest years to the list
    while counter<len(growth_rates):
        retireList.append(postRetire*(1+(float(growth_rates[counter])*0.01))
                          -expenses)
        postRetire = retireList[counter]
        counter += 1
    return retireList
