#  The list of the wilaya in Arabic
wilayaAr = ["أدرار", "الشلف", "الأغواط", "أم البواقي", "باتنة", "بجاية", "بسكرة",
 "بشار", "البليدة", "البويرة", "تمنراست", "تبسة", "تلمسان", "تيارت", "تيزي وزو",
 "الجزائر", "الجلفة", "جيجل", "سطيف", "سعيدة", "سكيكيدة", "سيدي بلعباس", "عنابة",
 "قالمة", "قسنطينة", "المدية", "مستغانم", "المسيلة", "معسكر", "ورقلة", "وهران", "البيض",
 "إليزي", "برج بوعريريج", "بومرداس", "الطارف", "تندوف", "تسمسيلت", "الوادي", "خنشلة",
 "سوق الأهراس", "تيبازة", "ميلة", "عين الدفلى", "النعامة", "عين تموشنت", "غرداية", "غليزان"]

#  The list of the wilaya in French
wilayaFr = \
["Adrar", "Chlef", "Laghouat", "Oum El Bouaghi", "Batna", "Bejaia", "Biskra",
 "Béchar", "Blida", "Bouira", "Tamanrasset", "Tébessa", "Tlemcen", "Tiaret",
 "Tizi Ouzou", "Alger", "Djelfa", "Jijel", "Sétif", "Saïda", "Skikda",
 "Sidi Bel Abbes", "Annaba", "Guelma", "Constantine", "Medea", "Mostaganem", "M'Sila",
 "Mascara", "Ouargla", "Oran", "El Bayadh", "Illizi", "Bordj Bou Arreridj", "Boumerdes",
 "El Tarf", "Tindouf", "Tissemsilt", "El Oued", "Khenchela", "Souk Ahras", "Tipaza",
 "Mila", "Aïn Defla", "Naama", "Aïn Temouchent", "Ghardaia", "Relizane"]


#  The list of the wilaya in there code number
wilayaCode = \
["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
 "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
 "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
 "48"]


#  The list of the wilaya in there post code
wilayaCodePost = \
["01000", "02000", "03000", "04000", "05000", "06000", "07000", "08000", "09000", "10000",
 "11000", "12000", "13000", "14000", "15000", "16000", "17000", "18000", "19000", "20000",
 "21000", "22000", "23000", "24000", "25000", "26000", "27000", "28000", "29000", "30000",
 "31000", "32000", "33000", "34000", "35000", "36000", "37000", "38000", "39000", "40000",
 "41000", "42000", "43000", "44000", "45000", "46000", "47000", "48000"]

# The list of the wilaya telephone code
wilayaCodeTel = \
[
 "49", "27", "29", "32", "33", "34", "33", "49", "25", "26",
 "29", "37", "43", "46", "26", "21", "27", "34", "36", "48",
 "38", "48", "38", "37", "31", "25", "45", "35", "45", "29",
 "41", "49", "29", "35", "24", "38", "49", "46", "32", "32",
 "37", "24", "31", "27", "49", "43", "29", "46"]

