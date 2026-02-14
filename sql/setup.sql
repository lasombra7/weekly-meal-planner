DROP DATABASE IF EXISTS meal_planner;

CREATE DATABASE meal_planner
DEFAULT CHARACTER SET utf8mb4;

USE meal_planner;

-- Core Lookup / Catalog tables
SOURCE 01_main.sql;
SOURCE 02_protein.sql;
SOURCE 03_vegetable.sql;
SOURCE 04_fruit.sql;
SOURCE 05_dairy.sql;
SOURCE 06_oil.sql;
SOURCE 07_seasoning.sql;

-- User state / persistence tables
SOURCE 08_user_profile.sql;
SOURCE 09_user_weekly_plan.sql;

-- Execution / recoed tables
SOURCE 10_daily_meal_record.sql;