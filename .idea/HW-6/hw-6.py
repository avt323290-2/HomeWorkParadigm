
def binary_search(arr, target):
    """
    Выполняет бинарный поиск элемента в отсортированном массиве.

    :param arr: Отсортированный массив, в котором ищется элемент.
    :type arr: list[int]
    :param target: Искомый элемент.
    :type target: int
    :return: Индекс элемента в массиве или -1, если элемент не найден.
    :rtype: int
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Нашли элемент, возвращаем индекс
        elif arr[mid] < target:
            low = mid + 1  # Искомый элемент находится в правой половине
        else:
            high = mid - 1  # Искомый элемент находится в левой половине

    return -1  # Элемент не найден

# Пример использования:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 5

result = binary_search(sorted_array, target_element)
if result != -1:
    print(f"Элемент {target_element} найден в массиве. Индекс: {result}")
else:
    print(f"Элемент {target_element} не найден в массиве.")