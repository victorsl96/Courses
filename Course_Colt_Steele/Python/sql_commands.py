import sqlite3
conn = sqlite3.connect("books.db")
c = conn.cursor()

# CREATING A TABLE------------------------------------------------------

#c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# INSERTING DATA--------------------------------------------------------

# people = [
# 	("Roald", "Amundsen", 5),
# 	("Rosa", "Parks", 8),
# 	("Henry", "Hudson", 7),
# 	("Neil", "Armstrong", 7),
# 	("Daniel", "Boone", 3)]

# for person in people:
# 	c.execute("INSERT INTO friends VALUES (?,?,?)", person)

#FORMS OF SELECTING-----------------------------------------------------
#c.execute("SELECT * FROM friends")
#c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
print(c.execute("SELECT * FROM books").text)

# ITERATION RETURNS VALUES--------------------------------
#for result in c:
#	print(result)

#ITERATION RETURNS A LIST OF TOUPLES WITH THE VALUES------
#print(c.fetchall())

#print(c.fetchone())

conn.commit()
conn.close()