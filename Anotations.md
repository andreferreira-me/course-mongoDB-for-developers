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

doc = { "name" : "Smith", "age" : 30, "profession" : "hacker" }

db      // return the name of the current database

db.people.insert( doc )     // insert a document in the 'people' collection

db.people.find().pretty()

db.people.insert( { "name" : "Ford", "age" : 34, "profession" : "lawyer" } )

// Usign findOne

db.people.findOne({ "name" : "Ford" })  // findOne document where key "name" is equal "Ford"

db.people.findOne({ "name" : "Ford" } , { "name" : true, "_id" : false }) // Show key "name", hidden key "_id"

// Using find

db.people.find()

for (i=0; i<1000; i++) { names=["exam", "essay", "quiz"]; for (j=0; j<3; j++) { db.scores.insert( { "student" : i , "type" : names[j], "score" : Math.round(Math.random()*100) } ); }}

db.scores.find().pretty()

// Query using field selection

db.scores.find( { "type" : "essay" })

db.scores.find( { student : 19 })

db.scores.find( { student : 19 , "type" : "essay" } , { "score" : true , "_id" : false })

// Querying using $gt, $gte, $lt and $lte

db.scores.find({ score : { $gt : 95 }})

db.scores.find({ score : { $gt : 95 , $lte : 98 } , type : "essay" })

// Inequalities on Strings

db.people.insert({ name : "Alice" })
db.people.insert({ name : "Misha" })
db.people.insert({ name : "Alan" })
db.people.insert({ name : "Mike" })
db.people.insert({ name : "John" })
db.people.insert({ name : "Smith" })
db.people.insert({ name : "Paul" })
db.people.insert({ name : "Carlos" })
db.people.insert({ name : "Bob" })

db.people.find({ name : { $lt : "D" }})

db.people.find({ name : { $lt : "D" , $gt : "B" }})

// Using regexes, $exists, $type

db.people.find()

db.people.find({ profession : { $exists : true }})
db.people.find({ profession : { $exists : false }})

db.people.find({ name : { $type : 2 }}) // BSON type

db.people.find({ name : { $regex : "a" }}) // Names wicht contains letter "a"
db.people.find({ name : { $regex : "e$" }}) // Names which ends with letter "e"

db.users.find({ name : { $regex : "q"}, email : { $exists : true } })

// Using $or
