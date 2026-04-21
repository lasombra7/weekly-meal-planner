# Weekly Meal Planner

A modular, constraint-based nutritition planning system built with *python* and *MySQL*
The system integrates user modeling, strategy-driven selection, discrete portion scaling, and explainable macro validation to generate reproducible weekly meal plans.

---

## Project Motivation
Nutrition planning is often heuristic-driven and lacks transparency in decision logic.

This project was designed to explore:
- Structured constraint-based planning under nutritional bounds
- Modular system design for experimentation
- Reproducible decision pipelines
- Explainable portion scaling logic

Rather than building a simple meal generator, the goal was to construct a layered planning system capable of evolving into a macro-aware optimization framework.

---

## Design Philosophy

The system is built on five guiding principles:
1. Separation of Concerns
   User modeling, strategy selection, constraint validation, and persistence are decoupled.
2. Deterministic Constraints over Randomness
   Random selection is constrained by hard macro bounds and fallback search mechanisms.
3. Explainability over Black-Box Decisions  
   Each meal decision exposes evaluation signals and macro-level reasoning.
4. Reproducibility  
   Weekly plans are stored as versioned snapshots with macro summaries.
5. Extensibility  
   The architecture allows future integration of optimization solvers and feedback loops without restructuring core logic.
   
---

## 🚀 v1.0 Features

- Automatic **7-day meal plan generation**
- Calorie and protein **target-based planning**
- Support for **2-meal and 3-meal daily structures**
- Strategy-based food selection framework
- Constraint-aware macro balancing
- Optional snack generation
- **Explainable decision tracing**
- Weekly evaluation metrics (calorie deviation, protein deviation, stability)
- Visitor mode demo for quick system testing
- Persistent weekly plan storage for registered users

---

## System Architecture

```
User Input
   │
   ▼
Target Calculation
   │
   ▼
Meal Structure Selection
   │
   ▼
Strategy-Based Food Selection
   │
   ▼
Daily Meal Generation
   │
   ▼
Explanation Layer
   │
   ▼
Weekly Evaluation
   │
   ▼
Database Persistence (MySQL)
```

---

## Installation
Clone the repository:

```bash
git clone https://github.com/lasombra7/weekly-meal-planner.git
cd weekly-meal-planner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
mysql < sql/setup.sql
```

Run the demo:

```bash
python run_demo.py
```

---

## Example Output

```text
Weekly Meal Planner Demo (Visitor Mode)

User Profile
  Height: 180 cm
  Weight: 75 kg
  Age: 28
  Sex: male
  Activity Level: moderate
  Goal: maintain
  Meal Structure: two_meals

Targets
  Calorie Target: 2697 kcal
  Protein Range: 120 - 150 g
  Strategy: random

Day 1
----------------------------------------
  Main Meal 1
    - Main: White Bread (350g, 265 kcal/100g, 9 g protein/100g)
    - Protein: Cottage Cheese (250g, 98 kcal/100g, 11 g protein/100g)
    - Vegetable: Bok Choy (200g)

Weekly Metrics
Average Calorie Deviation: -271.3
Protein Failure Days: 0
Snack Usage Rate: 0.29
```

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

### Phase 1: Database Foundation ✅
Built a normalized MySQL nutrition database for structured meal planning.
- Normalized food-category tables
- Extensible nutrition schema
- Seed data support

### Phase 2: Constraint-Based Meal Generation ✅
Connected Python with MySQL to generate 7-day meal plans under calorie and protein constraints.
- Python–MySQL integration
- Meal generation pipeline
- Constraint validation
- Optional snack logic

### Phase 3: Strategy Framework ✅
Refactored the generator into a strategy-driven planning system.
- Strategy abstraction
- Random / Greedy / Weighted strategies
- Configurable strategy injection

### Phase 4: Personalization & Meal Structure ✅
Added user-driven target calculation and flexible daily meal structures.
- User / Visitor modes
- Dynamic calorie and protein targets
- 2-meal and 3-meal planning
- Persistent weekly plan storage

### Phase 5: Explainability, Evaluation & Reproducibility ✅
Improved transparency and system reliability for experimental use.
- Explainable generation signals
- Daily / weekly evaluation metrics
- Discrete constrained optimization
- Fallback search and configurable tolerances

---

## Long-Term Vision

This project serves as a foundation for future research in computational nutrition planning and personalized health systems.
The current rule-based planner can be extended toward optimization, learning-based recommendation, and explainable decision systems.

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

---

## Summary

This project is not just a meal generator.  
It is a **data-driven, constraint-based, and extensible planning framework** built with a modular architecture that decouples:

- Data access (DAO layer)
- Target computation
- Strategy-driven food selection
- Portion-aware meal generation
- Persistence and evaluation logic

Version 1.0 focuses on calorie- and protein-driven planning with explainable 
evaluation metrics. The architecture is intentionally designed to support 
future multi-objective optimization without disrupting the core system.

The system is designed to evolve into a research-oriented planning platform 
suitable for graduate-level study, experimentation, and optimization research.
