select name from (
	select rtrim(fares_jan18.station) as name, 
	sum(fares_jan18.ff) as 1ff, 
	sum(fares_feb1.ff) as 2ff
	from fares_jan18 
	inner join fares_feb1 
	on fares_jan18.remote = fares_feb1.remote 
	group by name) as foo 
where 1ff-2ff>1000;