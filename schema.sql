CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN,
    timestamp TIMESTAMP
    visible BOOLEAN
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    topic TEXT UNIQUE
    visible BOOlEAN
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    forum_id INTEGER,
    timestamp TIMESTAMP
    visible BOOLEAN
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER,
    topic_id INTEGER,
    timestamp TIMESTAMP
    visible BOOLEAN
);
