# 2-7. Stripping Names: 
# Use a variable to represent a person’s name
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions
# lstrip(), rstrip(), and strip().”

name = " emil "
print(f"{name}\n\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}\n\t")
