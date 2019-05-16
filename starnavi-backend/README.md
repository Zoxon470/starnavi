# Starnavi technical task


# How to run?

### Clone services
```.sh
$ mkdir starnavi && cd starnavi # creating folder
$ git clone https://github.com/Zoxon470/starnavi-backend # Clone Backend 
service
$ git clone https://github.com/Zoxon470/starnavi-bot # Clone bot service
```


## Run via docker

```.bash
$ docker-compose up --build
```

Environment variables

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | mysecretkey  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://postgres:postgres@db:5432/starnavi |
| `POSTGRES_USER`  | Postgres username |   postgres   |
| `POSTGRES_PASSWORD`  | Postgres password |  postgres    |
| `POSTGRES_DB`  | Postgres database name | starnavi |
| `PGDATA`  | Postgres volume | /var/lib/postgresql/data |
| `CLEARBIT_KEY`  | Clearbit key from https://dashboard.clearbit.com/api | |
| `HUNTER_KEY`  | Hunter key from https://hunter.io/api_keys |  |
