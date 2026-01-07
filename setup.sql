CREATE DATABASE IF NOT EXISTS meal_planner
DEFAULT CHARACTER SET utf8mb4;

USE meal_planner;

-- Core Lookup / Catalog tables
SOURCE data/meal_planner_main.sql;
SOURCE data/meal_planner_protein.sql;
SOURCE data/meal_planner_vegetable.sql;
SOURCE data/meal_planner_fruit.sql;
SOURCE data/meal_planner_dairy.sql;
SOURCE data/meal_planner_oil.sql;
SOURCE data/meal_planner_seasoning.sql;

-- System / runtime tables
SOURCE data/meal_planner_meal_plan.sql;
SOURCE data/meal_planner_user_profile.sql;