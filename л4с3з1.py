class MyList:
    def __init__(self, initial_data=None):
        self.data = initial_data if initial_data is not None else []

    def append(self, item):
        self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
        else:
            print(f"{item} not found in the list.")

    def get_length(self):
        return len(self.data)

    def get_element_at_index(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print(f"Index {index} is out of range.")

    def clear(self):
        self.data = []


my_list = MyList([1, 2, 3, 4, 5])

my_list.append(6)
print("List after appending 6:", my_list.data)

my_list.remove(3)
print("List after removing 3:", my_list.data)
print("Length of the list:", my_list.get_length())

element_at_index = my_list.get_element_at_index(2)
print("Element at index 2:", element_at_index)

my_list.clear()
print("List after clearing:", my_list.data)


