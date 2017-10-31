# find help in ipython
# function?
# function??

# ternary conditional operator
cat = "xinrui" if 2 > 1 else "leilei"
# cat will be called "xinrui" if 2 bigger than 1,otherwise it will be called "leilei"
print(cat)


# elegance
condition = 5 > 3
if condition:
    return True
else:
    return False
# you can use this
return condition


# tuple assignment
(a, b) = (2, 3)  # the numbers must be matched
# trick
a, b = b, a  # swap the values of a and b


# "chain" assignment
x = y = []
# this equals to below(x and y points to the same empty list)
temp = []
x = temp
y = temp
# and is not equals to(x and y points to different empty list)
x = []
y = []

