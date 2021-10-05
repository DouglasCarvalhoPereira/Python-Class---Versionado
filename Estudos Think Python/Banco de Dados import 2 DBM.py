import dbm

db = dbm.open("Mundos", "c")
db["cleese.png"] = 'Photo of John Cleese.'


for key in db:
    print(key, db[key])

 




