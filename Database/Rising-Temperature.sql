select
    Q1.id AS Id
from Weather as Q1
    left join Weather as Q2
    on Q2.recordDate = DATEADD(day, -1, Q1.recordDate)
where
    Q1.temperature >  Q2.temperature 