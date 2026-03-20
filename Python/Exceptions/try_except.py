chai_menu = {"masala":30, "ginger":40}
try:
    chai_menu["elaichi"]
except KeyError:
    print("The Key is Unavailable")
    