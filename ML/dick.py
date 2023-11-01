from sklearn.datasets import fetch_openml

# Загрузка датасета "ERA"
dataset = fetch_openml(name='ERA', version='active')

# Получение данных и меток
X, y = dataset.data, dataset.target

# Сохранение данных и меток в CSV-файлы
X.to_csv('ERA_data.csv', index=False)
y.to_csv('ERA_target.csv', index=False)

print("Датасет успешно загружен и сохранен в локальные файлы.")
