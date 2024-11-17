# API de Pokémon - Challenge Técnico

Esta es una API desarrollada en Python con Flask como parte de un challenge técnico para la empresa Mercado Libre. La API interactúa con la [PokeAPI](https://pokeapi.co/) para obtener información sobre los Pokémon.

## *Endpoints*

### **1. /auth/login**
- *Método:* POST
- *Descripción:* Permite a un usuario autenticarse y obtener un token JWT.

#### *Ejemplo de Solicitud*
json
POST /auth/login
Content-Type: application/json
{
    "username": "admin",
    "password": "password123"
}


#### *Respuesta Exitosa*
json
200 OK
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}


#### *Errores Comunes*
- *Credenciales incorrectas:*
  json
  401 Unauthorized
  {
      "error": "Credenciales inválidas"
  }
  

---

### **2. /pokemon/<string:name>**
- *Método:* GET
- *Descripción:* Obtiene los tipos de un Pokémon específico.
- *Autenticación requerida:* Sí (Authorization: Bearer <token>).

#### *Ejemplo de Solicitud*
http
GET /pokemon/pikachu
Authorization: Bearer <token>


#### *Respuesta Exitosa*
json
200 OK
{
    "name": "pikachu",
    "types": ["electric"]
}


#### *Errores Comunes*
- *Pokémon no encontrado:*
  json
  404 Not Found
  {
      "error": "Pokémon no encontrado"
  }
  
- *Token inválido o faltante:*
  json
  401 Unauthorized
  {
      "error": "Token no proporcionado"
  }
  

---

### **3. /pokemon/random/<string:type_name>**
- *Método:* GET
- *Descripción:* Devuelve un Pokémon al azar de un tipo específico.
- *Autenticación requerida:* Sí.

#### *Ejemplo de Solicitud*
http
GET /pokemon/random/fire
Authorization: Bearer <token>


#### *Respuesta Exitosa*
json
200 OK
{
    "type": "fire",
    "pokemon": "charmander"
}


#### *Errores Comunes*
- *Tipo de Pokémon no encontrado:*
  json
  404 Not Found
  {
      "error": "Tipo de Pokémon no encontrado"
  }
  

---

### **4. /pokemon/longest/<string:type_name>**
- *Método:* GET
- *Descripción:* Devuelve el Pokémon con el nombre más largo de un tipo específico.
- *Autenticación requerida:* Sí.

#### *Ejemplo de Solicitud*
http
GET /pokemon/longest/grass
Authorization: Bearer <token>


#### *Respuesta Exitosa*
json
200 OK
{
    "type": "grass",
    "pokemon": "tangrowth"
}


#### *Errores Comunes*
- *No hay Pokémon de este tipo:*
  json
  404 Not Found
  {
      "error": "No hay Pokémon de este tipo"
  }
  

---

## *Autenticación*
La API utiliza autenticación basada en tokens JWT. Sigue estos pasos para autenticarte:

1. *Solicita un token JWT* haciendo un POST a /auth/login con las credenciales correctas.
2. *Incluye el token* en el encabezado Authorization en los endpoints protegidos:
   
   Authorization: Bearer <token>
   

3. Los tokens expiran después de 1 hora. Si el token expira, debes autenticarte nuevamente.

---





