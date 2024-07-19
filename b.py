class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        return None

    seen = set()
    current = head
    seen.add(current.val)
    
    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
array = [3, 5, 3, 7, 8, 5, 10]
linked_list = create_linked_list(array)
print("Original list:")
print_linked_list(linked_list)

linked_list = remove_duplicates(linked_list)
print("List after removing duplicates:")
print_linked_list(linked_list)
