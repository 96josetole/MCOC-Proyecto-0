# MCOC-Proyecto-0
MCOC-Proyecto-0
# Introduccion
La perdida de significancia ocurre en calculos numericos realizados en computador debido a que se considera una menor cantidad de cifras significativas. Dicho fenomeno se ve reflejado en el siguiente ejemplo.
# Perdida de significancia en calculo de desviacion estandar 
En este caso se aborda la operacion de calculo de desviacion estandar `np.std` de una muestra de datos, donde se percibe una perdida de significancia notable al hacer uso de datos `dtype=np.float16`. El ejemplo a plantear en este documnto, es una discusion mas elaborada de lo que se encuentra especificado en la [documentación de scipy] (https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.std.html).

Se comparan los siguientes procesos de calculo de desviacion estandar:

 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `np.std`. 
 2. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `np.std` con un acumulador interno de tipo `np.float64`. 
 3. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `np.std` con un acumulador interno de tipo `np.float16`.
 4. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar una función de desviacion estandar `stdev64`, donde en su definicion se utilizo el calculo de promedio `np.mean` con un acumulador interno de tipo `np.float64`. 
 5. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar una función de desviacion estandar `stdev64`, donde en su definicion se utilizo el calculo de promedio `np.mean` con un acumulador interno de tipo `np.float32`.

