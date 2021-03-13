# Apache SuperSet overview

intro

Apache SuperSet is an open source software ......



<img src="/home/terman37/MyGit/VIZ_French_Accidents/pictures/result.jpg" style="zoom:50%;" />

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

navigate to:`127.0.0.1:8088` and login as `admin` / `admin`

Pretty straight forward: in the top right corner: settings / users

<img src="pictures/add_user.png" alt="add_user"  />

## Used Dataset

### Description

Dataset found [here](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/) on data.gouv.fr

Complete field description [here](docs/description-des-bases-de-donnees-onisr-annees-2005-a-2019.pdf) in french only, sorry :-(

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

I made a script to import datas to mysql:

```bash
python src/import.py
```

![import_to_mysql](/home/terman37/MyGit/VIZ_French_Accidents/pictures/import_to_mysql.png)

## Give Superset access to datas

### Connection driver

You might need to install connection driver if you want to access particular database. Follow superset [instructions](https://superset.apache.org/docs/databases/installing-database-drivers)

### Add Database connection

in menu: data/databases click on `+ DATABASE` and fill in necessary informations:

![](pictures/add_db.png)

### Add Table as dataset

in menu: data/datasets click on `+ DATASET and fill in necessary informations:

<img src="pictures/add_dataset.png" alt="add_dataset" style="zoom: 80%;" /><img src="/home/terman37/MyGit/VIZ_French_Accidents/pictures/datasets.png" alt="datasets" style="zoom: 80%;" />

### Add calculated field

In the datasets view click on edit button at the end of the dataset row

![add_calculated_column](/home/terman37/MyGit/VIZ_French_Accidents/pictures/add_calculated_column.png)

### Add Virtual Dataset

If you need to have more than one table, you manually create a SQL query (using SQL Lab Editor)

 



## Dashboards & Charts

### Available Visualizations

A lot of nice visualizations are available, lets' checkout some of them

![](pictures/visualizations.png)





### Table



### BigNumber



### Map ScatterPlot using MapBox



### Bar Chart



### Area Chart



### HeatMap



### FilterBox



