# SQL: 
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
SellStartDate                 StartDate            FormattedStartDate

2002-06-01T00:00:00.0000000   Jun 1 2002 12:00AM   6/1/2002
2002-06-01T00:00:00.0000000   Jun 1 2002 12:00AM   6/1/2002

