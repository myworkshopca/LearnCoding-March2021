# define a list.
l = ['a', 'b', 23, 45, "hello",
   [1,2,3,'a']
]

print(l)

print("first item: {0}".format(l[0]))
length = len(l)
print("list length: {0}".format(length))
print("last item: {0}".format(l[length - 1]))
print("last item: {0}".format(l[-1]))

for item in l:
    print(item)

print(l[-1][-2])