misc=(10, 5.0, True, ['red','white','black'], 0,1,2,3)
print(len(misc))
print(misc[2])
print(misc)

try:
    misc[2]='False'
except TypeError:
    print('Tuples are immutable')

print(type(misc))

for item in misc:
    print(item)

bools=True,0,False,1
print(bools)
print(type(bools))

