# Documentación de la API

## Obtener todos los posts

### Request

```
GET /get_posts/
```

### Response

Devuelve un objeto JSON con un array de todos los posts.

```json
{
    "respone": "OK",
    "data": [
        {
            "id": 1,
            "title": "First post",
            "content": "This is the first post",
            "author": "John Doe"
        },
        // ...
    ]
}
```

## Obtener un post por ID

### Request

```
GET /get_post/<id>
```

Reemplace `<id>` con el ID del post que desea obtener.

### Response

Devuelve un objeto JSON con el post solicitado.

```json
{
    "respone": "OK",
    "data": [
        {
            "id": 1,
            "title": "First post",
            "content": "This is the first post",
            "author": "John Doe"
        }
    ]
}
```

## Crear un usuario

### Request

```
POST /new_user/
```

En el cuerpo del request, incluya un objeto JSON con el nickname del nuevo usuario.

```json
{
    "name": "John Doe"
}
```

### Response

Devuelve un objeto JSON con el usuario recién creado.

```json
{
    "respone": "OK",
    "data": {
        "id": 1,
        "nickname": "John Doe"
    }
}
```

## Crear un post

### Request

```
POST /new_post/
```

En el cuerpo del request, incluya un objeto JSON con el título, el contenido y el autor del nuevo post.

```json
{
    "tittle": "First post",
    "content": "This is the first post",
    "author": "John Doe"
}
```

### Response

Devuelve un objeto JSON con el post recién creado.

```json
{
    "respone": "OK",
    "data": {
        "id": 1,
        "title": "First post",
        "content": "This is the first post",
        "author": "John Doe"
    }
}
```

## Eliminar un usuario

### Request

```
DELETE /delete_user/<id>
```

Reemplace `<id>` con el ID del usuario que desea eliminar.

### Response

Devuelve un objeto JSON con un mensaje de éxito.

```json
{
    "response":"OK",
    "data":"User with id 1 deleted"
}
```

## Eliminar un post

### Request

```
DELETE /delete_post/<id>
```

Reemplace `<id>` con el ID del post que desea eliminar.

### Response

Devuelve un objeto JSON con un mensaje de éxito.

```json
{
    "response":"OK",
    "data":"Post with id 1 deleted"
}
```

## Modificar un usuario

### Request

```
PUT /modify_user/<id>
```

Reemplace `<id>` con el ID del usuario que desea modificar. En el

 cuerpo del request, incluya un objeto JSON con el nuevo nickname del usuario.

```json
{
    "name": "Jane Doe"
}
```

### Response

Devuelve un objeto JSON con un mensaje de éxito.

```json
{
    "response":"OK",
    "data":"User with id 1 changed name to Jane Doe"
}
```

## Modificar un post

### Request

```
PUT /modify_post/<id>
```

Reemplace `<id>` con el ID del post que desea modificar. En el cuerpo del request, incluya un objeto JSON con el nuevo título y contenido del post.

```json
{
    "tittle": "Modified post",
    "content": "This is a modified post"
}
```

### Response

Devuelve un objeto JSON con un mensaje de éxito y el post modificado.

```json
{
    "response":"OK",
    "data":{
        "id": 1,
        "title": "Modified post",
        "content": "This is a modified post",
        "author": "John Doe"
    }
}
```