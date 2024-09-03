#ejemplo de uso de listas
misnovias=["agripina","Anastacia","Maria"]
misnumeros=[666,77,10]
# mostrando mis novias
print (misnovias)
#mostrando mis numeros
print (misnumeros)
print ("----accendiento a los elementos de la lista----")
print(misnovias[0])
if "agrpina" in misnovias:
    print("si,´agripina´ esta en la lista de mis novias")
else:
    print("chale no eres mi novia")
print("numeros de novias")
nnovias=len(misnovias)
print(f"numero de novias={nnovias}")
print("ciclo for en listas")
posicion =0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1