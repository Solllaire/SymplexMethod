import pulp

# Тут нужно определить каждую переменную
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
# Сюда вводить целевую функцию
problem += 3 * x1 + 4 * x2, "Функция цели"
# Сюда вводить ограничения
problem += 2 * x1 + 3 * x2 <= 1200, "1"
problem += 12 * x1 + 30 * x2 <= 9600, "2"
problem += x1 + x2 <= 550, "3"
# Тут уравнение решается
problem.solve()
# Тут вывод
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
print(pulp.value(problem.objective))
