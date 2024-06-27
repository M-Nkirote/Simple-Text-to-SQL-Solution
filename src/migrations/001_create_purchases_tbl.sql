CREATE TABLE Purchases
(
    purchaseId UInt32,
    customerName String,
    productName String,
    quantity UInt8,
    pricePerItem Decimal(10, 2),
    purchaseDate Date,
    totalPurchaseAmount Decimal(10, 2)
)
ENGINE = MergeTree()
ORDER BY purchaseId;
