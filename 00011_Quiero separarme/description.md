Dejemos atrás los cines y cambiemos un poco nuestro lote de datos. Al comenzar esta lección te contamos que _csv_ es una extensión de archivos que tiene sus valores separados por comas. Sin embargo, a veces puede suceder que se utilice otro carácter para separar los valores, como por ejemplo, punto y coma: 

```csv
nombre;apellido;edad
Feli;Perez;24
Dani;Lopez;32
Juani;Vazquez;19
```

El problema es que en estos casos `read_csv` no funcionará :grimacing:. Pero que no cunda el pánico se soluciona muy fácil.

> El archivo con el que vamos a trabajar a partir de ahora está separado por `;`, para leerlo escribí en el editor de código:
> 
> ```python
> import pandas as pd
> pd.read_csv(LIBRERIAS, sep=";")
> ```
