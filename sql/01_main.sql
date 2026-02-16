USE meal_planner;

-- =============================
-- Table: main
-- Description: Main products
-- =============================

CREATE TABLE IF NOT EXISTS main (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Rice / Corn / Whole Grains / Legumes / Pasta / Noodle
  food_subgroup VARCHAR(40),
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO main 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Rice
('M1', 'White Rice (Cooked)', 'Grain', 'White Rice', 130, 2.4, 28.0, 0.3),
('M2', 'Brown Rice (Cooked)', 'Grain', 'Brown Rice', 123, 2.7, 25.6, 1.0),

-- Corn
('M3', 'Corn (Boiled)', 'Grain', 'Corn', 96, 3.4, 21.0, 1.5),

-- Whole Grains
('M4', 'Quinoa (Cooked)', 'Whole Grain', 'Quinoa', 120, 4.4, 21.0, 1.9),
('M5', 'Oats (Cooked)', 'Whole Grain', 'Oats', 71, 2.5, 12.0, 1.5),
('M6', 'Whole Wheat Bread', 'Whole Grain', 'Bread', 247, 13.0, 41.0, 4.2),
('M7', 'White Bread', 'Whole Grain', 'Bread', 265, 9.0, 49.0, 3.2),
('M8', 'Millet (Cooked)', 'Whole Grain', 'Millet', 119, 3.5, 23.0, 1.0),

-- Legumes
('M9', 'Lentils (Cooked)', 'Legume', 'Lentils', 116, 9.0, 20.0, 0.4),
('M10', 'Chickpeas (Cooked)', 'Legume', 'Chickpeas', 164, 8.9, 27.0, 2.6),

-- Tubers
('M11', 'Potato (Boiled)', 'Tuber', 'Potato', 87, 2.0, 20.0, 0.1),
('M12', 'Sweet Potato (Boiled)', 'Tuber', 'Sweet Potato', 90, 2.0, 21.0, 0.1),

-- Pasta
('M13', 'White Pasta (Cooked)', 'Pasta', 'White Pasta', 131, 5.0, 25.0, 1.1),

-- Noodle
('M14', 'Udon (Cooked)', 'Noodles', 'Udon', 127, 3.0, 25.0, 0.3);