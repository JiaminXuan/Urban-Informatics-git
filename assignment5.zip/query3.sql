SELECT stations.lat as lat, stations.lng as lng, SUM(fares_jan18.ff) AS `ff`
FROM stations
INNER JOIN fares_jan18
ON stations.name=fares_jan18.station
WHERE stations.line='Broadway'
GROUP BY stations.lat
ORDER BY `ff` DESC