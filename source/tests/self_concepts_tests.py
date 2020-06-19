import self_concepts

c = self_concepts.Concept("name")
print("Concept: " + c.name)

p1 = self_concepts.Property("p1", "v1")
p2 = self_concepts.Property("p2", "v2")
print("p1: " + p1.name + "/" + p1.value)
print("p2: " + p2.name + "/" + p2.value)

c.properties.add(p1)
c.properties.add(p2)

print("...")
for p in c.properties:
    print("Property: " + p.name + "/" + p.value)
    p.name = "new name"
    p.value = "new value"

print("...")
for p in c.properties:
    print("Property: " + p.name + "/" + p.value)
    p.name = "new name"
    p.value = "new value"

print("...")
print("p1: " + p1.name + "/" + p1.value)
print("p2: " + p2.name + "/" + p2.value)


