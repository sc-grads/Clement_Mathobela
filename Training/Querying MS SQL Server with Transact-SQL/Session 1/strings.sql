------------------------Activity 5:
select [name]+'A' as name
from sys.all_columns

select [name]+ N'Ⱥ' as name
from sys.all_columns

select SUBSTRING([name],2,len([name]))
from sys.all_columns

select SUBSTRING([name],1,LEN([name])-1)
from sys.all_columns