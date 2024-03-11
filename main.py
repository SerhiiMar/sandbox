arr = [
  123,
  "abc",
  [456, "def"]
  ]
print(f"\n{arr = }")


a = arr[0]
b = arr[1]
c = arr[2]

print(f"\n{a = }\n{b = }\n{c = }")


a += 333
b += "def"
c.append(789)


print(f"\n{a = }\n{b = }\n{c = }")
print(f"\n{arr = }\n")
