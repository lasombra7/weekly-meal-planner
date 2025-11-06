# Weekly Meal Planner

A Python + MySQL project that automatically generates balanced weekly meal plans based on calorie and protein goals.  
It helps users design healthy and efficient meal schedules, combining Python logic and database automation.


---

## Features (Current Phase)

· Generates a 7-day plan (two main meals + optional snack a day)  
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

## Project Plan

### ~~Phase 1: Database Design~~
- ~~Built 8 tables: main, protein, vegetable, fruit, oil, seasoning, dairy, meal_plan~~
- ~~Added sample data in `data.sql`~~
- ~~Supports Chinese input and floating-point nutrition data~~

### Phase 2: Python Integration (In Progress)
**Goal:**  
Use Python to connect with the MySQL database and automatically generate weekly meal plans.

**Requirements:**  
- 7-day meal plan, 2 main meals per day (+ optional snack)
- Daily protein: **130–150 g**  
- Daily calories: **1500-1800 kcal**  
- Each main meal: around **700–850 kcal**
- Optional daily snack: **200–300 kcal**  
- Weekly total ingredients: **10–15 unique items**
  - Main: 3–4 types
  - Protein: 3–6 types
  - Vegetable: 4–6 types
  - Fruit: 2–4 types (used in snacks) 
  - Dairy: 1–2  types (used in snacks)
  - Oil & Seasoning: reserved for future Recipe Mode expansion

**Next Steps:**  
- [x] Connect Python to MySQL  
- [x] Randomly select one food per category to form each meal  
- [x] Calculate total daily calories and protein  
- [x] Generate full 7-day meal plans  
- [ ] Save results to the `meal_plan` table  

### Phase 3: Personalized Meal Planning
**Goal:**  
Introduce 2 geberation modes: **User Mode** and **Visitor Mode**

**Features:**
- Automatically calculate daily energy and nutrient requirements based on user attributes
- Generate customized 7-day meal plans with calorie and protein constraints
- Provide flexible input options for both registered users and visitors

**Requirements:** 
**User Mode**
- Uses pre-recorded user information stored in the database
- Includes parameters: username, height, weight, age, exercise frequency
- Automatically computes daily calorie and protein targets using standard metabolic formulas
- Users only need to input their username to generate a full weekly meal plan
- Record previous week plan

**Visitor Mode**
- Designed for first-time or unregistered users
- Requires manual input of height, weight, age, and exercise frequency
- Calculates daily energy needs dynamically based on user input
- Generates a complete 7-day meal plan following the same logic as User Mode

---

### Phase 4: Future Development
- Add calorie and protein tracking by weight  
- Record user fitness and weight progress  
- Implement visual charts for calories, protein, and progress trends  
- Add recipe recommendation system
- Set the oil content as an meal limit


