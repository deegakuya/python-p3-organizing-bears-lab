# Query 1
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# Query 2
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM bears
    ORDER BY name;
"""

# Query 3
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1
    ORDER BY age;
"""

# Query 4
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Query 5
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age
    LIMIT 1;
"""
