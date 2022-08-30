¡Esto es un desorden!

Pero traemos buenas noticias, podemos ordenar nuestros DataFrames por la columna que queramos y no eso no es todo ¡podemos hacerlo al derecho y al revés!

`sort_values` es una función infija que nos permite ordenar nuestras tablas a partir de una columna haciendo `tabla.sort_values(nombre_columna)`. Por defecto lo hará de forma ascendente. Por ejemplo, si la columna elegida es numérica ordenará de menor a mayor, pero si es de strings lo hará en orden alfabético.

Si en cambio queremos que el ordenamiento sea descendente debemos hacer `tabla.sort_values(nombre_columna, ascending=False)`

¡Probémoslo!

> Escribí lo siguiente en la consola:
>
```python
cines.sort_values("COLUMNA")
```
>
```python
cines.sort_values("COLUMNA", ascending=False)
```
>
```python
cines.sort_values("COLUMNA NUMERICA")
```
>
```python
cines.sort_values("COLUMNA NUMERICA", ascending=False)
```
