
traduceri = {
    "ro": {
        "no1":"Introduceti  un număr: ",
        "numeric":"Inserati numai numere",
        "no2":"Introduceti al doilea numar:",
        "op": "Alegeti operatia:(+.-,*,/):",
        "re_op":"Alegeti daor din +,-,*,/",
        "rez":"Rezultatul este:",
    },
   "en": { 
       "no1":"Enter a number: ",
       "numeric": "Insert only number",
       "no2" :"Enter your second number:",
        "op":"Choose the operatiom:(+,-,*,/):",
         "re_op":"Choose only from  +,-,*,/",
       "rez": "The result is:",
    },
   "de":
       { "no1": "Geben Sie eine Zahl ein: ",
       "numeric": "Bitte nur Zahlen eingeben",
       "no2": "Geben Sie die zweite Zahl ein:",
       "op": "Wählen Sie die Operation (+,-,*,/):",
       "re_op": "Wählen Sie nur aus +,-,*,/",
        "rez": "Das Ergebnis ist:",
       },
     "it": { 
       "no1":"Inserire il primo nummer0:",
        "numeric" :"Inserisce solo numere",
        "no2": "Inserire il  secondo numero",
        "op": "Scogli operazione:(*,-,/,*):",
         "re_op":"Scegli solo tra +,-,*,/",
        "rez": "Il resultato:",
     },
     "fr":{"no1": "Entrez un nombre : ",
         "numeric": "Veuillez entrer uniquement des chiffres",
         "no2": "Entrez le deuxième nombre :",
        "op": "Choisissez l’opération (+,-,*,/) :",
        "re_op": "Choisissez uniquement parmi +,-,*,/",
          "rez": "Le résultat est :"
     }
     }

lang = input(f"Alege limba {list(traduceri.keys())} ")

while lang not in traduceri.keys():
    lang = input (f"Please choose from {list(traduceri.keys())}")
    
no1 = input(traduceri[lang]["no1"])
while not no1.isnumeric():
    no1 = input(traduceri[lang]["numeric"])
no1= int(no1)
print( no1)

no2 = input(traduceri[lang]["no2"])
while not no2.isnumeric():
    no2=input(traduceri[lang]["numeric"])
no2 =int(no2)    
print(no2)

op = input(traduceri[lang] ["op"])
while op not in ("+","-","*","/"):
    op = input (traduceri[lang]["re_op"])
    
if op == "+":
    rezultat =no1+no2
elif op == "-":
    rezultat = no1-no2 
elif op == "*":
    rezultat =no1*no2
elif op == "/":
    rezultat =no1/no2       
    
rezultat= no1+no2
print(traduceri [lang]["rez"],rezultat)
    