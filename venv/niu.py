import random

numeros = list(range(1, 101));  # arreglo del 1 al 100
numeros = random.sample(numeros, 10);  # obtener 10 números aleatorios
numeros.sort() ; # ordenar los números
print(numeros);

num_usuario = int(input('Ingrese un número entre 1 y 100: '));

menores = [];
mayores = [];

for n in numeros:
    if n < num_usuario:
        menores.append(n);
    else:
        mayores = numeros[numeros.index(n):];
        break

print(f'Los números menores a {num_usuario} son: {menores}');
print(f'Los números mayores a {num_usuario} son: {mayores}');