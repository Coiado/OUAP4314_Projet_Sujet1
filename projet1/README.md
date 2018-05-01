# Data Engineering Project OUAP-4314 : Historic monuments of Paris

This project is a project done during the 4th year of engineering school at ESIEE Paris.</br>
We scrap and store data in a database from the website : http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC). Then we will be able to query this database to get specific informations and values.

## First steps

### Git

* First of all clone this project to your work area, with the follow command:

```
$ git clone https://github.com/Coiado/OUAP4314_Projet_Sujet1.git
```

### Docker

* At first, be sure you have docker install in your computer and you are logged in docker, to run docker in mac or windows you need to use docker toolbox, to see more details give a look here [here](https://docs.docker.com/toolbox/overview/ )

> Then, type follow command to create a docker container in the projet folder:
```
$ docker-compose build
```

> Now you can run the container:
```
$ docker-compose up
```

This operation could take some time, you need to wait till Scrapy finish to scrapy all the webpage.

>  You will see the follow message in your terminal:
```
scrapy_1    |  'title': ' Ancien hôpital de la Santé ou hôpital Sainte-Anne'}
projet1_scrapy_1 exited with code 0
db_1        | 2018-05-01T11:09:39.301+0000 I NETWORK  [conn3] end connection 172.17.0.3:60518 (2 connections now open)
frontend_1  |  * Debugger PIN: 145-804-917
```

### Flask

* To acess the flask web application you have to know which IP in your computer, could acess the docker container.
To do that, run the follow command in your terminal:
```
$ docker-machine ip
```

* With the IP, you can see the application running in this port:
```
http://<IP got with the last command>:5000/
```


* Now you can use the flask application to make some search in your database created by Scrapy, you can search for some monuments, for example you can search for "Brasserie Bofinger".

## Explaination

The web application is coded with the Python framework __Flask__ and we use three dockers containers to run this application
One for flask; other for mongodb and another to scrapy our data.
So we use Scrapy to get Informations about historic monuments of Paris from the website http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC) 
and stored in our own database. More details about those framework could be see in next links.


## Built with

* [Docker](https://hub.docker.com/) - Containerization
* [Flask](flask.pocoo.org/) - Build web application
* [Scrappy](https://scrapy.org/) - Scrapping framework
* [MongoDB](https://www.mongodb.com/fr/) - Data store



## Group project members

* **Clément BERRURIER** 
* **Alexis CHARVET** 
* **Lucas COIADO MOTA**
* **Hung Hoang DANG**


