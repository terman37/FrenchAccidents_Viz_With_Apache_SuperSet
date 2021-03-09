# Apache SuperSet overview

intro

## Installation

### Run with docker compose

[Clone Superset's repo](https://github.com/apache/superset) in your terminal with the following command:

```bash
git clone https://github.com/apache/superset.git
```

Once that command completes successfully, you should see a new `superset` folder in your current directory.

```bash
cd superset
docker-compose up
```

### Connect and create user

Pretty straight forward: in the top right corner: settings / users

<img src="pictures/add_user.png" alt="add_user"  />

## Used Dataset

### Description



### Database

#### Launch

from docker-compose in my repo

```bash
docker-compose up
```

#### Create MySQL user

connect to container

```bash
docker ps
docker exec -it <CONTAINER ID> /bin/bash
mysql -u root -p
```

from mysql shell:

```mysql
CREATE USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%';
FLUSH PRIVILEGES;
```

#### Datas preprocessing

I made a script to upload datas:

- choosing right data type
- preprocessing dates
- removing unnecessary columns

```bash
python src/import.py
```



## Give Superset access to datas

### Connection driver

You might need to install connection driver if you want to access particular database. Follow superset [instructions](https://superset.apache.org/docs/databases/installing-database-drivers)

### Create DB

### Create Dataset



## Dashboards & Charts