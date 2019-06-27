DESCRIPTION:
-
[Fr] Une base de données qui contient les Wilayas at Baladia(communes), de l'algerie. Avec toutes leurs donnes possible.<br>
[En] A database containing the Wilayas at Baladia (communes), Algeria. With all their data possible.<br>
[Ar]  قاعدة بيانات تحتوي على الولايات و البلديات بالجزائر. مع كل البيانات الخاصة بهم



THE HIRARCHY:
-
```
wilayaApi/
├── config.py
├── crowlers
│   ├── baladiyaCrowler.py
│   ├── __init__.py
│   └── wilayaCrewler.py
├── data
│   ├── csvData
│   │   ├── BALADIYA_AR.csv
│   │   ├── BALADIYA_CODE.csv
│   │   ├── BALADIYA.csv
│   │   ├── BALADIYA_FR.csv
│   │   ├── __init__.py
│   │   ├── WILAYA_AR.csv
│   │   ├── WILAYA_CODE.csv
│   │   ├── WILAYA_CODE_POST.csv
│   │   ├── WILAYA_CODE_TEL.csv
│   │   ├── WILAYA.csv
│   │   └── WILAYA_FR.csv
│   ├── __init__.py
│   ├── jsonData
│   │   ├── baladiyaAr.json
│   │   ├── baladiyaCode.json
│   │   ├── baladiyaFr.json
│   │   ├── baladiya.json
│   │   ├── data.json
│   │   ├── __init__.py
│   │   ├── wilayaAr.json
│   │   ├── wilayaCode.json
│   │   ├── wilayaCodePost.json
│   │   ├── wilayaCodeTel.json
│   │   ├── wilayaFr.json
│   │   └── wilaya.json
│   ├── pythonData
│   │   ├── baladiya.py
│   │   ├── __init__.py
│   │   └── wilaya.py
│   └── sqlData
│       ├── dbSqlite.sql
│       ├── __init__.py
│       ├── manager
│       │   ├── __init__.py
│       │   ├── merger.py
│       │   ├── queires.py
│       │   └── tables.py
│       ├── sqlData.sql
│       ├── sqliteSchema.sql
│       └── sqlSchema.sql
├── easySqlite3.py
├── __init__.py
└── README.md

```


HOW TO READ THE CODE:
-
1. easySqlite3
2. config
3. crowlers/*
4. data/pythonData/*
5. data/jsonData/*
6. data/sqlData | csvData/*


TOOLS:
-
* Language
	* Python 3.5

* Libraries
	* re, sqlite3, requests, BeautifulSoup
  
  
  NOTES:
  * Some of the cities have the same name, and some telephone codes also get the same code.
  * every thing is a String, varchar(50), text. No mixed up types.
  * config File, contains all the used recources in the Project.
  * The crowlers and scrapers, are all done in Python.
  * https://github.com/HerharFares/easySqlite3
  
  
  DATA FILE:
  -
  I did my best to make the collected data into all the most used formats,<br>
  since I used Pytohn, the pythonData contains the data as Python data structers.<br>
  jsonData contains the data as json files. sqlData contains an dbSqlite.sql<br>
  [https://github.com/HerharFares/wilayaApi/blob/master/data/sqlData/dbSqlite.sql]<br>
  so for the users of portable data basse and sqlite the dbSqlite.sql satisfies the need.<br>
  sqliteSchema.sql, contains the database Shema as sqlite, sqlSchema.sql as usual Sql<br>
  sqlData.sql, contains the data so you can insert it into you new data basse.
  
<h1> Please check the files, for a better undertanding </h1>  
