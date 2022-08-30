Previamente, conocimos la forma de acceder a una columna particular pero hasta ahora no accedimos a una fila específica. Para hacerlo contamos con `iloc` que también lo utilizaremos con corchetes `[]`. Por ejemplo, si quisiéramos obtener la quinta fila de nuestro dataset deberíamos hacer:

```python
cines.iloc[4]
```

¿Por qué 4 si es la quinta fila? Porque al igual que las listas, las filas empiezan desde la posición 0.

¡Pongámoslo en práctica!

> Obtené la séptima fila de nuestro DataFrame cines.
