import sqlite3 as lite


def get_user_input():
    """Function that prompts end user for the id of a pet owner and returns it to caller
    param:
    return: choice: An int value representing an end user's pet owner id choice
    """
    
    # loop to prompt until a valid input is provided
    while True:
        
        try: 
            choice = int(input('\nEnter Id: '))
        except:
            print('\n\tYou\'ve entered an invalid input. Please try again.')
        else:
            break
    
    return choice


def query_db(db_name, person_id):
    """Function that takes in a database name and id, and queries for the person's data

    param: db_name: a string value for the database we need to connect to
    param: person_id: a int value that we will query for
    return: Tuple
    """
    
    # set connection variable to None
    conn = None

    # try block to test for errors
    try:
        # open connection to database
        conn = lite.connect(db_name)

        # create cursor
        cursor = conn.cursor()

        # execute query on person table to get details for id entered
        cursor.execute('SELECT first_name, last_name, age FROM person WHERE id = {}'.format(person_id))
        
        # get one row for the person linked to person id
        person_query = cursor.fetchone()

        # execute join query to get pet details for person id entered
        cursor.execute('''SELECT 
                        pet.name, 
                        pet.breed, 
                        pet.age,
                        pet.dead
                        FROM person_pet
                        LEFT JOIN person
                        ON person_pet.person_id = person.id
                        LEFT JOIN pet
                        ON person_pet.pet_id = pet.id
                        WHERE person.id = {}'''.format(person_id))
        
        # get all rows for pets linked to person id
        pet_query = cursor.fetchall()

        # close cursor
        cursor.close()

        return (person_query, pet_query)

    except lite.Error as error:

        print('Error: {}'. format(error))

        # return 0 so that the application can manage this error
        return 0

    finally:

        # close connection
        conn.close()


def display_data(choice, data):
    
    print('\n-------------------------')
    print('Lookup Results for ID "{}"'.format(choice))
    print('-------------------------')
    print('\n{} {}, is {} years old.\n'.format(data[0][0], data[0][1], data[0][2]))

    # print('Pet Details:')
  
    # loop through rows to print pet details
    for row in data[1]:
        
        # check to see if pet is dead or not and assign appropriate words
        if row[3] == 1:
            word1 = 'owned'
            word2 = 'was'
        else:
            word1 = 'owns'
            word2 = 'is'

        # print pet details
        print('\t{} {} {} {}, a {}, that {} {} years old.'.format(data[0][0], data[0][1], word1, 
                                                            row[0], row[1], word2, row[2]))


def main():

    # print statements for the end user
    print('-' * 55)
    print('{:^55}'.format('Pet Owner Lookup'))
    print('-' * 55)   
    print('\nInsturction:')
    print('\t1) Enter the ID number of the person you are trying to lookup.')
    print('\t2) To exit the applicaiton, enter "-1".')

    # database that we will query
    db_name = 'pets.db'

    # initialize choice with a 0
    choice = 0

    # loop the applicaiton until user enters in -1
    while choice != -1:
        
        # call function to get user's input
        choice = get_user_input()

        # check to see if -1 was entered by user
        if choice != -1:

            # call function to query database for user's input anf store results
            data = query_db(db_name, choice)

            # check to make sure query came back with results
            if data[0] != None and data != 0:

                # call function to display data
                display_data(choice, data)
            
            else:
                print('\n\tThere isn\'t anyone linked to ID "{}". Please try again!\n'.format(choice))


if __name__ == '__main__':


    main()