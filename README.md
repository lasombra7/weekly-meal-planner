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
|------|------------|---------|
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
It is also the foundation for a future **research-oriented, personalized, and explainable meal planning system**.

---

## Project Roadmap

### Phase 1: Database Design ✅ *(Completed)*

- Built 8 normalized nutrition tables  
- Designed structured schemas for food categories  
- Added sample data with UTF-8 (Chinese) support  
- Exported schema and seed data via MySQL Workbench  

---

### Phase 2: Python Integration & Constraint-Based Planning ✅ *(Completed)*

**Goal:**  
Use Python to connect with MySQL and generate balanced 7-day meal plans under strict nutritional constraints.

**Implemented Logic:**
- Two main meals must satisfy:
  - **Calorie range:** 1600–1800 kcal  
  - **Protein range:** 130–150 g  
- Snack is optional and evaluated daily:
  - Only added if main meals < 1700 kcal  
  - Must not exceed daily upper bounds  

**Completed Tasks**
- [x] MySQL → Python integration  
- [x] Randomized meal composition (main / protein / vegetable)  
- [x] Calorie & protein constraint validation  
- [x] Optional snack decision logic  
- [x] 7-day weekly meal plan generator  
- [x] Console output with full food-level details  

---

### Phase 3: Strategy Framework & Goal-Based Planning *(Planned)*

**Goal:**  
Extend the generator into a **multi-strategy planning framework** that adapts to different nutrition goals.

**Planned Features**
- Support multiple user goals:
  - Maintain weight  
  - Fat loss  
  - Muscle gain  
  - Recomposition (fat loss + muscle retention)  
- Automatically convert goals into personalized calorie & protein ranges  
- Implement multiple generation strategies:
  - **Random Strategy** (baseline)  
  - **Greedy Strategy** (prioritize protein satisfaction)  
  - **Weighted Strategy** (optimize overall meal quality)  
- Allow strategy selection via configuration or command-line options  

---

### Phase 4: User Modeling & Personalization *(Planned)*

**Goal:**  
Move from static targets to **user-centered personalized meal planning**.

**Planned Features**
- Add `user_profile` table:
  - user_id, height, weight, age, sex, activity_level, goal  
- Support two operating modes:
  - **User Mode:** load saved user profiles  
  - **Visitor Mode:** temporary input without persistence  
- Integrate a target calculation module:
  - Compute calorie & protein targets from user attributes  
  - Adjust targets based on selected goal  
- Store generated meal plans linked to user_id and date  

---

### Phase 5: Explainable Planning & Evaluation *(Planned)*

**Goal:**  
Make meal plan generation **transparent, interpretable, and measurable**.

**Planned Features**
- Explainable decision logs for each generated day:
  - Why a specific food or protein source was selected  
  - Why a snack was added or omitted  
  - Which constraint influenced the decision  
- Structured explanation output (console and optional database storage)  
- Introduce evaluation metrics:
  - Daily calorie deviation from target  
  - Daily protein deviation from target  
  - Snack usage frequency  
  - Ingredient repetition rate  

---

