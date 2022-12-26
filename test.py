a = "m a r y us."
new_a = ""
for char in range(len(a) - 1, -1, -1):
    if a[char] == " " or a[char] == ".":
        pass
    else:
        new_a += a[char]

print(new_a)
