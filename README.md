# RE:Cards Scheduling Service
This is a scheduling service for my [RE:Cards](https://github.com/r3dm1ke/re-cards) project.

### Why
As Firebase does not allow scheduling function invocation in a cron-like fashion
while on free account, I had to resort to this. This is hosted on Heroku and pings a certain Firebase function 
on repeat.

### Technologies used
- Backend
    - Python
    - `schedule` package
- DevOps & Deployment
    - Heroku


