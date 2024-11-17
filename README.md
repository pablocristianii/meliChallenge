# API de Pokémon - Challenge Técnico

Esta es una API desarrollada en Python con Flask como parte de un challenge técnico para la empresa XXX. La API interactúa con la [PokeAPI](https://pokeapi.co/) para obtener información sobre los Pokémon.

## Endpoints

### 1. Obtener el tipo de un Pokémon

**Método:** `GET`  
**Ruta:** `/pokemon/<nombre>`  

#### Descripción:
Este endpoint recibe el nombre de un Pokémon y devuelve los tipos asociados (por ejemplo, fuego, agua, tierra, aire, etc.).

#### Parámetros:
- `nombre` (ruta): El nombre del Pokémon cuyo tipo se desea obtener. El nombre debe estar en minúsculas.

#### Respuesta:
Si el Pokémon existe, la respuesta será un JSON con el nombre del Pokémon y sus tipos.

**Ejemplo:**
```json
{
    "name": "charizard",
    "types": ["fire", "flying"]
}



