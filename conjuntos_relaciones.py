# Notación de conjuntos 

A = set({1, 2, 3, 4})  # Notación de Conjuntos

def verificar_extension(A): #verificacion del conjunto A
    if set(A) == {1,2,3,4}: 
        print(" A contine los valores esperados. ")
         
    else :
        print(" El conjunto A no contiene los valores esperados ")

verificar_extension(set(A)) # envia los valores a la funcion
print(" El conjunto de valoes de A son: ", A)

B = set ({i for i in range(1, 21) if i%2 == 0}) #comprension de valores

def verificar_conjuntos(conjunto,n): #verificacion del conjunto B
    if set(conjunto) == {2,4,6,8,10,12,14,16,18,20}: 
        print(f" El conjunto {n} contiene los valores esperados. ")
        print(" El conjunto de valores pares de B son: ", conjunto)
    else : 
        print(f" El conjunto {n} no contiene los valores esperados ")
        print(" El conjunto de valores pares de B son: ", conjunto)

verificar_conjuntos(list(B), "B") # envia los valores a la funcion

# Cardinalidad
cardinalidad_a = len(A) #longitud de A

def verificar_cardinalidad(A, esperado): #verificacion de la cardinalidad
    if len(A) == esperado:
        print(f" La cardinalidad del conjunto A es correcta, el valor esperado es {esperado} ")
    else:
        print(f" La cardinalidad del conjunto A es incorrecta, el valor esperado es {esperado} ")

verificar_cardinalidad(A, 4) # envia los valores a la funcion

#conjuntos infinitos(Simulacion con cortes finitos)
for n in range (1,101):
    print(n)

longitud = len(range (1,101))
def verificar_tamaño(longitud, tamaño): #verificacion del ciclo
    #verifica que la longitud del conjunto dea correcta
    if longitud == tamaño:
        print(f" La longitud del conjunto es la correcta {tamaño}")
    else:
        print(f" la longitud es incorrecta, la longitd esperada es{tamaño}")

verificar_tamaño(longitud, 100)

#operaciones con conjuntos
union = set(A).union(set(B))
interseccion = set(A).intersection(set(B))
diferencia = set(A).difference(set(B))
diferencia_simetrica = set(A).symmetric_difference(set(B))

print(" La Union de A y B es: ", union)
print(" La Interseccion de A y B es: ", interseccion)
print(" La Diferencia de A y B es: ", diferencia)
print(" La Diferencia Simetrica de A y B es: ", diferencia_simetrica)

def verificacion(A, B, resultado, n):
    if resultado == set(A).union(set(B)): #Verifica si el resultado de una operación es el esperado.
        print(f" La {n} es correcta: {resultado}")
    else:
        print(f" La {n} es incorrecta: {resultado}")
#Envia los valores a la funcion verificar
verificacion(set(A),set(B), union, "Union")
verificacion(set(A),set(B), interseccion, " Interseccion")
verificacion(set(A),set(B), diferencia, " Diferencia")
verificacion(set(A),set(B), diferencia_simetrica, "Diferencia Simetrica")

# Definición del conjunto universal
U = set(range(1, 21))
print("El conjunto universal U es:", U)

# Complemento de A
complemento_A = U.difference(A)
print("El complemento de A (U - A) es:", complemento_A)

# Función de verificación del complemento
def verificar_complemento(original, complemento, universal):
    union_complemento = original.union(complemento)# La unión de un conjunto y su complemento debe ser el conjunto universal
    interseccion_complemento = original.intersection(complemento)# La intersección de un conjunto y su complemento debe ser un conjunto vacío
    
    if union_complemento == universal and interseccion_complemento == set(): #verificacion del complemento
        print(" La verificación del complemento de A es correcta.")
    else:
        print(" La verificación del complemento de A es incorrecta.")

verificar_complemento(A, complemento_A, U)#Llamada a la función de verificación

producto_cartesiano_AB = {(a, b) for a in A for b in B}# Producto cartesiano de A y B
print("El producto cartesiano de A y B es:", producto_cartesiano_AB)

# Función de verificación del producto cartesiano
def verificar_productocartesiano(conjunto1, conjunto2, resultado):
    tamaño = len(conjunto1) * len(conjunto2) #Tamaño del  producto cartesiano
    
    if len(resultado) == tamaño: #verificacion del producto cartesiano
        print(f" La verificación del producto cartesiano es correcta. El tamaño es {len(resultado)}.")
    else:
        print(f" La verificación del producto cartesiano es incorrecta. El tamaño esperado era {tamaño}, pero se obtuvo {len(resultado)}.")

