import numpy as np

#cwiczenia z https://favtutor.com/blogs/numpy-exercises-python

#1
print(np.__version__)

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