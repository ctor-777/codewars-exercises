class node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def next_node(self, next):
        self.next = next
    

class linked_list:
    def __init__(self):
        self.nodes = []
        self._i = 0
        pass

    def add_node(self, value):
        
        
        if self._i == 0:
            self._temp = node(value)
            self.nodes.append(self._temp)
            self._i += 1
        else:
            self._temp = node(value)
            self.nodes.append(self._temp)
            self.nodes[self._i - 1].next = self.nodes[self._i]
            self._i += 1
    
    def len(self):
        return len(self.nodes)


def len_ll(head):
    i = 1
    while True:
        if head.next != None:
            i += 1
            head = head.next
        else:
            break
    return i

    



if __name__ =="__main__":
    head = node(1)
    node2 = node(2)
    node3 = node(3)
    node4 = node(4)
    
    head.next_node(node2)
    node2.next_node(node3)
    node3.next_node(node4)
    
    l = len_ll(head)
    print(l)


"""     ll = linked_list()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
"""
""" print(ll.len()) """