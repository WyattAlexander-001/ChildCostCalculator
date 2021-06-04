"""
Can you afford to have a child?
https://www.usda.gov/media/blog/2017/01/13/cost-raising-child

$284,570 from age 0-18 CURRENTLY, There's always inflation

https://www.kiplinger.com/taxes/602431/child-tax-credit-2021-who-gets-3600-will-i-get-monthly-payments-and-other-faqs#:~:text=2020%20Child%20Tax%20Credit&text=Answer%3A%20For%202020%20tax%20returns,six%20months%20during%20the%20year.
You get $2000 per child

https://poverty.ucdavis.edu/faq/what-are-annual-earnings-full-time-minimum-wage-worker#:~:text=The%20annual%20earnings%20for%20a%20full%2Dtime%20minimum%2Dwage%20worker,is%2040%20hours%20each%20week.
Net Annual Income for a minimum wage worker: $15,080

"""

print("Thinking of having a child? Lets do some math!")
netAnnualIncome = float(input("Enter your YEARLY NET INCOME:\n$"))
children = int(input("Enter how many children you want:\n"))

#--------------------------------------------------------------------------#

#USER INCOME
netMonthlyIncome = netAnnualIncome/12
netWeeklyIncome = netAnnualIncome/52.143
netDailyIncome = netAnnualIncome/365
netIncomeYouWouldHaveOverEighteenYearsNoInflation = netAnnualIncome *18

#USER INCOME WITH INFLATION #1.36 is from 2% inflation eg: 2/100 = 0.02 * years to get 0.36, then add 1 to get 1.36
netMonthlyIncomeWithInflation = netAnnualIncome/12 *1.36
netWeeklyIncomeWithInflation  = netAnnualIncome/52.143 * 1.36
netDailyIncomeWithInflation  = netAnnualIncome/365 * 1.36
netIncomeYouWouldHaveOverEighteenYearsWithInflation = netAnnualIncome *18 * 1.36

#TAX CREDIT
childTaxCreditPerChild = children * 2000
childTaxCreditPerChildToAgeSeventeen = children * childTaxCreditPerChild  * 17 
childTaxCreditPerChildToAgeSeventeenWithInflation = children * childTaxCreditPerChild  * 17 *1.36

#COST OF CHILD The totalCostForChild number was from 2015
totalCostForChild = children * 284570
totalCostForChildWithInflation = children * totalCostForChild * 1.36

#COST OF CHILD  NO INFLATION
yearlyCostForChild = children * (totalCostForChild/18)
monthlyCostForChild = children * (totalCostForChild/216)
weeklyCostForChild = children * (totalCostForChild/938.57)
dailyCostForChild = children * (totalCostForChild/6570)

#COST OF CHILD  INFLATION
yearlyCostForChildWithInflation = children * (totalCostForChildWithInflation/18)
monthlyCostForChildWithInflation = children * (totalCostForChildWithInflation/216)
weeklyCostForChildWithInflation = children *  (totalCostForChildWithInflation/938.57)
dailyCostForChildWithInflation = children * (totalCostForChildWithInflation/6570)

#NO INFLATION WITH TAX CREDIT
totalIncomeNoInflation = netIncomeYouWouldHaveOverEighteenYearsNoInflation + childTaxCreditPerChildToAgeSeventeen
totalIncomeWithInflation = netIncomeYouWouldHaveOverEighteenYearsWithInflation + childTaxCreditPerChildToAgeSeventeenWithInflation

#--------------------------------------------------------------------------#
print('\n----------------------------\n')
print(f'The TOTAL cost to raise {children} children from age 0 to 18 is: ${totalCostForChild}')
print(f'The TOTAL cost to raise {children} from age 0 to 18 accounting for inflation is: ${totalCostForChildWithInflation}')
print()
print(f'Without accounting for inflation ')
print(f'That would be a YEARLY cost of: ${yearlyCostForChild}')
print(f'That would be a MONTHLY cost of: ${monthlyCostForChild}')
print(f'That would be a WEEKLY cost of: ${weeklyCostForChild}')
print(f'That would be a DAILY cost of: ${dailyCostForChild}')
print()
print(f'With accounting for inflation ')
print(f'That would be a YEARLY cost of: ${yearlyCostForChildWithInflation}')
print(f'That would be a MONTHLY cost of: ${monthlyCostForChildWithInflation}')
print(f'That would be a WEEKLY cost of: ${weeklyCostForChildWithInflation}')
print(f'That would be a DAILY cost of: ${dailyCostForChildWithInflation}')

print('\n----------------------------\n')

print(f'With your net income of: ${netAnnualIncome}')
print(f'Over 18 years WITHOUT accounting for a inflation/raises your income would be: ${netIncomeYouWouldHaveOverEighteenYearsNoInflation}')
print(f'Over 18 years ACCOUNTING for a minimum 2% raise your income would be: ${netIncomeYouWouldHaveOverEighteenYearsWithInflation}')
print()
print('Your Income Without Inflation:')
print(f'Your MONTHLY income is: ${netMonthlyIncome}')
print(f'Your WEEKLY income is: ${netWeeklyIncome}')
print(f'Your Daily income is: ${netDailyIncome}')
print()
print('Your Income With Inflation:')
print(f'Your MONTHLY income is: ${netMonthlyIncomeWithInflation}')
print(f'Your WEEKLY income is: ${netWeeklyIncomeWithInflation}')
print(f'Your Daily income is: ${netDailyIncomeWithInflation}')
print()
print("The government gives an annual TAX CREDIT for each child UNDER age 18: ")
print(f'Your tax credit: ${childTaxCreditPerChild}')
print(f'Your tax credit value over 17 years: ${childTaxCreditPerChildToAgeSeventeen}')
print(f'Your tax credit value over 17 years with 2% yearly inflation: ${childTaxCreditPerChildToAgeSeventeenWithInflation}')
print()
print("WITHOUT INFLATION:")
print(f'Your TOTAL INCOME: ${totalIncomeNoInflation}')
print("WITH INFLATION:")
print(f'Your TOTAL INCOME: ${totalIncomeWithInflation}')


print('\n----------------------------\n')

print(f'SHOULD YOU HAVE {children} CHILDREN?\nWell, as of right now:')

if totalIncomeNoInflation > (2.0 * totalCostForChild) :
    print(f"You can EASILY afford {children} children ")
elif totalIncomeNoInflation > (1.5 * totalCostForChild):
    print(f"You can with SOME DIFFICULTY you can afford {children} children")
elif totalIncomeNoInflation >= (1.0 * totalCostForChild):
    print(f"You can BARELY afford {children} children")
elif totalIncomeNoInflation < (1.0 * totalCostForChild):
    print(f"You should NOT have {children} children, at your income level")
else:
    print("Error")

#--------------------------------------------------------------------------#




