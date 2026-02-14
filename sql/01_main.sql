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
('M6', 'Barley (Cooked)', 'Whole Grain', 'Barley', 123, 2.3, 28.0, 0.4),
('M7', 'Buckwheat (Cooked)', 'Whole Grain', 'Buckwheat', 92, 3.4, 20.0, 0.6),
('M8', 'Millet (Cooked)', 'Whole Grain', 'Millet', 119, 3.5, 23.0, 1.0),
('M9', 'Farro (Cooked)', 'Whole Grain', 'Farro', 125, 5.0, 25.0, 1.0),

-- Legumes
('M10', 'Lentils (Cooked)', 'Legume', 'Lentils', 116, 9.0, 20.0, 0.4),
('M11', 'Chickpeas (Cooked)', 'Legume', 'Chickpeas', 164, 8.9, 27.0, 2.6),
('M12', 'Red Beans (Cooked)', 'Legume', 'Red Beans', 127, 8.7, 22.8, 0.5),

-- Tubers
('M13', 'Potato (Boiled)', 'Tuber', 'Potato', 87, 2.0, 20.0, 0.1),
('M14', 'Sweet Potato (Boiled)', 'Tuber', 'Sweet Potato', 90, 2.0, 21.0, 0.1),
('M15', 'Taro (Boiled)', 'Tuber', 'Taro', 112, 1.5, 26.0, 0.2),

-- Pasta
('M16', 'Whole Wheat Pasta (Cooked)', 'Pasta', 'Whole Wheat Pasta', 124, 5.0, 25.0, 1.1),
('M17', 'White Pasta (Cooked)', 'Pasta', 'White Pasta', 131, 5.0, 25.0, 1.1),

-- Noodle
('M18', 'Udon (Cooked)', 'Noodles', 'Udon', 127, 3.0, 25.0, 0.3);