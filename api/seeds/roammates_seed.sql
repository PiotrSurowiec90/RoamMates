

DROP TABLE IF EXISTS preferences;
DROP SEQUENCE IF EXISTS preferences_id_seq;
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
DROP TABLE IF EXISTS profiles;
DROP SEQUENCE IF EXISTS profiles_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  password text,
  email text,
  UNIQUE (email)
);

INSERT INTO users (username, password, email) VALUES ('amina', 'amina1', 'amina@gmail.com');
INSERT INTO users (username, password, email) VALUES ('daniel', 'daniel1', 'daniel@gmail.com');
INSERT INTO users (username, password, email) VALUES ('piotr', 'piotr1', 'piotr@gmail.com');
INSERT INTO users (username, password, email) VALUES ('david', 'david1', 'david1@gmail.com');


-- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS profiles_id_seq;
CREATE TABLE profiles (
  user_id INT PRIMARY KEY,
  picture text,
  name text,
  age text,
  gender text,
  bio text,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (1, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Amina', '28', 'Female', 'Test bio Amina');
INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (2, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Daniel', '24', 'Male', 'Test bio Daniel');
INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (3, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Piotr', '33', 'Male', 'Test bio Piotr');
INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (4, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'David', '24', 'Male', 'Test bio David');

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
  id SERIAL PRIMARY KEY,
  status boolean,
  request_from int,
  request_to int,
  FOREIGN KEY (request_to) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (request_from) REFERENCES users(id) ON DELETE CASCADE

);

INSERT INTO requests (status, request_from, request_to) VALUES (null, 1, 2); -- unresolved request
INSERT INTO requests (status, request_from, request_to) VALUES (true, 2, 1); -- resolved request (accepted)
-- INSERT INTO requests (status, request_from, request_to) VALUES (null, 3, 1); -- unresolved request
-- INSERT INTO requests (status, request_from, request_to) VALUES (null, 4, 1);

CREATE SEQUENCE IF NOT EXISTS preferences_id_seq;
CREATE TABLE preferences (
  id SERIAL PRIMARY KEY,
  user_id INT,
  age_slot VARCHAR(10) CHECK (age_slot IN ('[18, 24]', '[25, 30]', '[30, 100]')) NOT NULL,
  gender VARCHAR(10) CHECK (gender IN ('male', 'female', 'other')) NOT NULL,
  continent VARCHAR(20) CHECK (continent IN ('Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica')) NOT NULL,
  season VARCHAR(10) CHECK (season IN ('spring', 'summer', 'autumn', 'winter')) NOT NULL,
  category VARCHAR(20) CHECK (category IN ('mountains', 'beach', 'resort', 'city', 'nature', 'sport')) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (1, '[18, 24]', 'other', 'North America', 'winter', 'resort'); 
INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (2, '[25, 30]', 'female', 'Europe', 'spring', 'beach'); 

-- # Write file into database in terminal
-- run from api dir
-- psql -h 127.0.0.1 roammates < seeds/roammates_seed.sql
-- or run from main dir
-- psql -h 127.0.0.1 roammates < api/seeds/roammates_seed.sql
