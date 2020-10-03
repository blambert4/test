class linkedlist:
	def __init__(self, value, nextnode = None):
		self.value = value
		self.nextnode = nextnode

node1 = linkedlist("12")
node2 = linkedlist("13")
node3 = linkedlist("14")

node1.nextnode = node2
node2.nextnode = node3

def print_body():
	currentnode = node1
	while True:
		print(currentnode.value, "->")
		if currentnode.nextnode is None:
			break
		currentnode = currentnode.nextnode
				
print_body()