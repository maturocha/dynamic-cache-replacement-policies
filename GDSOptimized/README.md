## Sinopsis

Implementación de la técnica de Algoritmos de reemplazo GDS basada en el uso de Listas enlazadas y nodos, para entender su concepto.

Es una versión optimizada del algoritmo original, ante la necesidad de mejorar la eficiencia del mismo a la hora de actualizar no realiza la búsqueda lineal del elemento sino que siempre agrega y mantiene en una estructura auxiliar el valor del score actualizado.


## Politica de desalojo

GDS. Elimina el nodo con menor score H, donde H = L + 1 / costo(elemento) * Frecuencia (elemento)

Los costos de los elementos se calcularon en base a una colección procesada en Terrier, a la cual se le calculo el tiempo en procesar determinadas consultas.

##Metricas

Hit Ratio fue la metrica principal por la cual se midio, como asi también el tiempo de procesamiento.


## Motivacion

Script realizado bajo el proyecto de pasantía rentada de la UNLU


## Ejecucion

Para la ejecución del mismo:

Modificar el archivo de test.txt, con los valores de TAMAÑO DE CACHE, WARM-UP, QUERYS DE TESTEOS respectivamente.

Ejecutar script.py, el cual levantará automaticamente ese archivo.

## Autor

Matías Rocha
