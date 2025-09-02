# class Rectangle : 
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
#     def area (self) :
#         return self.width * self.height
# Rectangle1 = Rectangle(5,6)
# print(Rectangle1.area())


# class Counter : 
#     count = 0
#     def __init__(self):
#         self.count = 0
#     def increament (self):
#         type (self).count +=1
#     def get_count (self):
#         return type (self).count
# count1 = Counter()
# count2 = Counter()
# count1.increament()
# count2.increament()
# print(Counter.count) # prints 2


# class Employee :
#     raise_amount = 1.04
#     def __init__(self,salary) :
#         self.salary = salary
#     def apply_raise (self) :
#         self.salary = self.salary * self.raise_amount
#     @classmethod
#     def set_raise_amount(cls, amount) :
#         cls.raise_amount = amount
# emp1 = Employee(5000)
# emp1.apply_raise()
# print(emp1.salary)  
# Employee.set_raise_amount(1.05)
# emp1.apply_raise()
# print(emp1.salary)  
        
        
# class MathHelper : 
#     @staticmethod
#     def add (a,b):
#         return a + b
#     @staticmethod
#     def multiply (a,b):
#         return a * b
# result1 = MathHelper.add(2,3)
# print(result1) # prints 5
# result2 = MathHelper.multiply(2,3)
# print(result2) # prints 6


# class Student : 
#     def __init__(self, name, grade) :
#         self.name  = name
#         self.__grade  = grade
#     def display (self):
#         return f"the student his name is {self.name} , and his grade is {self.__grade}"
#     def set_grade (self ,grade):
#         self.__grade = grade
#     def get_grade (self):
#         return self.__grade
# student1 = Student("Abdallah" , "A+")
# print(student1.display()) 


# class Animal : 
#     def __init__(self, name) :
#         self.name =  name 
#     def speak (self):
#         pass
# class Dog (Animal) :
#     def speak (self):
#         return "Woof Woof"
#     def fetch (self):
#         return "Dog fetch!"
# dog1 = Dog("Racis")
# print(dog1.speak()) 


# class Flyer :
#     def fly (self):
#         return "I can fly "
# class Swimmer :
#     def swim (self):
#         return "I can swim "
# class Bird (Flyer , Swimmer) :
#     def __init__(self , name):  
#         self.name = name
#     def fly (self):
#         return f"{self.name} can fly "
#     def swim (self):
#         return f"{self.name} can swim "
# bird1 = Bird("Peguin")
# print(bird1.fly()) 
# print(bird1.swim())

# class Vector:
#     def __init__(self, values=None):
#         self.list = values if values is not None else []
#     def __add__(self, other):
#         if len(self.list) == len(other.list):
#             return Vector([self.list[i] + other.list[i] for i in range(len(self.list))])
#         else:
#             raise ValueError("Error, the vectors are not the same size")
#     def __str__(self):
#         return str(self.list)

# vector1 = Vector([1, 2, 3])
# vector2 = Vector([4, 5, 6])

# print(vector1)
# print(vector2)
# print(vector1 + vector2)


# class Shape : 
#     def area (self):
#         pass 
# class Rectangle (Shape) :
#     def __init__(self , length , width):
#         self.length = length
#         self.width = width
#     def area (self):
#         return self.width * self.length
# class Circle (Shape) :
#     def __init__(self , radius ) :
#         self.radius =  radius
#     def area (self):
#         return 3.14 * (self.radius ** 2)
    
    
# def Bubble_sort (A):
#     for i in range (0 , len(A)-1):
#         for j in range (0 , len(A)-i-1):
#             if A[j] > A[j+1]:
#                 A[j] , A[j+1] = A[j+1] , A[j]
#     return A
# print(Bubble_sort([64,34,25,12,22,11,90]))

# def insertion_sort (arr):
#     for i in range (1, len(arr)):
#         for j in range (i-1 , -1 , -1 ):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#     return arr 


# def selection_sort (arr):
#     for i in range (0 , len(arr)-1):
#         min_index = i
#         for j in range (i+1 , len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#             if min_index != i :
#                 arr[i] , arr[min_index] = arr[min_index] , arr[i]
#     return arr


# def Bubble_sort (arr):
#     for i in range (0 , len(arr)-1):
#         for j in range (0 , len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#     return arr
# print(Bubble_sort([64,34,25,12,22,11,90]))


# def insertion_sort (arr):
#     for  i in range (1 , len(arr)-1):
#         for j in range (i-1 , -1 , -1 ):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#     return arr
# print(insertion_sort([64,34,25,12,22,11,90]))


# def selection_sort (arr):
#     for i in range (0 , len(arr)-1):
#         min_index = i
#         for j in range (i+1 , len(arr)):
#             if arr[j] > min_index[i]:
#                 min_index = j 
#             if min_index != i :
#                 arr[i] , arr[min_index] = arr[min_index] , arr[i]
#     return arr
# print(selection_sort([64,34,25,12,22,11,90]))


# def Linear_Search (arr , target):
#     for i in range (0 , len(arr)):
#         if arr[i] == target :
#             return i
#         return -1


# def Binary_Search (arr , low , high , x):
#     if low <= high :
#         mid = low + (high - low ) // 2
#     if arr[mid] == x :
#         return mid 
#     if arr[mid] > x :
#         high = mid -1 
#     elif arr[mid] < x :
#         low = mid + 1
#     else : 
#         return -1


# def factorial (n):
#     if n == 0 :
#         return 1
#     else :
#         return n * factorial (n-1)
# print(factorial(5))


