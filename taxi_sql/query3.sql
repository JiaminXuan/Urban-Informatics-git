select avg(2ff-1ff) as broadway_ff_avg_diff from (
    select rtrim(fares_jan18.station) as name,
    sum(fares_jan18.ff) as 1ff, 
    sum(fares_feb1.ff) as 2ff,
    stations.line as station_name
    from fares_jan18 
    inner join fares_feb1 on fares_jan18.remote = fares_feb1.remote 
    inner join stations on fares_jan18.station=stations.name
    group by name ) as foo
where station_name='Broadway';
