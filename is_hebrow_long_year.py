year = int(input("hebrow year:"))
numbers = [3,6,8,11,14,17,0]
is_long = False
for number in numbers:
    if year % 19 == number:
        is_long = True
if is_long:
    print("long year")
else:
    print("ragular year")
