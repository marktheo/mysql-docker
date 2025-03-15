# MySQL deploy guide for Docker

**Create the container volume before running docker compose**
```
docker volume create mysql-data
```

<br>

**Access the cloned repository folder and run docker compose**
```
docker compose up -d
```
