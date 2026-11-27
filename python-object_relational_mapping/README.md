# python-object_relational_mapping

Python scripts that use MySQL with `MySQLdb` and `SQLAlchemy`.

Each script takes the MySQL username, password and database name as its
first arguments.

- `0-select_states.py`: Lists all states from a database.
- `1-filter_states.py`: Lists all states with a name starting with N.
- `2-my_filter_states.py`: Displays the states matching a name.
- `3-my_safe_filter_states.py`: Displays the states matching a name, safe from SQL injection.
- `4-cities_by_state.py`: Lists all cities with their state.
- `5-filter_cities.py`: Lists all cities of a given state.
- `7-model_state_fetch_all.py`: Lists all State objects.
- `8-model_state_fetch_first.py`: Prints the first State object.
- `9-model_state_filter_a.py`: Lists the State objects containing the letter a.
- `10-model_state_my_get.py`: Prints the id of the State with a name.
- `11-model_state_insert.py`: Adds the State Louisiana.
- `12-model_state_update_id_2.py`: Renames the State with id 2.
- `13-model_state_delete_a.py`: Deletes the State objects containing the letter a.
- `14-model_city_fetch_by_state.py`: Prints all City objects by state.
- `model_state.py`: the `State` model
- `model_city.py`: the `City` model
