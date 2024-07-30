import re

def check_password_strength(password):

    strength = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
 
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
   
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    if strength == 5:
        strength_rating = "Very Strong"
    elif strength == 4:
        strength_rating = "Strong"
    elif strength == 3:
        strength_rating = "Moderate"
    elif strength == 2:
        strength_rating = "Weak"
    else:
        strength_rating = "Very Weak"
    
    feedback.append(f"Password Strength: {strength_rating}")
    
    return feedback

password = input("Enter a password to assess its strength: ")
feedback = check_password_strength(password)
print("\n".join(feedback))
