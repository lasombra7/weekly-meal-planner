USE meal_planner;

-- ============================
-- Table: dairy
-- Description: Dairy products
-- ============================

CREATE TABLE IF NOT EXISTS dairy (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit：g',
  calorie INT COMMENT 'Unit：kcal',
  protein FLOAT COMMENT 'Unit：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO dairy (id, name, type, weight, calorie, protein)
VALUES
  ('D1', 'Yogurt (100g)', 'Yogurt', 100, 61, 3.5),
  (
    'D2',
    'Flavored Yogurt (100g)',
    'Yogurt',
    100,
    95,
    3.0
  ),
  (
    'D3',
    'High-Protein Yogurt (100g)',
    'Yogurt',
    100,
    65,
    9.0
  ),
  ('D4', 'Skim Milk (250ml)', 'Milk', 250, 85, 8.5),
  (
    'D5',
    'Mozzarella Cheese (30g)',
    'Cheese',
    30,
    85,
    6.6
  ),
  (
    'D6',
    'Unsweetened Soy Milk (250ml)',
    'Soy Milk',
    250,
    90,
    7.0
  );