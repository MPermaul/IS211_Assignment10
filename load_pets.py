import sqlite3


def create_tables (db_name, person, pet, person_pet):
    """Function that takes in a database object, 3 sets of tuple data, and populates a database with them.
    
    param: db_name: a string containing the database name to connect to
    param: person: a tuple containing data for person table
    param: pet: a tuple containing data for pet table     
    param: person_pet: a tuple containing data for person_pet table
    return:
    """

    # create connection to "pets.db"
    con = sqlite3.connect(db_name)
    
    # with the connection open
    with con:

        # create the cursor
        cursor = con.cursor()

        # create person table and populate it with data
        cursor.execute("DROP TABLE IF EXISTS person")
        cursor.execute("CREATE TABLE person(id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT)")
        cursor.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
        print('\tTable "person" has been created.')

        # create pet table and populate it with data
        cursor.execute("DROP TABLE IF EXISTS pet")
        cursor.execute("CREATE TABLE pet(id INT PRIMARY KEY, name TEXT, breed TEXT, age INT, dead INT)")
        cursor.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
        print('\tTable "pet" has been created.')

        # create person_pet table and populate it with data
        cursor.execute("DROP TABLE IF EXISTS person_pet")
        cursor.execute("CREATE TABLE person_pet(person_id INT, pet_id INT)")
        cursor.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)
        print('\tTable "person_pet" has been created.')


def main():

    # database that we will execute on
    db_name = 'pets.db'

    # data for "person" table
    person = (
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    )

    # data for "pet" table
    pet = (
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    )

    # data for "person_pet" table
    person_pet = (
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    )

    # call function to execute on the database and pass in the details
    create_tables(db_name, person, pet, person_pet)


if __name__ == '__main__':

    main()
    