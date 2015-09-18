import datetime

class Node:
	def __init__(self, animal_name):		
		self.an = animal_name
		self.ts = datetime.datetime.now()
		self.next = None

class queue:
	def __init__(self, node):
		self.head = node
		self.tail = node
	def enqueue(self, node):
		self.tail.next = node
		self.tail = self.tail.next
	def dequeue(self):
		temp = self.head
		self.head = self.head.next
		return temp

ll_dog = queue(Node("Dog1"))
ll_dog.enqueue(Node("Dog2"))
ll_dog.enqueue(Node("Dog3"))
ll_dog.enqueue(Node("Dog4"))

ll_cat = queue(Node("Cat1"))
ll_cat.enqueue(Node("Cat2"))
ll_cat.enqueue(Node("Cat3"))
ll_cat.enqueue(Node("Cat4"))

def dequeue_any():
	#dog_time = (ll_dog.head.ts).replace(hour=0, minute=0, second=0, microsecond=0)
	#cat_time = (ll_cat.head.ts).replace(hour=0, minute=0, second=0, microsecond=0)
	#if dog_time > cat_time:
	if ll_dog.head.ts > ll_cat.head.ts:
		return ll_cat.dequeue()
	else:
		return ll_dog.dequeue()

def dequeue_dog():
	return ll_dog.dequeue()
def dequeue_cat():
	return ll_cat.dequeue()

q = dequeue_any()

print "Dequeue any: Name:" + q.an + " Timestamp:" + str(q.ts)

q = dequeue_dog()
print "Dequeue Dog: Name:" + q.an + " Timestamp:" + str(q.ts)


q = dequeue_cat()
print "Dequeue cat: Name:" + q.an + " Timestamp:" + str(q.ts)