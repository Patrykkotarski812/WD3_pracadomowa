#ZAD1
# a = [1 - x for x in range(1, 10)]
# b = [4 ** x for x in range(8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)

#ZAD2
# import random
# listalosowa= [random.randint(1, 100) for x in range(10)]
# listaparzysta = [x for x in listalosowa if x % 2 == 0]
# print(listalosowa)
# print(listaparzysta)

#ZAD3
# produkty ={'sok': 'karton', 'chipsy': 'paczka', 'ziemniaki': 'kg'}
# print(produkty)
#
# slownik_odwrocone = {value: key for key, value in produkty.items()}
# print(slownik_odwrocone)


#ZAD4

# def prostokatny(a, b, c):
#         if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(c).isdigit() == False):
#             return "Wpisałeś nieprawidłowe wartości"
#         else:
#             a = float(a)
#             b = float(b)
#             c = float(c)
#             if (a<=0)|(b<=0)|(c<=0):
#                 return "Wpisałeś nieprawidłowe wartości"
#             elif (a > b) & (a > c):
#                 check = b**2 + c**2
#                 if a**2 == check:
#                     return "Trójkąt prostokątny"
#                 else:
#                     return "Trójkat nie jest prostokątny"
#             elif (b > a) & (b > c):
#                 check = a**2 + c**2
#                 if b**2 == check:
#                     return "Trójkat prostokątny"
#                 else:
#                     return "Trójkat nie jest prostokątny"
#             else :
#                 check = b ** 2 + a ** 2
#                 if c ** 2 == check:
#                     return "Trojkąt prostokątny"
#                 else:
#                     return "Trójkat nie jest prostokątny"
#
#
#
# a = input("Długość pierwszego boku: ")
# b = input("Długość drugiego boku: ")
# c = input("Długość trzeciego boku: ")
# print(prostokatny(a, b, c))



#ZAD5
# def pole_trapezu(a=1, b=1, h=1):
#     if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(h).isdigit() == False):
#         return "Wpisałeś nieprawidłowe wartości"
#     else:
#         a = float(a)
#         b = float(b)
#         h = float(h)
#         if (a<=0)|(b<=0)|(h<=0):
#             return "Wpisałeś nieprawidłowe wartości"
#         else:
#             pole = h*(a+b)/2
#             return pole
#
# print(pole_trapezu())
# a = input("Długość pierwszej podstawy: ")
# b = input("Długość drugiej podstawy: ")
# h = input("Wysokość: ")
# print(pole_trapezu(a, b, h))


#ZAD6

# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     if ile == 1:
#         return a
#     return (a * b ** (ile - 1)) * iloczyn_ciagu(a, b, ile - 1)
#
# print(iloczyn_ciagu())



#ZAD8

# Zad8
# def zakupy(**koszyk):
#     produkty = len(koszyk)
#     if produkty != 0:
#         suma = 0
#         ceny = [cena for cena in koszyk.values() if isinstance(cena, float) == True or isinstance(cena, int) == True]
#         print(ceny)
#         for x in range (len(ceny)):
#             suma+=float(ceny[x])
# 
#     else:
#         return "Pusty koszyk"
#     return suma
#
# print(zakupy(chleb = 1, maslo = 3, sok = 5 ))
