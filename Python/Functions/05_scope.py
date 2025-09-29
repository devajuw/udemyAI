def main():
    color = "Orange"
    def colors():
        nonlocal color # GLOBAL puts the value globaly only outside all of the funcs
        color = "red"
    colors()
    print(color)
main()
