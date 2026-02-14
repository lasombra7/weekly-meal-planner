# Weekly Meal Planner

A Python + MySQL system that automatically generates balanced weekly meal plans based on calorie and protein goals.
This project integrates structured nutrition data with constraint-based planning, strategy-driven selection, and user modeling to produce realistic and extensible meal schedules.

---

## Features (Current Phase)

- Generates a full **7-day meal plan**
- Supports **2-meal or 3-meal daily structures**
- Each day consists of:
  - Main meals (lunch / dinner or breakfast / lunch / dinner)
  - Optional snack (fruit + dairy)
- Ensures each day meets **calorie and protein targets**
- Applies strict **lower-bound + upper-bound** constraint logic
- Automatically determines whether a snack can be added
- Flexible food database (main, protein, vegetable, fruit, oil, dairy)
- Strategy-based food selection framework
- Persistent weekly plan storage for registered users
- Visitor (guest) mode without persistence

---

## System Architecture Overview

The system is structured as a layered planning pipeline:

User / Visitor Input  
→ Target Calculation (calorie & protein)  
→ Meal Structure Selection (2-meal / 3-meal)  
→ Strategy-Based Food Selection  
→ Constraint-Based Meal Generation  
→ Weekly Plan Persistence (User Mode)

This separation allows independent experimentation with:
- user modeling
- meal structure
- food selection strategies
- constraint logic

---

## Technical Design

**Language:** Python  
**Database:** MySQL  

The system decouples:
- Data Access Layer (DAO): Responsible for retrieving normalized food data from the database.
- Target Computation Layer: Computes daily nutritional targets based on user profile and goals.
- Strategy Layer: Applies rule-based heuristics to select food categories and meal composition.
- Meal Generation Layer: Performs portion scaling and target-driven nutrient balancing.
- Persistence Layer: Stores generated plans and evaluation metrics as JSON snapshots.

### Database Tables

| Table | Description | Columns |
|------|------------|---------|
| `main` | Staple foods(carbohydrate-dominant) | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `protein` | Protein sources (raw standardized) | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `vegetable` | Vegetables | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `oil` | Fats & oils | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `seasoning` | Seasonings | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `fruit` | Fruits (used for snacks) | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `dairy` | Dairy (used for snacks) | id, name, food_group, food_subgroup, calorie_per_100g, protein_per_100g, carb_per_100g, fat_per_100g |
| `user_profile` | Persistent user attributes | user_id, height_cm, weight_kg, age, sex, activity_level, goal, created_at |
| `user_weekly_plan` | Weekly meal plan snapshot with versioning and macro summary | id, user_id, plan_date, plan_version, plan_json, total_calorie_week, total_protein_week, total_carb_week, total_fat_week, created_at |
| `daily_meal_record` | Generated daily meal records with selected food items and macro summary | id, date, meal_type, main_id, protein_id, vegetable_id, fruit_id, oil_id, seasoning_id, dairy_id, total_calorie, total_protein, total_carb, total_fat, food_item_count |

---

## Strategy Framework

Meal selection logic is abstracted via a unified strategy interface.

Available strategies:
- **RandomStrategy** — baseline randomized selection
- **GreedyStrategy** — protein-density–priority selection
- **WeightedStrategy** — probabilistic selection weighted by protein density

Strategies are registered centrally and injected at runtime without modifying core generation logic.

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

### Phase 3: Strategy Framework & Goal-Based Planning ✅ *(Completed)*

**Goal:**  
Extend the generator into a **multi-strategy planning framework** that adapts to different nutrition goals while keeping the generation flow modular and extensible.

**Design Focus:**
- Decouple *food selection logic* from *meal generation flow*
- Enable strategy-based experimentation without changing core constraints
- Prepare the system for explainability and personalization in later phases

**Completed Tasks**
- [x] Introduced a **Strategy abstraction layer** for main meal selection  
- [x] Defined a unified `MealStrategy` interface (`pick_main / pick_protein / pick_vegetable`)  
- [x] Implemented **RandomStrategy** as a baseline strategy  
- [x] Refactored `generate_main_meal()` to be **strategy-driven**  
- [x] Preserved Phase 2 behavior while upgrading system architecture  
- [x] Ensured strategy injection via function parameters (default fallback supported)
- [x] Implemented **Greedy Strategy** (protein-priority selection)
- [x] Implemented **Weighted Strategy** (quality-aware probabilistic selection)
- [x] Expose strategy selection via centralized registry (configuration-ready)

---

### Phase 4: User Modeling & Personalized Targets ✅ *(Completed)*

**Goal:**  
Move from static nutrition targets to **user-centered, profile-driven meal planning**.

**Design Focus:**
- Separate *user modeling* from *meal generation logic*
- Support both persistent users and temporary visitors
- Compute calorie and protein targets dynamically from user attributes
- Prepare the system for multi-user and personalized planning scenarios

