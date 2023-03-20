DECLARE @myxml XML
SET @myxml = '<Shopping ShopperName="Clement">
<ShoppingTrip ShoppingTripID= "L1">
	<item Cost="3">Bananas</item>
	<item Cost="5">Appless</item>
	<item Cost="10">Cherries</item>
</ShoppingTrip>
<ShoppingTrip ShoppingTripID="L2">
	<item>Emeralds</item>
	<item>Diamonds</item>
	<item>Saphires</item>
</ShoppingTrip>
</Shopping>'
SET @myxml.modify('replace value of (/Shopping/ShoppingTrip[1]/Item[3]/@Cost)[1] with "12"')

SELECT @myxml

--FLWOR:
--for and return:
DECLARE @myxml XML
SET @myxml = '<Shopping ShopperName="Clement">
<ShoppingTrip ShoppingTripID= "L1">
	<item Cost="3">Bananas</item>
	<item Cost="5">Appless</item>
	<item Cost="10">Cherries</item>
</ShoppingTrip>
<ShoppingTrip ShoppingTripID="L2">
	<item>Emeralds</item>
	<item>Diamonds</item>
	<item>Saphires</item>
</ShoppingTrip>
</Shopping>'
SELECT @myxml.query('for $ValueRetrived in /Shopping/ShoppingTrip/item
				  return concat(string($ValueRetrived),";")')

--where, order by, return

DECLARE @myxml XML
SET @myxml = '<Shopping ShopperName="Clement">
<ShoppingTrip ShoppingTripID= "L1">
	<item Cost="3">Bananas</item>
	<item Cost="5">Appless</item>
	<item Cost="10">Cherries</item>
</ShoppingTrip>
<ShoppingTrip ShoppingTripID="L2">
	<item>Emeralds</item>
	<item>Diamonds</item>
	<item>Saphires</item>
</ShoppingTrip>
</Shopping>'
SELECT @myxml.query('for $ValueRetrived in /Shopping/ShoppingTrip/item
					where $ValueRetrived >= 4
					order by ($ValueRetrived)/@Cost
				  return concat(string($ValueRetrived),";")')

--nodes(Shredding a variable):

DECLARE @myxml XML
SET @myxml = '<Shopping ShopperName="Clement">
<ShoppingTrip ShoppingTripID= "L1">
	<item Cost="3">Bananas</item>
	<item Cost="5">Appless</item>
	<item Cost="10">Cherries</item>
</ShoppingTrip>
<ShoppingTrip ShoppingTripID="L2">
	<item>Emeralds</item>
	<item>Diamonds</item>
	<item>Saphires</item>
</ShoppingTrip>
</Shopping>'
SELECT  tbl.col.value('.', 'varchar(50)') AS item
		,tbl.col.value('@Cost', 'varchar(50)') AS Cost
into tblxml
FROM @myxml.nodes('/Shopping/ShoppingTrip/item') as tbl(col)

SELECT * FROM tblxml

DROP TABLE tblxml


