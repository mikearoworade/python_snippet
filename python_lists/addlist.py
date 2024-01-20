# append, insert, extend
names = ["Michael", "Ayodele", "Oluwaseun"]
bio = ["Software Engineer", "Python", "SQL"]

print(names)
names.append("Aroworade")
print(names)
names.insert(2, "Vastcrown")
print(names)

names = ["Michael", "Ayodele", "Aroworade"]
names.extend(bio)
print(names)