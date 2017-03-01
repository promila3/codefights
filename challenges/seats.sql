/*Please add ; after each select statement*/
CREATE PROCEDURE freeSeats()
BEGIN
	
    select fI.id flight_id , (totals - count(purchases.flight_id)) free_seats
    from 
    (select f.flight_id id, sum(p.number_of_seats) totalS 
    from flights f, planes p
    where f.plane_id = p.plane_id
    group by f.flight_id ) as fI LEFT JOIN purchases
    ON fI.id = purchases.flight_id
    group by purchases.flight_id
    order by fI.id;
    


 
END
