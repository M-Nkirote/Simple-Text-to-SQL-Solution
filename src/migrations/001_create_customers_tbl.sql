CREATE TABLE Customers
(
    customerId UInt32,
    name String,
    firstName String,
    lastName String,
    email String,
    city String,
    zipCode String
)
ENGINE = MergeTree()
ORDER BY customerId;