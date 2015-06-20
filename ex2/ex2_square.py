#!/usr/bin/env python3
def square_printing(n):
    
    squareLen="#"*(2*n+1)   #define the first and last line

    #set counters
    counter=1
    counter2=0
    eaZugy=1   #counter for the space between the "*"

    #define the second and the one before last line (only one *)
    line1="#"+" "*(n-counter)+"*"+" "*(n-counter)+"#"
    
    print(squareLen)   #print the first line (all #)
    
    while counter<=int(n*2-1):
        #print second and one before last
        if counter==1 or counter==(2*n-1):
            print(line1)
            counter+=1
            counter2+=1
        #print first half of meuyan
        elif counter<=n:
            print("#"+" "*(n-counter)+"*"+" "*(eaZugy)+"*"+" "*(n-counter)+"#")
            counter+=1
            counter2+=1
            eaZugy+=2
        #print second half of meuyan
        else:
            counter+=1
            counter2-=1
            eaZugy-=2
            print("#"+" "*(n-counter2)+"*"+" "*(eaZugy-2)+"*"+" "*(n-counter2)+"#")
            
    print(squareLen)  #print last line (all #)



#Here to help you test your code.
if __name__=="__main__":  #If we are the main script, and not imported
    from sys import argv
    try:
        n = int(argv[1])
    except:
        n = int(input("Please enter a positive integer: "))
    square_printing(n)
