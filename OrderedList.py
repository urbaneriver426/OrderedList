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
		if self.len() == 0:
			return None
		else:
			currNode = self.head
			v1Found= False
			v2Found = False
			while ((v1Found is False and v2Found is False) 
				or currNode is not None):
				if currNode.value == v1:
					v1Found = True
				if currNode.value == v2:
					v2Found = True
				currNode = currNode.next
			if v1Found == True and v2Found == True:
				if v1 < v2:
					return -1
				elif v1 == v2:
					return 0
				else:
					return +1
			return None
		# -1 если v1 < v2
		# 0 если v1 == v2
		# +1 если v1 > v2

	def add(self, value):
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
		else:
			currNode = self.head
			prevNode = None
			if currNode.next is not None:
				currNode, prevNode = currNode.next, currNode 
				cont = True
				while cont == True:
					if currNode is not None:
						if (prevNode.value <= value <= currNode.value 
							or prevNode.value >= value >= currNode):
							cont = False
						else:
							currNode, prevNode = currNode.next, currNode
					else:
						cont = False
				if currNode is not None:
					prevNode.next = Node(value)
					currNode.prev = prevNode.next
					prevNode.next.prev, prevNode.next.next = prevNode, currNode
				else:
					self.tail.next = Node(value)
					self.tail.next.prev, self.tail = self.tail, self.tail.next
			else:
				if self.__ascending == True:
					if currNode.value <= value:
						self.tail = Node(value)
						self.head.next, self.tail.prev = self.tail, self.head
					else:
						self.head = Node(value)
						self.head.next, self.tail.prev = self.tail, self.head
				else:
					if currNode.value <= value:
						self.head = Node(value)
						self.head.next, self.tail.prev = self.tail, self.head
					else:
						self.tail = Node(value)
						self.head.next, self.tail.prev = self.tail, self.head

	def find(self, val):
		if self.len() == 0:
			return None
		else:
			currNode = self.head
			while currNode.value != val or currNode is not None:
				currNode = currNode.next
			if currNode is not None:
				return currNode
			else:
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
		pass # здесь будет ваш код

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
