class Product:
    def __init__(self,id,name,type,price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def apply(self, dis):
        if dis <=0:
            return
        discount = (dis/100)*self.price
        print(discount)
        self.price = self.price - discount

class Store:
    def __init__(self,name,p_list):
        self.name = name
        self.p_list = p_list

    def calculate(self,disp,p_type):
        lst = []
        for item in self.p_list:
            if item.type == p_type:
                item.apply(disp)
                lst.append(item)
        if len(lst) > 0:
            lst.sort(key= lambda x:x.price, reverse = True)
            return lst
        else:
            return None

if __name__ == '__main__':
    num = int(input())
    p_list = []
    for i in range(num):
        a = int(input())
        b = input()
        c = input().lower()
        d = float(input())
        obj = Product(a,b,c,d)
        p_list.append(obj)
    ty = input().lower()
    dis = float(input())
    s_name = "Store"
    s_obj = Store(s_name, p_list)
    res = s_obj.calculate(dis,ty)
    if res != None:
        for item in res:
            print(item.name + " " + str(item.price))
    else:
        print("product Not Found")
