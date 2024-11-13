# Spotify_Data_Exploration

You can download the Dataset from Kaggle using the [link](https://www.kaggle.com/datasets/sandeepkumar7372/spotify-dataset).


Create the Table using the following query before importing the Dataset in Database:

>I created the Table with the name `spotify`

`DROP TABLE IF EXISTS spotify;`

`CREATE TABLE spotify (
    artist VARCHAR(255),
    track VARCHAR(255),
    album VARCHAR(255),
    album_type VARCHAR(50),
    danceability FLOAT,
    energy FLOAT,
    loudness FLOAT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    duration_min FLOAT,
    title VARCHAR(255),
    channel VARCHAR(255),
    views FLOAT,
    likes BIGINT,
    comments BIGINT,
    licensed BOOLEAN,
    official_video BOOLEAN,
    stream BIGINT,
    energy_liveness FLOAT,
    most_played_on VARCHAR(50)
);`


#### Performed Exploratory Data Analysis (EDA) on the Table to get the Better Understand about the Table `Spotify`.

##### Total Number of Rows in the Table `Spotify`.

##### Unique Values present in the Album Column.

##### Unique Values present in the Artist Column.
