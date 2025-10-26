from strength_analyser import password_strength_analyzer
from been_pwned import is_pwned
from common_attack_patterns import check_for_common_attack_patterns


# --- main program ---

if __name__ == "__main__":
    # User input to choose testing method
    user_input = input("Enter '1' to test a single password, '2' to use the included test list of passwords, or '3' to test passwords from a file: ")  
    while user_input not in ['1', '2', '3']:
        user_input = input("Invalid input. Please enter '1', '2', or '3'")

    if user_input == '1': # Single password test
        pwd = input("Enter a password to test: ")
        check_for_common_attack_patterns(pwd) # Check for common attack patterns
        password_strength_analyzer(pwd) # Analyze password strength
        is_pwned(pwd) # Check if password is found in breaches
    elif user_input == '2': # Test included password list
        test_list = [
            "password", "123456", "qwerty", "letmein","Qa1zxcode*1007", "Qazxcode*1007", "M0N@L1s4", "SoilPlantS001", "P@ssw0rd",
            "admin123!", "BlueCar#7","7vR$k9!tQx","OpenMyAccount$1","m9Gf#2LpV8wQz!s",
            "Tr0ub4dor&3", "S0lar:)(:2024!", "Zebra-42-OpenSky", "Random*Pass#204",
        ]   
        for pwd in test_list: # Iterate through test passwords
            check_for_common_attack_patterns(pwd) # Check for common attack patterns
            password_strength_analyzer(pwd) # Analyze password strength
            is_pwned(pwd) # Check if password is found in breaches
            print("|-------------------------------|")
          
    elif user_input == '3': # Test passwords from a file
        file_path = input("Enter the path to the file containing passwords: ") # Get file path from user
        try: # Open and read the file
            with open(file_path, 'r') as file:
                for line in file:
                    pwd = line.strip() # Remove whitespace/newline characters
                    if pwd:  # Avoid empty lines
                        check_for_common_attack_patterns(pwd) # Check for common attack patterns
                        password_strength_analyzer(pwd) # Analyze password strength
                        is_pwned(pwd) # Check if password is found in breaches
                        print("|-------------------------------|")
        except FileNotFoundError: #Handle file not found error
            print(f"File not found: {file_path}")
   