# Llamada a la función de verificación
verificar_productocartesiano(A, B, producto_cartesiano_AB)
#RELACIONES
#conjuntos
C = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}

# Reflexiva
def reflexiva(relacion, conjunto):
    return all((x, x) in relacion for x in conjunto)

print(f"Relación R: {R}")
print(f"Conjunto C: {C}")

# Simétrica
def simetrica(relacion):
    return all((y, x) in relacion for x, y in relacion)

# Antisimétrica
def antisimetrica(relacion):
    for x, y in relacion:
        if (y, x) in relacion and x != y:
            return False
    return True

# Transitiva
def transitiva(relacion):
    for a, b in relacion:
        for c, d in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True

# Verificación de propiedades para R
print(f"Reflexiva: {reflexiva(R, C)}")
print(f"Simétrica: {simetrica(R)}")
print(f"Antisimétrica: {antisimetrica(R)}")
print(f"Transitiva: {transitiva(R)}")

# Relaciones de Equivalencia y de Orden
def verificar_relacion_equivalencia(relacion, conjunto):
    return reflexiva(relacion, conjunto) and simetrica(relacion) and transitiva(relacion)

def verificar_relacion_orden(relacion, conjunto):
    return reflexiva(relacion, conjunto) and antisimetrica(relacion) and transitiva(relacion)

#relación de equivalencia
R_equivalencia = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)}
print(f" Relación : {R_equivalencia}")
print(f" Es una relación de equivalencia: {verificar_relacion_equivalencia(R_equivalencia, C)}")

#relación de orden
r_orden = {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)}
print(f" Relación: {r_orden}")
print(f"Es una relación de orden: {verificar_relacion_orden(r_orden, C)}")

# Funciones
dominio = {1, 2, 3, 4, 5}
codominio = {2, 4, 6, 8, 10}
f1 = { (x, 2 * x) for x in dominio } # f(x) = 2x

dominio2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
codominio2 = {0, 1, 2}
f2 = { (x, x % 3) for x in dominio2 } # f(x) = x mod 3

dominio3 = {1, 2, 3}
codominio3 = {2, 3, 4}
f3 = { (x, x + 1) for x in dominio3 } # f(x) = x + 1

# Inyectiva
def inyectiva(funcion):
    valores_imagen = [par[1] for par in funcion]
    return len(valores_imagen) == len(set(valores_imagen))

print(f"Función f(x) = 2x: {f1}")
print(f"Es inyectiva: {inyectiva(f1)}")

#Sobreyectiva
def sobreyectiva(funcion, codominio):
    valores_imagen = {par[1] for par in funcion}
    return valores_imagen == codominio

print(f"Función f(x) = x mod 3: {f2}")
print(f"Codominio: {codominio2}")
print(f"Es sobreyectiva: {sobreyectiva(f2, codominio2)}")

# Biyectiva: es inyectiva y sobreyectiva
def biyectiva(funcion, codominio):
    return inyectiva(funcion) and sobreyectiva(funcion, codominio)

print(f"\nFunción f(x) = x + 1: {f3}")
print(f"Codominio: {codominio3}")
print(f"Es biyectiva: {biyectiva(f3, codominio3)}")

# clausuras
R_original = {(1, 2), (2, 3)} #relacion original
print(f"Relación original: {R_original}")

#Clausura Reflexiva
def clausura_reflexiva(relacion, conjunto):
    return relacion.union({(x, x) for x in conjunto})

R_reflexiva = clausura_reflexiva(R_original, C)
print(f"Clausura Reflexiva: {R_reflexiva}")
print(f"Es reflexiva: {reflexiva(R_reflexiva, C)}")

#Clausura Simétrica
def clausura_simetrica(relacion):
    return relacion.union({(y, x) for x, y in relacion})

R_sim = clausura_simetrica(R_original)
print(f"Clausura Simétrica: {R_sim}")
print(f"Es simétrica: {simetrica(R_sim)}")

#Clausura Transitiva
def clausura_transitiva(relacion):
    clausura = set(relacion)
    while True:
        nueva_clausura = clausura.union({(a, c) for a, b in clausura for c, d in clausura if b == c})
        if nueva_clausura == clausura:
            return clausura
        clausura = nueva_clausura

R_transitiva = clausura_transitiva(R_original)
print(f"Clausura Transitiva: {R_transitiva}")
print(f"Es transitiva: {transitiva(R_transitiva)}")

