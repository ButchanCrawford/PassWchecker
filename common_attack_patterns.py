import enchant
import re


years_list = [str(year) for year in range(1930, 2025)]  # List of years from 1930 to 2025 

# Check for char sequences 
def has_char_sequence(password):
    sequential_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"# Sequential characters string
    password_str = str(password) # Ensure password is a string
    min_seq_len = 3 # Minimum sequence length to detect

    # Check for sequence in both ascending and descending string orders
    for seq in (sequential_chars, sequential_chars[::-1]): 
        for i in range(len(seq) - min_seq_len + 1):
            segment = seq[i:i + min_seq_len]
            if segment in password_str:
                return True
    return False




# Check for keyboard sequences 
def has_keyboard_sequence(password):

    keyboard_sequences = [ # Common keyboard sequences
    "1234567890", "0987654321",
    "!@#$%^&*()", ")(*&^%$#@!",
    "qwertyuiop", "poiuytrewq",
    "asdfghjkl", "lkjhgfdsa",
    "zxcvbnm", "mnbvcxz",
    "qazwsx","qazxsw","wsxedc", "edcrfv", "rfvtgb", "tgbzhn",
    "asdf1234", "qwer1234", "zxcv1234", "a1b2c3d4e5f6g7h890"
    ]

    password_lower = password.lower()  # Normalize to lowercase for matching
    sequence_length = 4  # Minimum sequence length to detect

    # Check each keyboard line
    for seq in keyboard_sequences:
        # Check both forward and backward (to catch "qwerty" or "trewq")
        for direction in (seq, seq[::-1]):
            # Slide through substrings of the sequence
            for i in range(len(direction) - sequence_length + 1):
                segment = direction[i:i + sequence_length]
                if segment in password_lower:
                    return True
    return False



# Check for dictionary words   
def is_dictionary_word(password):
    d = enchant.Dict("en_US")
     #Split the password into chunks of only letters (ignore numbers/symbols)
    words = re.findall(r"[A-Za-z]+", password)

    for w in password:
        # Slide through the word and test every substring of length >= 3
        for i in range(len(w) - 2):
            sub = w[i:]
            if d.check(sub.capitalize()):
                print(f"Found dictionary word in password: {sub}")
                return True
            else:
                print("out")
    return False



# C0mbines all common attack pattern checks
def check_for_common_attack_patterns(password):
    findings = ["Current Passord: ", password] # Initialize findings list ith a header 
    attack_pattern_count = 0 # Attack pattern counter
    
    if is_dictionary_word(password): 
        attack_pattern_count += 1
        findings.append("  dictionary word") # Add finding to list
    if has_keyboard_sequence(password):
        attack_pattern_count += 1
        findings.append("  keyboard sequence") # Add finding to list
    if has_char_sequence(password):
        attack_pattern_count += 1
        findings.append("  character sequence") # Add finding to list
    for year in years_list:
        if year in password:
            attack_pattern_count += 1
            findings.append(f"  contains a year: {year}") # Add finding to list
    if attack_pattern_count > 0:
        findings.insert(2," contains common attack patterns: ")# Add header if patterns found
    print(findings) 
    return findings, attack_pattern_count # Return findings and count of attack patterns found


# Combines all common attack pattern checks (modified to count the number of attack patterns found)
def check_for_common_attack_patternsV2(password):
    attack_pattern_count = 0 # Attack pattern counter: incremented for each pattern found (used in strength analyser to reduce score if a pattern is found)
    if is_dictionary_word(password): 
        attack_pattern_count += 1
    if has_keyboard_sequence(password):
        attack_pattern_count += 2
    if has_char_sequence(password):
        attack_pattern_count += 2
    for year in years_list:
        if year in password:
            attack_pattern_count += 1
    return  attack_pattern_count