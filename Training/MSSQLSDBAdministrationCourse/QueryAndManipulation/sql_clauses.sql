USE AdventureWorks2019
Go
SELECT * FROM Sales.SalesOrderDetail WHERE OrderQty > 20 AND UnitPrice > 100
SELECT * FROM Sales.SalesOrderDetail WHERE OrderQty/2 > 10
ORDER BY OrderQty ASC

SELECT MAX(OrderQty) FROM Sales.SalesOrderDetail
SELECT MAX(UnitPrice) FROM Sales.SalesOrderDetail
SELECT COUNT(*) AS NoOfOrders,ProductID FROM Sales.SalesOrderDetail GROUP BY ProductID ORDER BY NoOfOrders DESC

SELECT * FROM Sales.SalesOrderDetail WHERE UnitPrice >= 3578.27 AND ModifiedDate >= '2012-01-01 00:00:00' ORDER BY ModifiedDate DESC
SELECT * FROM Sales.SalesOrderDetail WHERE UnitPrice >= 3578.27 AND Year(ModifiedDate) = '2011'