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

db.people.find({ $or: [{ name : { $regex : "e$" }}, { age : {$exists: true}}]})
db.scores.find({ $or: [{ score : { $lt : 50 }}, { score : { $gt : 90 }}] })

// Using $and

db.people.find({ $and: [{ name: { $gt : "C" }}, {name: { $regex : "a"}}] })
db.people.find({ name: { $gt : "C" , $regex : "a"}})  // Same querie without $and

// Querying Inside Arrays

db.accounts.insert({ name : "George", favorites : ["ice cream", "pretzels"]})
db.accounts.insert({ name : "Howard", favorites : ["beer", "pretzels"]})

db.accounts.find().pretty()

db.accounts.find({ favorites: "pretzels"})
db.accounts.find({ favorites: "beer"})
db.accounts.find({ favorites: "beer", name : {$gt : "H"}})
db.accounts.find({ favorites: "pretzels", name : {$gt : "H"}})

// Using $in and $all to querie inside an array

db.accounts.insert({ name: "Irving", favorites: ["beer", "pretzels", "cheese"]})
db.accounts.insert({ name: "John", favorites: ["beer", "cheese"]})

db.accounts.find({favorites : {$all : ["pretzels", "beer"]}})

db.accounts.find({name : {$in : ["Howard", "John"]}})
db.accounts.find({favorites : {$in : ["beer", "ice cream"]}})

db.users.find( { friends : { $all : [ "Joe" , "Bob" ] }, favorites : { $in : [ "running" , "pickles" ] } } )

// Queries with Dot Notation

db.users.insert({ name : "Richard" , email: { work : "richard@10gen.com", personal : "kreuter@example.com"}})
db.users.find({ email: { work : "richard@10gen.com", personal : "kreuter@example.com"} })
db.users.find({ email: { personal : "kreuter@example.com", work : "richard@10gen.com"} }) // Error because the order of the fileds are wrong
db.users.find({ email: { work : "richard@10gen.com"} }) // Error

db.users.find({ "email.work" : "richard@10gen.com"}) // Rigth way

db.catalog.find({ price : { $gt : 10000 }, "reviews.rating" : { $gte : 5 } }) // Problem answer

// Querying, Cursors

cur = db.people.find(); null;
cur.hasNext()
cur.next()
while (cur.hasNext()) printjson(cur.next())

cur = db.people.find(); null;
cur.limit(5); null;

cur = db.people.find(); null;
cur.sort({ name: -1}); null; // Reverse alphabetical order by name

cur = db.people.find(); null;
cur.sort({ name: -1}).limit(3); null;

cur = db.people.find(); null;
cur.sort({ name: -1}).limit(3).skip(2); null

// Counting results

db.scores.find({"type":"exam"});
db.scores.count({"type":"exam"});

// Wholesale Updating of a Document

db.people.find()
db.people.update({name:"Smith"}, {name: "Thompson", salary: 5000}) // Update the docuement but erase other fields in that document
db.people.find()

// Using the $set and $inc Command

db.people.find()
db.people.update({name:"Bob"}, { $set: {name: "André", salary: 7000}})
db.people.update({name:"André"}, { $inc: {salary: 10000}})

db.users.update({ username : "splunker" }, { $set: {country : "RU"}}) // Problem answer

// Using the $unset Command

db.people.find()
db.people.update({name:"Ford"}, { $unset: {profession: 1}})
db.people.find({name: "Ford"})

db.users.update({'username' : 'jimmy'}, {'$unset' : {'interests' : 1}}) // Problem answer

// Using $push, $pop, $pull, $pullAll, $addToSet

db.arrays.insert({_id: 0, a : [1,2,3,4]})
db.arrays.find();
db.arrays.update({_id:0}, {$set : {"a.2" : 5}})

db.arrays.update({_id:0}, {$push : {a : 6}})
db.arrays.update({_id:0}, {$pushAll : {a : [7 , 8, 9]}})

db.arrays.update({_id:0}, {$pop : {a : 1}}) // Remove the element from right of the array
db.arrays.update({_id:0}, {$pop : {a : -1}}) // Remove the element from left of the array

db.arrays.update({_id:0}, {$pull : {a : 5}}) // Remove the value '5' from the array
db.arrays.update({_id:0}, {$pullAll : {a : [2, 4, 7]}}) // Remove the value '2', '4', '7' from the array

db.arrays.update({_id:0}, {$addToSet : {a : 5}})

// Upserts
db.people.find()
db.people.update({ name : "George"}, { $set: { age: 40} }, { upsert : true})

db.people.update({ age : {$gt : 50}}, {$set : { name : "William"}}, { upsert : true})

// Multi-update

db.people.update({}, {$set:{ title : "Dr"}}, {multi : true});

db.scores.update({ score : { $lt : 70}}, {$inc : { score : 20}}, { multi : true}) // Problem answer

// Removing data

db.people.remove({ name : "Alan"})

db.people.remove({ name : { $gt : "M" }})

db.people.remove() // Remove all documents from 'people'

db.people.drop() // Remove the collections 'people'

db.scores.remove({ score : { $lt : 60}}) // Problem answer
