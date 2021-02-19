def resultado(hora,minutos):
    minutos=minutos/60
    hora=hora+minutos
    print(hora)

    

tupla_hora=(':')
tupla_minuto=("33","40","12","17","19","50","40","2","22","54","49","51","33","48","14","13","19","7","12","4","1")

with open('pythonsumahoras.txt') as infile:
    archivo=infile.read().splitlines()
    archivo_union=' '.join(archivo)
    archivo_separador=archivo_union.split(" ")
  
  

ocurrencia_hora=[]
ocurencia_minuto=[]

suma_minutos=0
suma_horas=0
#horas
for i in archivo_separador:
    if tupla_hora in i:
        ocurrencia_hora.append(i)
separar_paso_union=''.join(ocurrencia_hora)
ocurrencia_hora=separar_paso_union.split(":")
del ocurrencia_hora[-1]
for x in range(0,len(ocurrencia_hora)):
    ocurrencia_hora[x]=int(ocurrencia_hora[x])

for j in range(0,len(ocurrencia_hora)):
    suma_horas=suma_horas+ocurrencia_hora[j] 
#finhoras

#minutos
for i in archivo_separador:
    if i in  tupla_minuto:
        ocurencia_minuto.append(i)
for x in range(0, len(ocurencia_minuto)):
    ocurencia_minuto[x]=int(ocurencia_minuto[x])

for j in range(0,len(ocurencia_minuto)):
    suma_minutos=suma_minutos+ocurencia_minuto[j]
#finminutos

print('horas',ocurrencia_hora)
print (suma_horas)
print('minutos',ocurencia_minuto)
print(suma_minutos)


resultado(suma_horas,suma_minutos)
