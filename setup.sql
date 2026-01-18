CREATE DATABASE IF NOT EXISTS meal_planner
DEFAULT CHARACTER SET utf8mb4;

USE meal_planner;

-- Core Lookup / Catalog tables
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_main.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_protein.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_vegetable.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_fruit.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_dairy.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_oil.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_seasoning.sql;

-- User state / persistence tables
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_user_weekly_plan.sql;
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_user_profile.sql;

-- Execution / recoed tables
SOURCE D:/0 Learning/GitHub/weekly-meal-planner/data/meal_planner_daily_meal_record.sql;