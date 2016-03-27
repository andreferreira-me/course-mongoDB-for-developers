// Start the mongo shell

mongo

// Execute little piece of Javascript code in mongo shell

for (i = 0; i < 3; i++) print("Hello, MongoDB developer! " + i)

// List of topics about mongo shell

help

// Insert a document and update it

db.names.insert({ name: "André Ferreira" });
db.names.find()
var a = db.names.findOne()
a.name = "Paulo"
a
db.names.save(a)
db.names.find()

// BSON

obj = { "a" : 1, "b" : "hello", "c" : [ "apples", "tomatoes" ]}

NumberInt(1)
NumberLong(1)
new Date()

obj = { "a" : 1, "b" : ISODate("2016-03-27T02:07:11.519Z"), "c" : NumberLong(42)}

// Inserting Docs
