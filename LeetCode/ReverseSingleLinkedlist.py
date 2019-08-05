#Reverse a Single Linked list


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        return

class LinkedList_tail:
	def __init__(self):	
		self.head = None
		self.tail = None
		return

	def print_list(self):


		
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def add(self,data):
		node = Node(data)
		if self.head = None
			self.head = node
		else:
			self.tail.next = node
		self.tail = node	
		return
	
	
		
	def length_list(self):
		n = 0
		cur_node = self.head
		while cur_node:
			cur_node = cur_node.next
			n = n+1
		return n

	def reverse_iterative(self):
		prev = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
		self.head = prev
		return self

l = LinkedList_tail()

l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)

l.reverse_iterative()
l.print_list()








