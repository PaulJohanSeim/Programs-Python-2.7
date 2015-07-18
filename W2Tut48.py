# Copyright Paul-Johan Seim

# Credit card calculation

balance = 5000.00
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0 #In %: 0.18/12 = 0.015
monthlyPaymentRate = 0.02

count=0
paycount=0

while count<12:
    balance = round(balance,2) #Rounding
    
    count+=1

    print('Month: ' +str(count))
    minMonthlyPayment = monthlyPaymentRate*balance #2%x5000.00
    minMonthlyPayment = round(minMonthlyPayment,2) #Rounding
    print ('Minimum Monthly Payment: ' +str(minMonthlyPayment))
    monthlyUnpaidBalance = balance - minMonthlyPayment #5000.00-100 = 4900

    updatedBalancePerMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance) #4900+1.5%*4900
    updatedBalancePerMonth = round(updatedBalancePerMonth,2) #Rounding
    print('Remaining balace: ' +str(updatedBalancePerMonth))
    
    balance = updatedBalancePerMonth
    paycount+=minMonthlyPayment

    balance = round(balance,2) #Rounding
    paycount = round(paycount, 2) #Rounding


print ('Total paid: ' +str(paycount))
print ('Remaining balance: ' +str(balance))
