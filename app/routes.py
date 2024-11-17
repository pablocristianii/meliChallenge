import random
import requests
from.auth import token_required
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/pokemon/<string:name>', methods=['GET'])
@token_required
def get_pokemon_type(name):
    """
    Obtiene los tipos de un Pokémon por su nombre usando la PokeAPI.
    """
    try:
        # Hacer la solicitud a la PokeAPI
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code != 200:
            return jsonify({"error": "Pokémon no encontrado"}), 404

        # Extraer datos del JSON
        data = response.json()
        types = [t['type']['name'] for t in data['types']]

        return jsonify({"name": name, "types": types}), 200
    except Exception as e:
        return jsonify({"error": "Error al procesar la solicitud", "details": str(e)}), 500

@api_bp.route('/pokemon/random/<string:type_name>', methods=['GET'])
@token_required
def get_random_pokemon_by_type(type_name):
    """
    Obtiene un Pokémon al azar de un tipo específico usando la PokeAPI.
    """
    try:
        # Hacer la solicitud a la PokeAPI para obtener Pokémon de ese tipo
        response = requests.get(f'https://pokeapi.co/api/v2/type/{type_name.lower()}')
        if response.status_code != 200:
            return jsonify({"error": "Tipo de Pokémon no encontrado"}), 404

        # Extraer la lista de Pokémon
        data = response.json()
        pokemons = data['pokemon']
        if not pokemons:
            return jsonify({"error": "No hay Pokémon de este tipo"}), 404

        # Elegir un Pokémon al azar
        random_pokemon = random.choice(pokemons)['pokemon']['name']

        return jsonify({"type": type_name, "pokemon": random_pokemon}), 200
    except Exception as e:
        return jsonify({"error": "Error al procesar la solicitud", "details": str(e)}), 500

@api_bp.route('/pokemon/longest/<string:type_name>', methods=['GET'])
@token_required
def get_longest_pokemon_name_by_type(type_name):
    """
    Obtiene el Pokémon con el nombre más largo de un tipo específico usando la PokeAPI.
    """
    try:
        # Hacer la solicitud a la PokeAPI para obtener Pokémon de ese tipo
        response = requests.get(f'https://pokeapi.co/api/v2/type/{type_name.lower()}')
        if response.status_code != 200:
            return jsonify({"error": "Tipo de Pokémon no encontrado"}), 404

        # Extraer la lista de Pokémon
        data = response.json()
        pokemons = data['pokemon']
        if not pokemons:
            return jsonify({"error": "No hay Pokémon de este tipo"}), 404

        # Encontrar el Pokémon con el nombre más largo
        longest_name_pokemon = max(pokemons, key=lambda p: len(p['pokemon']['name']))

        return jsonify({
            "type": type_name,
            "pokemon": longest_name_pokemon['pokemon']['name']
        }), 200
    except Exception as e:
        return jsonify({"error": "Error al procesar la solicitud", "details": str(e)}), 500
    

