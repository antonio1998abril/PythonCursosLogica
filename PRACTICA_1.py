#nombre="toño"
#ciudad ="jalisco"
#presentacion= ("hola soy"+ nombre + "de " + ciudad);
#prueba = ("hola soy {} de {} amor y poaz").format(nombre,ciudad);
#print(prueba)
#estructura de datos
#frutas=["1","2","3", "caca"];
#print(frutas[2])
#cadena = raw_input(“Introduce una cadena de texto: “) print “La cadena que ingreso es:\n”,cadena. ...
#numero = input(“Introduce un numero: “) ...
#cadena = input(“Introduce una cadena de texto: “) ...
#numero = int(input(“Introduce un numero: “)) ...
#numero = float(input(“Introduce un numero: “))

#for i in range(11,1,-1):
#   print (i)
# nombre=(input("ingresa nombre"))
# edad=(input("ingresa la edad"))
# curp=(input("ingresa tu curp"))

# clase={
  #   "NOMBRE":nombre,
   #  "EDAD":edad,
    # "CURP":curp
# }
# listas=['clase','otro'];

# for i in clase:
  #   print (i, ":", clase[i] )
#%%
semana={
    "lunes":1,
    "martes":2,
    "miercoles":3
}
for i in semana:
    print(i.upper(),":", semana[i])

letra= input("ingresa tu nombre: ")
if letra != "ANTONIO":
    print ("No valido")
else:
    print("HOLA")
#
#%%
numero="10.5"
try:
        numero = int (numero)
except Exception as e:
        print ("error en el valor {}".format(numero))
        print ("el mensahe de error:")

#
#%%
#while(1) = verdadero
semana={
    "lunes":1,
    "martes":2,
    "miercoles":3,
    "jueves":4,
    "viernes":5,
    "sabado":6,
    "domingo":7
}
dias=[]
for i in semana:
    if "o" in i:
        dias.append(i.upper())
    print(i.upper(),":", semana[i])
print(dias)

#
#%%
def suma(numero,numera,texto):

    resultado=numero*numera
    print(resultado, texto)
  

a=int (input("valor a: "))
b=int (input("valor a: "))
c=input("escribe: ")
suma(a,b,c)



#%%

def conversion(char):
    resultado=(char[::-1])
    print(" ".join(resultado))
       
texto=input("ingresa la frase: ")
char=texto.split()
conversion(char)

#
#%%

def calculdora(operador,a,b):
    if operador== "+":
        resultado= a+b
        print(resultado)
    elif operador=="-":
        resultado= a-b
        print(resultado)

oper=input("ingresa el operador: ")
a=int(input("ingresa primer numero: "))
b=int(input("ingresa primer numero: "))
calculdora(oper,a,b)
#
#%%
add = lambda a: a + a
print(add(20))



conv = lambda texto:texto.lower()
print(conv("TELA"))



texto =input("inregsa ")
meta = lambda texto:texto.lower()
print(meta(texto))
#
#%%
def conversion_1(char):
    resultado=(char[::-1])
    print(" ".join(resultado))
       
texto=input("ingresa la frase: ")
char=texto.split()
conversion_1(char)
#
#%%
from collections import defaultdict
#lista de diccionario
pokemon_lista=[
    ['e','ash','nidorian'],
    ['e','ash','charmander'],
    ['y','ash','rattata'],
    ['y','misty','pikachu'],
    ['u','misty','charmander'],
    ['u','brok','nidorian']
]
pokemon =defaultdict(list)
for i,y,j in pokemon_lista:
    
    pokemon[i].append(y)
    pokemon[i].append(j)
print(pokemon)
from collections import defaultdict
#lista de diccionario
pokemon_lista=[
    ['ash','nidorian'],
    ['ash','charmander'],
    ['ash','rattata'],
    ['misty','pikachu'],
    ['misty','charmander'],
    ['brok','nidorian']
]
pokemon =defaultdict(list)
for i,y in pokemon_lista:
    pokemon[i].append(y)
print(pokemon)
#conversion
lista_dict=[]
for tupla in pokemon_lista:
        lista_dict.append({"entrenador":tupla[0],"pokemon":tupla[1]})
print(lista_dict)
#
#%%

#encontrar palabras comunes dentro de una lisat
def most_frequent(List): 
    counter = 0
    i = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            i=i
    return i
  
List = [2, 1, 2, 2, 1, 3,1,1] 
print(most_frequent(List))
#
#%%
from collections import Counter

#encontrar palabras comunes dentro de una lisat
def frecuencia(frase): 
    contador= Counter([
        letra for letra in frase
        if letra not in ",.\n"
    ])
    lista= contador.most_common(3)
    print(lista)

