select
    Users.name as name,
    sum(Transactions.amount) as balance
from
    Transactions
    inner join Users
    on Transactions.account = Users.account
group by
    Transactions.account
having
    sum(amount) > 10000
