Ahora que importamos la biblioteca `pandas`, el siguiente paso es conseguir un lote de datos, como por ejemplo, el listado de cines que hay que Argentina, cuya dirección es [ésta](CINES DE ARGENTINA),

Un vez que hayamos encontrado la dirección (y copiado en nuestro portapapeles 📋, para no tener que escribir la dirección a mano), podremos finalmente cargarla en un `DataFrame` llamado `cines` utilizando la función `pd.read_csv`:

```python
cines = pd.read_csv("LINK")
cines
```

> Probá éste código y observá qué sucede.
