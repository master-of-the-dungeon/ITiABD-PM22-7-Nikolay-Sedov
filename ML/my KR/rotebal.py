from sklearn.datasets import fetch_openml
import pandas as pd

# Загрузка датасета
ricci_data = fetch_openml(name='ricci_vs_destefano', version=1)

# Создание DataFrame из датасета
ricci_df = pd.DataFrame(data=ricci_data.data, columns=ricci_data.feature_names)
ricci_df['target'] = ricci_data.target

# Сохранение DataFrame в файл CSV
csv_file_path = 'ricci_vs_destefano.csv'
ricci_df.to_csv(csv_file_path, index=False)

print(f"Датасет сохранен в файл '{csv_file_path}'")
