class stack:
	def __init__(self):
		self.stack = []
	def push(self, data):
		self.stack.append(data)
	def pop1(self):
		return self.stack.pop()

class myqueue:
	def __init__(self):
		self.st1 = stack()
		self.st2 = stack()
	def enqueue(self, data):
		self.st1.push(data)
	def dequeue(self):
		if len(self.st2.stack)==0:
			for i in range(len(self.st1.stack)):
				self.st2.push(self.st1.pop1())
		return self.st2.pop1()

x = raw_input("Enter elements to be added to queue:")

temp = x.split()

que = myqueue()
for i in temp:
	que.enqueue(i)

print "1st element dequeued: " + que.dequeue()

print "2nd element dequeued: " + que.dequeue()
print "3rd element dequeued: " + que.dequeue()

x = raw_input("Enter more elements for your queue:")

for i in x.split():
	que.enqueue(i)

print "4th element dequeued: " + que.dequeue()
print "5th element dequeued: " + que.dequeue()
print "6th element dequeued: " + que.dequeue()
print "7th element dequeued: " + que.dequeue()


