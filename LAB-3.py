#LAB-3
#Removing Duplicate Values
a = [3, 2, 7, 3, 5, 2]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)





#To find whether the linked list has a loop or NOT
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_loop(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  

print("to check if a linked list has a loop", find_loop(node1))




#Time Complexity: N log N
def n_log_n(arr):
    sorted_arr = sorted(arr)
    return sorted_arr
arr = [4, 2, 7, 1, 9, 5]
print("Sorted array:", n_log_n(arr))




#Maximum Sum
def max_sum(arr):
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [1, -3, 4, -2, -1, 6]
print("Maximum sum of an arr:",max_sum(arr) )
