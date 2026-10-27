-- При условии, что до этого таблицы participants, award_types и achievements были пусты

-- PARTICIPANTS
INSERT INTO participants (firstname, lastname, grade, registered_at) VALUES ('Ivan', 'Ivanov', 11, '10-27-2026');
INSERT INTO participants (firstname, lastname, grade, registered_at) VALUES ('Dima', 'Dmitrov', 9, '10-27-2026');
INSERT INTO participants (firstname, lastname, grade, registered_at) VALUES ('Danil', 'Semenov', 6, '10-27-2026');
INSERT INTO participants (firstname, lastname, grade, registered_at) VALUES ('Sasha', 'Petrov', 7, '10-27-2026');

-- Award
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'SCHOOL', 'GRANDPRIX', '25');
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'DISTRICT', 'FIRST', '15');
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'REGIONAL', 'SECOND', '35');
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'INTERREGIONAL', 'THIRD', '20');

-- ACHIEVEMENTS
INSERT INTO achievements (participant_id, award_type_id, event, received_at) VALUES (4, 1, 'None', '10-27-2026');
INSERT INTO achievements (participant_id, award_type_id, event, received_at) VALUES (3, 2, 'None', '10-27-2026');
INSERT INTO achievements (participant_id, award_type_id, event, received_at) VALUES (2, 3, 'None', '10-27-2026');
INSERT INTO achievements (participant_id, award_type_id, event, received_at) VALUES (1, 4, 'None', '10-27-2026');
