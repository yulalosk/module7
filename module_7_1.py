# a = 'hello'
# chars = []
# for i in a:
#     chars.append(ord(i))
# print(chars)
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name,'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a+')
        for product in products:
            if str(product) not in current_products:
                file.write(str(product)+'\n')
                current_products += str(product)+'\n'

            else:
                product.name = str(product).split(',')[0]
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#print(p1,p2,p3, sep='\n') # __str__
s1.add(p1, p2, p3)
print(s1.get_products())