import random
import string

# Function to generate a random password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for all character types.")
        return None
    
    # Define character pools
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special = random.choice('@_&.-')
    
    # Pool for the remaining characters
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + '@_&.-'
    
    # Create the password with required characters and random ones for the rest
    password = [uppercase, lowercase, number, special] + [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle to ensure randomness of character positions
    random.shuffle(password)
    
    return ''.join(password)

# Main program
if __name__ == "__main__":
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length (minimum 4): "))
        
        if length < 4:
            print("Please enter a length of at least 4.")
        else:
            # Generate the password and display it
            generated_password = generate_password(length)
            if generated_password:
                print(f"Your random password is: {generated_password}")
    except ValueError:
        print("Please enter a valid number.")
