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
### NULL

MySQL uses three-valued logic -- TRUE, FALSE and UNKNOWN. Anything compared to NULL evaluates to the third value: UNKNOWN. That “anything” includes NULL itself! That’s why MySQL provides the IS NULL and IS NOT NULL operators to specifically check for NULL.

LeetCode Ex: 
```
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
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


