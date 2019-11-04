-- drop tables
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS songs;

-- create artist table with artist_id as primary key
CREATE TABLE artist
(
artist_id INTERGER PRIMARY KEY, 
artist_name TEXT
);

-- create album table with album_id as primary key
-- artist_id is a foreign key of artist_id from artist table
CREATE TABLE album
(
album_id INTERGER PRIMARY KEY, 
album_name TEXT,
artist_id INTEGER,
FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

-- create songs table with song_id as primary key
-- album_id is a foreign key of album_id from album table
CREATE TABLE songs(
song_id INTERGER PRIMARY KEY,
song_name TEXT,
album_id INT,
track_num INT,
track_length INT,
FOREIGN KEY (album_id) REFERENCES album(album_id)
);