-- ==========================================================================================
-- Table: meal_plan
-- Description: Generated daily meal plans with selected food items and nutrition summary
-- ==========================================================================================
USE meal_planner;
CREATE TABLE IF NOT EXISTS daily_meal_record (
  id INT AUTO_INCREMENT,
  date DATE,
  meal_type ENUM('Lunch', 'Dinner'),
  main_id CHAR(5),
  protein_id CHAR(5),
  vegetable_id CHAR(5),
  fruit_id CHAR(5),
  oil_id CHAR(5),
  seasoning_id CHAR(5),
  dairy_id CHAR(5),
  total_calorie INT COMMENT 'Unit: kcal',
  total_protein FLOAT COMMENT 'Unit: g',
  food_item_count INT,
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;