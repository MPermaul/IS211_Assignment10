# IS211_Assignment10
Week 10 Assignment 10

Author: Moses Permaul - moses.permaul13@spsmail.cuny.edu

Application Details:

1) There are 3 main files for this applcation:
	a) load_pets.py
	b) query_pets.py
	c) pets.db

2) The load_pets.py file creates the tables within the pets database and populates then with data.

3) The query_pet.py file connects to the pets database and displays data based on user input.
	
	a) The application will prompt the user for a person's id. Tests are done to ensure a valid entry is given.
	
		Main Display:
	
			-------------------------------------------------------
								Pet Owner Lookup
			-------------------------------------------------------

			Insturction:
					1) Enter the ID number of the person you are trying to lookup.
					2) To exit the applicaiton, enter "-1".

			Enter Id:
	
	b) The application will query the pets database for the person's details based on the id.
	
	c) If the user is found, a display like the below will be shown:
			
			-------------------------
			Lookup Results for ID "1"
			-------------------------

			James Smith, is 41 years old.

				James Smith owned Rusty, a Dalmation, that was 4 years old.
				James Smith owns Bella, a Alaskan Malamute, that is 3 years old.
	
	d) If the user is not found, a display like the below will be shown before being prompted for another id.
	
			There isn't anyone linked to ID "5". Please try again!
	
	e) If there is an issue with the database or query, a error message will be displayed and the application will exit. 

			For example:
			
				Error: near "ELECT": syntax error
				
				Error: no such table: person
				
	
	f) To exit the application, enter "-1" as the id to look up.
	
			
	
			