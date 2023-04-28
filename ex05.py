name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If a add {age}, {height} and {weight} I get {total}.")

# 1.
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If a add {age}, {height} and {weight} I get {total}.")


def inches2cm(inches):
    """Convert inches to cm"""

    return inches * 2.54


inch2cm = inches2cm(float(input('Enter inches: ')))
print(inch2cm)


def lbs2kg(lbs):
    """Convert pounds to kg"""

    return lbs * 0.45359237


lb2kg = lbs2kg(float(input('Enter pounds: ')))
print(lb2kg)
