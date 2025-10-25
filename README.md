# PassWchecker

About
PassWchecker is A simple, password checker that:
•	Rates password strength (Very Weak, Weak, Strong, Very Strong) 
•	Provides actionable tips to improve Very Weak and Weak password
•	Flags common attack patterns such as keyboard sequences, character sequences and years
•	Checks if a password appears in known data breaches via Have I Been Pwned (HIPB) API

Usage:
Run the main program: python passwchecker.py
Upon running the program, the user ill be prompted to select from a series of actions:
1.	Test a single password > enter a single password in the CLI
2.	Test a list of built in passwords > program ill begin analyzing the test list 
3.	Test passwords from a text file > read passwords from a file (one per line).

Requirements
requests 2.31.0
pyenchant 3.2.2
hashlib

Privacy
The HIBP API call never sends your password or full hash—only the first 5 chars of its SHA-1 hash (k-Anonymity model).
