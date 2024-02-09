from Node import *

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_Data() == item:
                found = True
            else:
                if current.get_Data() > item:
                    stop = True
                else:
                    current = current.get_Next()
        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_Data() > item:
                stop = True
            else:
                previous = current
                current = current.get_Next()

        temp = Node(item)
        if previous == None:
            temp.set_Next(self.head)
            self.head = temp
        else:
            temp.set_Next(current)
            previous.set_Next(temp)

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.get_Data() != item:
                index += 1
                current = current.get_Next()
            else:
                found = True
        if found:
            return index
        else:
            return "Not Found"

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_Next()
        return count

    def check_num(self): #ฟังก์ชันเช็คตัวซ้ำ
        check = OrderedList()
        current = self.head
        previous = None
        while current != None:
            if current.get_Data() != previous:
                check.add(current.get_Data())
            previous = current.get_Data()
            current = current.get_Next()
        check.show_value()
        # print('check : [', end='')
        # while check.head != None:
        #     print(check.head.get_Data(), end='')
        #     check.head = check.head.get_Next()
        #     if check.head != None:
        #         print(",", end="")
        # print(']')

    def eo_number(self): #ฟังก์ชันแยกเลขคู่คี่
        Even = OrderedList()
        Odd = OrderedList()
        current = self.head
        while current != None:

            if (current.get_Data() % 2)== 0:
                Even.add(current.get_Data())

            else:
                Odd.add(current.get_Data())

            current = current.get_Next()
        Even.show_value()
        Odd.show_value()
        # print('Even : [', end='')
        # while Even.head != None:
        #     print(Even.head.get_Data(), end='')
        #     Even.head = Even.head.get_Next()
        #     if Even.head != None:
        #         print(",", end="")
        # print(']')
        # print('Odd : [', end='')
        # while Odd.head != None:
        #     print(Odd.head.get_Data(), end='')
        #     Odd.head = Odd.head.get_Next()
        #     if Odd.head != None:
        #         print(",", end="")
        # print(']')

    def show_value(self):
        current = self.head
        print("[", end='')
        while current != None:
            print(current.get_Data(), end='')
            current = current.get_Next()
            if current != None:
                print(",", end="")
        print(']')

o = OrderedList()
o.add(1)
o.add(1)
o.add(3)
o.add(4)
o.add(2)
o.add(5)
o.eo_number()
o.check_num()
