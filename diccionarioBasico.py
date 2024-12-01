#diccionarios
# estructura de datos que almacena pares clave-valor, permitiendo un acceso rápido a los valores mediante sus claves únicas
# valores de la izquierda se llaman key/llaves (no se repiten...) y valores de la derecha se llaman values/valores
#si alguna llave se repite este sobreescribe el valor de la llave al nuevo valor agregado...

palabras = {
            'blanco': 'white',
            'negro': 'black',
            'morado': 'purple',
            'gris': 'gray',
           }
opcion = ""
while opcion != "salir":
   print("Digite 1 para traducir palabra")
   print("Digite 2 para borrar palabra")
   print("Digite 3 para mostrar diccionario")
   opcion=input("Digite una opcion (digite salir para terminar): ").lower()
   if opcion == "1":
      color=input("Digite el color: ").lower()
      if color in palabras:
         print(palabras[color])
      else:
         if color != "salir":
            print("no conozco ese color")
            print("solo conozco estas palabras")
            print(palabras.keys())
            traduccion=input("Digita por favor la traduccion del color "+color+": ")
            palabras[color]=traduccion
            print("Palabra agregada")
   elif opcion == "2":
      color=input("Digite el color: ").lower()
      if color in palabras:
         del palabras[color]
         print("Palabra eliminada")
   elif opcion == "3":
      print(palabras)
   else:
      print("Gracias")
