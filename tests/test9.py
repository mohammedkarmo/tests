def firstword(name):
    return name.split()[0]
names=['kareem mahmoud','saly ahmad','leeeen naser']
names.sort(key=firstword)
print(names)