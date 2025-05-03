CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    image BLOB
);

CREATE TABLE threads (
    id INTEGER PRIMARY KEY,
    title TEXT,
    user_id INTEGER REFERENCES users,
    post_type TEXT not NULL,
    status TEXT not NULL,
    priority TEXT not NULL
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    content TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads
    );

CREATE INDEX idx_thread_messages ON messages (thread_id);
CREATE INDEX idx_user_messages ON messages (user_id);