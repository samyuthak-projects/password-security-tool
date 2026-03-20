# Password Security Tool

A Python-based password security tool that analyses password strength, estimates crack time, and demonstrates key cybersecurity concepts such as hashing and brute-force attacks.


## Features

- Password strength analysis using regex and scoring
- Estimated crack time based on password complexity
- Secure password hashing using bcrypt
- Password verification system (login simulation)
- Brute-force attack demo (educational use only)


## Security Concepts Demonstrated

- Password strength evaluation
- Brute-force attack principles
- Secure password storage using hashing
- Salting and slow hashing (bcrypt)
- Authentication and verification logic


## Brute Force Demo Notice

This project includes a brute-force simulation for educational purposes only.

The demo is limited to very short passwords to illustrate how attackers attempt to guess passwords. It does NOT target real systems.


## Technologies Used

- Python
- regex (`re` module)
- bcrypt


## How to Run

1. Clone the repository

2. Install dependencies:
    pip install -r requirements.txt

3. Run the program:
    python src/password_checker.py


## Project Purpose

I built this project to explore fundamental cybersecurity concepts and demonstrate how password security works in real systems.

It highlights both defensive techniques (hashing and secure storage) and attacker methods (brute-force simulation), providing a balanced understanding of password security.
