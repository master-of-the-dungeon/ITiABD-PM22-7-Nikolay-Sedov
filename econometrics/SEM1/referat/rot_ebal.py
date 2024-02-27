import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('combined_market_data.csv')  

# Подготовка данных
# Удаление строк с отсутствующими данными
df = df.dropna()

# Определение независимых переменных (X) и зависимой переменной (y)
X = df[['SP500_Close', 'USD_RUB']]
y = df['MOEX_Close']

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создание модели линейной регрессии
model = LinearRegression()

# Обучение модели на тренировочных данных
model.fit(X_train, y_train)

# Прогнозирование значений для тестового набора
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
print(f"Среднеквадратическая ошибка (MSE): {mse}")

# Вывод коэффициентов модели
print("Коэффициенты модели:", model.coef_)
print("Пересечение (интерсепт):", model.intercept_)
