ids={11,12,13,14,14,15,16,16,17,18,18}
print(ids)

try:
    print(ids[2])
except TypeError:
    print('Items in a set are not ordered! So yoy cannot use index')

print(len(ids))

for item in (ids):
    print(item)

duplicates=['I','I','You','You','We','We','Us','Us']
print(set(duplicates))
print(sorted(set(duplicates)))

bools={True,1,False,0}
print(bools)