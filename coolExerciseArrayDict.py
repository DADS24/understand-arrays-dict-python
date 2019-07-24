a = [24,83,{'a':8,'b':'a'},[100,123],{}]

#Acceder al valor 100
print(a[3][0])

#insertar un número en el array
a[3].append(24)
print(a[3])

#Acceder al valor de la propiedad 'b' del dict
print(a[2]['b'])

#Insertar un numero en el diccionario vacio
a[4]=23
print(a[4])

#Guardar en una variable el array completo
myVar = a[3]
print(myVar)

#Guardar en una variable el dict en pos INDEX =2
myVar2 = a[2]
print(myVar2)

#Meter dict en pos INDEX =2 en el dict vacio
a[4] = a[2]
print(a[4])

# 2 teniendo el siguiente diccionario:

garaje = {
    'puertas':2,
    'equipo':['abs','llantas','xenon'],
    'ruedas':5,
    'rueda_repuesto':True,
    'owners':{
        'cantidad':3,
        'accidentes':0,
        'provincias':['santander','cadiz'] 
    }
} 

# Acceder a la palabra 'llantas'
print(garaje['equipo'][1])

# Acceder al valor de accidentes
print(garaje['owners']['accidentes'])

#Insertar string en el array equipo
garaje['equipo'].append('sensei')
print(garaje['equipo'])

#cambiar el valor de rueda_repuesto
garaje['rueda_repuesto'] = False
print(garaje['rueda_repuesto'])

#obtener el valor de cadiz en owners
print(garaje['owners']['provincias'][1])