#Array is List in python
class array:
    def __init__(self,data):
        self.data = data
        self.length = len(data)
    
#Add is implemented through append
    def add_value(self,data):
        self.data.append(data)

#Insertion by value and location is done using index
    def insert_value_at(self,location,data):
        self.data.insert(location,data)
    
#Removal by location is done using pop()
    def remove_element_index(self,index):
        self.data.pop(index)

#Removal Lastval is done using pop()
    def remove_last_val(self):
        self.data.pop()

#Extension of list is done using extend    
    def extend(self,data1,data2):
        self.data.extend(data1,data2)

#Removal by value is done using remove
    def remove_by_val(self,data):
        self.data.remove(data)

    def print(self):
        print("Array is:",self.data)
        print("Length is:",self.length)

#Index of a value is found using this
    def search(self,data1):
        return self.data.index(data1)

#Ascending to Descending Order List
    def sort(self):
        return self.data.sort()

#Removes all element of List
    def clear(self):
        return self.data.clear()

if __name__ == "__main__":        
    lst = [1,2,3,4,5]
    b = [6,7,8,9,10]

    a = array(lst)
    a.print()
    print(a.search(4))
    a.print()

