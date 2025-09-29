def infinite_colors():
    count = 1
    while True:
        yield f"Color #{count}"
        count=count+1
color = infinite_colors()

for _ in range (6):
    print(next(color))            