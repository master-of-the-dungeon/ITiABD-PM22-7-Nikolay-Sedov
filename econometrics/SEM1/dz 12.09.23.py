import matplotlib.pyplot as plt
unemployed = [13.9, 12.4, 11.1, 8.9, 7.1, 6.1, 7.8, 7.1]
years = [2014,2015,2016,2017, 2018, 2019, 2020, 2021]
vvpusd = [229630, 199080,204000, 238000, 238000, 231000, 254000, 252000]
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(x = unemployed, y = vvpusd)
plt.xlabel(years)
plt.ylabel('y')

plt.show()
import matplotlib.pyplot as plt

unemployed = [13.9, 12.4, 11.1, 8.9, 7.1, 6.1, 7.8, 7.1]
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
vvpusd = [229630, 199080, 204000, 238000, 238000, 231000, 254000, 252000]

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x=years, y=vvpusd)
plt.xlabel('Year')
plt.ylabel('Unemployed')
plt.title('Unemployment vs. Year')

plt.show()
import matplotlib.pyplot as plt

unemployment_rate = [13.9, 12.4, 11.1, 8.9, 7.1, 6.1, 7.8, 7.1]
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
gdp_portugal = [229630, 199080, 204000, 238000, 238000, 231000, 254000, 252000]

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x=gdp_portugal, y=unemployment_rate)
plt.xlabel('GDP of Portugal (in millions USD)')
plt.ylabel('Unemployment Rate (%)')
plt.title('Unemployment Rate vs. GDP of Portugal (2014-2021)')

plt.show()
import matplotlib.pyplot as plt

unemployment_rate = [13.9, 12.4, 11.1, 8.9, 7.1, 6.1, 7.8, 7.1]
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
gdp_portugal = [229630, 199080, 204000, 238000, 238000, 231000, 254000, 252000]

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x=gdp_portugal, y=unemployment_rate)
plt.xlabel('GDP of Portugal (in USD)')
plt.ylabel('Unemployment Rate (%)')
plt.title('Unemployment Rate vs. GDP of Portugal (2014-2021)')

# Добавляем надпись на график
for i, year in enumerate(years):
    plt.annotate(year, (gdp_portugal[i], unemployment_rate[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
