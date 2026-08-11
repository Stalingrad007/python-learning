item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("how many would you like?: "))
total = price * quantity
print(f"total would be {total}$")

print(f"you have bought {quantity} {item} that cost {price} per each")