frase = ("""me la pelas perrofgfd
dfdffffffffffffffffffffffdfdff""")

frecuencia(frase)


#
#%%
with open('curso.txt') as infile:
    x=infile.read().splitlines() 
cadena="".join(x)

print(cadena)
                  

mayor=""
palabra=""

for c in cadena:
  if c == " ":
    if palabra != "":
      mayor = palabra if len(mayor)<len(palabra) or mayor == "" else mayor
    palabra = ""
  palabra = palabra + c
print(mayor)

#
#%%
def diccionario(n):
    guardar={}
    for i in range(0, n +1):
        nombre=input("Ingresa el nombre ")
        nick=input("Ingresa el nick ")
        tel=input("Inngresa telfono")
        guardar[i]=nombre,nick,tel
      
    return guardar

def Buscar(n,resultado):
    if (n in resultado):
        nombre=input("Ingresa el nombre ")
        nick=input("Ingresa el nick ")
        tel=input("Inngresa telfono")
        resultado[n]=nombre,nick,tel
    return resultado

def menu(): #El menu de opciones 
    opc=input("Deseas continuar?: ")
    while (opc=='si'):
        opc2=input("ingresa opcion (2) para insertar cantidad (3)para actualizar:")
        if(opc2=="2"):
                number = int(input("Introduce la cantida que ingresaras: ")) 
                resultado = diccionario(number)
                print(resultado)
        elif(opc2=="3"):
                buscar = int(input("Introduce la posicion que quieres actualizar: "))
                Buscar(buscar,resultado)
                print(resultado)
        elif(opc=="1"):       
            return menu()
menu()
#
#%%
tupla_endemonico=("LDAA","JMP","ADD")
tupla_operando_decimal=("#")
tupla_operando_hexa=("$")
tupla_comentario=(";")
tupla_Etiqueta=(':')

tupla_operando=("$","#")

#with open('assembler.txt') as infile:
#    x=infile.read().splitlines() 
#cadena="\n".join(x)
#lista1=cadena.split('\n')
#lista2= ' '.join(lista1)
#lista3=lista2.split(" ")
with open('assembler.txt') as infile:
    x=infile.read().splitlines() 
lista2= ' '.join(x)
lista3=lista2.split(" ")
print(lista3,type(lista3))
print(lista3)

occurrencia_lista=[]
occurrencia_comentario=[]
occurrencia_operando=[]
occurrencia_endemonico=[]

for i in lista3:
    if tupla_Etiqueta in i:
        occurrencia_lista.append(i) 
print ('Etiquetas',occurrencia_lista)

for y in lista3:
    if tupla_comentario in y:
        occurrencia_comentario.append(y)
print ('Comentarios',occurrencia_comentario)

for decimal in lista3:
    if tupla_operando_decimal in decimal:
        occurrencia_operando.append(decimal)
for hexa in lista3:
    if tupla_operando_hexa in hexa:
        occurrencia_operando.append(hexa)
print('Operandos',occurrencia_operando)

for a in lista3:
    if a in tupla_endemonico:
        occurrencia_endemonico.append(a)
print('Endemonicos',occurrencia_endemonico)

indexados1=[]
indexados2=[]
for MODO  in lista3:
    if (MODO == "ADD"):  
        indexados1.append(MODO)
    elif (tupla_operando_hexa in MODO): 
        indexados2.append(MODO)
        
if(indexados2 == []):
    indexados2.append("error")
         
    
print('Indexado:',indexados1,indexados2)
#pass sirve para romper cosas que no se usan
#continuo sirve para ignorar un procesos
#
#%%
#en caso de importlos desde otro archivo seria from classe.Auto import auto
class auto:
    def __init__(self, peso,color,modelo,placas):
        self.Modelo=modelo
    def getResultado(self):
        if (self.Modelo== "TOYOTA"):
            print("price car: 2000")
        else:
            print("I don't know")
modelo=input("Inrgesa el valor:")
Busqueda=auto(10,10,modelo,12332)
Busqueda.getResultado()
#
#%%
#archivo json
import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file =open("./ages.json", "r+")
    data =json.loads(old_file.read())
    print("current age is", data["age"], "_ adding a year. ")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file=open("./ages.json", "w+")
    data ={"name":"Nick","age":27}
    print("No file fund, satting default age to",data["age"])
old_file.seek(0)
old_file.write(json.dumps(data))
#
#%%
#para mongo db inizialisar
import pymongo
from pymongo import MongoClient
myclient=MongoClient()
db=myclient.mydb
users=db.users
print(users.find().count())

#