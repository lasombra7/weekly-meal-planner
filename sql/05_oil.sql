USE meal_planner;

-- =================================
-- Table: oil
-- Description: Oil products
-- =================================

CREATE TABLE IF NOT EXISTS oil (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Oil / Animal Fat / Plant Fat
  food_subgroup VARCHAR(40), 
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO oil 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Plant Oils
('O1', 'Olive Oil', 'Oil', 'Olive Oil', 884, 0.0, 0.0, 100.0),
('O2', 'Canola Oil', 'Oil', 'Canola Oil', 884, 0.0, 0.0, 100.0),
('O3', 'Sesame Oil', 'Oil', 'Sesame Oil', 884, 0.0, 0.0, 100.0),

-- Animal Fats
('O4', 'Butter', 'Animal Fat', 'Butter', 717, 0.9, 0.1, 81.0),
('O5', 'Lard', 'Animal Fat', 'Lard', 902, 0.0, 0.0, 100.0);