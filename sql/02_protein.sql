USE meal_planner;

-- =================================
-- Table: protein
-- Description: Protein products
-- =================================

CREATE TABLE IF NOT EXISTS protein (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Poultry / Beef / Pork / Seafood / Plant Proteins / Dairy / Egg
  food_subgroup VARCHAR(40),
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO protein 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Poultry
('P1', 'Chicken Breast (Raw)', 'Poultry', 'Chicken', 120, 22.5, 0.0, 2.6),
('P2', 'Chicken Thigh (Raw)', 'Poultry', 'Chicken', 177, 18.0, 0.0, 9.7),
('P3', 'Turkey Breast (Raw)', 'Poultry', 'Turkey', 114, 23.5, 0.0, 1.2),

-- Beef
('P4', 'Lean Beef (Raw)', 'Beef', 'Beef', 187, 26.0, 0.0, 10.0),
('P5', 'Ground Beef (Raw, 85% lean)', 'Beef', 'Beef', 250, 26.0, 0.0, 20.0),

-- Pork
('P6', 'Ground Pork (Raw)', 'Pork', 'Pork', 260, 18.0, 0.0, 21.0),
('P7', 'Pork Rib (Raw)', 'Pork', 'Pork', 291, 17.0, 0.0, 24.0),

-- Seafood
('P8', 'Shrimp (Raw)', 'Seafood', 'Shrimp', 99, 24.0, 0.2, 0.3),
('P9', 'Cod (Raw)', 'Seafood', 'Cod', 82, 18.0, 0.0, 0.7),
('P10', 'Salmon (Raw)', 'Seafood', 'Salmon', 208, 20.0, 0.0, 13.0),
('P11', 'Canned Tuna (In Water)', 'Seafood', 'Tuna', 116, 25.0, 0.0, 1.0),
('P12', 'Canned Salmon', 'Seafood', 'Canned Salmon', 140, 20.0, 0.0, 6.0),
('P13', 'Scallop (Raw)', 'Seafood', 'Scallop', 88, 16.0, 3.0, 0.8),

-- Plant Proteins
('P14', 'Tofu', 'Plant Protein', 'Tofu', 80, 9.0, 2.0, 4.8),
('P15', 'Tempeh', 'Plant Protein', 'Tempeh', 193, 19.0, 9.0, 11.0),
('P16', 'Soy Milk', 'Plant Protein', 'Soy Milk', 44, 2.8, 3.3, 2.0),

-- Dairy
('P17', 'Greek Yogurt (Plain)', 'Dairy', 'Greek Yogurt', 59, 10.0, 3.6, 0.4),
('P18', 'Cottage Cheese', 'Dairy', 'Cottage Cheese', 98, 11.0, 3.4, 4.3),

-- Eggs
('P19', 'Egg (Whole)', 'Egg', 'Whole Egg', 143, 12.6, 1.1, 10.0);