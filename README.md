# Project description

### This project was implemented in educational purposes only, with technology stack including Bottle web framework, Celery job queue including Redis backend and RabbitMQ broker, PostgresQL, Docker, Docker compose.

This services lets you to divide two integers and get result. If you too lazy to pick numbers, you can get division result of two random integers. Also you can check statistics of how much calculation tasks were performed, and which numbers were involved into operations more often

# Instruction
## Prerequisits
Prior to using this service on your host, you should have Docker installed.

## Getting the copy of this project
`clone https://github.com/geterodyn/docker_web.git`
## Running the code
```cd docker_web.git
docker-compose up -d
```
That's it, you're awesome!
## What's next?
After a while you're able to enter http://127.0.0.1:5005/ into your browser and try to get result of two random integers division and make sure it works. The calculation process is queued in Celery, and the calculation result is cached in database.

# API description

- http://127.0.0.1:5005/ outputs with JSON that contain following information:
  - Random numerator
  - Random denominator
  - Answer or notification message if answer is not in database
  - ID of job in Celery queue
  - Date and time of calculation
  * Examples:
   `curl 127.0.0.1:5005`
   `http :5005`

- http://127.0.0.1:5005/divide/<top:int>/<bottom:int> outputs with JSON that contain following information:
  - Numerator
  - Denominator
  - Answer or notification message if answer is not in database
  - ID of job in Celery queue
  - Date and time of calculation
  * Examples:
   `curl 127.0.0.1:5005/divide/25/5`
   `http :5005/divide/63/17`

- http://127.0.0.1:5005/statistics outputs with JSON that contain following information:
  - number of operations made
  - most frequent numbers in calculations
  - how often these numbers are processed
