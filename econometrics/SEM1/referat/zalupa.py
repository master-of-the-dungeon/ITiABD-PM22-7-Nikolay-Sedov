import yfinance as yf
import pandas as pd

# Установка периода для сбора данных
start_date = '2022-01-01'
end_date = '2022-12-31'

# Загрузка данных
moex = yf.Ticker("IMOEX.ME")
sp500 = yf.Ticker("^GSPC")
usd_rub = yf.Ticker("USDRUB=X")

# Извлечение исторических данных
moex_data = moex.history(start=start_date, end=end_date)['Close']
sp500_data = sp500.history(start=start_date, end=end_date)['Close']
usd_rub_data = usd_rub.history(start=start_date, end=end_date)['Close']

# Объединение данных в один DataFrame
combined_data = pd.DataFrame(index=moex_data.index)
combined_data['MOEX_Close'] = moex_data
combined_data['SP500_Close'] = sp500_data.reindex(combined_data.index, method='ffill')
combined_data['USD_RUB'] = usd_rub_data.reindex(combined_data.index, method='ffill')

# Вычисление дневных процентных изменений для MOEX
combined_data['MOEX_Percent_Change'] = combined_data['MOEX_Close'].pct_change() * 100

# Обработка отсутствующих данных
combined_data.fillna(method='ffill', inplace=True)

# Сохранение данных в файл CSV
file_name = "combined_market_data_suka.csv"
combined_data.to_csv(file_name)
print(f"Данные сохранены в файл {file_name}")