**Completed Tasks**
- [x] Designed and implemented `user_profile` table (height / weight / age / sex / activity_level / goal)
- [x] Introduced **User Mode** (persistent profiles stored in database)  
- [x] Introduced **Visitor Mode** (temporary input without persistence)  
- [x] Implemented calorie & protein target calculation module  
- [x] Supported goal-aware target adjustment (maintain / lose / gain)  
- [x] Decoupled user modeling, target computation, and meal generation  
- [x] Implemented persistent weekly plan storage (`user_weekly_plan`)  
- [x] Enabled loading latest weekly meal plan snapshot per user  
- [x] Supported multi-user profile switching and independent plan generation  

---

### Phase 4.5: Meal Structure Modeling ✅ *(Completed)*

**Goal:**  
Introduce **flexible daily meal structures** while preserving existing nutrition constraints.

**Design Focus:**
- Treat meal structure (2-meal / 3-meal) as a *structural parameter*, not a nutrition change
- Reuse existing constraint logic with different per-meal target allocations
- Keep meal structure independent from strategy and food selection logic
- Ensure both structures support optional snack logic consistently

**Completed Tasks**
- [x] Introduced `meal_structure` as an explicit planning parameter  
- [x] Refactored legacy daily generation into `generate_two_meal_day()`  
- [x] Defined clear per-meal calorie & protein distributions:
  - 2-meal structure: Lunch (40%), Dinner (60%)
  - 3-meal structure: Breakfast (25%), Lunch (35%), Dinner (40%)
- [x] Centralized meal structure routing via `generate_daily_meal_with_structure()`  
- [x] Preserved calorie & protein validation logic across meal structures  
- [x] Enabled optional snack generation for both 2-meal and 3-meal days  
- [x] Ensured weekly plan generation remains structure-agnostic
- [x] Bind `meal_structure` preference to `user_profile` (persistent users)  
- [x] Support visitor-mode meal structure override without persistence

---

### Phase 5: Explainable Planning & Evaluation ✅ *(Completed)*

**Goal:**  
Make meal plan generation **transparent, interpretable, and measurable**.

**Design Focus:**
- Expose *why* a specific food or meal combination was selected
- Separate explanation logic from generation logic
- Enable systematic evaluation of plan quality and stability

**Completed Tasks**
- [x] Surface key decision factors used during generation
- [x] Introduce basic evaluation metrics for daily and weekly plans
- [x] Add explainability signals to meal plan output
- [x] Support user-facing explainability output (e.g. console-level)
- [x] Add basic testing coverage for explanation and evaluation logic

---

### Phase 6: Feedback Loop, Reproducibility & System Polish *(In Progress)*

**Goal:**  
Evolve the project into a **reproducible experimental system** suitable for long-term research and extension.

**Design Focus:**
- Close the loop between generated plans and real user outcomes
- Improve experiment reproducibility and configuration control
- Strengthen system modularity and usability

**Planned Features**
- Introduce user weight log table for longitudinal tracking  
- Implement simple feedback rules to adjust calorie targets over time  
- Support reproducible meal generation via fixed random seeds  
- Centralize system parameters into configuration files  
- Add environment and dependency setup artifacts:
  - `requirements.txt`  
  - `.env.example`  
  - database initialization scripts  
- Further modularize DAO, planning, strategy, and evaluation layers
- Enable optional persistence of explanation or evaluation results

---

## Long-Term Vision

This project serves as a foundation for future research and system expansion in:

### 1. Macro-Aware Nutritional Planning
- Multi-macro tracking (calorie, protein, carbohydrate, fat)
- Macro-balanced meal generation
- Portion-adjustable meal construction
- Goal-aware macro distribution strategies (cut, bulk, maintenance)

### 2. Constraint-Based Optimization
- Linear programming for macro and calorie constraints
- Hard vs soft constraint modeling
- Multi-objective optimization (nutrition + diversity + cost)

### 3. Personalized Recommendation Systems
- User-specific preference modeling
- Habit-aware meal generation
- Diversity-aware food rotation
- Adaptive macro targeting

### 4. Explainable Planning Algorithms
- Traceable food selection reasoning
- Constraint satisfaction transparency
- Version-controlled generation logic
- Reproducible weekly plan snapshots

### 5. Food Diversity & Statistical Analysis
- Food group coverage metrics
- Weekly diversity scoring
- Macro distribution variance tracking
- Longitudinal user nutrition pattern analysis

### 6. Scalable Health Data Platform
- Structured food taxonomy (food_group / food_subgroup)
- Macro-aware database schema
- Version-controlled plan storage
- Research-ready experimental framework
---

## Summary

This project is not just a meal generator.  
It is a **data-driven, constraint-based, and extensible planning framework** built with a modular architecture that decouples:

- Data access (DAO layer)
- Target computation
- Strategy-driven food selection
- Portion-aware meal generation
- Persistence and evaluation logic

The system integrates:

- Structured SQL databases (raw-standardized, per-100g macro schema)
- Target-driven protein scaling
- Rule-based and strategy-based generation logic
- User modeling and personalization
- Explainability, evaluation, and weekly stability metrics
- Forward-compatible macro support (carb/fat ready)

Version 1.0 focuses on calorie- and protein-driven planning with explainable 
evaluation metrics. The architecture is intentionally designed to support 
future multi-objective optimization without disrupting the core system.

The system is designed to evolve into a research-oriented planning platform 
suitable for graduate-level study, experimentation, and optimization research.
