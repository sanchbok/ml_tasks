select distinct day, wau
from (
    select toDate(timestamp) as day, user_id, 
        count(distinct user_id) over(order by day range between 6 preceding and current row) as wau
    from default.churn_submits
)