SELECT RTRIM(fares_jan18.station) AS `name`, SUM(fares_feb1.ff-fares_jan18.ff) AS `diff_feb1_jan18`
FROM fares_jan18
	INNER JOIN fares_feb1
		ON fares_feb1.remote=fares_jan18.remote
	LEFT JOIN stations
		ON stations.name=fares_jan18.station
WHERE stations.line='Broadway'
GROUP BY `name`
ORDER BY `name`