i = 1
total = 0
while i <= 10:
    total = total + i
    if i % 2 == 0:
        print("i = {0} Total = {1}".format(i, total))
    i = i + 1

print("Final total: ", total)


#who = input("Who are you?")
#
#if who == "dog":
#    print("bark!")
#elif who == "cat":
#    print("Meow!")
#else:
#    print("Nothing")
#
#age = int(input("How old are you?"))
## str to convert int to string.
#if age < 16:
#    print("need to be 16 years old!")
#else:
#    print("you are ok to go!")