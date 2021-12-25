a = "henry"
b = 12
c = 12.6666
d = True

print(type(d))


# STRING

e = list(range(12))
# print(e)

for i in range(12):
    pass


f = {
    "name": "Rama",
    "age": 36,
    "job": "Developer"
}
print(f.values())
for i, k in f.items():
    if k == 36:
        print(i)

# print(f.get("nami", "This key doesn't exists."))

# for i in f.values():
#     print(i)

g = [1, 2, 5, 4, 6]
g.sort()
z = sorted(a)
a_string = "".join(z)


print(sorted(g, reverse=True))
print(g)
print(sorted(a))
print(a_string)
