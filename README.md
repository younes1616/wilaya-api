# Algerian Wilaya Data List

## DESCRIPTION

[Fr] Une base de données qui contient les Wilayas at Baladia(communes), de l'algerie. Avec toutes leurs donnes possible.  
[En] A database containing the Wilayas at Baladia (communes), Algeria. With all their data possible.  
[Ar]  قاعدة بيانات تحتوي على الولايات و البلديات بالجزائر. مع كل البيانات الخاصة بهم

## HOW TO READ THE CODE

1. easySqlite3
2. config
3. crowlers/*
4. data/pythonData/*
5. data/jsonData/*
6. data/sqlData | csvData/*

## TOOLS

* Language
  * Python 3.5
* Libraries
  * re, sqlite3, requests, BeautifulSoup
  
## NOTES

* Some of the cities have the same name, and some telephone codes also get the same code.
* every thing is a String, varchar(50), text. No mixed up types.
* config File, contains all the used recources in the Project.
* The crowlers and scrapers, are all done in Python.
* <https://github.com/HerharFares/easySqlite3>
  
## DATA FILE

I did my best to make the collected data into all the most used formats,  
since I used Pytohn, the pythonData contains the data as Python data structers.  
jsonData contains the data as json files. sqlData contains an dbSqlite.sql  
[https://github.com/HerharFares/wilayaApi/blob/master/data/sqlData/dbSqlite.sql]  
so for the users of portable data basse and sqlite the dbSqlite.sql satisfies the need.  
sqliteSchema.sql, contains the database Shema as sqlite, sqlSchema.sql as usual Sql,  
sqlData.sql, contains the data so you can insert it into you new data basse.
  
***Please check the files, for a better undertanding***
