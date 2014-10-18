SELECT RTRIM(fares_jan18.station) AS `name`, SUM(fares_feb1.7d-fares_jan18.7d) AS ` diff_7d`,SUM(fares_feb1.30d-fares_jan18.30d) AS ` diff_30d`
FROM fares_jan18
	INNER JOIN fares_feb1
		ON fares_feb1.remote=fares_jan18.remote
	LEFT JOIN stations
		ON stations.name=fares_jan18.station
WHERE stations.line='Broadway'
GROUP BY `name`
ORDER BY `name`