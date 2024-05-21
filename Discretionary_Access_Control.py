class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            
    def search(self, x):
        current = self.head
        while current is not None:
            if current.data[0] == x:
                return current
            current = current.next
        return None

    def delete_subject(self, x):
        if self.head is None:
            print("NO records found!")
            return
        if self.head.data[0] == x:
            self.head = self.head.next
            if self.head is None:
                self.last_node = None
            print(f"Subject {x} and its access rights deleted.")
            return
        current = self.head
        while current.next:
            if current.next.data[0] == x:
                current.next = current.next.next
                if current.next is None:
                    self.last_node = current
                print(f"Subject {x} and its access rights deleted.")
                return
            current = current.next
        print(f"Subject {x} not found.")
        
        
def grant(sub, obj, ar):
    existing_node = obj.search(sub)
    if existing_node:
        existing_node.data[1].extend(ar) 
        print("Access right granted successfully.") 
    else:
        obj.append([sub, ar]) 
        print("Access right granted successfully.") 
    print()


def revoke(sub, obj, ar):
    existing_node = obj.search(sub)
    if existing_node:
        for right in ar:
            if right in existing_node.data[1]:
                existing_node.data[1].remove(right)
                print(f"Access right '{right}' revoked successfully.")
            else:
                print(f"Access right '{right}' not found.")
    else:
        print("Subject not found.")

def show(sub, obj):
    print("Access rights are:")
    subject_node = obj.search(sub)
    if subject_node:
        for i in subject_node.data[1]:
            print(i,end=' ') 
    else:
        print("Subject not found.")
    print()
    

def verify(sub, obj,right):
    existing_node = obj.search(sub)
    if existing_node:
        if right in existing_node.data[1]:
            print("Permission Granted.")
             
        else:
            print("Permission Denied")
    else:
        print("Subject not found.")
    print()
    

def show_table(objects):
    print("Access Permission Table:")
    print("{:<10} {:<15} {:<20}".format("Subject", "Object", "Access Rights"))
    for obj_key, obj_list in objects.items():
        obj_name = ""
        if obj_key == 1:
            obj_name = "File-1"
        elif obj_key == 2:
            obj_name = "File-2"
        elif obj_key == 3:
            obj_name = "Process-1"
        elif obj_key == 4:
            obj_name = "Process-2"
        elif obj_key == 5:
            obj_name = "Drive-1"
        elif obj_key == 6:
            obj_name = "Drive-2"
        current = obj_list.head
        while current is not None:
            subject = current.data[0]
            access_rights = ', '.join(current.data[1])
            print("{:<10} {:<15} {:<20}".format(subject, obj_name, access_rights))
            current = current.next


file1 = Linked_List()
file2 = Linked_List()
process1 = Linked_List()
process2 = Linked_List()
drive1 = Linked_List()
drive2 = Linked_List()

objects = {
    1: file1,
    2: file2,
    3: process1,
    4: process2,
    5: drive1,
    6: drive2
}

while True:
    print("1. GRANT\n2. REVOKE\n3. DISPLAY RIGHTS\n4. VERIFICATION\n5. VISUALIZE")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Enter the object on which you want access control: "))
        access_rights = []
        sub = input("Enter SID: ")
        num = int(input("Enter the number of rights you want to grant: "))
        for i in range(num):
            a = input(f"Specify right {i + 1}: ")
            access_rights.append(a)
        obj = objects.get(object_choice)
        grant(sub, obj, access_rights)
        
    elif choice == 2:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Enter the object on which you want access control: "))       
        access_rights = []
        sub = input("Enter SID: ")
        num = int(input("Enter the number of rights you want to revoke: "))
        for i in range(num):
            a = input(f"Specify right {i + 1}: ")
            access_rights.append(a)
        obj = objects.get(object_choice)
        revoke(sub, obj, access_rights)

    elif choice == 3:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Enter the object on which you want access control: "))
        sub = input("Enter SID: ")
        obj = objects.get(object_choice)
        show(sub, obj)
        
    elif choice ==  4:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Enter the object on which you want access control: "))
        sub = input("Enter SID: ")
        right=input('Enter the access right you want to verify:')
        obj = objects.get(object_choice)
        verify(sub, obj,right)
          
    elif choice == 5:
        show_table(objects)
    else:
        print("Invalid choice!!!\n Please enter correct option.")
