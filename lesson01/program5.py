print("Точка А :")
a_x = float(input('координата по х : '))
a_y = float(input('координата по y : '))

print("Точка B :")
b_x = float(input('координата по х : '))
b_y = float(input('координата по y : '))

rasst = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5
print("Расстояние между точками А и В = {:5.2f}".format(rasst))