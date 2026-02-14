USE meal_planner;

-- ============================
-- Table: dairy
-- Description: Dairy products
-- ============================

CREATE TABLE IF NOT EXISTS dairy (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(80),
  food_group VARCHAR(30),  -- Yogurt / Milk / Cheese / Plant Milk
  food_subgroup VARCHAR(40), 
  calorie_per_100g FLOAT COMMENT 'Unit: kcal',
  protein_per_100g FLOAT COMMENT 'Unit: g',
  carb_per_100g FLOAT COMMENT 'Unit: g',
  fat_per_100g FLOAT COMMENT 'Unit: g'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO dairy 
(id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g)
VALUES
-- Yogurt
('D1', 'Plain Yogurt', 'Yogurt', 'Regular Yogurt', 61, 3.5, 4.7, 3.3),
('D2', 'Greek Yogurt (Low Fat)', 'Yogurt', 'Greek Yogurt', 65, 9.0, 3.6, 0.4),
('D3', 'Flavored Yogurt', 'Yogurt', 'Flavored Yogurt', 95, 3.0, 15.0, 2.5),
('D4', 'Kefir', 'Yogurt', 'Kefir', 60, 3.3, 4.8, 3.5),

-- Milk
('D5', 'Whole Milk', 'Milk', 'Whole Milk', 60, 3.2, 4.8, 3.3),
('D6', 'Low-Fat Milk (2%)', 'Milk', 'Low-Fat Milk', 50, 3.4, 4.9, 2.0),
('D7', 'Skim Milk', 'Milk', 'Skim Milk', 34, 3.4, 5.0, 0.1),

-- Cheese
('D8', 'Mozzarella Cheese', 'Cheese', 'Mozzarella', 280, 22.0, 3.0, 22.0),
('D9', 'Cheddar Cheese', 'Cheese', 'Cheddar', 403, 25.0, 1.3, 33.0),
('D10', 'Cottage Cheese', 'Cheese', 'Cottage Cheese', 98, 11.0, 3.4, 4.3),

-- Plant Milk
('D11', 'Unsweetened Soy Milk', 'Plant Milk', 'Soy Milk', 33, 3.3, 0.7, 1.8),
('D12', 'Unsweetened Almond Milk', 'Plant Milk', 'Almond Milk', 17, 0.6, 0.3, 1.2);