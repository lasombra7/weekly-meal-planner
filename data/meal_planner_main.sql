-- =============================
-- Table: main
-- Description: Main products
-- =============================
USE meal_planner;
CREATE TABLE IF NOT EXISTS main (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit：g',
  calorie INT COMMENT 'Unit：kcal',
  protein FLOAT COMMENT 'Unit：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  main (id, name, type, weight, calorie, protein)
VALUES
  ('M1', 'Rice (200g)', 'Rice', 200, 260, 5.2),
  (
    'M10',
    'Whole Wheat Bread (2 slices)',
    'Whole Wheat Bread',
    60,
    150,
    6.0
  ),
  (
    'M11',
    'Whole Wheat Bread (4 slices)',
    'Whole Wheat Bread',
    120,
    300,
    12.0
  ),
  ('M12', 'Shin Ramen', 'Noodles', 120, 505, 10.0),
  (
    'M13',
    'Wulong Noodles',
    'Noodles',
    110,
    510,
    9.0
  ),
  (
    'M14',
    'Udon Noodles (200g)',
    'Udon Noodles',
    200,
    220,
    6.0
  ),
  ('M15', 'Taro (150g)', 'Taro', 150, 135, 2.2),
  ('M16', 'Taro (250g)', 'Taro', 250, 225, 3.8),
  ('M2', 'Rice (300g)', 'Rice', 300, 390, 7.8),
  (
    'M3',
    'Sweet Potato (200g)',
    'Sweet Potato',
    200,
    180,
    2.6
  ),
  (
    'M4',
    'Sweet Potato (300g)',
    'Sweet Potato',
    300,
    270,
    3.9
  ),
  (
    'M5',
    'Shandong Noodles (Dry, 85g)',
    'Noodles',
    85,
    300,
    10.0
  ),
  (
    'M6',
    'Shandong Noodles (Dry, 170g)',
    'Noodles',
    170,
    600,
    20.0
  ),
  (
    'M7',
    'Canned Corn (150g)',
    'Corn',
    150,
    135,
    4.8
  ),
  (
    'M8',
    'Canned Corn (300g)',
    'Corn',
    300,
    270,
    9.6
  ),
  (
    'M9',
    'Boiled Corn (1 ear)',
    'Corn',
    180,
    160,
    5.4
  );