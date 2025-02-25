import sqlite3
import requests

# Database setup for Pokemon
def setup_database():
    """Creates a SQLite database and a table for storing Pokémon details."""
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            height INTEGER,
            weight INTEGER,
            base_experience INTEGER
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(identifier):
    """Fetches Pokémon details from the PokéAPI using either name or ID."""
    url = f"{base_url}{identifier}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "id": pokemon_data["id"],
            "name": pokemon_data["name"].capitalize(),
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "base_experience": pokemon_data["base_experience"]
        }
        return pokemon_info
    else:
        return None

def add_pokemon_to_db(pokemon):
    """Adds a Pokémon's details to the database."""
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (id, name, height, weight, base_experience) VALUES (?, ?, ?, ?, ?)",
                   (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"], pokemon["base_experience"]))
    conn.commit()
    conn.close()
    print(f"{pokemon['name']} added to the database!")

def remove_pokemon_from_db(pokemon_id):
    """Removes a Pokémon from the database using its ID."""
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))
    conn.commit()
    conn.close()
    print(f"Pokémon with ID {pokemon_id} removed from the database!")

def display_pokemon_info(pokemon_info):
    """Displays Pokémon details in a clean, formatted output."""
    print("\nPokémon Details:")
    print(f"ID: {pokemon_info['id']}")
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Base Experience: {pokemon_info['base_experience']}")

def main():
    """Runs the interactive menu for Pokémon database management."""
    while True:
        print("\nPokémon Database Menu:")
        print("1. Get Pokémon by ID")
        print("2. Get Pokémon by Name")
        print("3. Add Pokémon to Database")
        print("4. Remove Pokémon from Database")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            pokemon_id = input("Enter Pokémon ID: ")
            pokemon_info = get_pokemon_info(pokemon_id)
            if pokemon_info:
                display_pokemon_info(pokemon_info)
            else:
                print("Pokémon not found!")
        
        elif choice == "2":
            pokemon_name = input("Enter Pokémon Name: ")
            pokemon_info = get_pokemon_info(pokemon_name.lower())
            if pokemon_info:
                display_pokemon_info(pokemon_info)
            else:
                print("Pokémon not found!")
        
        elif choice == "3":
            pokemon_name = input("Enter Pokémon Name to add: ")
            pokemon_info = get_pokemon_info(pokemon_name.lower())
            if pokemon_info:
                add_pokemon_to_db(pokemon_info)
            else:
                print("Pokémon not found!")
        
        elif choice == "4":
            pokemon_id = input("Enter Pokémon ID to remove: ")
            remove_pokemon_from_db(pokemon_id)
        
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
