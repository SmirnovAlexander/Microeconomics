import matplotlib.pyplot as plt
plt.style.use("seaborn")

year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

bread_consumption = [1, 0.99, 0.99, 0.98, 0.98, 0.98, 0.975, 0.98]
fish_consumption = [1, 1.06, 1.15, 1.15, 1.06, 0.92, 0.9, 0.91]

bread_price = [43, 45, 51, 55, 59, 65, 68, 45]
fish_price = [79, 87, 86, 91, 111, 138, 148, 153]

bread_price, bread_consumption = zip(*sorted(zip(bread_price, bread_consumption)))

plt.plot(bread_price, bread_consumption)
plt.title("Bread Demand")
plt.ylabel("Consumption")
plt.xlabel("Price")
plt.grid(True)
plt.savefig("./bread_demand.png")
plt.clf()

fish_price, fish_consumption = zip(*sorted(zip(fish_price, fish_consumption)))

plt.plot(fish_price, fish_consumption)
plt.title("fish Demand")
plt.ylabel("Consumption")
plt.xlabel("Price")
plt.grid(True)
plt.savefig("./fish_demand.png")
plt.clf()

bdc = (max(bread_consumption) - min(bread_consumption)) / (max(bread_consumption) + min(bread_consumption))
bdp = (max(bread_price) - min(bread_price)) / (max(bread_price) + min(bread_price))

elasticity = bdc / bdp
print(f"bread elasticity: {round(elasticity, 2)}")

bdc = (max(fish_consumption) - min(fish_consumption)) / (max(fish_consumption) + min(fish_consumption))
bdp = (max(fish_price) - min(fish_price)) / (max(fish_price) + min(fish_price))

elasticity = bdc / bdp
print(f"fish elasticity: {round(elasticity, 2)}")
