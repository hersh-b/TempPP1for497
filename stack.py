
#Linked List Nodes
class _StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link



#Stack class
class Stack :
    def __init__( self ):
        self._top = None
        self._size = 0
        
    def peek( self ):
        assert not self.__is_empty__(), "Cannot peek at an empty stack"
        return (self._top.item)
    

    #Pushes item onto top of stack
    def push( self, item ):

        if(self.__is_empty__()): #Stack is empty so we just set this as the top of the stack ez pz
            newNode = _StackNode(item, None)
            self._top = newNode

        else: #There was an object already on the stack, so we set the top's link to the new node and set the top pointer to the new node
            newNode = _StackNode(item, self.peek())
            self._top = newNode

        self._size = len(self) + 1

        return("Pushed")
        



    #Takes the top item off of the stack
    def pop(self):
        if(self.__is_empty__()):
            return("Can't pop, stack empty ;(") # NOOOOOOOOOOO ITS EMPTY D:

        else:
            poppedNode = self.peek()  # Stores the popped node here

            self._top.item = self._top.next # Changes the top to the one under the popped

            self._size = len(self) - 1

            return(poppedNode)


    #Returns the size of the stack
    def __len__(self):
        return(self._size)


    #Returns boolean result of checking if size is 0 (aka empty)
    def __is_empty__(self):
        return(self._size == 0)
    
