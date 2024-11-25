#CIS 103 XY Fundamentals of Programming
#Lab 8 Assignment Stacks and Queues
#Author: Annie Yung
#Date: 11/23/2024

print("Activity 1: Implementing a Stack")

from collections import deque

class CheckoutQueue:
    def __init__(self, service_time):
        self.queue = deque()  # creating a queue of customers
        self.service_time = service_time  # time taken to serve each customer

    def add_customer(self, customer_name):
        self.queue.append(customer_name)

    def serve_customer(self):
        if not self.is_empty():
            customer = self.queue.popleft()  #removing the customer from the front of the queue
            return customer
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def calculate_total_wait_time(self):
        #defining total wait time
        total_wait_time = 0
        customers_served = 0

        while not self.is_empty():
            customer = self.serve_customer()
            if customer:
                wait_time = customers_served * self.service_time
                print(f"Customer {customer} is being served. Wait time: {wait_time} minutes.")
                total_wait_time += wait_time
                customers_served += 1

        return total_wait_time

#defining simulation
def checkout_simulation(customers, service_time_per_customer):
    queue = CheckoutQueue(service_time_per_customer)

    # Adding all customers to the queue
    for customer in customers:
        queue.add_customer(customer)

    # Calculating the total wait time for all customers
    total_wait_time = queue.calculate_total_wait_time()

    print(f"\nTotal wait time for all customers: {total_wait_time} minutes.")

#example
customers = ["James", "Sarah", "Bob", "Diane"]
service_time_per_customer = 5  # 5 minutes per customer

checkout_simulation(customers, service_time_per_customer)

print("Activity 1.2: Matching Parantheses")


def is_balanced(expression):
    #Creating an empty stack
    stack = []

    matching_bracket = {')': '(', '}': '{', ']': '['}

    # Traverse the expression
    for char in expression:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack[-1] != matching_bracket[char]:
                return "Not Balanced"
            stack.pop()

    return "Balanced" if not stack else "Not Balanced"

#Example
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("{[}"))
print(is_balanced("()"))
print(is_balanced("({[()]})"))
print(is_balanced("()[]{}"))
print(is_balanced("[({})]"))

print("Activity 1.3 Convert Infix to Postfix")

def infix_to_postfix(expression):
    # Define operator
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    left_associative = {'+': True, '-': True, '*': True, '/': True, '^': False}

    # Create stack and output list
    stack = []
    output = []

    # Traverse the expression
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   (precedence[char] < precedence.get(stack[-1], 0) or
                    (precedence[char] == precedence.get(stack[-1], 0) and left_associative.get(char, True)))):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

#Examples
print(infix_to_postfix("A*(B+C)"))
print(infix_to_postfix("A+B*C"))
print(infix_to_postfix("(A+B)*(C-D)"))
print(infix_to_postfix("A+B*(C-D)"))
print(infix_to_postfix("A^B^C"))
print(infix_to_postfix("A+(B*C-(D/E^F)*G)*H"))

print("Activity 2.1 Implementing a Queue")

class Queue:
    def __init__(self):
        #Creating an empty deque for the queue
        self.queue = deque()

    def enqueue(self, element):
        # Add an element to the end of the queue
        self.queue.append(element)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.popleft()  # Remove and return from the front of the queue
        else:
            raise IndexError("dequeue from an empty queue")  # Raise error if the queue is empty

    def peek(self):
        # Return the front element without taking it out
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")  # Raise error if the queue is empty

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0


#Example
def test_queue():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Dequeue one element and display the result
    print(f"Dequeued element: {q.dequeue()}")  # Expected output: 10

    # Peek at the front element of the queue
    print(f"Front element after dequeue: {q.peek()}")  # Expected output: 20

test_queue()

print("Activity 2.2 Customer Checkout Simulation")

class CheckoutQueue:
    def __init__(self, service_time):
        # Initialize the queue and the service time per customer
        self.queue = deque()
        self.service_time = service_time  # Time taken to serve each customer

    def add_customer(self, customer_name):
        # Add a customer to the queue
        self.queue.append(customer_name)

    def serve_customer(self):
        # Serve a customer from the queue and return their name
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def calculate_total_wait_time(self):
        # Calculate the total wait time for all customers
        total_wait_time = 0
        customers_served = 0

        while not self.is_empty():
            customer = self.serve_customer()
            if customer:
                wait_time = customers_served * self.service_time
                print(f"Serving {customer}")
                total_wait_time += wait_time
                customers_served += 1

        return total_wait_time

#Defining simulation function
def simulate_checkout(customers, service_time_per_customer):
    queue = CheckoutQueue(service_time_per_customer)

    # Add customers to the queue
    for customer in customers:
        queue.add_customer(customer)

    # Calculate and display the total wait time
    total_wait_time = queue.calculate_total_wait_time()
    print(f"Total wait time: {total_wait_time} minutes.")

#Example
customers = ["John", "Laura", "Charlie", "Diana"]
service_time_per_customer = 5  # Each customer takes 5 minutes

simulate_checkout(customers, service_time_per_customer)


