-- ============================
-- Table: vegetable
-- Description: Vegetable products
-- ============================
USE meal_planner;
CREATE TABLE IF NOT EXISTS vegetable (
  id CHAR(5),
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit: g',
  calorie INT COMMENT 'Unit: kcal',
  protein FLOAT COMMENT 'Unit: g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  vegetable (id, name, type, weight, calorie, protein)
VALUES
  (
    'V1',
    'Iceberg Lettuce (Raw/Boiled, 300g)',
    'Iceberg Lettuce',
    300,
    45,
    3.6
  ),
  (
    'V2',
    'Iceberg Lettuce (Raw/Boiled, 500g)',
    'Iceberg Lettuce',
    500,
    75,
    6.0
  ),
  (
    'V3',
    'Chinese Broccoli (Raw, 300g)',
    'Chinese Broccoli',
    300,
    105,
    9.6
  ),
  (
    'V4',
    'Tomato (Raw, 300g)',
    'Tomato',
    300,
    66,
    3.0
  ),
  (
    'V5',
    'Napa Cabbage (Raw, 200g)',
    'Napa Cabbage',
    200,
    34,
    2.0
  ),
  (
    'V6',
    'Napa Cabbage (Raw, 300g)',
    'Napa Cabbage',
    300,
    51,
    3.0
  ),
  (
    'V7',
    'Tomato (Raw, 150g)',
    'Tomato',
    150,
    33,
    1.5
  ),
  (
    'V8',
    'Chinese Broccoli (Raw, 150g)',
    'Chinese Broccoli',
    150,
    52,
    4.8
  ),
  (
    'V9',
    'Green Peas (Raw, 150g)',
    'Green Peas',
    150,
    186,
    12.6
  ),
  (
    'V10',
    'Green Peas (Raw, 200g)',
    'Green Peas',
    200,
    248,
    16.8
  ),
  (
    'V11',
    'Cucumber (Raw, 200g)',
    'Cucumber',
    200,
    30,
    1.4
  ),
  (
    'V12',
    'Cucumber (Raw, 300g)',
    'Cucumber',
    300,
    45,
    2.1
  ),
  (
    'V13',
    'Bok Choy (Raw, 200g)',
    'Bok Choy',
    200,
    42,
    3.2
  ),
  (
    'V14',
    'Daikon Radish (Raw, 200g)',
    'Daikon Radish',
    200,
    36,
    1.2
  ),
  (
    'V15',
    'Onion (Raw, 100g)',
    'Onion',
    100,
    40,
    1.1
  ),
  (
    'V16',
    'Lettuce (Raw, 200g)',
    'Lettuce',
    200,
    30,
    2.4
  ),
  (
    'V17',
    'Carrot (Raw, 200g)',
    'Carrot',
    200,
    66,
    1.6
  ),
  (
    'V18',
    'Tomato (Raw, 200g)',
    'Tomato',
    200,
    44,
    2.0
  );