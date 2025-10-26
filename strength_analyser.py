#!/usr/bin/env python3
from common_attack_patterns import check_for_common_attack_patternsV2




# password_strength_analyzer checks the strength of a given password and outputs a strength rating.
def password_strength_analyzer(password):
    attack_pattern_count = check_for_common_attack_patternsV2(password) # Get number of attack patterns found

    password_score = 0 - attack_pattern_count# Default password score - number of attack patterns found ( attack pattrens in reduces total score)
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


    # Rating based on total score, also provides tips for improving weak / very eak passwords
    if password_score <= 4: # Very Weak
        print(" Password is Very Weak") 
        if length < 8:
            tip_count += 1
            print(f"Tip {tip_count}: Password length should be 8 characters or more")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_lower:
            tip_count += 1
            print(f"Tip {tip_count}: Include Lowercase characters")
        if not has_symbol:
            tip_count += 1
            print(f"Tip {tip_count}: include special characters")
        if not has_digit:
            tip_count += 1
            print(f"Tip {tip_count}: Include numbers")
      
    elif password_score <= 5: # Weak
        print(" Password is Weak") 
        if length < 8:
            tip_count += 1
            print(f"Tip {tip_count}: Password length should be 8 characters or more")
        if not has_upper:
            tip_count += 1
            print(f"Tip {tip_count}: Include Uppercase characters")
        if not has_lower:
            tip_count += 1
            print(f"Tip {tip_count}: Include Lowercase characters")
        if not has_symbol:
            tip_count += 1
            print(f"Tip {tip_count}: Include special characters")
        if not has_digit:
            tip_count += 1
            print(f"Tip {tip_count}: Include numbers")
       
    elif password_score <= 7: # Strong
        print(" Password is Strong") 
    else: # Very Strong
        print(" Password is Very Strong") 
       



