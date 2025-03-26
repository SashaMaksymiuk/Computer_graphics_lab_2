import matplotlib.pyplot as plt

# Функція для побудови кривої Мінковського на відрізку
def minkowski_curve(p1, p2, depth):
    if depth == 0:
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2

    dx = (x2 - x1) / 4
    dy = (y2 - y1) / 4

    # Генерація точок кривої Мінковського
    points = [
        p1,
        (x1 + dx, y1 + dy),
        (x1 + dx + dy, y1 + dy - dx),
        (x1 + 2 * dx + dy, y1 + 2 * dy - dx),
        (x1 + 2 * dx, y1 + 2 * dy),
        (x1 + 2 * dx - dy, y1 + 2 * dy + dx),
        (x1 + 3 * dx - dy, y1 + 3 * dy + dx),
        (x1 + 3 * dx, y1 + 3 * dy),
        p2
    ]
    # Це працює, бо обертання на 90° вліво описується рівняннями:
    # X' = x - dy
    # Y' = y + dx

    # Oбертання на 90° вправо:
    # X' = x + dy
    # Y' = y - dx

    # Рекурсія для кожного сегмента
    result = []
    for i in range(len(points) - 1):
        segment_points = minkowski_curve(points[i], points[i + 1], depth - 1)
        result += segment_points[:-1]  # Додаємо всі точки, окрім останньої

    result.append(p2)
    return result

# Функція для побудови фрактала на основі квадрата
def minkowski_fractal_square(iterations):
    square = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    result = []

    for i in range(len(square) - 1):
        curve = minkowski_curve(square[i], square[i + 1], iterations)
        result += curve[:-1]

    result.append(square[0])

    x_vals, y_vals = zip(*result)
    plt.plot(x_vals, y_vals, 'k-', linewidth=1)
    plt.axis('equal')
    plt.title(f'Фрактал Мінковського (квадрат), рівень {iterations}')
    plt.show()

# Функція для побудови кривої Мінковського на відрізку
def draw_minkowski_curve(iterations):
    p1 = (0, 0)
    p2 = (1, 0)
    result = minkowski_curve(p1, p2, iterations)

    x_vals, y_vals = zip(*result)
    plt.plot(x_vals, y_vals, 'k-', linewidth=1)
    plt.axis('equal')
    plt.title(f'Крива Мінковського, рівень {iterations}')
    plt.show()

# Вибір варіанту побудови
choice = input("Basic figure: 1 - segment, 2 - square: ")

depth = int(input("Enter the recursion depth: "))

if choice == '1':
    draw_minkowski_curve(depth)
elif choice == '2':
    minkowski_fractal_square(depth)
else:
    print("Incorrect choice!")
