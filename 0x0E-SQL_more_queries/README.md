## SQL - More queries
### General
    - How to create a new MySQL user
    - How to manage privileges for a user to a database or table
    - What’s a PRIMARY KEY
    - What’s a FOREIGN KEY
    - How to use NOT NULL and UNIQUE constraints
    - How to retrieve datas from multiple tables in one request
    - What are subqueries
    - What are JOIN and UNION

#### MySQL constraints
- They limit the data that can be inserted into tables.

1. *NOT NULL constraint*
- A column with a NOT NULL constraint, cannot have EMPTY values.
2. *UNIQUE constraint*
- Ensures that all data are unique in a column.
NB: _PRIMARY KEY constraint automatically has a UNIQUE constraint defined on it_
3. *Primary key*
- Primary keys are UNIQUE and cannot be NULL.
- Primary keys become foreign keys in other tables
4. *Foreign key*
- They are PRIMARY keys in other tables
- Identifies column or set of columns in another table
5. *ENUM constraint*
- These are string object with a value chosen from a list of permitted values