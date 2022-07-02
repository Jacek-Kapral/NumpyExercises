import numpy as np

#cwiczenia z https://favtutor.com/blogs/numpy-exercises-python

#1
print('Wersja biblioteki Numpy to:', np.__version__)

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])

c = a + b

print('Wynik dodawania macierzy a\n', a, '\ni macierzy b\n', b, '\nto:\n',  c)

#2
d = np.array([[1,2,3],
             [4,5,6]])
e = 2*d

print('Wynik mnożenia macierzy d\n', d, '\n przez 2 to:\n', e)

#3

f = np.eye(4)
print('Wygenerowana macierz jednostkowa 4x4:\n', f)

#4

g = np.array([x for x in range(27)])

h = g.reshape((3,3,3))

print('Wygenerowana macierz jednowymiarowa skonwertowana na macierz trójwymiarową:\n', h)

#5

i = np.array([[2.5, 3.8, 1.5],
              [4.7, 2.9, 1.56]])

j = i.astype('int')

print('Macierz, którą numpy konwertuje z float:\n', i, '\nna int\n', j)

#6

k = np.array([[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]])

l = k.astype('bool')

print('Konwersja macierzy jednostkowej na wartości logiczne:\n', l)

#7

a1 = np.array([[1,2,3],
               [4,5,6]])

a2 = np.array([[7,8,9],
               [10,11,12]])

m = np.hstack((a1, a2))

print('Konwersja dwóch macierzy:\n', a1, '\n\n', a2,  '\nna jedną macierz, która ma tą samą liczbę wierszy:\n', m)

#8

b1 = np.array([[1,2],
               [3,4],
               [5,6]])

b2 = np.array([[7,8],
               [9,10],
               [11,12]])

n = np.vstack((b1, b2))

print('Konwersja dwóch macierzy:\n', b1, '\n\n', b2,  '\nna jedną macierz, która ma tą samą liczbę kolumn:\n', n)

#9

o = np.arange(0, 101, 2)

print('Macierz, w której numpy generuje liczby od 0 do 100, skacząc o 2:\n', o)

#10

p = np.array([1,2,3,4,5])

r = np.array([1,3,2,4,5])

print('Porównanie indeksów macierzy, na których występują te same elementy:\n', np.where(p == r))

#11

s = np.linspace(0, 100, 5)

print('Macierz z pięcioma wygenerowanymi liczbami od 0 do 100 z takim samym poskokiem:\n', s)

#12

t = np.full((2, 3), 5)

print('Generowanie macierzy wypełnionej piątkami o danym rozmiarze (2x3):\n', t)

#13

u = np.array([[1,2,3],
              [4,5,6]])

v = np.tile(u, 10)

print('Macierz wygenerowana poprzez powtórzenie mniejszej macierzy 10 razy:\n', v)

#14

np.random.seed(123)

w = np.random.randint(0, 10, size = (5,5))

print('Losowo wygenerowana macierz 5x5 z liczbami w zakresie od 0 do 9:\n', w)

#15

np.random.seed(123)

x = np.random.normal(size = (3,3))

print('Macierz 3x3 z wygenerowanymi liczbami z wykresu rozkładu normalnego:\n', x)

#16

y = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

z = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])

yz = np.matmul(y, z)

print('Wynik mnożenia macierzy przez macierz:\n', yz)

#17

aa = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

aa_transpose = aa.T

print('Transponowanie macierzy (zamiana wierszy z kolumnami):\n', aa_transpose)

#18

miaryKatow = np.array([3.14, 3.14/2, 6.28])

sinusyMiar = np.sin(miaryKatow)

print('Sinusy danych kątów w macierzy to:\n', sinusyMiar)

#19

miaryKatow2 = np.array([3.14, 3.14/2, 6.28])

cosinusyMiar = np.cos(miaryKatow2)

print('Cosinusy danych kątów w macierzy to:\n', cosinusyMiar)

#20

macierz = np.array([10,1,5,2])

indeksy = np.argsort(macierz)

print('Macierz, która pokazuje indeksy liczb w porządku rosnącym opartym o wielkości danych liczb:\n', indeksy)

