# Currency Converter USD/CNY
def CC(amount, rate):
    return amount * rate


amount_usd = [1, 1500, 25000]
amount_cny = [1, 1750, 28000]
USD2CNY = 6.74
rate = USD2CNY
data = "Jan 31, 2023"
print(f"{data} : 1 USD = {USD2CNY} CNY / 1 CNY = {round(1/USD2CNY, 3)} USD\n")
for i in range(0, len(amount_usd)):
    amount = amount_usd[i]
    result = CC(amount, rate)
    print(f"Amount {amount_usd[i]} USD = {result:.2f} CNY")
for j in range(0, len(amount_cny)):
    amount = amount_cny[j]
    result = CC(amount, 1 / rate)
    print(f"Amount {amount_cny[j]} CNY = {result:.2f} USD")
