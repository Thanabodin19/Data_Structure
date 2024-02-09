class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Unordered:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

        # index of item in the list

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() != item:
                index += 1
                current = current.getNext()
            else:
                found = True

        if found:
            return index
        else:
            return "Not Found"

    # insert item in the pos-th of the list
    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = Node(item)

        while current != None and index < pos:
            previous = current
            current = current.getNext()
            index += 1

        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            if current == None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)

    # remove last item of the list
    def pop(self, pos=None):
        current = self.head
        previous = None
        count_index = 0
        found = False

        while current != None and not found:
            if pos == 0 and previous == None:  # Position = 0
                self.head = current.getNext()
                found = True

            elif count_index == int(self.size()) - 1 and pos == None:  # don't have Position
                if self.size() == 1:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                found = True

            elif count_index == pos and count_index > 0:  # tell Position
                previous.setNext(current.getNext())
                found = True

            else:
                count_index += 1
                previous = current
                current = current.getNext()

        return current.getData()

    # remove item from the pos-th of the list
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0

        if current == None:
            return "No item in list"

        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index += 1

        if current == None:
            return "No item in list"
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()

    def make_list(self):
        current = self.head
        newlist = []
        while current != None:
            newlist.append(current.getData())
            current = current.getNext()
        return newlist


class Stack:
    def __init__(self):
        self.link_list = Unordered()

    def is_empty(self):
        return self.link_list.isEmpty()

    def push(self, item):
        self.link_list.add(item)

    def pop(self):
        return self.link_list.delete(0)

    def peek(self):
        x = self.link_list.make_list()
        return x[-1]

    def size(self):
        return self.link_list.size()

    def show_stack(self):
        return self.link_list.make_list()


class Queue:
    def __init__(self):
        self.link_list = Unordered()

    def is_empty(self):
        return self.link_list.isEmpty()

    def enqueue(self, item):
        self.link_list.insert(0, item)

    def dequeue(self):
        return self.link_list.pop()

    def size(self):
        return self.link_list.size()

    def show_stack(self):
        return self.link_list.make_list()
print("unorder")
u = Unordered()
u.add(10)
u.make_list()
print('==========Stack==========')
a = Stack()
a.push("Hello")
a.push('World')
a.push(123)
print(a.pop())
print(a.pop())
print(a.pop())

print('==========Queue==========')
b = Queue()
b.enqueue("Hello")
b.enqueue('World')
b.enqueue(123)
print(b.dequeue())
print(b.dequeue())
print(b.dequeue())