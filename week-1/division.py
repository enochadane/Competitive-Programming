def division(dividend, divisor):
    dividend = str(dividend)
    subDividend = ''
    quotient = ''
    remainder = 0
    i = 0
    while(i < len(dividend)):
        subDividend += dividend[i]
        if(subDividend == '0' and int(subDividend) % divisor == 0):
            quotient += '0'
            i += 1
        if(int(subDividend) >= divisor):
            subQuotient = str(int(subDividend) // divisor)
            if(int(subDividend) % divisor != 0):
                remainder = int(subDividend) % divisor
            quotient += subQuotient
            dividend = str(remainder) + dividend[i+1:]
            subDividend = ''
            i = 0
        else:
            i += 1
    print(quotient)
    return quotient


division(700, 5)

