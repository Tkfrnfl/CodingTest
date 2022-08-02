SELECT 
    COUNT(NAME) As count 
    FROM (
    	select name 
    	from ANIMAL_INS 
    	group by name
    )A -- 서브쿼리에 alias 안주면 mysql에선 무조건 에러남
