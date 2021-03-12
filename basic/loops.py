# define a list:
alist = ["a", "b", 12, 34, 
  [2, 3, 4, "aaaa", "bbbb"]
]

print("length of a list: ",
len(alist))

# how to access items in a list.
print("First Item: ", alist[0])
print("4th Item: ", alist[3])
print("Last Item: ", alist[-1])
print("The first item of the last item for list {0}: {1}".format(alist, alist[4][0]))
print("The second item of the last item for list {0}: {1}".format(alist, alist[4][1]))