'''
Написать программу на языке Prolog для вычисления суммы
элементов списка. На вход подаётся целочисленный массив.
На выходе - сумма элементов массива.
'''

% Правило для вычисления суммы элементов пустого списка (сумма равна 0).
sum_list([], 0).

% Правило для вычисления суммы элементов непустого списка.
sum_list([Head | Tail], Sum) :-
sum_list(Tail, TailSum),  % Рекурсивный вызов для оставшейся части списка.
Sum is Head + TailSum.    % Суммируем текущий элемент с суммой оставшейся части.

% Пример использования:
% Вызов: sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Result).
% Результат: Result = 55.