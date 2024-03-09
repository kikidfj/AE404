# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:40:44 2023

@author: user
"""
import sys, math
IS_DEBUG = False
CROSS = 10
DIVIDE = 11

def bugPrint(_inpStr):
    if IS_DEBUG:
        bugPrint(_inpStr)

# cleanCrossDevideList: 如果_crossDivideOperands,  _crossDivideOperators 有算式
# 則計算其中的算式並回傳結果。如果_crossDivideOperands,  _crossDivideOperators是空
# 的，則直接回傳_numberTotal 當結果
def cleanCrossDevideList(_numberTotal, _crossDivideOperands, _crossDivideOperators):
    res = float(_numberTotal)
    while len(_crossDivideOperators) > 0 :
        operand = _crossDivideOperands.pop()
        operator = _crossDivideOperators.pop()
        if operator == CROSS:
            res = res * operand
        if operator == DIVIDE:
            res = res / operand
    return res

def calByFormula(formulaStr):
    total = 0.0;
    forSize = len(formulaStr)
    if IS_DEBUG:
        bugPrint("forSize = " + str(forSize))
    digitCount = 0  #用來計算運算元的長度
    numberTotal = 0 #用來計算運算元的值
    crossDivideOperands = []
    crossDivideOperator = []
    for r in range(0, forSize):
        i = forSize-r - 1
        bugPrint(str(i) + "," + str(formulaStr[i]))
        #如果碰到"加號/減號"，先利用cleanCrossDevideList()把CrossDevideList 儲存的
        #算式算出來，並且重新計算運算元值(numberTotal)和指到的位數(digitCount)
        if formulaStr[i] == '+':
            res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
            total = total + res
            numberTotal = 0
            digitCount = 0 
            
        elif formulaStr[i] == '-':
            res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
            total = total - res
            numberTotal = 0
            digitCount = 0            

        elif formulaStr[i] == '*':
            crossDivideOperator.append(CROSS)
            crossDivideOperands.append(numberTotal)
            numberTotal = 0
            digitCount = 0

        elif formulaStr[i] == '/':
            crossDivideOperator.append(DIVIDE)
            crossDivideOperands.append(numberTotal)
            numberTotal = 0
            digitCount = 0            
        else:
            numberTotal = numberTotal + int(formulaStr[i]) * pow(10, digitCount)
            digitCount = digitCount + 1 #運算元長度加一
    res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
    total = total + res
    print(str(total))
return str(total)
    