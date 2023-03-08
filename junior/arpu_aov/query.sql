select date(date_trunc('month', date)) as time, sum(amount)/count(distinct email_id) as arppu,
    sum(amount)/count(distinct id) as aov
from new_payments
where status = 'Confirmed'
group by 1
order by 1