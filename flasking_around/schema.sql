CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fortunes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fortunes TEXT NOT NULL
);

INSERT INTO fortunes
    (fortunes)
VALUES
    ('You will find $5'),
    ('Even the wise man finds a broken branch.'),
    ('Blank fortune.'),
    ('I''m feeling very pressured to say something right now.'),
    ('The day they release reverse Reese''s is the day.'),
    ('A Grand Canyon like figurine could soon be in your possession.'),
    ('Financial sucess.'),
    ('Beginning is just the beginning.'),
    ('An episode of Bar Resucue is waiting for you.'),
    ('Come up with your own fortune. Believe in yourself.'),
    ('Just scootch over a little to the left.'),
    ('Next time hanging up a picture: First try, perfect leveling.'),
    ('Cherish this moment'),
    ('Playing hopscotch would make you play hopscotch.'),
    ('Hotdogs bring great joy.'),
    ('You would look good in a vintage leather jacket.'),
    ('uh.......................................................'),
