USE meal_planner;

-- =================================
-- Table: seasoning
-- Description: Seasoning products
-- =================================

CREATE TABLE IF NOT EXISTS seasoning (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Sauce / Acid / Paste / Spice / Aromatics
  food_subgroup VARCHAR(40), 
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO seasoning
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Sauces
('S1', 'Soy Sauce', 'Sauce', 'Soy Sauce', 53, 8.1, 4.9, 0.1),
('S2', 'Oyster Sauce', 'Sauce', 'Oyster Sauce', 51, 1.3, 11.0, 0.0),
('S3', 'Fish Sauce', 'Sauce', 'Fish Sauce', 35, 5.0, 0.7, 0.0),

-- Acid
('S4', 'Vinegar', 'Acid', 'Vinegar', 18, 0.0, 0.0, 0.0),

-- Paste
('S5', 'Miso Paste', 'Paste', 'Miso', 199, 12.0, 26.0, 6.0),

-- Spice
('S6', 'Black Pepper', 'Spice', 'Pepper', 251, 10.0, 64.0, 3.3),

-- Aromatics
('S7', 'Green Onion (Raw)', 'Aromatic', 'Green Onion', 32, 1.8, 7.3, 0.2),
('S8', 'Ginger (Raw)', 'Aromatic', 'Ginger', 80, 1.8, 18.0, 0.8);