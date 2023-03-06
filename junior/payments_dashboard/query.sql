select to_char(date_trunc('month', date), 'MM/DD/YY')::date as time, mode, 
    100 * sum(case when status = 'Confirmed' then 1 else 0 end)/count(status)::real as percents
from new_payments
where mode != 'Не определено'
group by 1, 2
order by 1 asc, 2 asc