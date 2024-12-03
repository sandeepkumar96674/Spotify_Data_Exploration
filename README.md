![image](https://github.com/user-attachments/assets/e19b73af-10b6-4dce-a6e2-2e6141b52b48)



# Spotify_Data_Exploration

You can download the Dataset from Kaggle using the [link](https://www.kaggle.com/datasets/sandeepkumar7372/spotify-dataset).


Create the Table using the following query before importing the Dataset in Database:

> I have created the Table with the name `"spotify"`

```
DROP TABLE IF EXISTS spotify;
```

```
CREATE TABLE spotify (
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
);
```


#### Performed Exploratory Data Analysis (EDA) on the Table to get the Better Understand about the Table `Spotify`.

<br>

**Exploratory Data Analysis 🔎**

<hr>

```
select count(*) from spotify;
```

<br>

>**Count the Distinct Artist in "Artist" Column.**

```
select count(distinct artist) from spotify;
```

<br>

>**Count the Distinct Album present in the Column**

```
select count(distinct album) from spotify;
```

<br>

>**Count the Distinct Artist present in the Column**

```
select count(distinct artist) from spotify;
```

<br>

>**Maximum "Duration_min"**

```
select max(duration_min) from spotify;
```

<br>

>**Minimum "Duration_Min"**

```
select min(duration_min) from spotify;
```

<br>

>**Selecting the Rows with 0 Duration_Min**

```
select * from spotify
where duration_min = 0;
```

<br>

>**Deleting the Rows of Duration_min column with the value 0 and Validating the Data.**

```
delete from spotify
where duration_min = 0;
select * from spotify
where duration_min = 0;
```

<hr>

## Business Problems with their Solution Queries:

<br>

>**Q1. Retrieving the names of all the tracks that have more than 1 Billion Streams.**

```
select * from spotify
where stream > 1000000000;
```

<br>

>**Q2. List all the Albums along with their respective Artist**

```
select distinct album,artist from spotify
order by 1;
```

<br>

>**Q3. Get the total number of Comments for Track where value of licensed column is True.**

```
select sum(comments) as Total_Comment
from spotify
where licensed is true;
```

<br>

>**Q4. Find all the Tracks that belongs to the Album type "Single".**

```
Select * from spotify 
where album_type = 'single';
```
<br>
<br>

>**Q5. Total number of Tracks by each Artists**

```
select count(album)as Total_Track,artist
from spotify
group by artist
order by 1;
```

>**Q6. Calculate the Average Danceability  of Tracks in each Album**


>**Q7. Find the Top-5 Tracks with the Highest energy values**

>**List all the Tracks along with thier Views and Likes**
