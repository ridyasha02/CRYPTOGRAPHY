class AccessControl:
    def __init__(self):
        self.subjects = {}

    def grant_access(self, subject_id, access_rights):
        if subject_id in self.subjects:
            self.subjects[subject_id].extend(access_rights)
        else:
            self.subjects[subject_id] = access_rights
        print("Access rights granted successfully.")
        print()

    def revoke_access(self, subject_id, access_rights):
        if subject_id in self.subjects:
            for right in access_rights:
                if right in self.subjects[subject_id]:
                    self.subjects[subject_id].remove(right)
                    print(f"Access right '{right}' revoked successfully.")
                else:
                    print(f"Access right '{right}' not found.")
        else:
            print("Subject not found.")
        print()

    def display_rights(self, subject_id):
        print("Access rights are:")
        if subject_id in self.subjects:
            for right in self.subjects[subject_id]:
                print(right, end=' ')
            print()
        else:
            print("Subject not found.")
        print()
    
    def verify_access(self, subject_id, right):
        if subject_id in self.subjects:
            if right in self.subjects[subject_id]:
                print("Permission Granted.")
            else:
                print("Permission Denied.")
        else:
            print("Subject not found.")
        print()
    
    def display_access_table(self, objects):
        print("Access Permission Table:")
        print("{:<10} {:<15} {:<20}".format("Subject", "Object", "Access Rights"))
        for obj_key, obj in objects.items():
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
            for subject, rights in obj.subjects.items():
                access_rights = ', '.join(rights)
                print("{:<10} {:<15} {:<20}".format(subject, obj_name, access_rights))

# Initialize objects
file1 = AccessControl()
file2 = AccessControl()
process1 = AccessControl()
process2 = AccessControl()
drive1 = AccessControl()
drive2 = AccessControl()

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
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Select the object for access control: "))
        access_rights = []
        subject_id = input("Enter SID: ")
        num_rights = int(input("Enter the number of rights to grant: "))
        for i in range(num_rights):
            right = input(f"Specify right {i + 1}: ")
            access_rights.append(right)
        obj = objects.get(object_choice)
        obj.grant_access(subject_id, access_rights)
        
    elif choice == 2:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Select the object for access control: "))       
        access_rights = []
        subject_id = input("Enter SID: ")
        num_rights = int(input("Enter the number of rights to revoke: "))
        for i in range(num_rights):
            right = input(f"Specify right {i + 1}: ")
            access_rights.append(right)
        obj = objects.get(object_choice)
        obj.revoke_access(subject_id, access_rights)

    elif choice == 3:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Select the object for access control: "))
        subject_id = input("Enter SID: ")
        obj = objects.get(object_choice)
        obj.display_rights(subject_id)
        
    elif choice ==  4:
        print("1. File-1\n2. File-2\n3. Process-1\n4. Process-2\n5. Drive-1\n6. Drive-2\n")
        object_choice = int(input("Select the object for access control: "))
        subject_id = input("Enter SID: ")
        right = input("Enter the access right to verify: ")
        obj = objects.get(object_choice)
        obj.verify_access(subject_id, right)
          
    elif choice == 5:
        for obj_key in objects:
            objects[obj_key].display_access_table(objects)
    else:
        print("Invalid choice! Please enter a valid option.")
