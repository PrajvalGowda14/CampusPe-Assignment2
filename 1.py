"""
Question 1: Personal Bio Card
"""


# variables holding personal details
name = "Prajval Gowda"
age = "21 years"
course = "Generative AI"
college = "SJB Institute of Technology"
email = "prajvalmhgowda@gmail.com"


width = 45  # width of the card

# printing details
print("╔" + "═" * (width - 2) + "╗")
print(f"║{'STUDENT BIO CARD':^{width-2}}║")
print("╔" + "═" * (width - 2) + "╗")
print(f"║ Name    : {name}" + " " * (width - 14 - len(name)) + " ║")            #14 is the length of "║ Name    :  ║"   for spacing
print(f"║ Age     : {age}" + " " * (width - 14 - len(age)) + " ║")
print(f"║ Course  : {course}" + " " * (width - 14 - len(course)) + " ║")
print(f"║ College : {college}" + " " * (width - 14 - len(college)) + " ║")
print(f"║ Email   : {email}" + " " * (width - 14 - len(email)) + " ║")
print("╚" + "═" * (width - 2) + "╝")



"""
OUTPUT:

╔═══════════════════════════════════════════╗
║             STUDENT BIO CARD              ║
╔═══════════════════════════════════════════╗
║ Name    : Prajval Gowda                   ║
║ Age     : 21 years                        ║
║ Course  : Generative AI                   ║
║ College : SJB Institute of Technology     ║
║ Email   : prajvalmhgowda@gmail.com        ║
╚═══════════════════════════════════════════╝

"""