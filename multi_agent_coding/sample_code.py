#!/usr/bin/env python3
"""
Sample Python code for testing AI analysis capabilities.
This file contains various patterns and potential issues for analysis.
"""

import os
import sys
import requests
import time
from typing import List, Dict, Optional

class UserManager:
    def __init__(self):
        self.users = []
        self.current_user = None

    def add_user(self, username, password):
        # Potential security issue: storing plain text passwords
        user = {
            'username': username,
            'password': password,
            'created_at': time.time()
        }
        self.users.append(user)
        return user

    def authenticate(self, username, password):
        # Inefficient: O(n) search every time
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                return True
        return False

    def get_all_users(self):
        # Potential privacy issue: returning all user data including passwords
        return self.users

def fetch_user_data(user_id):
    # Potential security issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"

    # Potential performance issue: no error handling for network calls
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

def process_large_dataset(data):
    # Performance issue: inefficient nested loops
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] > data[j]:
                result.append((i, j))
    return result

def calculate_fibonacci(n):
    # Performance issue: inefficient recursive implementation
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# Global variables (potential design issue)
global_cache = {}
debug_mode = True

if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("admin", "password123")

    # Hardcoded credentials (security issue)
    if manager.authenticate("admin", "password123"):
        print("Login successful!")

    # Performance test
    large_data = list(range(1000))
    result = process_large_dataset(large_data)

    # Fibonacci test
    fib_result = calculate_fibonacci(35)
    print(f"Fibonacci result: {fib_result}")