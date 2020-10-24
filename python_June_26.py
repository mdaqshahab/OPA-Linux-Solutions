import string
class Vegetable:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self, storeName, vegList):
        self.storeName = storeName
        self.vegList = vegList

    def categorizeVegetablesAlphabetically(self):
        self.vegList.sort(key= lambda x: x.name)
        a = list(string.ascii_lowercase)
        d_veg = {}
        for i in a:
            d_list = []
            for j in self.vegList:
                if i == j.name[0]:
                    d_list.append(j.name)
            if len(d_list) > 0:
                d_veg[i] = tuple(d_list)
        return d_veg

    def filterVegetablesForPriceRange(self, min, max):
        self.vegList.sort(key= lambda x: x.name)
        temp = []
        for item in self.vegList:
            if item.price >= min and item.price <= max:
                temp.append(item.name)
        return temp

if __name__ == '__main__':
    n = int(raw_input())
    temp = []
    for i in range(n):
        name = raw_input()
        price = float(raw_input())
        quantity = int(raw_input())
        v = Vegetable(name.lower(), price, quantity)
        temp.append(v)
    s_name = raw_input()
    min1 = float(raw_input())
    max1 = float(raw_input())
    store = Store(s_name, temp)
    arrange = store.categorizeVegetablesAlphabetically()
    price_veg = store.filterVegetablesForPriceRange(min1,max1)
    for keys, value in arrange.items():
        print(keys)
        for x in value:
            print(x)
            
    if len(price_veg) > 0:
        for x in price_veg:
            print(x)
    else:
        print("No Vegetables in the given price range")

