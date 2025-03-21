import string

passw = list(input("Enter your password "))
strength = 0

# Mininmum length should be more than or equal to 8.
def minimum_length():
 if len(passw) >= 8:
    return True     
 else:
    return False 
if minimum_length() == True:
    strength += 1    


# Must contain a special character.
def speacial_char():
    return any(char in string.punctuation for char in passw)
if speacial_char() == True:
    strength += 1

# Atleast 1 character must be of upercase
def upercase():
    return any(char.isupper() for char in passw)
if upercase() == True:
    strength += 1   

# Atleast 1 character must be of lowercase
def lowercase():
    return any(char.islower() for char in passw)
if lowercase() == True:
    strength += 1 

# Must have atleast 1 number
def num_1():
    return any(char.isdigit() for char in passw)
if num_1() == True:
    strength += 1

def feedback():
    print("Feedback:- ")
    if strength == 5:
        print("Strong ! ")
    elif strength >= 3:
        print("Medium ! ")
    else:
        print("Weak ! ")        
def main():
    print ("Improvements:- ")
    if minimum_length() and speacial_char() and upercase() and num_1() == True:
        print("Your Password include all important factors it does not need improvement ")

    elif minimum_length() == False:
        print("Your password is too short add atleast 8 or more character ")

    elif speacial_char() == False:
        print("Your password does not contain any special character. Password should contain atleast one special character ")     
    
    elif upercase() == False:
        print("Your password should contain atleast one uppercase letter ")

    elif lowercase() == False:
        print("Your password should contain atleast one lowercase letter ")        

    elif num_1() == False:
        print("Your password must contain one digit ")

    elif minimum_length() and speacial_char() and upercase() and num_1() == False:
        print("Please make your password more strong ")        

    else:
        print("Your password is weak ")

feedback()
main()    