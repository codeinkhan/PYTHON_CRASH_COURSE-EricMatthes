#2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.
#     Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed.
#     Then print the name using each of the three stripping functions, 1strip(), rstrip(), and strip().

name="           Codein Khan          ";
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())
