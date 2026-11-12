# SQL_more_queries

MySQL exercises on users and privileges, table constraints, foreign keys, subqueries and joins.

## Usage

Each script is run by piping it into the `mysql` client. Scripts that work on a table or query take the database name as an argument:

```
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of `user_0d_1` and `user_0d_2` on localhost. |
| `1-create_user.sql` | Creates `user_0d_1` (password `user_0d_1_pwd`) with all privileges. |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and `user_0d_2` with only `SELECT` on it. |
| `3-force_name.sql` | Creates `force_name` (`id INT`, `name VARCHAR(256) NOT NULL`). |
| `4-never_empty.sql` | Creates `id_not_null` (`id INT DEFAULT 1`, `name VARCHAR(256)`). |
| `5-unique_id.sql` | Creates `unique_id` (`id INT DEFAULT 1 UNIQUE`, `name VARCHAR(256)`). |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and its `states` table. |
| `7-cities.sql` | Creates the `cities` table with a foreign key to `states`. |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery (no `JOIN`). |
| `9-cities_by_state_join.sql` | Lists all cities with their state name using a `JOIN`. |
| `10-genre_id_by_show.sql` | Lists shows that have at least one genre linked. |
| `11-genre_id_all_shows.sql` | Lists all shows, showing `NULL` for shows without a genre. |
| `12-no_genre.sql` | Lists shows without any genre linked. |
| `13-count_shows_by_genre.sql` | Lists genres with the number of shows linked to each. |
| `14-my_genres.sql` | Lists all genres of the show Dexter. |
| `15-comedy_only.sql` | Lists all Comedy shows. |
| `16-shows_by_genre.sql` | Lists all shows and their genres, with `NULL` when none. |
