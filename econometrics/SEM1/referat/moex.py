
import yfinance as yf

# Получение данных об индексе Московской биржи (MOEX)
moex = yf.Ticker("IMOEX.ME")

# Извлечение исторических данных за последний год
moex_data = moex.history(period="1y")

# Сохранение данных в файл CSV
moex_data.to_csv("moex_data.csv")

print("Данные сохранены в файл 'moex_data.csv'")