# The list of all the wilayas, with all the attributes
wilaya = {
"27": {
	"code": "27",
	"nameFr": "Mostaganem",
	"codeTel": "45",
	"nameEn": "Mostaganem",
	"nameAr": "مستغانم",
	"codePost": "27000"},

"12": {
	"code": "12",
	"nameFr": "Tébessa",
	"codeTel": "37",
	"nameEn": "Tébessa",
	"nameAr": "تبسة",
	"codePost": "12000"},

"20": {
	"code": "20",
	"nameFr": "Saïda",
	"codeTel": "48",
	"nameEn": "Saïda",
	"nameAr": "سعيدة",
	"codePost": "20000"},

"46": {
	"code": "46",
	"nameFr": "Aïn Temouchent",
	"codeTel": "43",
	"nameEn": "Aïn Temouchent",
	"nameAr": "عين تموشنت",
	"codePost": "46000"},

"8": {
	"code": "8",
	"nameFr": "Béchar",
	"codeTel": "49",
	"nameEn": "Béchar",
	"nameAr": "بشار",
	"codePost": "08000"},

"40": {
	"code": "40",
	"nameFr": "Khenchela",
	"codeTel": "32",
	"nameEn": "Khenchela",
	"nameAr": "خنشلة",
	"codePost": "40000"},

"2": {
	"code": "2",
	"nameFr": "Chlef",
	"codeTel": "27",
	"nameEn": "Chlef",
	"nameAr": "الشلف",
	"codePost": "02000"},

"38": {
	"code": "38",
	"nameFr": "Tissemsilt",
	"codeTel": "46",
	"nameEn": "Tissemsilt",
	"nameAr": "تسمسيلت",
	"codePost": "38000"},

"9": {
	"code": "9",
	"nameFr": "Blida",
	"codeTel": "25",
	"nameEn": "Blida",
	"nameAr": "البليدة",
	"codePost": "09000"},

"24": {
	"code": "24",
	"nameFr": "Guelma",
	"codeTel": "37",
	"nameEn": "Guelma",
	"nameAr": "قالمة",
	"codePost": "24000"},

"43": {
	"code": "43",
	"nameFr": "Mila",
	"codeTel": "31",
	"nameEn": "Mila",
	"nameAr": "ميلة",
	"codePost": "43000"},

"47": {
	"code": "47",
	"nameFr": "Ghardaia",
	"codeTel": "29",
	"nameEn": "Ghardaia",
	"nameAr": "غرداية",
	"codePost": "47000"},

"29": {
	"code": "29",
	"nameFr": "Mascara",
	"codeTel": "45",
	"nameEn": "Mascara",
	"nameAr": "معسكر",
	"codePost": "29000"},

"25": {
	"code": "25",
	"nameFr": "Constantine",
	"codeTel": "31",
	"nameEn": "Constantine",
	"nameAr": "قسنطينة",
	"codePost": "25000"},

"16": {
	"code": "16",
	"nameFr": "Alger",
	"codeTel": "21",
	"nameEn": "Alger",
	"nameAr": "الجزائر",
	"codePost": "16000"},

"7": {
	"code": "7",
	"nameFr": "Biskra",
	"codeTel": "33",
	"nameEn": "Biskra",
	"nameAr": "بسكرة",
	"codePost": "07000"},

"11": {
	"code": "11",
	"nameFr": "Tamanrasset",
	"codeTel": "29",
	"nameEn": "Tamanrasset",
	"nameAr": "تمنراست",
	"codePost": "11000"},

"33": {
	"code": "33",
	"nameFr": "Illizi",
	"codeTel": "29",
	"nameEn": "Illizi",
	"nameAr": "إليزي",
	"codePost": "33000"},

"34": {
	"code": "34",
	"nameFr": "Bordj Bou Arreridj",
	"codeTel": "35",
	"nameEn": "Bordj Bou Arreridj",
	"nameAr": "برج بوعريريج",
	"codePost": "34000"},


"41": {
	"code": "41",
	"nameFr": "Souk Ahras",
	"codeTel": "37",
	"nameEn": "Souk Ahras",
	"nameAr": "سوق الأهراس",
	"codePost": "41000"},

"26": {
    "code": "26",
    "nameFr": "Medea",
    "codeTel": "25",
    "nameEn": "Medea",
    "nameAr": "المدية",
    "codePost": "26000"},

"18": {
	"code": "18",
	"nameFr": "Jijel",
	"codeTel": "34",
	"nameEn": "Jijel",
	"nameAr": "جيجل",
	"codePost": "18000"},

"48": {
	"code": "48",
	"nameFr": "Relizane",
	"codeTel": "46",
	"nameEn": "Relizane",
	"nameAr": "غليزان",
	"codePost": "48000"},

"4": {
	"code": "4",
	"nameFr": "Oum El Bouaghi",
	"codeTel": "32",
	"nameEn": "Oum El Bouaghi",
	"nameAr": "أم البواقي",
	"codePost": "04000"},

"15": {
	"code": "15",
	"nameFr": "Tizi Ouzou",
	"codeTel": "26",
	"nameEn": "Tizi Ouzou",
	"nameAr": "تيزي وزو",
	"codePost": "15000"},

"17": {
	"code": "17",
	"nameFr": "Djelfa",
	"codeTel": "27",
	"nameEn": "Djelfa",
	"nameAr": "الجلفة",
	"codePost": "17000"},

"14": {
	"code": "14",
	"nameFr": "Tiaret",
	"codeTel": "46",
	"nameEn": "Tiaret",
	"nameAr": "تيارت",
	"codePost": "14000"},

"22": {
	"code": "22",
	"nameFr": "Sidi Bel Abbes",
	"codeTel": "48",
	"nameEn": "Sidi Bel Abbes",
	"nameAr": "سيدي بلعباس",
	"codePost": "22000"},

"21": {
	"code": "21",
	"nameFr": "Skikda",
	"codeTel": "38",
	"nameEn": "Skikda",
	"nameAr": "سكيكيدة",
	"codePost": "21000"},

"30": {
	"code": "30",
	"nameFr": "Ouargla",
	"codeTel": "29",
	"nameEn": "Ouargla",
	"nameAr": "ورقلة",
	"codePost": "30000"},

"32": {
	"code": "32",
	"nameFr": "El Bayadh",
	"codeTel": "49",
	"nameEn": "El Bayadh",
	"nameAr": "البيض",
	"codePost": "32000"},

"6": {
	"code": "6",
	"nameFr": "Bejaia",
	"codeTel": "34",
	"nameEn": "Bejaia",
	"nameAr": "بجاية",
	"codePost": "06000"},

"23": {
	"code": "23",
	"nameFr": "Annaba",
	"codeTel": "38",
	"nameEn": "Annaba",
	"nameAr": "عنابة",
	"codePost": "23000"},

"13": {
	"code": "13",
	"nameFr": "Tlemcen",
	"codeTel": "43",
	"nameEn": "Tlemcen",
	"nameAr": "تلمسان",
	"codePost": "13000"},

"10": {
	"code": "10",
	"nameFr": "Bouira",
	"codeTel": "26",
	"nameEn": "Bouira",
	"nameAr": "البويرة",
	"codePost": "10000"},

"1": {
	"code": "1",
	"nameFr": "Adrar",
	"codeTel": "49",
	"nameEn": "Adrar",
	"nameAr": "أدرار",
	"codePost": "01000"},

"19": {
	"code": "19",
	"nameFr": "Sétif",
	"codeTel": "36",
	"nameEn": "Sétif",
	"nameAr": "سطيف",
	"codePost": "19000"},

"31": {
	"code": "31",
	"nameFr": "Oran",
	"codeTel": "41",
	"nameEn": "Oran",
	"nameAr": "وهران",
	"codePost": "31000"},

"42": {
	"code": "42",
	"nameFr": "Tipaza",
	"codeTel": "24",
	"nameEn": "Tipaza",
	"nameAr": "تيبازة",
	"codePost": "42000"},


"44": {
	"code": "44",
	"nameFr": "Aïn Defla",
	"codeTel": "27",
	"nameEn": "Aïn Defla",
	"nameAr": "عين الدفلى",
	"codePost": "44000"},

"37": {
	"code": "37",
	"nameFr": "Tindouf",
	"codeTel": "49",
	"nameEn": "Tindouf",
	"nameAr": "تندوف",
	"codePost": "37000"},

"35": {
	"code": "35",
	"nameFr": "Boumerdes",
	"codeTel": "24",
	"nameEn": "Boumerdes",
	"nameAr": "بومرداس",
	"codePost": "35000"},

"36": {
	"code": "36",
	"nameFr": "El Tarf",
	"codeTel": "38",
	"nameEn": "El Tarf",
	"nameAr": "الطارف",
	"codePost": "36000"},


"3": {
	"code": "3",
	"nameFr": "Laghouat",
	"codeTel": "29",
	"nameEn": "Laghouat",
	"nameAr": "الأغواط",
	"codePost": "03000"},

"28": {
	"code": "28",
	"nameFr": "M'Sila",
	"codeTel": "35",
	"nameEn": "M'Sila",
	"nameAr": "المسيلة",
	"codePost": "28000"},

"5": {
	"code": "5",
	"nameFr": "Batna",
	"codeTel": "33",
	"nameEn": "Batna",
	"nameAr": "باتنة",
	"codePost": "05000"},

"39": {
	"code": "39",
	"nameFr": "El Oued",
	"codeTel": "32",
	"nameEn": "El Oued",
	"nameAr": "الوادي",
	"codePost": "39000"},

"45": {
	"code": "45",
	"nameFr": "Naama",
	"codeTel": "49",
	"nameEn": "Naama",
	"nameAr": "النعامة",
	"codePost": "45000"}}
