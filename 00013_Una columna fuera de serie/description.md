Ya sabemos que a lo que llamamos tabla `pandas` lo llama `DataFrame`. De la misma forma, lo que llamamos columna `pandas` lo llama `Series`. ¡Sí, en plural aunque sea una! 

```python
type(librerias[COLUMNA])
COMPLETAR
```

Esto significa que cada DataFrame está compuesto por muchas Series. Algo muy interesante es que hay funciones y procedimientos que funcionan tanto con los DataFrames como con los Series. Por ejemplo, de la misma forma que podemos obtener las primeras y últimas filas de una tabla, también podemos obtener los primeros valores de una columna.

> Probá en la consola lo siguiente en orden:
>
```python
librerias["COLUMNA"].head(3)
```
>
```python
librerias["OTRA_COLUMNA"].tail(4)
```
