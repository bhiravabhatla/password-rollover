select line, position, text
from user_errors
where name = 'BADPROC' and type = 'PROCEDURE'
order by name, type, line, position