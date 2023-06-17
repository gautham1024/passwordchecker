import re
import streamlit as st
import random
import string
st.title("Password Checker and Generator")

menu = ["Password Checker","Password Generator"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Password Checker":
    def password_check_strength(password):
        length_regex = re.compile(r'.{8,}')
        uppercase_regex = re.compile(r'[A-Z]')
        lowercase_regex = re.compile(r'[a-z]')
        digit_regex = re.compile(r'\d')
        special_char_regex = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

        if not length_regex.search(password):
            return "Weak: Password should be atleast 8 characters long."
        if not uppercase_regex.search(password):
            return "Weak: Password should contain atleast one uppercase letter."
        if not lowercase_regex.search(password):
            return "Weak: Password should contain atleast one lowercase letter."
        if not digit_regex.search(password):
            return "Weak: Password should contain atleast one digit."
        if not special_char_regex.search(password):
            return "Weak: Password should contain atleast one special character."
        
        return "Strong: Password is strong."
    password = st.text_input("Enter the password: ")
    result = password_check_strength(password)
    st.write(result)

if choice == "Password Generator":
    passw_regex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[' + re.escape(string.punctuation) + r'])[\w' + re.escape(string.punctuation) + r']{8,}$')
    passlen = st.number_input("Enter Password Length: ", min_value=8)
    
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(passlen)))
        if passw_regex.match(password):
            break
    
    st.write("Generated Password:", password)