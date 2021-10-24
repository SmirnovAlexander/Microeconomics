import matplotlib.pyplot as plt
plt.style.use("seaborn")

year = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
consumption = [3.12, 3.35, 3.6, 3.78, 4.06, 4.3, 4.07]
price = [40.7, 25.3, 36.5, 58.8, 75.2, 39, 31]

plt.plot(price, consumption)
plt.title("Oil Demand")
plt.ylabel("Consumption")
plt.xlabel("Price")
plt.savefig("./oil_demand.png")

dc = (max(consumption) - min(consumption)) / (max(consumption) + min(consumption))

dp = (max(price) - min(price)) / (max(price) + min(price))

elasticity = dc / dp
print(elasticity)
