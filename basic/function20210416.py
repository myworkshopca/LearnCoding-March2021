# define a simple function
def greeting(name1, name2):
    msg = "Hello {0} - {1}!".format(name1, name2)
    print(msg)

def greeting_msg(name1, name2):
    msg = "Hello {0} - {1}!".format(name1, name2)
    return msg

#greeting("Sean", "Chen")
m = greeting_msg("Sean", "Chen")
m = m.upper()
print(m)