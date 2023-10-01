import matplotlib.pyplot as plt

years = list(range(2005, 2021))
gdp = [204, 217, 230, 240, 233, 238, 245, 212, 220, 230, 240, 255, 270, 280, 295, 280]
unemployment_rate = [7.6, 7.7, 8.0, 7.6, 9.5, 10.8, 12.7, 15.5, 16.2, 13.9, 12.4, 11.1, 8.9, 7.0, 6.5, 6.8]

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Год')
ax1.set_ylabel('ВВП (млрд. долларов США)', color=color)
ax1.plot(years, gdp, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # создаем вторую ось Y
color = 'tab:red'
ax2.set_ylabel('Уровень безработицы (%)', color=color)
ax2.plot(years, unemployment_rate, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # чтобы подписи не перекрывались
plt.title('Динамика ВВП и уровня безработицы в Португалии (2005-2020)')
plt.grid(True)
plt.show()