# def Fibonacci (n):
#     if n == 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     else :
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(10))



# def Linear_Search (arr , target):
#     for i in range (0 , len(arr)):
#         if arr[i] == target : 
#             return i 
#     return -1 
# print(Linear_Search([1,2,3,4,5,6,7,8] , 3 ))


# def Binary_Search (arr , low , high , x):
#     if low <= high : 
#         mid = low + (high - low ) // 2
#     if arr[mid] == x : 
#         return mid 
#     elif arr[mid] > x : 
#         high = mid -1
#     else :
#         low = mid + 1



# class Node : 
#     def __init__(self , data):
#         self.data = data
#         self.next = None 
# class LinkedList :
#     def __init__(self):
#         self.head  = None 
#     def insert (self , newelement):
#         newnode =  Node(newelement)
#         newnode.next = self.head
#         self.head = newnode
#     def traverse (self):
#         temp = self.head 
#         while temp != None : 
#             print(temp.data)
#             temp = temp.next
#         print()
#     def insert_at_last (self , newelement):
#         newnode = Node(newelement)
#         if (self.head == None):
#             self.head = newnode
#         else :
#             temp = self.head
#             while(temp.next != None):
#                 temp = temp.next
#         temp.next = newnode
#     def insert_at_position (self , position , newelement):
#         newnode = Node(newelement)
#         if position == 0 :
#             newnode.next = self.head
#             self.head = newnode
#         else :
#             temp = self.head
#             for i in range(position - 1):
#                 temp = temp.next
#                 newnode.next = temp.next
#                 temp.next = newnode
                
                
# class Node : 
#     def __init__(self , data):
#         self.data = data
#         self.next = None
# class LinkedList :
#     def __init__(self):
#         self.head = None 
#     def insert_at_head (self , newelement):
#         newnode  = Node(newelement)
#         newnode.next = self.head
#         self.head = newnode
#     def traverse (self):
#         temp = self.head
#         while (temp != None):
#             print(temp.data)
#             temp = temp.next
#             print()
#     def insert_at_end (self , newelement):
#         newnode = Node(newelement)
#         if (self.head == None):
#             self.head = newnode
#         else :
#             temp = self.head
#             while(temp.next != None):
#                 temp = temp.next
#                 temp.next = newnode
#     def search_element(self, search_value):
#         temp = self.head
#         found = 0
#         i = 0
#         while (temp!= None):
#           i += 1
#           if(temp.data == search_value):
#              found += 1
#              break
#           temp = temp.next
#         if (found == 1):
#              print(search_value, "is found at index = ", i)
#         else:
#              print(search_value, "is not found in the list.")
        
        
# class Stack : 
#     def __init__(self):
#         self.stack = []
#     def push(self, item):
#         self.stack.append(item)
#     def pop (self):
#         if self.isEmpty (self):
#             return "Stack is empty"
#         else :
#             return self.stack.pop()
#     def peek (self):
#         if self.isEmpty (self): 
#             return "Stack is empty"
#         else :
#             return self.stack[-1]
#     def isEmpty (self):
#         return len(self.stack) == 0


# class Queue : 
#     def __init__(self):
#         self.Queue = []
#     def enqueue (self, item):
#         self.Queue.append(item)
#     def dequeue (self):
#         if self.isEmpty (self):
#             return "Queue is empty"
#         else :
#             return self.Queue.pop(0)
#     def peek (self):
#         if self.isEmpty (self):
#             return "Queue is empty"
#         else :
#             return self.Queue[0]
#     def isEmpty (self):
#         return len(self.Queue) == 0

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.length = 0

#     def enqueue(self, element):
#         new_node = Node(element)
#         if self.rear is None:
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self.length += 1

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         temp = self.front
#         self.front = temp.next
#         self.length -= 1
#         if self.front is None:
#           self.rear = None
#         return temp.data

#     def peek(self):
#       if self.isEmpty():
#         return "Queue is empty"
#       return self.front.data


#     def isEmpty(self):
#         return self.length == 0


#     def printQueue(self):
#       temp = self.front
#       while temp:
#         print(temp.data, end=" ")
#         temp = temp.next
#       print()


# class Node : 
#     def __init__(self , data):
#         self.data = data
#         self.right = None 
#         self.left = None 
# def inorder (root):
#     if root is None : 
#         return
#     inorder (root.left)
#     print (root.data , end = " ")
#     inorder (root.right)
# def preorder (root):
#     if root is None : 
#         return 
#     print (root.data , end = " ")
#     preorder(root.left)
#     preorder(root.right)
# def postorder (root):
#     if root is None :
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.data , end = " ")
# def insert (root , key):
#     if root is None : 
#         return Node(key)
#     if root.val == key : 
#         return root
#     if root.val < key :
#         root.right = insert(root.right , key)
#     else : 
#         root.left = insert(root.left , key)
#     return root 
    

# class Node : 
#     def __init__(self , data):
#         self.data = data
#         self.right = None 
#         self.left = None 
# def Level_order_Traversal (root):
#     if root is None :
#         return
#     queue = []
#     queue.append(root)
#     while (len(queue) > 0):
#         print(queue[0].data , end=" ")
#         node = queue.pop(0)
#         if node.left is not None :
#             queue.append(node.left)
#         if node.right is not None :
#             queue.append(node.right)
# def search (root , key ):
#     if root is None or root.key == key :
#         return root
#     if root.key < key :
#         return search(root.right , key)
#     return search(root.left , key )

    