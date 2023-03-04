days = [ 'Monday', 'Tuesday', 'Wednesday' ]
fruits = [ 'banana', 'orange', 'peach' ]
drinks = [ 'coffee', 'tea', 'beer' ]

# zip
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, ": drink", drink, "- eat", fruit)
