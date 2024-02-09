from Node import *

class Unorderedlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_Next(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_Data() == item:
                found = True
            else:
                current = current.get_Next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_Data() == item:
                found = True
            else:
                previous = current
                current = current.get_Next()

        if previous == None:
            self.head = current.get_Next()
        else:
            previous.set_Next(current.get_Next())

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_Next()
        return count

    # index of item in the list
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

    # insert item in the pos-th of the list
    def insert(self, pos, item):#ฟังก์ชั่นที่ทำการเพิ่ม Node ลงไปตามตำแหน่งที่ระบุในฟังก์ชั่นของ Unordered List
        current = self.head
        previous = None
        index = 0
        temp = Node(item)

        while current != None and index < pos:
            previous = current
            current = current.get_Next()
            index += 1

        if pos == 0:
            temp.set_Next(self.head)
            self.head = temp
        else:
            if current == None:
                previous.set_Next(temp)
            else:
                temp.set_Next(current)
                previous.set_Next(temp)

    # remove last item of the list
    def pop(self, pos=None):
        current = self.head
        previous = None
        count_index = 0
        found = False

        while current != None and not found:
            if pos == 0 and previous == None:  # Position = 0
                self.head = current.get_Next()
                found = True

            elif count_index == int(self.size()) - 1 and pos == None:  # don't have Position
                if self.size() == 1:
                    self.head = current.get_Next()
                else:
                    previous.set_Next(current.get_Next())
                found = True

            elif count_index == pos and count_index > 0:  # tell Position
                previous.set_Next(current.get_Next())
                found = True

            else:
                count_index += 1
                previous = current
                current = current.get_Next()

        return current.get_Data()

    # remove item from the pos-th of the list
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0

        if current == None:
            return "No item in list"

        while index < pos and current != None:
            previous = current
            current = current.get_Next()
            index += 1

        if current == None:
            return "No item in list"
        else:
            if previous == None:
                self.head = current.get_Next()
            else:
                previous.set_Next(current.get_Next())
            return current.get_Data()

    def make_list(self):
        current = self.head
        newlist = []
        while current != None:
            newlist.append(current.get_Data())
            current = current.get_Next()
        return newlist

    def make_list2(self):
        current = self.head
        newlist = []
        while current != None:
            newlist.insert(0, current.get_Data())
            current = current.get_Next()
        return newlist

    def reverse(self):
        output = Unorderedlist()
        while self.head != None:
            output.add(self.head.get_Data())
            self.head = self.head.get_Next()
        return output

    def change_head(self):
        Ch = self.pop()
        self.add(Ch)

    def pr_head(self):
        current = self.head
        a = current.get_Data()
        return a
    
print("Unorder")
a = Unorderedlist()

a.add(10)
a.add(20)
a.add(30)
a.insert(2, 40)
a.add(50)
print(a.make_list2())