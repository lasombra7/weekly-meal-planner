-- =================================
-- Table: oil
-- Description: Oil products
-- =================================
USE meal_planner;
CREATE TABLE IF NOT EXISTS oil (
  id CHAR(5),
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit: g',
  calorie INT COMMENT 'Unit: kcal',
  protein FLOAT COMMENT 'Unit: g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  oil (id, name, type, weight, calorie, protein)
VALUES
  (
    'O1',
    'Cooking Oil (1 tbsp)',
    'Cooking Oil',
    10,
    90,
    0.0
  ),
  (
    'O2',
    'Olive Oil (1 tbsp)',
    'Olive Oil',
    10,
    90,
    0.0
  );