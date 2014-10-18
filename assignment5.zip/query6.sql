SELECT name AS stop_f
FROM stations
WHERE `lines` LIKE '%F%'
ORDER BY name