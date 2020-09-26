class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def __str__(self):
        output = ''
        if self.head is None:
            return "There are no any nodes"
        
        else:
            current = self.head
            
            while current:
                output += f"\nValue:  {current.get_value()}"
                current = current.get_next()
        return output

#Time Complexity: O(n)
#Space Complexity: O(1)
    def reverse_list(self, node, prev):
        if node is None:
            return
        if node is self.head:
            prev = None
        following = node
        while node is not None:
            following = following.get_next()
            node.set_next(prev)
            prev = node
            node = following
        self.head = prev

#--------------recursive reverse function-----------------------------
    def reverse_list_recurcive(self, node, prev): 
        if self.head is None: 
            return   
        # If last node mark it head 
        if node.next_node is None : 
            self.head = node  
              
            # Update next to prev node 
            node.next_node = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = node.next_node
  
        # And update next  
        node.next_node = prev 
      
        self.reverse_list_recurcive(next, node)  
    
   #------------------------------------------     
   

my_list = LinkedList()
my_list.add_to_head(1)
my_list.add_to_head(2)
my_list.add_to_head(3)
my_list.add_to_head(4)
my_list.add_to_head(5)
print(my_list)
my_list.reverse_list(my_list.head, None)
print(my_list)
my_list.reverse_list_recurcive(my_list.head, None)
print(my_list)

