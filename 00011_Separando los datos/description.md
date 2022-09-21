Al comenzar esta lección te contamos que _csv_ es una extensión de archivos que tiene sus valores separados por comas. Sin embargo, a veces puede suceder que se utilice otro carácter para separar los valores, como por ejemplo, punto y coma: 

```csv
nombre;apellido;edad
Feli;Perez;24
Dani;Lopez;32
Juani;Vazquez;19
```

El problema es que en estos casos `read_csv` no funcionará :grimacing:. Pero que no cunda el pánico que se soluciona muy fácil 😌.

> Dejemos atrás los cines y cambiemos nuestro lote de datos. El archivo con el que vamos a trabajar a partir de ahora está separado por `;`. Cargalo en una celda nueva haciendo lo siguiente…
> 
> ```python
> import pandas as pd # si en una celda anterior ya cargaste pandas,  
                                        # esta línea la podés omitir
> librerias = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1473087913&single=true&output=csv", sep=";")
> librerias
> ```
> 
> … y nos vemos en el ejercicio siguiente. 
