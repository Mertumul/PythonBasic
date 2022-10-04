# Find the user's body mass index based on the height and weight values you get from the user.

height = float(input("please enter your height(m):"))
weight = float(input("please enter your weight(kg):"))
boddymassindex = weight/(height*height)
print("your boddy mass index is {0}".format(boddymassindex))
