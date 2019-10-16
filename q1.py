# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
#Mortgage repayments using python
n=1
initialLevelOfdebt= int(input("What is your initial level of debt: "))
interestPercentage= int(input("What is your interest percentage: "))
repaymentPercentage= int(input("What is the repayment percentage: "))
debtAfterInterestApplied= initialLevelOfdebt+(initialLevelOfdebt*(interestPercentage/100))
print('Debt After Interest Applied in month 1 = ',debtAfterInterestApplied)
totalAmountSpent= int(initialLevelOfdebt*(repaymentPercentage/100))
print('Total amount spent= ',totalAmountSpent)
debtAfterRepaymentApplied= int(debtAfterInterestApplied -(initialLevelOfdebt*(repaymentPercentage/100))) 
print('Debt After Repayment Applied= ',debtAfterRepaymentApplied)
while debtAfterRepaymentApplied>50:
  newInterest= (interestPercentage/100)*debtAfterRepaymentApplied
  newInitialdebt= debtAfterRepaymentApplied+ newInterest
  debtAfterRepaymentApplied= newInitialdebt - totalAmountSpent
  n+=1
else:
    finalRepayment= int(debtAfterRepaymentApplied)
    finalAnswer = int((totalAmountSpent*n)+finalRepayment+totalAmountSpent)
    print('Total number of repayments: ',n)
    print('Final repayment: ',finalRepayment)
    print('Deposit: ',totalAmountSpent)
    print('Final Answer:',finalAnswer) 

  # modify and then return the variable below
  answer = finalAnswer
  return answer
