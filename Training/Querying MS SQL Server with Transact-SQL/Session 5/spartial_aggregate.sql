
SELECT EmployeeNumber,sum(aMOUNT) OVER(PARTITION BY EmployeeNumber ORDER BY) AS TotalAmount From tblTransaction
ORDER BY EmployeeNumber
--
CREATE TABLE tblGeom
(GXY geometry,
Description VARCHAR(30),
IDtblGeom INT CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(1,1))

INSERT INTO tblGeom
VALUES (geometry::STGeomFromText('POINT (3 4)',0),'First point'),
	   (geometry::STGeomFromText('POINT (4 6)',0),'Second point'),
	   (geometry::STGeomFromText('MULTIPOINT (3 4),(2 3),(3 4)',0),'First point')

SELECT IDtblGeom,GXY.STGeometryType()  AS MyType
,GXY.STStartPoint().ToString() AS StartingPoint
,GXY.STEndPoint().ToString() AS EndingPoint
,GXY.STNumPoints() AS NumberPoint
 FROM tblGeom

 DECLARE @g AS GEOMETRY
 DECLARE @h AS GEOMETRY

 SELECT @g = GXY FROM tblGeom WHERE IDtblGeom = 1
 SELECT @h = GXY FROM tblGeom WHERE IDtblGeom = 3

 SELECT @g.STDistance(@h) AS MyDistance

 --
 INSERT INTO tblGeom
 VALUES(geometry::STGeomFromText('LINESTRING (1 1,5 5 )',0),'First line'),
       (geometry::STGeomFromText('LINESTRING (5 1,1 4,2 5,5 1 )',0),'Second line'),
	   (geometry::STGeomFromText('CIRCULARSTRING (1 0,0 1,-1 0,0 -1,1 0 )',0),'Circle')

SELECT * FROM tblGeom