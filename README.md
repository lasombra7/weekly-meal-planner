# Weekly Meal Planner

A Python + MySQL project that automatically generates balanced weekly meal plans based on calorie and protein goals.  
It helps users design healthy and efficient meal schedules, combining Python logic and database automation.


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
| `main` | Staple food items | id, name, type, weight, calorie, protein |
| `protein` | Meat and protein sources | id, name, type, weight, calorie, protein |
| `vegetable` | Vegetables | id, name, type, weight, calorie, protein |
| `fruit` | Fruits | id, name, type, weight, calorie, protein |
| `oil` | Oils and fats | id, name, type, weight, calorie, protein |
| `seasoning` | Decorating the dish | id, name, weight, calorie, protein |
| `dairy` | Dairy products | id, name, type, weight, calorie, protein |
| `meal_plan` | Daily meal plan table | id, date, meal_type, main_id, protein_id, vegetable_id, fruit_id, oil_id, seasoning_id, dairy_id, total_calorie, total_protein, total_type |


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

### ~~Phase 1: Database Design~~
- ~~Built 8 tables: main, protein, vegetable, fruit, oil, seasoning, dairy, meal_plan~~
- ~~Added sample data in `data.sql`~~
- ~~Supports Chinese input and floating-point nutrition data~~

### <span style="color:red">Phase 2: Python Integration (In Progress)</span>
**Goal:**  
Use Python to connect with the MySQL database and automatically generate weekly meal plans.

**Requirements:**  
- 7-day meal plan, 2 meals per day (lunch and dinner)  
- Daily protein: **130–150 g**  
- Daily calories: **1800–2000 kcal**  
- Each meal: around **700 kcal**, not exceeding 850 kcal  
- Optional daily snack: **200–300 kcal**  
- Weekly total ingredients: **15–20 kinds**
  - Main: 3–4  
  - Protein: 3–6  
  - Vegetable: 4–6  
  - Fruit: 2–4  
  - Oil: 1–3  
  - Dairy: 1–2

**Next Steps:**  
- [x] Connect Python to MySQL  
- [x] Randomly select one food per category to form each meal  
- [ ] Calculate total daily calories and protein  
- [ ] Generate full 7-day meal plans  
- [ ] Save results to the `meal_plan` table  

---

### Phase 3: Future Development
- Add calorie and protein tracking by weight  
- Record user fitness and weight progress  
- Implement visual charts for calories, protein, and progress trends  
- Add recipe recommendation system
- Set the oil content as an meal limit
- Two mode to generate weekly meal plan: user and visitor


