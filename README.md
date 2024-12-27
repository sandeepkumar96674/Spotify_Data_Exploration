![image](https://github.com/user-attachments/assets/e19b73af-10b6-4dce-a6e2-2e6141b52b48)



# Spotify_Data_Exploration

You can download the Dataset from Kaggle using the [link](https://www.kaggle.com/datasets/sandeepkumar7372/spotify-dataset).

<br>

I have solved the Business Problem by using SQL and Python Both.

<br>

You can check my approach for Python Solution using the [link]().

<br>
<hr>
For Solution using SQL, Go through with the following: 

<br>
<br>
Create the Table using the following query before importing the Dataset in Database:

<br>
<br>

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

### Exploratory Data Analysis(EDA) to know more about the Dataset 🔎

<hr>

```
select count(*) from spotify;
```

<br>

#### Count the Distinct Artist in "Artist" Column.

```
select count(distinct artist) from spotify;
```

<br>

#### Count the Distinct Album present in the Column

```
select count(distinct album) from spotify;
```

<br>

#### Count the Distinct Artist present in the Column

```
select count(distinct artist) from spotify;
```

<br>

#### Maximum "Duration_min"

```
select max(duration_min) from spotify;
```

<br>

#### Minimum "Duration_Min"

```
select min(duration_min) from spotify;
```
<br>

#### Selecting the Rows with 0 Duration_Min

```
select * from spotify
where duration_min = 0;
```

<br>

#### Deleting the Rows of Duration_min column with the value 0 and Validating the Data.

```
delete from spotify
where duration_min = 0;
select * from spotify
where duration_min = 0;
```

<hr>

## Business Problems with their Solution Queries:
<hr>

**Q1. Retrieving the names of all the tracks that have more than 1 Billion Streams.**

```
select * from spotify
where stream > 1000000000;
```
<hr>

**Q2. List all the Albums along with their respective Artist**

```
select distinct album,artist from spotify
order by 1;
```
<hr>

**Q3. Get the total number of Comments for Track where value of licensed column is True.**

```
select sum(comments) as Total_Comment
from spotify
where licensed is true;
```
<hr>

**Q4. Find all the Tracks that belongs to the Album type "Single".**

```
Select * from spotify 
where album_type = 'single';
```
<hr>

**Q5. Total number of Tracks by each Artists**

```
select count(album)as Total_Track,artist
from spotify
group by artist
order by 1;
```
<hr>

**Q6. Calculate the Average Danceability  of Tracks in each Album**
```
select album,avg(danceability) from spotify
group by 1
order by 2 desc;
```
<hr>

**Q7. Find the Top-5 Tracks with the Highest energy values**
```
select track, max(energy) from spotify
group by 1
order by 2 desc
limit 5;
```

<hr>

**Q8. List all the Tracks along with thier Views and Likes where official_video = TRUE**
```
select track,sum(views),sum(likes) from spotify
where official_video=true
group by 1
order by 2;
```
<hr>

**Q9. Calcualte the total views of all associated Tracks for each Album**
```
select album,track,sum(views) from spotify
group by 1,2;
```
<hr>

**Q10. Retrieve the Track Names that have been streamed on Spotify more than YouTube**
```
select * from (
select track,
coalesce(sum(case when most_played_on = "Youtube" then Stream end),0) as Youtube
coalesce(sum(case when most_played_on = "Spotify" then Stream end),0) as Spotify
from spotify
group by 1) as t1
where Spotify > Youtube and Youtube <>0;
```
<hr>
