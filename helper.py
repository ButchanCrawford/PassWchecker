
years_list = [str(year) for year in range(1500, 2051)]  # List of years from 1500 to 2050 (what is a fitting year range for this)
sequential_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# check for char sequences (CoPilot suggested - need to test this)
def contains_sequential_chars(password, seq_length=3):
    for i in range(len(sequential_chars) - seq_length + 1):
        seq = sequential_chars[i:i + seq_length]
        if seq in password:
            return True
    return False

keyboard_sequences = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "1234567890", "!@#$%^&*()"
]

# check for keyboard sequences (CoPilot suggested - need to test this)
def contains_keyboard_sequence(password, seq_length=3): 
    for seq in keyboard_sequences:
        for i in range(len(seq) - seq_length + 1):
            sub_seq = seq[i:i + seq_length]
            if sub_seq in password.lower():
                return True
    return False

# check for dictionary words (CoPilot suggested - need to test this)
dictionary_words = set()()
def load_dictionary(file_path):     
    global dictionary_words
    with open(file_path, 'r') as f:
        for line in f:
            dictionary_words.add(line.strip().lower())
    for word in dictionary_words:
        dictionary_words.add(word.capitalize())                 
def contains_dictionary_word(password):
    password_lower = password.lower()
    for word in dictionary_words:
        if word in password_lower:
            return True
    return False


