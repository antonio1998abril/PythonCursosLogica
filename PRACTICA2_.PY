tupla_endemonico=("LDAA","JMP","ADD")
tupla_operando_decimal=("#")
tupla_operando_hexa=("$")
tupla_comentario=(";")
tupla_Etiqueta=(':')

tupla_operando=("$","#")

with open('assembler.txt') as infile:
    x=infile.read().splitlines() 
lista2= ' '.join(x)
lista3=lista2.split(" ")
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
