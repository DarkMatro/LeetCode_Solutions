# Time:  O(n), n is size of Person Table
# Space: O(n)

select
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
from Person as Person
    left join Address as Address
    on Person.personId = Address.personId