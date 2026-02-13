USE meal_planner;

-- ===============================
-- Table: fruit
-- Description: Fruit products
-- ===============================

CREATE TABLE IF NOT EXISTS fruit (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Pome / Citrus / Berry / Tropical / Melon / Stone Fruit
  food_subgroup VARCHAR(40), 
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO fruit 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Pome Fruits
('F1', 'Apple (Raw)', 'Pome', 'Apple', 52, 0.3, 14.0, 0.2),
('F2', 'Pear (Raw)', 'Pome', 'Pear', 57, 0.4, 15.0, 0.1),

-- Citrus
('F3', 'Orange (Raw)', 'Citrus', 'Orange', 47, 0.9, 12.0, 0.1),

-- Berries
('F4', 'Grapes (Raw)', 'Berry', 'Grapes', 69, 0.6, 18.0, 0.2),
('F5', 'Cherry (Raw)', 'Berry', 'Cherry', 50, 1.0, 12.0, 0.3),
('F6', 'Strawberry (Raw)', 'Berry', 'Strawberry', 32, 0.7, 8.0, 0.3),
('F7', 'Blueberry (Raw)', 'Berry', 'Blueberry', 57, 0.7, 14.0, 0.3),

-- Tropical Fruits
('F8', 'Banana (Raw)', 'Tropical', 'Banana', 89, 1.1, 23.0, 0.3),
('F9', 'Pineapple (Raw)', 'Tropical', 'Pineapple', 50, 0.5, 13.0, 0.1),
('F10', 'Mango (Raw)', 'Tropical', 'Mango', 60, 0.8, 15.0, 0.4),
('F11', 'Kiwi (Raw)', 'Tropical', 'Kiwi', 61, 1.1, 15.0, 0.5),

-- Melons
('F12', 'Watermelon (Raw)', 'Melon', 'Watermelon', 30, 0.6, 8.0, 0.2),
('F13', 'Hami Melon (Raw)', 'Melon', 'Hami Melon', 34, 0.8, 8.2, 0.2),

-- Stone Fruits
('F14', 'Peach (Raw)', 'Stone Fruit', 'Peach', 39, 0.9, 10.0, 0.3);