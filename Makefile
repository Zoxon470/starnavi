show_env:
    cd docker/django
    nano .env

config:
    nano config.ini

# Start app in docker
docker_run:
    cd docker
    docker-compose up
