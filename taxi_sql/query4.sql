select name as station_with_largest_increase from (
	select rtrim(fares_jan18.station) as name,
	sum(fares_feb1.ff)-sum(fares_jan18.ff) as increase
	from fares_jan18 
	inner join fares_feb1 
	on fares_jan18.remote = fares_feb1.remote 
	group by name 
	order by increase desc) as foo 
limit 1;