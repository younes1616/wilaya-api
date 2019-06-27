from easySqlite3 import Db
from data.pythonData.baladiya import *
from data.pythonData.wilaya import *
from data.sqlData.manager.tables import *

DATA_BASE_PATH = 'dbSqlite.sql'

db = Db(DATA_BASE_PATH)
db.connect()

# creation des tables des baladiya
db.createTable(BALADIYA_CODE_TABLE)
db.createTable(BALADIYA_AR_TABLE)
db.createTable(BALADIYA_FR_TABLE)

# write data into the tables
db.prepareQuery('INSERT INTO BALADIYA_CODE(code) VALUES (?)')
for code in baladiyaCode:
	db.insertRow([code])

db.prepareQuery('INSERT INTO BALADIYA_FR(name_fr) VALUES (?)')
for code in baladiyaFr:
	db.insertRow([code])

db.prepareQuery('INSERT INTO BALADIYA_AR(name_ar) VALUES (?)')
for code in baladiyaAr:
	db.insertRow([code])

# creation des tables des donnes pour les wilaya
print(db.createTable(WILAYA_CODE_TABLE))
print(db.createTable(WILAYA_AR_TABLE))
print(db.createTable(WILAYA_FR_TABLE))
print(db.createTable(WILAYA_CODE_POST_TABLE))
print(db.createTable(WILAYA_CODE_TEL_TABLE))

# write data into the tables
db.prepareQuery('INSERT INTO WILAYA_Ar(name_ar) VALUES (?)')
for code in wilayaAr:
	print(db.insertRow([code]))

db.prepareQuery('INSERT INTO WILAYA_Fr(name_fr) VALUES (?)')
for code in wilayaFr:
	print(db.insertRow([code]))

db.prepareQuery('INSERT INTO WILAYA_CODE(code) VALUES (?)')
for code in wilayaCode:
	print(db.insertRow([code]))

db.prepareQuery('INSERT INTO WILAYA_CODE_TEL(code_tel) VALUES (?)')
for code in wilayaCodeTel:
	print(db.insertRow([code]))

db.prepareQuery('INSERT INTO WILAYA_CODE_POST(code_post) VALUES (?)')
for code in wilayaCodePost:
	print(db.insertRow([code]))

# creationd des deux tables wilaya et baladiya
db.createTable(BALADIYA_TABLE)
db.createTable(WILAYA_TABLE)

# insertion des donnes dans la tables Wilaya
db.prepareQuery("INSERT INTO WILAYA(code,code_tel,code_post,name_ar,name_fr,name_en) VALUES (?,?,?,?,?,?)")
for wl in wilaya:
	e = wilaya[wl]
	db.insertRow([e["code"], e["codeTel"], e["codePost"], e["nameAr"], e["nameFr"], e["nameFr"]])

# insertion des donnes dans la tables Baladiya
db.prepareQuery('INSERT INTO BALADIYA(code,name_ar,name_fr,name_en,wilaya_code) VALUES (?,?,?,?,?)')
for wl in baladiya:
	e = baladiya[wl]
	print(db.insertRow([e["code"], e["nameAr"], e["nameFr"], e["nameEn"], e["wilayaCode"]]))

db.close()
