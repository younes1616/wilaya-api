# table pour la liste des codes des baladiya
BALADIYA_CODE_TABLE = '''
CREATE TABLE IF NOT EXISTS BALADIYA_CODE(
    code TEXT PRIMARY KEY,
);
'''

# table pour la liste des noms des baladiya en latin
BALADIYA_FR_TABLE = '''
CREATE TABLE IF NOT EXISTS BALADIYA_FR(
    name_fr TEXT PRIMARY KEY,
);
'''

# table pour la liste des noms des baladiya en arabe
BALADIYA_AR_TABLE = '''
CREATE TABLE IF NOT EXISTS BALADIYA_AR(
    name_ar TEXT PRIMARY KEY,
);
'''

# table pour la liste des codes des wilaya
WILAYA_CODE_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA_CODE(
    code TEXT PRIMARY KEY,
);
'''

# table pour la liste des codes post des wilaya
WILAYA_CODE_POST_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA_CODE_POST(
    code_post TEXT PRIMARY KEY,
);
'''

# table pour la liste des codes post des wilaya
WILAYA_CODE_TEL_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA_CODE_TEL(
    code_tel TEXT PRIMARY KEY,
);
'''

# table pour la liste des noms des wilaya en latin
WILAYA_FR_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA_FR(
    name_fr TEXT PRIMARY KEY,
);
'''

# table pour la liste des noms des wilaya en arabe
WILAYA_AR_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA_AR(
    name_ar TEXT PRIMARY KEY,
);
'''

# table pour la liste baladiya, avec tous les donnes
BALADIYA_TABLE = '''
CREATE TABLE IF NOT EXISTS BALADIYA(
    code TEXT PRIMARY KEY,
    name_ar TEXT NOT NULL,
    name_fr TEXT NOT NULL,
    name_en TEXT NOT NULL,
    wilaya_code TEXT NOT NULL,
    FOREIGN KEY(wilaya_code) REFERENCES WILAYA(code)
);
'''

# table pour la liste wilaya, avec tous les donnes
WILAYA_TABLE = '''
CREATE TABLE IF NOT EXISTS WILAYA(
    code TEXT PRIMARY KEY,
    code_tel TEXT NOT NULL,
    code_post TEXT NOT NULL,
    name_ar TEXT NOT NULL,
    name_fr TEXT NOT NULL,
    name_en TEXT NOT NULL
);
'''