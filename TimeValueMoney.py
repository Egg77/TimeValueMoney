## Patrick Robert Willmann

import math
from typing import List

""" This class contains several methods corresponding to time value of money formulae. Each method takes a series of known
    inputs and solves for the value named in the method. In all cases, the last argument is a boolean variable which, when
    set to True, prompts a string representation of the formula used (incorporating the input values) to be printed to the 
    screen.

    All methods return float values, meaning these methods can be nested as needed for convenience. In cases of complex 
    nesting, it is recommended to set printTrue = False to avoid needless clutter or confusion.
"""

class TimeValueMoney:

    def FutureValue_Simple (self, presentValue: float, nominalInterest: float, period: float, printTrue: bool) -> float:
        
        futureValue: float = presentValue * (1 + (nominalInterest * period))

        if printTrue:
            print("\nFV = " + str(presentValue) + "(1 + " + str(nominalInterest) + " * " + str(period) + ")")
        
        return futureValue

    def PresentValue_Simple (self, futureValue: float, nominalInterest: float, period: float, printTrue: bool) -> float:
        
        presentValue: float = futureValue / (1 + (nominalInterest * period))

        if printTrue:
            print("\nPV = " + str(futureValue) + " / (1 + " + str(nominalInterest) + " * " + str(period) + ")")
        
        return presentValue    

    def FutureValue_Compound (self, presentValue: float, nominalInterest: float, period: float, printTrue: bool) -> float:
        
        futureValue: float = presentValue * ((1 + nominalInterest)**period)

        if printTrue:
            print("\nFV = " + str(presentValue) + "(1 + " + str(nominalInterest) + ")^"+ str(period))
        
        return futureValue

    def PresentValue_Compound (self, futureValue: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        presentValue: float = futureValue * ((1+ nominalInterest) ** (- period))

        if printTrue:
            print("\nPV = " + str(futureValue) + "(1 + " + str(nominalInterest) + ")^ (-"+ str(period) + ")")
        
        return presentValue

    def FutureValue_Ann (self, annuity: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        futureValue: float = annuity * ((((1 + nominalInterest) ** period) - 1) / nominalInterest)

        if printTrue:
            print("\nFV = " + str(annuity) + "[(1 + " + str(nominalInterest) + ")^"+ str(period) + " - 1) / " + str(nominalInterest) + "]")

        return futureValue

    def PresentValue_Ann (self, annuity: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        presentValue: float = annuity * (((1-(1 + nominalInterest) ** (-period))) / nominalInterest)

        if printTrue:
            print("\nPV = " + str(annuity) + "[1 - (1 + " + str(nominalInterest) + ")^ -"+ str(period) + ") / " + str(nominalInterest) + "]")

        return presentValue

    def FutureValue_Lin (self, G: float, nominalInterest: float, period: float, printTrue: bool) -> float:
        
        futureValue: float = (G / nominalInterest) * (((((1 + nominalInterest) ** period) - 1) / nominalInterest) - period)

        if printTrue:
            print("\nFV = " + str(G) + " / " + str(nominalInterest) + "[(((1 + " + str(nominalInterest) + ")^" + str(period) + " - 1) / " + str(nominalInterest) + ") - " + str(period) + "]")

        return futureValue

    def PresentValue_Lin (self, G: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        presentValue: float = G * ((((1 + nominalInterest) ** period) - (nominalInterest * period) - 1) / ((nominalInterest ** 2) * (1 + nominalInterest) ** period))

        if printTrue:
            print("\nPV = " + str(G) + "[(((1 + " + str(nominalInterest) + ")^" + str(period) + " - (" + str(nominalInterest) + " * " + str(period) + ") - 1) / (" + str(period) + "^2 (1 + " + str(nominalInterest) + ")^" + str(period) + ")))]" )
        
        return presentValue

    def FutureValue_Ann_Due (self, annuity: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        futureValue: float = annuity * (1 + nominalInterest) * ((((1 + nominalInterest) ** period)) / nominalInterest)

        if printTrue:
            print("\nFV = " + str(annuity) + "(1 + " + str(nominalInterest) + ")" + "[(1 + " + str(nominalInterest) + ")^"+ str(period) + ") / " + str(nominalInterest) + "]")

        return futureValue

    def SinkingFund (self, FV: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        sinkingFund: float = FV * (nominalInterest/(((1 + nominalInterest) ** period) - 1))

        if printTrue:
            print("\nA = " + str(FV) + "[" + str(nominalInterest) + "/ (1 + " + str(nominalInterest) + ")^" + str(period) + " - 1)]" )

        return sinkingFund

    def CapitalRecovery (self, PV: float, nominalInterest: float, period: float, printTrue: bool) -> float:

        capitalRecovery: float = PV * (nominalInterest * (((1 + nominalInterest) ** period))) / ((((1 + nominalInterest) ** period)) - 1)

        if printTrue:
            print("\nA = " + str(PV) + "[" + str(nominalInterest) + "(1 + " + str(nominalInterest) + ")^" + str(period) + "/(1 + " + str(nominalInterest) + ")^" + str(period) + " - 1)]")

        return capitalRecovery

    def EffectiveInterestPerPaymentPeriod (self, nominalInterest: float, compoundingPeriodPerYear: float, numberOfYears: float, compPerPayPeriod: float, printTrue: bool) -> float:

        effectiveRate: float = ((1 + (nominalInterest / compoundingPeriodPerYear)) ** (compPerPayPeriod)) - 1

        if printTrue:
            print ("\ni_a = (1 + (" + str(nominalInterest) + " / " + str(compoundingPeriodPerYear) + "))^(" + str(compPerPayPeriod) + ") - 1") 
        
        return effectiveRate
    
    def NPV_Irregular (self, initialInvestment: float, MARR: float, cashFlows, printTrue: bool) -> float:

        NPV: float = -(initialInvestment)
        periodCounter: int = 1

        workString: str = "\nNPV = -" + str(initialInvestment)

        for amount in cashFlows:
            NPV += self.PresentValue_Compound(amount, MARR, periodCounter, False)
            workString += " + " + str(amount) + "(P/F, " + str(MARR*100)+ "%, " + str(periodCounter) + ")"
            periodCounter += 1
        
        if printTrue == True:
            print (workString)
        
        return NPV

    def NPV_Annuity (self, initialInvestment: float, MARR: float, cashFlows, period: int, printTrue: bool) -> float:

        NPV: float = -(initialInvestment) + self.PresentValue_Ann(cashFlows, MARR, period, False)

        if printTrue == True:
            print ("\nNPV = -" + str(initialInvestment) + " + " + str(cashFlows) + "[1 - (1 + " + str(MARR) + ")^ -"+ str(period) + ") / " + str(MARR) + "]\n")
        
        return NPV


"""Main Function. All calculations can be programmed here (uncomment), or the class can simply be imported elsewhere."""
# if __name__== "__main__":
#     # No initialization arguments needed
#     TVM = TimeValueMoney()
#     # Equation steps will be printed to the console. Set the last argument in all functions to "False" if this is not desired.
#     # Prefix all methods with "TVM."
#     answer = 0
#     print(str(answer) + "\n")