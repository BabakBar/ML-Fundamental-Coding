# SQL
A primary key is defined for each table, and a reference to this key is defined as a foreign key in any related table.
Without diving into the mathematics of set theory, you can think of a set as "a collection of definite, distinct objects considered as a whole." In terms applied to SQL Server databases, you can think of a set as a collection of distinct objects containing zero or more members of the same type. For example, the Customer table represents a set: specifically, the set of all customers. You will see that the results of a SELECT statement also form a set.

## Selecting expressions
```
SELECT ProductID AS ID,
      Name + '(' + ProductNumber + ')' AS ProductName,
  ListPrice - StandardCost AS Markup
FROM Production.Product;
```

ID ProductName Markup
680 HL Road Frame - Black, 58(FR-R92B-58) 372.19
706 HL Road Frame - Red, 58(FR-R92R-58) 372.19

```
SELECT id_num, location
FROM salary_data
WHERE location IN(‘Boston’, ‘Denver’);
```
BETWEEN = Selects the values that are within a given range. Values can be numbers, texts, or dates. begin & end are inclusive

WHERE column_name BETWEEN value1 AND value2

DISTINCT = Used in conjunction with the SELECT clause ,removes duplicate rows from the result set.

```
SELECT location, COUNT(id_num)
FROM salary_data
GROUP BY location;
```

## Work with data types

conversion CAST, CONVERT have a TRY_CONVERT variant that returns NULL for incompatible values.
```
SELECT SellStartDate,
       CONVERT(varchar(20), SellStartDate) AS StartDate,
       CONVERT(varchar(10), SellStartDate, 101) AS FormattedStartDate 
FROM SalesLT.Product;
```
Result

    | SellStartDate               | StartDate          | FormattedStartDate |
    | 2002-06-01T00:00:00.0000000 | Jun 1 2002 12:00AM | 6/1/2002 |
    | 2002-06-01T00:00:00.0000000 | Jun 1 2002 12:00AM | 6/1/2002 | 
             
```
SELECT CAST(ProductID AS varchar(5)) + ': ' + Name AS ProductNameFROM SalesLT.Product; 
```
```
SELECT CONVERT(varchar(5), ProductID) + ': ' + Name AS ProductName
FROM SalesLT.Product; 
```
Note that the results of using CONVERT are the same as for CAST. The CAST function is an ANSI standard part of the SQL language that is available in most database systems, while CONVERT is a SQL Server specific function.
```
SELECT Name, TRY_CAST(Size AS Integer) AS NumericSize
FROM SalesLT.Product;
```
the numeric Size values are converted successfully to integers, but that non-numeric sizes are returned as NULL.

Use TRY_CONVERT to convert the char to an integer. If the conversion fails, NULL will be returned.


PARSE and TRY_PARSE:
convert formatted strings that represent numeric or date/time values.

```
SELECT PARSE('01/01/2021' AS date) AS DateValue,
   PARSE('$199.99' AS money) AS MoneyValue;
   ```

    | DateValue                   | MoneyValue | 
    | 2021-01-01T00:00:00.0000000 | 199.99     | 

STR : converts a numeric value to a varchar. 

```
SELECT ProductID,  '$' + STR(ListPrice) AS Price
FROM Production.Product;
```
Challenge:
Retrieve a list of sales order revisions
The SalesLT.SalesOrderHeader table contains records of sales orders. You have been asked to retrieve data for a report that shows:
The sales order number and revision number in the format () – for example SO71774 (2).
The order date converted to ANSI standard 102 format (yyyy.mm.dd – for example 2015.01.31).
```
SELECT SalesOrderNumber + ' (' + STR(RevisionNumber, 1) + ')' AS OrderRevision,   CONVERT(nvarchar(30), OrderDate, 102) AS OrderDateFROM SalesLT.SalesOrderHeader;
```

### NULL

MySQL uses three-valued logic -- TRUE, FALSE and UNKNOWN. Anything compared to NULL evaluates to the third value: UNKNOWN. That “anything” includes NULL itself! That’s why MySQL provides the IS NULL and IS NOT NULL operators to specifically check for NULL.

