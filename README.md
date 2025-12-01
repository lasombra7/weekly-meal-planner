# Weekly Meal Planner

A Python + MySQL system that automatically generates balanced weekly meal plans based on calorie and protein goals.  
This project integrates structured nutrition data with Python algorithms to produce realistic meal schedules that match health requirements.

---

## Features (Current Phase)

- Generates a full **7-day meal plan** (2 main meals + optional snack per day)  
- Ensures each day meets **calorie (1600–1800)** and **protein (130–150 g)** targets  
- Applies strict **lower-bound + upper-bound** logic to main meals and snacks  
- Automatically determines whether a snack can be added  
- Flexible food database (main, protein, vegetable, fruit, oil, dairy)  
- Includes console test view showing detailed food selections  
- Ready to expand toward nutrition tracking and user personalization

---

## Technical Design

**Language:** Python  
**Database:** MySQL  
**Goal:** Connect SQL food data with Python generation logic to create structured weekly meal plans.

### Database Tables

| Table | Description | Columns |
|--------|--------------|----------|
| `main` | Staple foods | id, name, type, weight, calorie, protein |
| `protein` | Protein sources | id, name, type, weight, calorie, protein |
| `vegetable` | Vegetables | id, name, type, weight, calorie, protein |
| `fruit` | Fruits (used for snacks) | id, name, type, weight, calorie, protein |
| `oil` | Fats & oils | id, name, type, weight, calorie, protein |
| `seasoning` | Seasonings | id, name, weight, calorie, protein |
| `dairy` | Dairy (used for snacks) | id, name, type, weight, calorie, protein |
| `meal_plan` | Stored weekly meal plan | id, date, meal_type, main_id, protein_id, vegetable_id, fruit_id, oil_id, seasoning_id, dairy_id, total_calorie, total_protein, total_type |

---

## Project Goal

This project is a practical experiment combining **data modeling**, **SQL**, and **Python generation logic**.  
It is also the foundation for a future **AI-powered personalized meal planning assistant**.

---

## Project Plan

### ~~Phase 1: Database Design~~
- ~~Built 8 structured nutrition tables~~  
- ~~Added sample data with Chinese input support~~  
- ~~Exported schema + data via MySQL Workbench~~

---

### Phase 2: Python Integration (**Completed** ✓)

**Goal:**  
Use Python to connect with MySQL and generate balanced 7-day meal plans.

**Implemented Logic:**
- Two main meals must meet:
  - **Calorie lower bound:** ≥ 1600 kcal  
  - **Calorie upper bound:** ≤ 1800 kcal  
  - **Protein lower bound:** ≥ 130 g  
  - **Protein upper bound:** ≤ 150 g  
- A snack is **optional but evaluated daily**:
  - Only allowed if main meals < 1700 kcal  
  - Must not push totals > 1800 kcal (calories) or > 150 g (protein)

**Completed Tasks**
- [x] MySQL → Python integration  
- [x] Random meal composition (main/protein/vegetable)  
- [x] Calorie & protein balancing algorithm  
- [x] Optional snack logic  
- [x] 7-day weekly generator  
- [x] Console test output showing full food details   

---

### Phase 3: Personalized Meal Planning (Process)

**Goal:**  
Introduce two modes — **User Mode** and **Visitor Mode** — to generate personalized 7-day plans.

#### User Mode
- Uses saved user data (username, height, weight, age, activity level)  
- Automatically computes calorie & protein needs  
- Generates weekly plan based on personalized ranges  
- Stores user history and last week's plan  

#### Visitor Mode
- For new users without accounts  
- Requires manual input of height, weight, age, and activity level  
- Auto-computes nutrition targets and generates a full weekly plan  

---

### Phase 4: Future Development

- Add calorie & protein tracking based on actual weight  
- Record fitness and weight progress  
- Visual charts for weekly/monthly nutrition  
- Recipe recommendation system  
- Add oil & seasoning logic into meals  
