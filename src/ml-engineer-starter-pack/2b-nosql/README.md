# NoSQL

Start database

```bash
docker run --name mongodb -d -p 27017:27017 mongo
docker ps
docker exec -it zc_mongo mongo
mongosh
```

Create sample tables

```js
// Create a collection named students
db.createCollection("students")

// Insert multiple documents into the students collection
db.students.insertMany([
    { name: "John Doe", age: 18, major: "Computer Science" },
    { name: "Jane Smith", age: 19, major: "Mathematics" },
    { name: "Emily Johnson", age: 20, major: "Physics" }
])
```

Query data

```js
db.students.aggregate([{$group: {_id: null, averageAge: { $avg: "$age" }}}])
db.students.aggregate([{$group: {_id: "$major", averageAge: { $avg: "$age" }}}])
```

NoSQL capabilities

```js
db.students.insertOne({
    name: "Michael Brown",
    age: 21,
    major: "Engineering",
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        zip: "12345"
    },
    courses: [
        { courseName: "Calculus", grade: "A" },
        { courseName: "Physics", grade: "B+" },
        { courseName: "Chemistry", grade: "A-" }
    ],
    advisor: {
        name: "Dr. Smith",
        office: "Room 123, Engineering Building"
    }
})

db.students.updateOne({name: "Emily Johnson"}, {"$set": {"courses": {"courseName": "Physics"}}})

db.students.find({ "courses.courseName": "Physics" })
```



