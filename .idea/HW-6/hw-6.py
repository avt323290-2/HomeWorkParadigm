
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
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Запрос на количество элементов в массиве
array_length = int(input("Введите количество элементов в массиве: "))
sorted_array = [int(input(f"Элемент {i + 1}: ")) for i in range(array_length)]

# Пример использования:
target_element = int(input("Введите элемент для поиска: "))

result = binary_search(sorted_array, target_element)
if result != -1:
    print(f"Элемент {target_element} найден в массиве. Индекс: {result}")
else:
    print(f"Элемент {target_element} не найден в массиве.")