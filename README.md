Pokémon Database Manager
This Python script connects to the PokéAPI to fetch Pokémon details and stores them in a local SQLite database. It provides an interactive menu for the user to retrieve, add, and remove Pokémon from the database.

Features:
- Fetch Pokémon details by ID or Name from the PokéAPI.
- Store Pokémon data in a SQLite database for easy access.
- Remove Pokémon from the database when no longer needed.
- Simple menu-based interface for easy navigation.

How It Works
1. Setting Up the Database
The script initializes a SQLite database (pokemon.db) and creates a table to store Pokémon details:

id (refers to the Pokémon ID)
name (refers to the Pokémon Name)
height (refers to the Height)
weight (refers to the Weight)
base_experience (refers to the Experience points)

2. Fetching Pokémon Data
When a user searches for a Pokémon based on his selection, the script queries the PokéAPI and retrieves:
- ID
- Name
- Height
- Weight
- Base Experience

3. Adding a Pokémon to the Database
Stores Pokémon details in the database.
Ensures duplicate entries are not added.
Displays a confirmation message after successfully adding a Pokémon.

4. Removing a Pokémon
Deletes a Pokémon from the database using its ID or Name.
Prints a success message when the removal is complete.

5. Displaying Pokémon Info
Prints Pokémon details.

6. Interactive Menu
The script runs a looping menu system, allowing users to:
-Get Pokémon by ID
-Get Pokémon by Name
-Add a Pokémon to the database
-Remove a Pokémon from the database
-Exit the program
