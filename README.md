## Búsqueda de ruta óptima entre distritos del Perú utilizando algoritmo de Fuerza Bruta en Grafos

#### I. PROPUESTA


**A) Objetivo de la propuesta**

Nuestra propuesta tiene como objetivo encontrar el camino de menor distancia de un distrito a otro en el Perú, pasando solamente una vez por cada uno y volviendo al punto inicial.

**B)	Técnica y metodología**

Frente a nuestra problemática, se ha decidido escoger el algoritmo de Dijkstra para implementarlo y poder dar solución a esta. El algoritmo de Dijkstra es el más usado para la minimización de rutas de transporte, pero también existen otros algoritmos o métodos que nos ayudan para este tipo de casos como Programación Dinámica, Backtracking, Método de Branch and Bound, entre otros. Por otro lado, al hacer la comparación de todos estos, el óptimo para encontrar el camino más corto entre dos nodos (distritos) fue el de Dijkstra, consiguiendo así con mayor seguridad, la ruta de menor costo total en km. Por último, con este se pueden enumerar todas las rutas posibles y poder obtener el número total de rutas válidas.


#### II.	DISEÑO DEL APLICATIVO


**A)	Análisis de los requisitos**

1)	Valor del producto

Como se ha mencionado anteriormente, la importancia de esta propuesta radica en la oportunidad que se tiene para impulsar el turismo descentralizado en el Perú al conseguir encontrar la mejor ruta para llegar los atractivos turísticos menos reconocidos del País. Por un lado, muchos turistas se ven beneficiados al encontrar nuevos destinos mágicos para visitar, mientras que los distritos se beneficiarán observando una mejora en su economía gracias al turismo.

2)	Público objetivo

El público para el cual está enfocada esta propuesta de software comprende a turistas y viajeros entusiastas por conocer la ruta óptima para recorrer los atractivos turísticos de los distintos distritos del Perú.

3)	Uso previsto

Al usar la aplicación, los turistas tendrán la oportunidad de:

•	Ingresar su distrito de origen y de destino.

•	Añadir distritos intermedios a su ruta.

•	Visualizar la ruta óptima.

•	Visualizar rutas alternativas.

Asimismo, podrán acceder a las funcionalidades secundarias como:

•	Registrarse e iniciar sesión en la plataforma.

•	Exportar las rutas encontradas a un documento de texto.

•	Exportar imágenes del grafo con las rutas encontradas.

4)	Requisitos funcionales

Para asegurar que la solución de software funcione de manera correcta, estos son algunos de los requisitos funcionales que se establecieron:

•	El programa debe soportar la lectura de datasets con 1500 registros.

•	El usuario debe ingresar un distrito de origen y de destino obligatoriamente.

•	El sistema debe permitir agregar un máximo de 5 distritos intermedios a la ruta.

•	El grafo debe contar con una leyenda, para identificar fácilmente a los distritos en la ruta encontrada.

5)	Requisitos no funcionales

Algunos de los requisitos no funcionales que permitirán controlar a los requisitos funcionales y garantizar la correcta participación de los usuarios, son:

•	El sistema debe contar con un breve manual de usuario.

•	El usuario debe iniciar sesión para acceder a funcionalidades como ‘Guardar grafo’ o ‘Guardar ruta’.

•	El sistema debe mostrar mensajes de error cuando ocurra una falla en el sistema, como una entrada incorrecta del usuario.

•	El sistema debe permitir exportar el grafo como imagen y/o la ruta encontrada en formato de texto.

•	Los campos de entrada deben estar bien definidos y ser fáciles de identificar para los usuarios.
