from collections import defaultdict
class Book:
    def __init__(self, id,name,subject,price):
        self.id = id
        self.name = name
        self.subject = subject
        self.price  = price

class Library:
    def __init__(self,libname, booklist):
        self.libname = libname
        self.booklist  = booklist

    def findSubjectWiseBooks(self):
        # d = defaultdict(0)
        d = dict()
        for i in self.booklist:
            if i.subject in d.keys():
                d[i.subject]+=1
            else:
                d[i.subject] = 1
        # for i in self.booklist:
        #     d[i.subject]+=1
        return d

    def checkBookCategoryByPrice(self, b_id):
        for i in self.booklist:
            if i.id == b_id:
                if i.price >= 1000:
                    return "High Price"
                elif i.price >= 750 and i.price < 1000:
                    return "Medium Price"
                elif i.price >=500 and i.price < 750:
                    return "Average Price"
                else:
                    return "Low Price"
        return None

if __name__ == '__main__':
    num = int(input())
    bl = []
    for i in range(num):
        a = int(input())
        b = input()
        c = input()
        d = int(input())
        obj = Book(a,b,c.lower(),d)
        bl.append(obj)
    f_id = int(input())
    l_name = "abcd"
    l_obj = Library(l_name,bl)
    res1 = l_obj.findSubjectWiseBooks()
    res2 = l_obj.checkBookCategoryByPrice(f_id)

    for keys,value in res1.items():
        print(keys + " " +str(value))

    if res2 != None:
        print(res2)
    else:
        print("Book Not Found")
