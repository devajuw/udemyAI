value=13
if remainder := value % 2:
    print(f"{value} is odd")
    
available_sizes = ["S", "M", "L"]
if (available_size := input("Enter your req sizes: ")) in available_sizes:
    print(f"Size {available_size} is available YAYY!!")
else:
    print(f"Size {available_size} is not available")