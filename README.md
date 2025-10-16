# Weekly Meal Planner

A Python + SQL based project that automatically generates balanced weekly meal plans according to nutritional goals and personal preferences.

---

## Overview

This project aims to **help users design healthy and efficient meal plans** for every week.  
It combines **Python logic** and **MySQL database** to automatically assemble daily menus based on calorie, protein, and fasting goals.

---

## Features (Current Phase)

· Generates a 7-day plan (2 meals per day)  
· Calculates total calories and protein for each day  
· Follows the 16:8 intermittent fasting schedule  
· Flexible food database (main, protein, vegetable, fruit, oil, dairy)  
· Ready to expand for nutrition tracking and fitness data

---

## Technical Design

**Main language:** Python  
**Database:** MySQL  
**Goal:** Link SQL food data with Python script to generate weekly meal combinations  

### Database Tables
| Table | Description | Columns |
|--------|--------------|----------|
| `main` | Staple food items | id, name, weight, calorie, protein |
| `protein` | Meat and protein sources | id, name, weight, calorie, protein |
| `vegetable` | Vegetables | id, name, weight, calorie, protein |
| `fruit` | Fruits | id, name, weight, calorie, protein |
| `oil` | Oils and fats | id, name, weignt, calorie, protein |
| `seasoning` | Decorating the dish | id, name, weignt, calorie, protein |
| `dairy` | Dairy products | id, name, weight, calorie, protein |
| `meal_plan` | Daily meal plan table | id, date, meal_type, main_id, protein_id, vegetable_id, fruit_id, oil_id, seasoning_id, dairy_id, total_calorie, total_protein |

---

## Future Expansion

· Add `Carbohydrate` and `Fat` tracking  
· Add `weight` and `fitness` record tables  
· Generate automatic charts for weight and calories  
· Add a “recipe recommendation” system based on selected food combinations  
· Generate daily/weekly/monthly completion badges  

---

## Project Goal

This project is a personal experiment and practical exercise to connect **data design**, **SQL logic**, and **Python programming**.  
It’s also a foundation for building a **health-oriented AI assistant** that plans meals intelligently.

---

## Next Steps

1. Implement database creation script in Python  
2. Connect MySQL and fetch sample data  
3. Write a function to assemble daily meals  
4. Add nutritional analysis & visualization  


## Project Plan

### Phase 1: Database Design
- Built 8 tables: main, protein, vegetable, fruit, oil, seasoning, dairy, meal_plan
- Added sample data in `data.sql`
- Supports Chinese input and floating-point nutrition data

### Phase 2: Python Integration 
- Connect MySQL with Python (using `mysql.connector`)
- Implement random meal generator (1 main + 1 protein + 1 vegetable)

### Phase 3: User Features 
- Add calorie/protein summary per meal
- Track weekly meal plan automatically
- Add optional seasoning table for detailed calorie tracking

