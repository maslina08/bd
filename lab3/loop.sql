DECLARE
    athletes_id             athletes.id%TYPE;
    athletes_name           athletes.name%TYPE;
    athletes_nationality    athletes.nationality%TYPE;
    athletes_sex            athletes.sex%TYPE;
    athletes_height         athletes.height%TYPE;
    athletes_weight         athletes.weight%TYPE;
    athletes_sport          athletes.sport%TYPE;
    athletes_gold           athletes.gold%TYPE;
    athletes_silver         athletes.silver%TYPE;
    count_count                   INTEGER := 20;
BEGIN  
    athletes_name := 'name';       
    athletes_nationality := 'nationality';
    athletes_sex := 'male';             
    athletes_sport :=  'sport';
    
    FOR i IN 1..count_count LOOP
        INSERT INTO athletes (
            athletes.id,    
            athletes.name,           
            athletes.nationality,
            athletes.sex,          
            athletes.height,         
            athletes.weight,        
            athletes.sport,          
            athletes.gold,           
            athletes.silver
        ) VALUES (
            i,
            TRIM(athletes_name) || i,
            TRIM(athletes_nationality) || i,
            athletes_sex,
            i,
            i,
            TRIM(athletes_sport) || i,
            i,
            i
        );
 
    END LOOP;
 
END;