# Starnavi technical task


# Configuration Backend

Environment variables

```.sh
$ cd docker/django
$ nano .env # See to table environment variables backend
```

# Configuration Bot

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

Environment variables backend

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | mysecretkey  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://postgres:postgres@db:5432/starnavi |
| `POSTGRES_USER`  | Postgres username |   postgres   |
| `POSTGRES_PASSWORD`  | Postgres password |  postgres    |
| `POSTGRES_DB`  | Postgres database name | starnavi |
| `PGDATA`  | Postgres volume | /var/lib/postgresql/data |
| `REDIS_HOST`  | Redis host | redis |
| `REDIS_PORT`  | Redis port | 6379 |
| `REDIS_DB`  | Redis database | 0 |
| `CLEARBIT_KEY`  | Clearbit key from https://dashboard.clearbit.com/api | |
| `HUNTER_KEY`  | Hunter key from https://hunter.io/api_keys |  |

Environment variables bot

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `JWT_SECRET_KEY`  | JWT secret key | mysecretkey              |
| `JWT_ALGORITHMS`  | JWT algorithms  | HS256              |


Config.ini


| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `api_url`  | Api url for backend | http://starnavi-backend:8000/api/v1 |   
| `path_to_emails`  | Path to user emails (format file .txt)  | email_list.txt |
| `number_of_users`  | Number of users | 1 |
| `max_posts_per_user`  | Max posts per user | 10 |
| `max_likes_per_user`  | Max likes per user | 3 |
    

# Run project

```.bash
$ docker-compose up
```
