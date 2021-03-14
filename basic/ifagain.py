i = 1
total = 0
while i <= 100:
    total = total + i
    # i = 1, total = 1
    print("i = {0}, total = {1}".format(i, total))
    i = i + 1
print("final total: {0}".format(total))

while True:
    animal = input("What animal is it? ")
    
    if animal == "dog":
        print("bark")
        print("bark")
    elif animal == "cat":
        print("meow")
        print("meow")
    elif animal == 'bye':
        break
    elif animal == 'con':
        continue
    else:
        print("I don't know you!")

    print('going to next round!')