# Clausura de Equivalencia: aplicada a las 3 clausuras
def clausura_equivalencia(relacion, conjunto):
    paso1 = clausura_reflexiva(relacion, conjunto)
    paso2 = clausura_simetrica(paso1)
    return clausura_transitiva(paso2)

R_eq_clausura = clausura_equivalencia(R_original, C)
print(f"Clausura de Equivalencia: {R_eq_clausura}")
print(f"Es una relación de equivalencia: {verificar_relacion_equivalencia(R_eq_clausura, C)}")


"""Universidad de Panamá
Centro Regional Universitario de Coclé
Lic. Ing. Informática

Materia: 
Informática teórica(INF 221)

Profesor:
Luis Domínguez 
Estudiantes: 
Giovanni Coronado
Jose Conte
Marielys Quiroz

Fecha: 
18-09-2025





Notación de conjuntos:
Extensión: 
Para describir los elementos de un determinado conjunto los puedes mencionar uno a uno, a esto se conoce como descripción por extensión.  Definamos como el conjunto conformado por los colores del arco iris, en este caso podemos describir el conjunto por extensión así:
Ejemplo: 
Q= {naranja, amarillo, verde, azul}

Comprensión:
Se puede entonces describir los conjuntos mencionando las características que comparten los elementos que los conforman.  Por ejemplo, si es el conjunto conformado por todos los países del mundo se puede escribir:
C = {x|x es un país}
En donde la barra | se lee como “tales que”.  Así, la anterior expresión se lee: “es el conjunto de los tales que es un país”.  En este caso el símbolo es usado simplemente para representar los elementos del conjunto.
Cardinalidad:
La cardinalidad se refiere al número que se obtiene al contar algo. Por lo tanto, la cardinalidad de un conjunto es el número de elementos que lo componen. 
Ejemplo: 
el conjunto {1, 2, 3, 4, 5} tiene una cardinalidad de cinco, que es mayor que la de {1, 2, 3}, que es tres.

Conjuntos infinitos: 
Los conjuntos infinitos son aquellos que contienen una cantidad ilimitada de elementos. Es decir, aquellos que se extienden de forma indefinida.
el conjunto de números naturales enteros es infinito, pero es numerable, pues es posible identificar el elemento 1, 2, 3, etc.


Operaciones con conjuntos:
Unión: 
La unión de dos o más conjuntos da como resultado un conjunto completamente nuevo que contiene una combinación de elementos presentes en ambos conjuntos.
Ejemplo: 
dos conjuntos A y B, donde A = {a, b, j, k} y B = {h, t, k, c}. Por lo tanto, los elementos de ambos conjuntos son a, b, c, j, k, h, t. 
Intersección: 
La intersección de conjuntos es el conjunto de elementos comunes a los conjuntos dados, es decir; los elementos del conjunto A que también están presentes en el conjunto B.
Ejemplo: 
A: {A, B, C, D} B: {B, E, C, D, J} 
Diferencia: 
La diferencia de dos conjuntos A y B se define como las listas de todos los elementos que están en el conjunto A pero que no están presentes en el conjunto B. 
Ejemplo: si A = {1, 2, 3} y B = {3, 5, 7}, entonces A - B es {1, 2}, ya que 1 y 2 están en A, pero no en B.
Diferencia simétrica:
La diferencia simétrica entre dos conjuntos, denotada, es el conjunto de elementos que pertenecen a uno de los conjuntos, pero no a ambos a la vez. 
Ejemplo: 
A = {1, 2, 3, 4} y B = {3, 4, 5, 6}, 
{1,2} (elementos en A pero no en B).
{5, 6} (elementos en B pero no en A).
Diferencia simétrica = {1, 2} {5, 6} = {1, 2, 5, 6}.
Complemento:
El complemento de un conjunto es el conjunto que incluye todos los elementos del conjunto universal que no están presentes en el conjunto dado.
Ejemplo: 
U= {1,2,3,5,6}
A={1,2,3}
Aª={4,5,6}
Producto cartesiano: 
El producto cartesiano es el producto de dos conjuntos cualesquiera , pero este producto está ordenado, es decir, el conjunto resultante contiene todos los pares posibles y ordenados, de modo que el primer elemento del par pertenece al primer conjunto y el segundo al segundo. 
Ejemplo: 
A × B = {(1, a), (1, b), (1, c), (2, a), (2, b), (2, c)}.
Relaciones y funciones 
Reflexiva: 
La relación reflexiva es una relación entre los elementos de un conjunto A, de modo que cada elemento del conjunto está relacionado consigo mismo.
Ejemplo: 
Sea A = {a, b, c, d, e} y R es una relación definida en A como R = {(a, a), (a, b), (b, b), (c, c), (d, d), (e, e), (c, e)}. Como (a, a), (b, b), (c, c), (d, d), (e, e), entonces R es una relación reflexiva ya que cada elemento de A está relacionado consigo mismo en R.
Simétrica: 
la relación simétrica se define como una relación binaria R en X si, y solo si, un elemento a está relacionado con b, entonces b también está relacionado con a para cada a, b en X.
Ejemplo: 
el conjunto A = {1, 2, 3} y la relación R = {(1, 2), (2, 1), (3, 3)}, entonces R es simétrica porque por cada par ordenado existe su inverso 


Antisimétrica: 
Una relación antisimétrica en un conjunto A es aquella donde, si un elemento 'a' está relacionado con 'b' y 'b' está relacionado con 'a', entonces 'a' debe ser igual a 'b'.
Ejemplo:
La relación "≤" (menor o igual que) en el conjunto de números enteros es antisimétrica. Si a ≤ b y b ≤ a, esto implica que a = b.
Transitiva:
Las relaciones transitivas son relaciones binarias definidas en un conjunto, de modo que si el primer elemento está relacionado con el segundo, y este con el tercero, entonces el primer elemento debe estarlo con el tercero. 
Ejemplo: 
para tres elementos a, b, c del conjunto A, si a = b y b = c, entonces a = c. 
Funciones
Inyectiva: 
Una función inyectiva f es si cada elemento del conjunto final Y tiene un único elemento del conjunto inicial X al que le corresponde. Es decir, no pueden haber más de un valor de X que tenga la misma imagen Y.
Ejemplo: 
La función f(x) = 2x+1 , con los elementos de su dominio restringidos a los números reales positivos, es inyectiva.

Sobreyectiva:
Una función sobreyectiva (o suprayectiva) f es una función tal que todos los elementos del conjunto final Y tienen al menos un elemento del conjunto inicial X al que le corresponde.
Ejemplo: 
la función en los números reales definida por f(x) = x+1. Es una función sobreyectiva. 


Biyectiva:
Una función biyectiva conecta elementos de dos conjuntos de tal manera que es inyectiva y sobreyectiva. 
Ejemplo:
A y B con el dominio del conjunto A y el codominio del conjunto B, de modo que cada elemento de A se relaciona con un elemento distinto de B, y cada elemento del conjunto B es la imagen de algún elemento del conjunto A.
Clausuras:
Reflexiva: 
 Es la relación más pequeña que contiene una relación dada y también cumple la propiedad de reflexividad. 
Ejemplo: 
una relación sobre el conjunto A={1, 2}. Si la relación R = {(1, 2)} se completa reflexivamente, se convierten en R' = {(1, 2), (1, 1), (2, 2)}. 

Simétrica: 
La clausura simétrica de una relación es la relación simétrica más pequeña que contiene la relación original. Se obtiene uniendo la relación original con su relación inversa. 
Ejemplo: 
Consideremos la relación R en el conjunto A = {1, 2, 3} dada por los pares ordenados (1, 2) y (3, 3). 
Relación original(R): {(1, 2), (3, 3)} 
Relación Inversa (R⁻¹): R⁻¹ es {(2, 1), (3, 3)}. 
Clausura Simétrica (S): La clausura simétrica se forma al unir R y R⁻¹. 
S = {(1, 2), (3, 3)} ∪ {(2, 1), (3, 3)}
S = {(1, 2), (3, 3), (2, 1)} 



Transitiva: 
La clausura transitiva de una relación es una nueva relación que incluye todas las conexiones directas e indirectas de la relación original.
Ejemplo: 
Si a – b es un entero y b – c es un entero, entonces (a – b) + (b – c) = a – c es un entero; en consecuencia, R es transitiva.

Equivalencia: 
una relación en un conjunto A se denomina relación de equivalencia si es reflexiva, simétrica y transitiva. Esto significa que si una relación cumple estas tres propiedades, se considera una relación de equivalencia y nos ayuda a agrupar elementos u objetos similares.
Ejemplo: 
Sea N el conjunto de los números naturales: N={0,1,2,3…8,9,10} y consideremos el conjunto NxN que consiste de todas las parejas
ordenadas de números naturales, donde ordenadas quiere decir que (2,4) no es lo mismo que (4,2). """

#Enlace del repositorio: https://github.com/Kan-25/Laboratorio_1.git