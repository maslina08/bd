CREATE OR REPLACE VIEW hotel_review_reviewer AS
    SELECT
        nationality,
        gold,
        silver,
        sport,
        sex
    FROM
        athletes;