age = input("How old are you?")
print("Age is: {0}".format(age))

print("35 / 2 = ", 35 / 2)
print("35 // 2 = ", 35 // 2)

a = 'Hello Somebody'
print("Repeating \"{0}\" {1} times: {2}".format(a, 4, a * 4))
print("Try the named index placeholder:")
print("Name: {name}, Age: {age}".format(age=100, name="Sean"))


b = "Hello\n\"World\"!"
#print(b + a)
c = """hello
Line one "world"
line two
line 4
"""
#print("original: " + c)

#print("Title:" + c.title())
#print("Capitalize:" + c.capitalize())
#print("Upper cases:" + c.upper())
#print("lower cases:" + c.lower())