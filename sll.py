class node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,data):
		self.data = data

	def setNext(self,next):
		self.next = next


class sll:

	def __init__(self, head):
		self.head = head

	def add(self, newdata):
		if(self.head == None):
			self.head = node(newdata)

		else:
			temp = node(newdata)
			current = self.head
			temp.setNext(current)
			self.head = temp

	def printList(self):
		current = self.head
		print(current.getData())
		while(current.getNext() != None):
			current = current.getNext()
			print(current.getData())


node1 = node(2)
node2 = node(3)
node1.setNext(node2)
test1 = sll(node(3))
test1.add(4)

test1.printList()
