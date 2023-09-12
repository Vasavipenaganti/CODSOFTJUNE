import random
import string

def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter desired length of the password: "))

    print("Select complexity level:")
    print("1. Low (Letters only)")
    print("2. Medium (Letters and Numbers)")
    print("3. High (Letters, Numbers, and Special Characters)")
    
    complexity = input("Enter complexity level (1/2/3): ")

    generated_password = generate_password(length, complexity)

    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
