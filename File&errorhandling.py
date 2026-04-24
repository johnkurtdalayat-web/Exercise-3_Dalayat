def main():
    try:
        # Ask the user to enter username and age
        username = input("Enter username: ")
        age = input("Enter age: ")

        # Convert age to integer to identify possible errors
        age = int(age)

        # Save the data if valid
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        # Display all saved users from the file
        print("\nAll saved users:")
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                print(user.strip())

    except ValueError:
        print("Error: Age must be a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("System complete.")

if __name__ == "__main__":
    main()                                                                                           