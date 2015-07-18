# Copyright Paul-Johan Seim

# Problem Set 2.3 - Bisection approach

balance = 5000.00
annualInterestRate = 0.2 #In %
monthlyInterestRate = annualInterestRate/12.0 #In %: 0.2/12 = 0.016666

low = balance/12.0
high = (balance*(1+monthlyInterestRate)**12)/12.0
x = lowMonthlyPay = (high + low)/2.0
y=101
ans=0
while ans<15:
    ubs=0 
    y = (balance-x)+(balance-x)*(monthlyInterestRate)
    y=round(y,2)
    while ubs<11:
        y = (y-x)+(y-x)*(monthlyInterestRate)
        y=round(y,2)
        ubs+=1
    
    if y==0:
        break
    if y < 0:
        high = x
    elif y > 0:
        low = x
        
    x=(high+low)/2.0
    x = round(x,2)
    ans+=1
print ('Lowest Payment: ' +str(x))
