-- =================================
-- Table: protein
-- Description: Protein products
-- =================================
USE meal_planner;
CREATE TABLE IF NOT EXISTS protein (
  id CHAR(5),
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT 'Unit: g',
  calorie INT COMMENT 'Unit: kcal',
  protein FLOAT COMMENT 'Unit: g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  protein (id, name, type, weight, calorie, protein)
VALUES
  (
    'P1',
    'Chicken Breast & Thigh (Cooked, 200g)',
    'Chicken',
    200,
    345,
    56.0
  ),
  (
    'P2',
    'Chicken Breast & Thigh (Cooked, 300g)',
    'Chicken',
    300,
    518,
    84.0
  ),
  ('P3', 'Tofu (300g)', 'Tofu', 300, 240, 27.0),
  (
    'P4',
    'Lean Beef (Cooked, 200g)',
    'Beef',
    200,
    380,
    60.0
  ),
  (
    'P5',
    'Lean Beef (Cooked, 300g)',
    'Beef',
    300,
    570,
    75.0
  ),
  ('P6', 'Tofu (150g)', 'Tofu', 150, 120, 13.5),
  ('P7', 'Tofu (200g)', 'Tofu', 200, 160, 18.0),
  ('P8', 'Egg (1 piece)', 'Egg', 50, 70, 6.3),
  ('P9', 'Egg (2 pieces)', 'Egg', 100, 140, 12.6),
  ('P10', 'Egg (3 pieces)', 'Egg', 150, 210, 18.9),
  (
    'P11',
    'Ground Pork (Raw, 50g)',
    'Pork',
    50,
    130,
    9.0
  ),
  (
    'P12',
    'Shrimp (Cooked, 50g)',
    'Shrimp',
    50,
    50,
    10.5
  ),
  (
    'P13',
    'Shrimp (Cooked, 100g)',
    'Shrimp',
    100,
    100,
    21.0
  ),
  (
    'P14',
    'Sole Fish (Raw, 100g)',
    'Sole Fish',
    100,
    80,
    17.0
  ),
  (
    'P15',
    'Sole Fish (Raw, 200g)',
    'Sole Fish',
    200,
    160,
    34.0
  ),
  (
    'P16',
    'Salmon (Raw, 100g)',
    'Salmon',
    100,
    208,
    20.0
  ),
  (
    'P17',
    'Salmon (Raw, 200g)',
    'Salmon',
    200,
    416,
    40.0
  ),
  (
    'P18',
    'Scallop Meat (Raw, 100g)',
    'Scallop',
    100,
    70,
    12.0
  ),
  (
    'P19',
    'Soy Milk (250ml)',
    'Soy Milk',
    250,
    110,
    7.0
  ),
  (
    'P20',
    'Canned Tuna (100g)',
    'Tuna',
    100,
    116,
    25.0
  );
