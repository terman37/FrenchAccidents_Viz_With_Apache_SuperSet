# Apache SuperSet analysing French kids accidents

![](pictures/superset_logo.png)

Apache Superset is a modern data exploration and visualization platform allowing to create nice and interactive dashboard for data visualization.

I wanted to test its capabilities through analysis of open dataset regarding road accidents in France (especially involving kids)

<img src="pictures/result.jpg" style="zoom:50%;" />

## Installation

- Version: 0.999.0dev

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

![import_to_mysql](pictures/import_to_mysql.png)

## Give Superset access to datas

### Connection driver

You might need to install connection driver if you want to access particular database. Follow superset [instructions](https://superset.apache.org/docs/databases/installing-database-drivers)

### Add Database connection

in menu: data/databases click on `+ DATABASE` and fill in necessary informations:

![](pictures/add_db.png)

### Add Table as dataset

in menu: data/datasets click on `+ DATASET and fill in necessary informations:

<img src="pictures/add_dataset.png" alt="add_dataset" style="zoom: 80%;" /><img src="pictures/datasets.png" alt="datasets" style="zoom: 80%;" />

### Add calculated field

In the datasets view click on edit button at the end of the dataset row

![add_calculated_column](pictures/add_calculated_column.png)

### Add Virtual Dataset

If you need to have more than one table, you manually create a SQL query (using SQL Lab Editor)

 ![](pictures/sql_lab.png)

Then by clicking Explore, you will be able to save it as a virtual dataset and use it to create reports

## Dashboards & Charts

### Available Visualizations

A lot of nice visualizations are available, lets' checkout some of them

![](pictures/visualizations.png)



### FilterBox

<img src="pictures/filterbox.png" style="zoom:50%;" />

### BigNumber

<img src="pictures/bignumber.png" style="zoom:50%;" /><img src="pictures/bignumber2.png" style="zoom:50%;" />

### Table

<img src="pictures/table.png" style="zoom:50%;" /><img src="pictures/table2.png" style="zoom:50%;" />

### Map ScatterPlot using MapBox

**Before using any visualization using MapBox you need to specify you token to access MapBox API**

Create an account on Mapbox.com and create a token.

<img src="pictures/mapbox.png" style="zoom:50%;" />

Copy the token and add it in your superset `.env` file

```
cd superset
echo MAPBOX_API_KEY=<you token> > docker/.env
```





<img src="pictures/map.png" style="zoom:50%;" /><img src="pictures/map2.png" style="zoom:50%;" />



### Area Chart

<img src="pictures/area.png" style="zoom:50%;" /><img src="pictures/area2.png" style="zoom:50%;" />

### Bar Chart

<img src="pictures/barchart.png" style="zoom:50%;" /><img src="pictures/barchart2.png" style="zoom:50%;" />

### HeatMap

<img src="pictures/heatmap.png" style="zoom:50%;" /><img src="pictures/heatmap2.png" style="zoom:50%;" />

 



