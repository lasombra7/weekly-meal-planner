USE meal_planner;

-- ==========================================================================================
-- Table: meal_plan
-- Description: Generated daily meal plans with selected food items and nutrition summary
-- ==========================================================================================

CREATE TABLE daily_meal_record (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE,
  meal_type ENUM('Lunch', 'Dinner'),

  -- Food IDs
  main_id CHAR(5),
  protein_id CHAR(5),
  vegetable_id CHAR(5),
  fruit_id CHAR(5),
  oil_id CHAR(5),
  seasoning_id CHAR(5),
  dairy_id CHAR(5),

  -- Portion (in grams)
  main_portion_g FLOAT,
  protein_portion_g FLOAT,
  vegetable_portion_g FLOAT,
  fruit_portion_g FLOAT,
  oil_portion_g FLOAT,
  seasoning_portion_g FLOAT,
  dairy_portion_g FLOAT,

  -- Nutrition summary
  total_calorie FLOAT COMMENT 'Unit: kcal',
  total_protein FLOAT COMMENT 'Unit: g',
  total_carb FLOAT COMMENT 'Unit: g',
  total_fat FLOAT COMMENT 'Unit: g',
  
  food_item_count INT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;