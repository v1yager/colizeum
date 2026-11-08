-- CERTIFICATE
INSERT INTO award_types (format, points) VALUES('CERTIFICATE', 5);

-- SCHOOL
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'SCHOOL', 'GRANDPRIX', '25') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'SCHOOL', 'FIRST', '20') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'SCHOOL', 'SECOND', '15') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'SCHOOL', 'THIRD', '10') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'SCHOOL', 'GRANDPRIX', '12') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'SCHOOL', 'FIRST', '10') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'SCHOOL', 'SECOND', '7') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'SCHOOL', 'THIRD', '5') ON CONFLICT DO NOTHING;


-- MUNICIPAL
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'MUNICIPAL', 'GRANDPRIX', '30') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'MUNICIPAL', 'FIRST', '25') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'MUNICIPAL', 'SECOND', '20') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'MUNICIPAL', 'THIRD', '15') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'MUNICIPAL', 'GRANDPRIX', '15') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'MUNICIPAL', 'FIRST', '12') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'MUNICIPAL', 'SECOND', '10') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'MUNICIPAL', 'THIRD', '7') ON CONFLICT DO NOTHING;


-- DISTRICT
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'DISTRICT', 'GRANDPRIX', '35') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'DISTRICT', 'FIRST', '30') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'DISTRICT', 'SECOND', '25') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'DISTRICT', 'THIRD', '20') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'DISTRICT', 'GRANDPRIX', '17') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'DISTRICT', 'FIRST', '15') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'DISTRICT', 'SECOND', '12') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'DISTRICT', 'THIRD', '10') ON CONFLICT DO NOTHING;

-- REGIONAL
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'REGIONAL', 'GRANDPRIX', '45') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'REGIONAL', 'FIRST', '40') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'REGIONAL', 'SECOND', '35') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'REGIONAL', 'THIRD', '30') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'REGIONAL', 'GRANDPRIX', '22') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'REGIONAL', 'FIRST', '20') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'REGIONAL', 'SECOND', '17') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'REGIONAL', 'THIRD', '15') ON CONFLICT DO NOTHING;

-- INTERREGIONAL
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'INTERREGIONAL', 'GRANDPRIX', '55') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'INTERREGIONAL', 'FIRST', '50') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'INTERREGIONAL', 'SECOND', '45') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'INTERREGIONAL', 'THIRD', '40') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'INTERREGIONAL', 'GRANDPRIX', '27') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'INTERREGIONAL', 'FIRST', '25') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'INTERREGIONAL', 'SECOND', '22') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'INTERREGIONAL', 'THIRD', '20') ON CONFLICT DO NOTHING;

-- RUSSIAN
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'RUSSIAN', 'GRANDPRIX', '70') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'RUSSIAN', 'FIRST', '60') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'RUSSIAN', 'SECOND', '55') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('PERSONAL', 'RUSSIAN', 'THIRD', '50') ON CONFLICT DO NOTHING;

INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'RUSSIAN', 'GRANDPRIX', '35') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'RUSSIAN', 'FIRST', '30') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'RUSSIAN', 'SECOND', '27') ON CONFLICT DO NOTHING;
INSERT INTO award_types (format, level, place, points) VALUES ('TEAM', 'RUSSIAN', 'THIRD', '25') ON CONFLICT DO NOTHING;
