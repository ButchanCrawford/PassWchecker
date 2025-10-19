#!/usr/bin/env python3
import enchant


# password_strength_analyzer checks the strength of a given password and returns a strength rating.
def password_strength_analyzer(password):
#  account for dictionary ords
#  account for  keyboard alks 
#  account for years range 1500-2050
#  account for sequential characters


    password_score = 0 # Default password score
    tip_count = 0   # Default tip counter

    length = len(password) # Get the length of the password
    has_upper = any(c.isupper() for c in password) # Check for uppercase letters
    has_lower = any(c.islower() for c in password) # Check for lowercase letters
    has_digit = any(c.isdigit() for c in password) # Check for digits / numbers
    has_symbol = any(not c.isalnum() for c in password) # Check for special characters / symbols


    #  Scoring Passords - if criteria met, increase score
    if length >= 8:
        password_score += 1
    if length >= 10: 
        password_score += 2 
    if length >= 15:
        password_score += 3 
    if has_upper:
        password_score += 1
    if has_lower:
        password_score += 1
    if has_lower and has_upper:
        password_score += 1
    if has_digit:
        password_score += 1
    if has_symbol:
        password_score += 1


    # Rating based on total score
    if password_score <= 4:
        print(password,length,"score: ",password_score, "  Very Weak") # Logging usage: should return instead of print
        if length < 8:
            tip_count += 1
            print(f"Tip {tip_count}: Password length should be 8 characters or more")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_symbol:
            tip_count += 1
            print(f"Tip {tip_count}: include special characters")
        if not has_digit:
            tip_count += 1
            print(f"Tip {tip_count}: Include numbers")
      
    elif password_score <= 5:
        print(password,length,"score: ",password_score, "  Weak") # Logging usage: should return instead of print
        if length < 8:
            tip_count += 1
            print(f"Tip {tip_count}: Password length should be 8 characters or more")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_symbol:
            tip_count += 1
            print(f"Tip {tip_count}: include special characters")
        if not has_digit:
            tip_count += 1
            print(f"Tip {tip_count}: Include numbers")
       
    elif password_score <= 7:
        print(password,length, "score: ",password_score, "  Strong") # Logging usage: should return instead of print
    else:
        print(password,length, "score: ",password_score, "  Very Strong") # Logging usage: should return instead of print
       


# --- main program ---
# Determine how user interfaces with program 
password = input("Enter a password to test: ")
rating = password_strength_analyzer(password)
print(f"Password strength: {rating}")
