from classes.class_Test import TestClass

random_values = TestClass(100)

print(random_values)

print(random_values.values)

print(random_values.maximum)
print(random_values.minimum)

print(random_values._range)
print(random_values.range)
print(random_values._range)

random_values.new_random_values(10)

print(random_values)

print(random_values.values)
print(random_values.range)

a = TestClass(10)
b = TestClass(10)

print(F"{a.maximum} > {b.maximum} {a > b}")
print(F"{a.minimum} < {b.minimum} {a < b}")

# print(a > 5.8)
print(a >= 5.8)
