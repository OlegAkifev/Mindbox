from pyspark.sql import SparkSession


def get_product_category_pairs(products_df, categories_df):
    # Объединяем датафреймы продуктов и категорий по общему столбцу 'product_id'
    joined_df = products_df.join(categories_df, products_df['product_id'] == categories_df['product_id'], how='full')

    # Формируем датафрейм с парами "Имя продукта - Имя категории"
    result_df = joined_df.select(products_df['product_name'], categories_df['category_name']) \
                         .filter(categories_df['category_name'].isNotNull())

    # Фильтруем продукты, у которых нет категорий
    products_without_categories_df = products_df.join(categories_df, products_df['product_id'] == categories_df['product_id'], how='left') \
                                                 .filter(categories_df['category_name'].isNull()) \
                                                 .select(products_df['product_name'])

    return result_df, products_without_categories_df


# Создаем Spark сессию
spark = SparkSession.builder.appName("ProductCategoryApp").getOrCreate()

# Пример данных (замените данными из вашего приложения)
products_data = [(1, 'Продукт 1'), (2, 'Продукт 2'), (3, 'Продукт 3')]
products_df = spark.createDataFrame(products_data, ['product_id', 'product_name'])

categories_data = [(1, 'Категория A'), (3, 'Категория C')]
categories_df = spark.createDataFrame(categories_data, ['product_id', 'category_name'])

# Получаем результаты
product_category_pairs, products_without_categories = get_product_category_pairs(products_df, categories_df)

# Выводим результаты
print("Пары \"Имя продукта - Имя категории\":")
product_category_pairs.show()

print("Продукты без категорий:")
products_without_categories.show()

# Завершаем Spark сессию
spark.stop()
