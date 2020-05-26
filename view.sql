CREATE OR REPLACE VIEW athl_inf AS
    SELECT
        nationality,
        gold,
        silver,
        sport,
        sex
    FROM
        athletes;
