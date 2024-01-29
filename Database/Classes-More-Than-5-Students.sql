select
    Courses.class
from
    Courses
group by
    class    
having
    COUNT(Courses.student) >= 5