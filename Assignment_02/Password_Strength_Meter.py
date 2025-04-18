import re
import streamlit as st

def check_password_strength(password):
    if not password:
        st.warning("Please enter a password")
        return
        
    score = 0
    progress_text = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
        progress_text.append("✅ Good length")
    else:
        progress_text.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        progress_text.append("✅ Good mix of cases")
    else:
        progress_text.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
        progress_text.append("✅ Contains numbers")
    else:
        progress_text.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        progress_text.append("✅ Contains special characters")
    else:
        progress_text.append("❌ Include at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    # Display all feedback
    for text in progress_text:
        st.write(text)
        
    # Show score progress bar
    st.progress(score/4)
    
    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

st.title("Password Strength Meter")
st.write("Enter your password to check its strength.")
password = st.text_input("Password", type="password")
check_password_strength(password)