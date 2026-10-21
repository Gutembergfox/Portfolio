CREATE TABLE daily_rentals (
    instant INTEGER PRIMARY KEY,
    dteday TEXT NOT NULL UNIQUE,
    season INTEGER NOT NULL CHECK (season BETWEEN 1 AND 4),
    yr INTEGER NOT NULL CHECK (yr IN (0,1)),
    mnth INTEGER NOT NULL CHECK (mnth BETWEEN 1 AND 12),
    holiday INTEGER NOT NULL CHECK (holiday IN (0,1)),
    weekday INTEGER NOT NULL CHECK (weekday BETWEEN 0 AND 6),
    workingday INTEGER NOT NULL CHECK (workingday IN (0,1)),
    weathersit INTEGER NOT NULL CHECK (weathersit BETWEEN 1 AND 4),
    temp REAL NOT NULL CHECK (temp BETWEEN 0 AND 1),
    atemp REAL NOT NULL CHECK (atemp BETWEEN 0 AND 1),
    hum REAL NOT NULL CHECK (hum BETWEEN 0 AND 1),
    windspeed REAL NOT NULL CHECK (windspeed BETWEEN 0 AND 1),
    casual INTEGER NOT NULL CHECK (casual >= 0),
    registered INTEGER NOT NULL CHECK (registered >= 0),
    cnt INTEGER NOT NULL CHECK (cnt >= 0 AND cnt = casual + registered)
);
