create or replace procedure create_user
(user_name IN varchar2 , u_password IN varchar2)
    IS
    stmt varchar(150);
    user_name_upper varchar(30) := UPPER(user_name) ;
    userexist integer;
BEGIN
    select count(1) into userexist from DBA_USERS where username = user_name_upper;
    if (userexist = 0) then
        stmt := 'create user ' || user_name_upper || ' identified by ' || u_password;
        EXECUTE IMMEDIATE ( stmt );
        stmt := 'grant create session to ' || user_name_upper ;
        EXECUTE IMMEDIATE ( stmt );
        stmt := 'alter user data_owner quota unlimited on ' || user_name_upper || '_TBS';
        DBMS_OUTPUT.PUT_LINE(CONCAT(user_name_upper, ' created  successfully'));
    else
        DBMS_OUTPUT.PUT_LINE(CONCAT(user_name_upper, ' already exists'));
    end if;
END;