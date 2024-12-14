from sympy import symbols, Eq, solve

# Определяем переменные
x1, x2 = symbols('x1 x2')

# Уравнения для ограничений
eq1 = Eq(x1 + x2, 2)          # x1 + x2 = 2
eq2 = Eq(-3 * x1 + 4 * x2, 12)  # -3x1 + 4x2 = 12
eq3 = Eq(x1 + 2 * x2, 12)       # x1 + 2x2 = 12

# Пересечения уравнений
intersection_1_2 = solve([eq1, eq2], (x1, x2))
intersection_1_3 = solve([eq1, eq3], (x1, x2))
intersection_2_3 = solve([eq2, eq3], (x1, x2))

# Пересечения с осями
intersection_1_axis = solve([eq1, Eq(x1, 0)], (x1, x2))
intersection_2_axis = solve([eq2, Eq(x1, 0)], (x1, x2))
intersection_3_axis = solve([eq3, Eq(x1, 0)], (x1, x2))

# Список всех точек (включая оси координат)
vertices = [
    intersection_1_2,
    intersection_1_3,
    intersection_2_3,
    intersection_1_axis,
    intersection_2_axis,
    intersection_3_axis,
    {'x1': 0, 'x2': 0}  # Ось координат (0, 0)
]

# Проверим все точки и выведем результаты
# Фильтруем только допустимые точки
feasible_points = []
for point in vertices:
    # Преобразуем словарь в числа
    x1_val, x2_val = point[x1], point[x2]

    # Проверяем выполнение всех ограничений
    if (x1_val >= 0 and x2_val >= 0 and
            x1_val + x2_val >= 2 and
            -3 * x1_val + 4 * x2_val <= 12 and
            x1_val + 2 * x2_val <= 12):
        feasible_points.append((x1_val, x2_val))


# Вычисляем значение функции Z в каждой точке
def compute_z(x1_val, x2_val):
    return (x1_val - 8) ** 2 + (x2_val - 6) ** 2


results = [(point, compute_z(*point)) for point in feasible_points]

# Находим максимум
max_point, max_value = max(results, key=lambda item: item[1])

# Вывод результатов
print("Допустимые точки:", feasible_points)
print("Значения функции Z в точках:", results)
print(f"Максимальное значение Z = {max_value} в точке {max_point}")
