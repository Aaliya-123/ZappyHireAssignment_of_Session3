from utils import create, retrieve, update, delete


def main():
    while True:
        print("\n1. Create a District")
        print("2. Retrieve a District")
        print("3. Update a District")
        print("4. Delete a District")
        print("5. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            name = input("\nEnter district name: ")
            create({"name": name})
        elif choice == "2":
            id = int(input("\nEnter district id: "))
            district = retrieve(id)
            if district:
                print(district)
            else:
                print("\nDistrict not found!")
        elif choice == "3":
            id = int(input("\nEnter district id: "))
            new_name = input("\nEnter new name: ")
            update(id, new_name)
        elif choice == "4":
            id = int(input("\nEnter district id: "))
            delete(id)
        elif choice == "5":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()
