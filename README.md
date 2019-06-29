# Starnavi

Test assignment for starnavi.io

Object of this task is to create a simple REST API. You have to use Django and Django rest
framework.
Social Network

Basic models:
  * User
  * Post (always made by a user)
Basic features:
  * user signup
  * user login
  * post creation
  * post like
  * post unlike

For User and Post objects, candidate is free to define attributes as they see fit.

Requirements:
  * Token authentication (JWT is prefered)
  * use Django with any other Django batteries, databases etc.
Optional (will be a plus):
  * use clearbit.com/enrichment for getting additional data for the user on signup
  * use emailhunter.co for verifying email existence on signup

Automated bot
Object of this bot demonstrate functionalities of the system according to defined rules.
This bot should read rules from a config file (in any format chosen by the candidate), but
should have following fields (all integers, candidate can rename as they see fit):
  * number_of_users
  * max_posts_per_user
  * max_likes_per_user
Bot should read the configuration and create this activity:
  * signup users (number provided in config)
  * each user creates random number of posts with any content (up to
max_posts_per_user)
  * After creating the signup and posting activity, posts should be liked randomly, posts
can be liked multiple times

Notes
  * emailhunter and clearbit have either free pricing plans or free trial, the candidate can
use their own account if he would like implement the functionality
  * visual aspect of the project is not important, the candidate can create a frontend for
viewing the result, but it is not necessary (will be a plus). Clean and usable REST
API is important
  * the project is not defined in detail, the candidate should use their best judgment for
every non-specified requirements (including chosen tech, third party apps, etc),
however
  * every decision must be explained and backed by arguments in the interview
  * Result should be sent by providing a Git url. This is a mandatory requirement.

### Configuration Backend

Environment variables

```.sh
$ cd docker/django
$ nano .env # See to table environment variables backend
```

### Configuration Bot

Environment variables

```.sh
$ cd docker/bot
$ nano .env # See to table environment variables bot
```

config.ini

if you wanna change configs for bot follow this commands:

```.sh
$ cd starnavi-bot
$ nano config.ini # See to table config.ini
```

### Environment variables backend

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | mysecretkey  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://postgres:postgres@db:5432/starnavi |
| `POSTGRES_USER`  | Postgres username |   postgres   |
| `POSTGRES_PASSWORD`  | Postgres password |  postgres    |
| `POSTGRES_DB`  | Postgres database name | postgres |
| `PGDATA`  | Postgres volume | /var/lib/postgresql/data |
| `REDIS_HOST`  | Redis host | redis |
| `REDIS_PORT`  | Redis port | 6379 |
| `REDIS_DB`  | Redis database | 0 |
| `CLEARBIT_KEY`  | Clearbit key from https://dashboard.clearbit.com/api | |
| `HUNTER_KEY`  | Hunter key from https://hunter.io/api_keys |  |

### Environment variables bot

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `JWT_SECRET_KEY`  | JWT secret key | secret-key              |
| `JWT_ALGORITHMS`  | JWT algorithms  | HS256              |


### Config.ini


| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `api_url`  | Api url for backend | http://starnavi-backend:8000/api/v1 |   
| `path_to_emails`  | Path to user emails (format file .txt)  | email_list.txt |
| `number_of_users`  | Number of users | 1 |
| `max_posts_per_user`  | Max posts per user | 10 |
| `max_likes_per_user`  | Max likes per user | 3 |
    

### Run project

```.bash
$ cd docker
$ docker-compose up
```
