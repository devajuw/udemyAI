colors = {
    "orange": ["Red","Yellow"],
    "Purple": ["Red","Blue"],
    "Green": ["Yellow","Blue"]
}

unique_colors = {col for color in colors.values() for col in color}
print(unique_colors)