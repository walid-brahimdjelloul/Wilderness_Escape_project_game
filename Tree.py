class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_children(self, new_child):
        print('adding', new_child.value)
        self.children.append(new_child)
    
    def remove_children(self, rm_child):
        print(f"Removing {rm_child.value} from {self.value}")
        new_childre = [child for child in self.children if child is not rm_child]
        self.children = new_childre
    
    def tarversing(self):
        start = [self]
        while start:
            current_new = start.pop(0)
            print("current value: ", current_new.value)
            start += current_new.children

root = Tree("CEO")
first_child = Tree("Vice-President")
second_child = Tree("Head of Marketing")
third_child = Tree("Marketing Assistant")

root.add_children(first_child)
root.add_children(second_child)
second_child.add_children(third_child)

root.tarversing()