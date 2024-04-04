WITH southmost_airport AS (
  SELECT
    timezone,
    MIN(coordinates[1]) AS southmost_latitude
  FROM
    airports_data
  GROUP BY
    timezone
)
SELECT
  ad.airport_code,
  ad.timezone,
  ad.coordinates[1] AS airport_latitude,
  ad.coordinates[1] - sa.southmost_latitude AS latitude_difference
FROM
  airports_data ad
  JOIN southmost_airport sa ON ad.timezone = sa.timezone
ORDER BY
  ad.timezone, latitude_difference;
