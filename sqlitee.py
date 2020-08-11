import sqlite3
import main
persons = [
    ("Jan Nowak", 33),
    ("Krzysztof Krawczyk", 74),
    ("Karol Krawczyk", 44),
    ("Maciej Atnczak", 22)
    ]
names = []
ages = []
for item in persons:
    names.append(item[0])
    ages.append(item[1])


# play with dict comprehension to create dict
persons_dict = {k: w for (k, w) in zip(names, ages)}

# sort by last name
persons_dict = main.sort_by_second_word_dict(persons_dict)

# cast persons into dict easy way
print(dict(persons))

print(persons_dict)


# main.sort_by_second_word_dict(dictionary=persons)
con = sqlite3.connect(":memory:")

# Create the table
con.execute("create table person(name, age)")

# Fill the table
con.executemany("insert into person(name, age) values (?, ?)", persons)

# Print the table contents
for row in con.execute("select name, age from person"):
    print(row)

print("I just deleted", con.execute("delete from person").rowcount, "rows")

# close is not a shortcut method and it's not called automatically,
# so the connection object should be closed manually
con.close()
