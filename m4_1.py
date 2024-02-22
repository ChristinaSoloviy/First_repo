"""
У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, 
якщо необхідно сплатити за рахунками. 
Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.
"""

def amount_payment(payment):
    result = 0
    for debt in payment:
        if debt <= 0:
            print("нічого не робимо, у нас переплата")
        else: 
            result = result + debt
    return result