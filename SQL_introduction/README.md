# SQL_introduction

Introductory MySQL exercises: creating and removing databases and tables, inserting rows, and querying data.

## Usage

Each script is run by piping it into the `mysql` client. For scripts that work on a table, the database name is passed as an argument:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Files

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server. |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` (does not fail if it exists). |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` (does not fail if it is missing). |
| `3-list_tables.sql` | Lists all the tables of a database. |
| `4-first_table.sql` | Creates the table `first_table` (`id INT`, `name VARCHAR(256)`). |
| `5-full_table.sql` | Prints the full description of `first_table` without `DESCRIBE` or `EXPLAIN`. |
| `6-list_values.sql` | Lists all rows of `first_table`. |
| `7-insert_value.sql` | Inserts the row `id = 89`, `name = Best School` into `first_table`. |
| `8-count_89.sql` | Displays the number of records with `id = 89` in `first_table`. |
| `9-full_creation.sql` | Creates `second_table` (`id`, `name`, `score`) and inserts four rows. |
| `10-top_score.sql` | Lists `score` and `name` of `second_table`, top score first. |
| `11-best_score.sql` | Lists records with a score >= 10, top score first. |
| `12-no_cheating.sql` | Updates the score of Bob to 10 using only the `name` field. |
| `13-change_class.sql` | Removes all records with a score <= 5. |
| `14-average.sql` | Computes the score average, in a column named `average`. |
| `15-groups.sql` | Lists the number of records per score (`number`), sorted descending. |
| `16-no_link.sql` | Lists `score` and `name`, skipping rows without a name, by descending score. |
