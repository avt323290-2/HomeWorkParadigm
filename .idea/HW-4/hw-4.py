"""
Корреляция
● Контекст
Корреляция - статистическая мера, используемая для оценки
связи между двумя случайными величинами.
● Ваша задача
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.

"""

from functools import reduce

def calculate_mean(data):
    """Расчет среднего значения."""
    return sum(data) / len(data)

def calculate_covariance(x, y, mean_x, mean_y):
    """Расчет ковариации между двумя массивами."""
    n = len(x)
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))

def calculate_variance(data, mean):
    """Расчет дисперсии массива."""
    return sum((xi - mean) ** 2 for xi in data)

def calculate_pearson_correlation(x, y):
    """
    Расчет корреляции Пирсона между двумя массивами.

    Параметры:
    - x (list): Первый массив данных.
    - y (list): Второй массив данных.

    Возвращает:
    - correlation (float): Коэффициент корреляции Пирсона.
    """
    # Проверка на равное количество элементов в обоих массивах
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    n = len(x)

    # Расчет средних значений
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    # Расчет ковариации и дисперсий
    cov_xy = calculate_covariance(x, y, mean_x, mean_y)
    var_x = calculate_variance(x, mean_x)
    var_y = calculate_variance(y, mean_y)

    # Расчет корреляции Пирсона
    correlation = cov_xy / (var_x ** 0.5 * var_y ** 0.5)

    return correlation

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [2, 3, 4, 5, 6]

correlation_result = calculate_pearson_correlation(array1, array2)
print(f"Корреляция Пирсона: {correlation_result}")