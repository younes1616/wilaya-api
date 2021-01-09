# Algerian Wilaya Data List

## Description

[En] A Data-Set, that containins the list of the Algerian ***States (Wilaya)*** and  ***Provinces (Baladiya)***. Wialaya codes, and Baladiya codes, post codes and phones codes, are all included in this Data set.  
The Data is represented into two formats, JSON and SQL.

[Fr] Une base de données qui contient les Wilayas at Baladia(communes), de l'algerie. Avec toutes leurs donnes possible.

[Ar]  قاعدة بيانات تحتوي على الولايات و البلديات بالجزائر. مع كل البيانات الخاصة بهم

## More Data About Algeria

You can download the Data only from the [DZ-Wilaya-Data](https://github.com/Ta7lil/DZ-Wilaya-Data) repository, and consider visiting the [Ta7lil Organisation](https://github.com/Ta7lil) GitHub account for more Data about Algeria.

## How To Read The Code

1. `easySqlite3.py`
2. `config.py`
3. `crowlers/`
4. `data/pythonData/`
5. `data/jsonData/`
6. `data/sqlData`

## Tools

* Language
  * Python 3.5
* Libraries
  * re, sqlite3, requests, BeautifulSoup
  
## Notes

* The Data goes to ***27 June 2019***, and it has never being modified or updated since.
* Some of the cities have the same name, and some telephone codes are also the same.
* every thing is a String, varchar(50), text. No mixed up types.
* `config.py` File, contains all the used recources in the Project.
* The crowlers and scrapers, are all done in Python.

## Resources

There are the following recources used to collect and combine the Data.

* Official Goverment websites:
  * <http://www.interieur.gov.dz/index.php/fr/component/annuaire>
  * <http://www.interieur.gov.dz/index.php/ar/component/annuaire>
  * <https://www.algerietelecom.dz/fr/annuaire>
  * <https://www.algerietelecom.dz/ar/annuaire>

* Non-official Goverment websites:
  * <https://abbassa.wordpress.com/wilayate/>
  * <https://dza.postcodebase.com/region1-text>
  * <http://www.algerie-poste.net/code-postal/>
  * <https://fr.wikipedia.org/wiki/Liste_des_communes_d%27Alg%C3%A9rie>

## Explain Data

I did my best to make the collected data into all the most used formats,  
since I used Pytohn, the pythonData contains the data as Python data structers.  

### Json Data

> Full Data Combined

* `Data.json`: All the Data below was combined into one big file, that contains a join of all the Data, as it follows.

```json
    "31": {
        "nameEn": "Oran",
        "nameAr": "وهران",
        "code": "31",
        "commune": [
            "3109",
            .
            .
            .
            "3114"
        ],
        "nameFr": "Oran",
        "codeTel": "41",
        "codePost": "31000"
    }
```

> The Data Related To The States (Wilaya)

* `wilaya.json`: The list of all the States (With all the Data, except Provinces).
* `wilayaAr.json`: The list of all the States names in Arabic.
* `wilayaFr.json`: The list of all the States names in French.
* `wilayaCode.json`: The list of all the States codes.
* `wilayaCodePost.json`: The list of all the States poste codes.
* `wilayaCodeTel.json`: The list of all the States telephone codes.

> The Data Related To The Provinces (Baladiya)

* `baladiya.json`: The list of all the Provinces (With all the Data).
* `baladiyaAr.json`: The list of all the Provinces names in Arabic.
* `baladiyaFr.json`: The list of all the Provinces names in French.
* `baladiyaCode.json`: The list of all the Provinces codes.

### Sql Data

> Tables Schemas

* `schema.sql`: The Tables Schema for the Sql, MySql like databases.
* `schema.sqlite`: The Tables Schema for the Sqlite databases.

> The Data

* `data.sql`: A Data migration file, for inserting all the Data after creating the tables, it is for Sql, MySql like databases.
* `data.sqlite`: The Sqlite Database, therefore it is portable, just copy paste it, and use it.
  
***Please check the files, for a better undertanding***
