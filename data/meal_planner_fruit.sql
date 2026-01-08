-- ===============================
-- Table: fruit
-- Description: Fruit products
-- ===============================
USE meal_planner;
CREATE TABLE IF NOT EXISTS fruit (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit：g',
  calorie INT COMMENT 'Unit：kcal',
  protein FLOAT COMMENT 'Unit：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  fruit (id, name, type, weight, calorie, protein)
VALUES
  ('F1', 'Apple (180–200g)', 'Apple', 180, 95, 0.5),
  ('F2', 'Apple (230–250g)', 'Apple', 230, 120, 0.6),
  (
    'F3',
    'Banana (1 piece)',
    'Banana',
    120,
    105,
    1.3
  ),
  (
    'F4',
    'Hami Melon (200g)',
    'Hami Melon',
    200,
    68,
    1.6
  ),
  ('F5', 'Pear (180–200g)', 'Pear', 180, 95, 0.6),
  ('F6', 'Pear (230–250g)', 'Pear', 230, 120, 0.8),
  ('F7', 'Grapes (100g)', 'Grape', 100, 69, 0.6),
  ('F8', 'Grapes (150g)', 'Grape', 150, 104, 0.9),
  (
    'F9',
    'Watermelon (200g)',
    'Watermelon',
    200,
    60,
    1.2
  ),
  (
    'F10',
    'Orange (1 piece)',
    'Orange',
    200,
    90,
    1.7
  ),
  ('F11', 'Cherries (100g)', 'Cherry', 100, 50, 1.0),
  ('F12', 'Cherries (150g)', 'Cherry', 150, 75, 1.5),
  (
    'F13',
    'Pineapple (100g)',
    'Pineapple',
    100,
    50,
    0.5
  ),
  ('F14', 'Kiwi (1 piece)', 'Kiwi', 100, 60, 1.2),
  ('F15', 'Kiwi (2 pieces)', 'Kiwi', 100, 120, 2.4);