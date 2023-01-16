class Tree:
    """
    Represents tree
    """

    def __init__(self,data) -> None:
        """
        Initialization of tree
        """
        self.data = data
        self.parent = None
        self.children=[]
    
    def add_child(self,data)->None:
        """
        Add child to tree
        """
        self.children.append(data)
        data.parent = self
    
    def print_tree(self):
        """
        Prints tree
        """
        indent = " " * self.get_depth() * 4
        print(f"{indent} -> {self.data}")
        
        for child in self.children:
            child.print_tree()
    
    def get_depth(self):
        level = 0
        parent = self.parent
        while parent:
            level+=1
            parent = parent.parent
        return level


t = Tree('Electronics')

laptop = Tree('Laptop')
mac_book = Tree('Macbook')
surface = Tree('Surface')
think_pad = Tree('Think pad')
laptop.add_child(mac_book)
laptop.add_child(surface)
laptop.add_child(think_pad)

cell_phone = Tree('Cell Phone')
tv = Tree('Television')

t.add_child(laptop)
t.add_child(cell_phone)
t.add_child(tv)

t.print_tree()

