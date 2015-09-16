class node:
	def __init__(self, data, nxt = None):
		self.data = data
		self.next = nxt
	
class link_list:	
	def __init__(self, head):
		self.head = head		
	'''def ll_add(self, nod):
		self.tail.next = nod
		self.tail = nod'''

n1 = node(5)
n2 = node(2)
n3 = node(4)

n1.next = n2
n2.next = n3
n3.next = n2

ll = link_list(n1)

hashmap = dict()

h = n1

flag = True
while flag:
	if h in hashmap:
		print h.data
		flag = False
	else:
		hashmap[h] = 1
		h = h.next
