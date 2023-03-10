select toStartOfMonth(toDate(buy_date)) as month, avg(check_amount) as avg_check,
    quantilesExactExclusive(0.5)(check_amount)[1] as median_check
from default.view_checks
group by month