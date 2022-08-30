¡Perfecto!

En la última consulta probablemente hiciste algo como:

```python
len(cines[COLUMNA].unique())
RETORNO
```

Como esta operación es tan común, contamos con un atajo, la función infija `nunique`:

```python
cines[COLUMNA].nunique()
RETORNO
```
