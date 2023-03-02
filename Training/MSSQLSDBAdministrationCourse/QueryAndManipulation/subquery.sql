USE AdventureWorks2019;

SELECT * FROM [Sales].CountryRegionCurrency WHERE CurrencyCode IN (
SELECT CurrencyCode FROM Sales.CountryRegionCurrency WHERE Year(ModifiedDate) = '2008')

SELECT * FROM [Sales].CountryRegionCurrency WHERE CurrencyCode IN (
SELECT CurrencyCode FROM Sales.Currency WHERE Year(ModifiedDate) = '2008')