LeetCode Ex: 
```
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
```
```
SELECT Name, ISNULL(TRY_CAST(Size AS Integer),0) AS NumericSize
FROM SalesLT.Product;
```
The ISNULL function replaces NULL values with a specified literal value. Sometimes, you may want to achieve the opposite result by replacing an explicit value with NULL. To do this, you can use the NULLLIF function.
```
SELECT Name, NULLIF(Color, 'Multi') AS SingleColor
FROM SalesLT.Product;
```
If there are only two arguments, COALESCE behaves like ISNULL. However, with more than two arguments, COALESCE can be used as an alternative to a multipart CASE expression using ISNULL.

```
SELECT EmployeeID,
      COALESCE(HourlyRate * 40,
                WeeklySalary,
                Commission * SalesQty) AS WeeklyEarnings
FROM HR.Wages;
```

The NULLIF function allows you to return NULL under certain conditions. This function has useful applications in areas such as data cleansing, when you wish to replace blank or placeholder characters with NULL.

NULLIF takes two arguments and returns NULL if they're equivalent. If they aren't equal, NULLIF returns the first argument.

```
SELECT SalesOrderID,
      ProductID,
      UnitPrice,
      NULLIF(UnitPriceDiscount, 0) AS Discount
FROM Sales.SalesOrderDetail;
```

In some scenarios, you might want to compare multiple columns and find the first one that isn't NULL. For example, suppose you want to track the status of a product's availability based on the dates recorded when it was first offered for sale or removed from sale. A product that is currently available will have a SellStartDate, but the SellEndDate value will be NULL. When a product is no longer sold, a date is entered in its SellEndDate column. To find the first non-NULL column, you can use the COALESCE function
find the first non-NULL date for product selling status.

```
SELECT Name, COALESCE(SellEndDate, SellStartDate) AS StatusLastUpdated
FROM SalesLT.Product;
```

If email is not NULL, the email address is returned. If email is NULL, the phone is returned.

```
SELECT CustomerID, COALESCE(EmailAddress, Phone) AS PrimaryContact
FROM SalesLT.Customer;
```

write an SQL to report all customers who never order anything.
Using sub-query and NOT IN clause
```
SELECT name AS Customers 
FROM Customers 
WHERE Customers.id NOT IN
(
    SELECT customerID FROM Orders
);
```

Retrieve customer contact names with middle names if known:
```
SELECT FirstName + ' ' + ISNULL(MiddleName + ' ', '') + LastName AS CustomerNameFROM SalesLT.Customer;
```
SELECT ISNULL(Cellphone, 'None') AS Cellphone FROM Sales.Customer;

### Use CASE to compare values

```
SELECT Name,    
  CASE        
    WHEN SellEndDate IS NULL THEN 'Currently for sale'        
    ELSE 'No longer available'    
  END AS SalesStatus
FROM SalesLT.Product;
```
```
SELECT Name,    
  CASE Size        
    WHEN 'S' THEN 'Small'        
    WHEN 'M' THEN 'Medium'        
    WHEN 'L' THEN 'Large'        
    WHEN 'XL' THEN 'Extra-Large'        
    ELSE ISNULL(Size, 'n/a')    
  END AS ProductSize
FROM SalesLT.Product; 
```

create a query that returns a list of sales order IDs and order dates with a column named ShippingStatus that contains the text Shipped for orders with a known ship date, and Awaiting Shipment for orders with no ship date.
```
SELECT SalesOrderID, OrderDate,    
  CASE        
    WHEN ShipDate IS NULL THEN 'Awaiting Shipment'        
    ELSE 'Shipped'    
  END AS ShippingStatus
FROM SalesLT.SalesOrderHeader;
```

Retrieve primary contact details:

my answer:
```
SELECT CustomerID,        CASE         WHEN EmailAddress IS NULL THEN Phone              ELSE EmailAddress        END AS PrimaryContactFROM SalesLT.Customer;
```
Mic answer:
```
SELECT CustomerID, COALESCE(EmailAddress, Phone) AS PrimaryContact
FROM SalesLT.Customer;
```
