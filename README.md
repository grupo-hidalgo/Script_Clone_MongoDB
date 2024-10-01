# Proyecto de Clonación de MongoDB y Consultas en Vertica

Este repositorio contiene un script de clonación de MongoDB que permite clonar toda una base de datos o colecciones específicas a otra base de datos en el mismo servidor o en uno diferente. 

## Tabla de Contenidos
1. [Clonación de MongoDB](#clonación-de-mongodb)
   - [Requisitos Previos](#requisitos-previos)
   - [Uso del Script de Clonación](#uso-del-script-de-clonación)
   - [Ejemplos](#ejemplos-de-uso)
   - [Funcionalidades](#funcionalidades)
   - [Validaciones](#validaciones)
   - [Manejo de Errores](#manejo-de-errores)
   

## Clonación de MongoDB

### Requisitos Previos
- **Python 3.x** instalado.
- Librería `pymongo` instalada:
  ```bash
  pip install pymongo
  ```

### Uso del Script de Clonación

El script de clonación de MongoDB puede utilizarse para clonar todas las colecciones de una base de datos o solo colecciones específicas a otra base de datos.

```bash
python clone_mongo.py --uri "<URI>" --source_db <BaseDeDatosOrigen> --target_db <BaseDeDatosDestino> [--collections <Colección1> <Colección2> ...]
```

#### Parámetros:
- `--uri`: La URI de conexión a MongoDB (por ejemplo, `mongodb+srv://usuario:contraseña@cluster.mongodb.net`).
- `--source_db`: Nombre de la base de datos de origen que deseas clonar.
- `--target_db`: Nombre de la base de datos de destino donde se copiarán las colecciones.
- `--collections`: Lista opcional de colecciones específicas a clonar. Si no se proporcionan, se clonan todas las colecciones de la base de datos de origen.

### Ejemplos de Uso

#### 1. Clonar toda la base de datos `sgc` a `sgc_dev`:
```bash
python clone_mongo.py --uri "mongodb+srv://usuario:contraseña@cluster.mongodb.net" --source_db sgc --target_db sgc_dev
```

#### 2. Clonar solo colecciones específicas de `sgc` a `sgc_dev`:
```bash
python clone_mongo.py --uri "mongodb+srv://usuario:contraseña@cluster.mongodb.net" --source_db sgc --target_db sgc_dev --collections collection1 collection2
```

### Funcionalidades
- **Clonación Completa**: Clona todas las colecciones de una base de datos a otra.
- **Clonación Selectiva**: Permite clonar colecciones específicas.
- **Manejo de Documentos Vacíos**: Si alguna colección está vacía, se notifica en la consola.

### Validaciones
- Verificación de que la colección tenga documentos antes de copiarla.
- Si no se especifica `--collections`, se clonan todas las colecciones de la base de datos.
- Si se especifican colecciones pero no existen en la base de datos de origen, se notifica en la consola.

### Manejo de Errores
- El script captura errores de conexión a MongoDB.
- Si una colección está vacía o no existe, el script no detiene el proceso y notifica en la consola.


## Contribuciones

Si deseas mejorar los scripts o agregar nuevas funcionalidades, puedes hacer un fork de este repositorio y enviar un pull request con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para más información.

---

Este README proporciona una descripción completa de ambos scripts, cubriendo tanto el clonador de MongoDB como el procesamiento de consultas en Vertica.