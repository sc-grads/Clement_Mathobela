SELECT SYSDATETIME()
SELECT SYSDATETIMEOFFSET()
SELECT SYSUTCDATETIME()


declare @mydate as datetime = '2023-03-13 16:20:19.563'
select 'The date and time is: ' + convert(nvarchar(20),@mydate,104) as MyConvertedDate
go
declare @mydate as datetime = '2023-03-13 16:20:19.563'
select cast(@mydate as nvarchar(20)) as MyCastDate