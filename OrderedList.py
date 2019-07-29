class Node:
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class OrderedList:
	def __init__(self, asc):
		self.head = None
		self.tail = None
		self.__ascending = asc

	def compare(self, v1, v2):
		if v1 < v2:
			return -1
		elif v1 == v2:
			return 0
		else:
			return +1
		
	def add(self, value):
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
		else:
			if self.__ascending == True:
				currNode = self.head
				prevNode = None
				cont = True
				while cont == True and currNode is not None:
					x = self.compare(value, currNode.value)
					if x == 1:
						currNode, prevNode = currNode.next, currNode
					else:
						if currNode is self.head:
							currNode.prev = Node(value)
							currNode.prev.next, self.head = self.head, currNode.prev
						else:
							currNode.prev = Node(value)
							prevNode.next = currNode.prev
						cont = False
				if currNode is None:
					self.tail = Node(value)
					self.tail.prev, prevNode.next = prevNode, self.tail
			else:
				currNode = self.tail
				prevNode = None
				cont = True
				while cont == True and currNode is not None:
					x = self.compare(value, currNode.value)
					if x != -1:
						currNode, prevNode = currNode.prev, currNode
					else:
						if currNode is self.tail:
							currNode.next = Node(value)
							currNode.next.prev, self.tail = self.tail, currNode.next
						else:
							currNode.prev= Node(value)
							prevNode.next = currNode.prev
						cont = False
				if currNode is None:
					self.head = Node(value)
					self.head.next, prevNode.prev = prevNode, self.head

	def find(self, val):
		if self.len() == 0:
			return None
		else:
			if self.__ascending == True:
				currNode = self.head
				while currNode is not None:
					x = self.compare(currNode.value, val)
					if x == 1:
						return None
					elif x == 0:
						return currNode
					else:
						currNode = currNode.next
			if self.__ascending == False:
				currNode = self.tail
				while currNode is not None:
					x = self.compare(currNode.value, val)
					if x == 1:
						return None
					elif x == 0:
						return currNode
					else:
						currNode = currNode.prev
			if currNode == None:
				return None


	def delete(self, val):
		currNode = self.head
		prevNode = None
		if self.head is None:
			return None
		else:
			if self.head.value == val:
				if self.len() == 1:
					self.head = None
					self.tail = None
					return
				else:
					currNode = self.head.next
					self.head = currNode
					currNode.prev = None
					return
		while currNode is not None:
			if currNode.value == val:
				prevNode.next = currNode.next
				if currNode is self.tail:
					self.tail = prevNode
				else:
					currNode.next.prev = prevNode
				return
			else:
				prevNode = currNode
				currNode = currNode.next

	def clean(self, asc):
		self.head = None
		self.tail = None
		self.__ascending = asc

	def len(self):
		currNode = self.head
		count = 0
		while currNode is not None:
			currNode = currNode.next
			count += 1
		return count

	def get_all(self):
		r = []
		node = self.head
		while node != None:
			r.append(node)
			node = node.next
		return r

class OrderedStringList(OrderedList):
	def __init__(self, asc):
		super(OrderedStringList, self).__init__(asc)

	def compare(self, v1, v2):
		test_string1 = v1.strip()
		test_string2 = v2.strip()
		if v1 < v2:
			return -1
		elif v1 == v2:
			return 0
		else:
			return +1
