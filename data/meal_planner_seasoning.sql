USE meal_planner;

-- =================================
-- Table: seasoning
-- Description: Seasoning products
-- =================================

CREATE TABLE IF NOT EXISTS seasoning (
  id CHAR(5),
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit: g',
  calorie INT COMMENT 'Unit: kcal',
  protein FLOAT COMMENT 'Unit: g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  seasoning (id, name, type, weight, calorie, protein)
VALUES
  (
    'S1',
    'Soy Sauce (1 tbsp)',
    'Soy Sauce',
    16,
    10,
    1.5
  ),
  ('S2', 'Vinegar (1 tbsp)', 'Vinegar', 15, 3, 0.0),
  (
    'S3',
    'Oyster Sauce (1 tbsp)',
    'Oyster Sauce',
    15,
    15,
    0.3
  ),
  (
    'S4',
    'Steamed Fish Soy Sauce (1 tbsp)',
    'Fish Soy Sauce',
    16,
    10,
    1.0
  );