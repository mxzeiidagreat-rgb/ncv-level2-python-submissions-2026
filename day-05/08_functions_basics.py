def order(item):
    print(f"order placed: your order is {item}")

def calculateTotal(item):
    basePrice = 25.5
    VAT = 0.15
    totalPrice = (basePrice + len(item)) * 1.15
    
    return totalPrice

def getOrder():
    print("Preparing order")
    return "order ready"

myFood = input("What would you like? ")
order(myFood)

print(getOrder())

orderTotal = calculateTotal(myFood)
print(f"Your order costs:  R{orderTotal}")
