USE meal_planner;

-- ============================
-- Table: vegetable
-- Description: Vegetable products
-- ============================

CREATE TABLE vegetable (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Leafy / Cruciferous / Root / Fruit Vegetable / Legume / Mushroom / Sea Vegetable
  food_subgroup VARCHAR(40), 
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO vegetable 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Leafy Vegetables
('V1', 'Iceberg Lettuce (Raw)', 'Leafy', 'Iceberg Lettuce', 15, 1.2, 2.9, 0.2),
('V2', 'Bok Choy (Raw)', 'Leafy', 'Bok Choy', 21, 1.6, 2.2, 0.2),
('V3', 'Chinese Broccoli (Raw)', 'Leafy', 'Chinese Broccoli', 35, 3.2, 5.0, 0.6),
('V4', 'Spinach (Raw)', 'Leafy', 'Spinach', 23, 2.9, 3.6, 0.4),
('V5', 'Kale (Raw)', 'Leafy', 'Kale', 49, 4.3, 9.0, 0.9),
('V6', 'Asparagus (Raw)', 'Leafy', 'Asparagus', 20, 2.2, 3.9, 0.1),

-- Cruciferous
('V7', 'Napa Cabbage (Raw)', 'Cruciferous', 'Napa Cabbage', 17, 1.0, 3.2, 0.2),
('V8', 'Broccoli (Raw)', 'Cruciferous', 'Broccoli', 34, 2.8, 6.6, 0.4),
('V9', 'Cauliflower (Raw)', 'Cruciferous', 'Cauliflower', 25, 1.9, 5.0, 0.3),

-- Root
('V10', 'Carrot (Raw)', 'Root', 'Carrot', 33, 0.8, 8.0, 0.2),
('V11', 'Daikon Radish (Raw)', 'Root', 'Daikon Radish', 18, 0.6, 4.1, 0.1),
('V12', 'Onion (Raw)', 'Root', 'Onion', 40, 1.1, 9.3, 0.1),
('V13', 'Garlic (Raw)', 'Root', 'Garlic', 149, 6.4, 33.1, 0.5),

-- Fruit Vegetables
('V14', 'Tomato (Raw)', 'Fruit Vegetable', 'Tomato', 22, 1.0, 4.8, 0.2),
('V15', 'Cucumber (Raw)', 'Fruit Vegetable', 'Cucumber', 15, 0.7, 3.6, 0.1),
('V16', 'Bell Pepper (Raw)', 'Fruit Vegetable', 'Bell Pepper', 31, 1.0, 6.0, 0.3),
('V17', 'Eggplant (Raw)', 'Fruit Vegetable', 'Eggplant', 25, 1.0, 6.0, 0.2),
('V18', 'Zucchini (Raw)', 'Fruit Vegetable', 'Zucchini', 17, 1.2, 3.1, 0.3),

-- Legume Vegetables
('V19', 'Green Peas (Raw)', 'Legume', 'Green Peas', 81, 5.4, 14.5, 0.4),
('V20', 'Snow Peas (Raw)', 'Legume', 'Snow Peas', 42, 2.8, 7.5, 0.2),

-- Mushroom
('V21', 'Mushroom (Raw)', 'Mushroom', 'White Mushroom', 22, 3.1, 3.3, 0.3),

-- Sea Vegetable
('V22', 'Wakame (Raw)', 'Sea Vegetable','Wakame', 45, 3.0, 9.0, 0.6);
