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

### Phase 4: User Modeling & Personalization ✅ *(Completed)*

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

**Completed Tasks**
- [x] Introduced a user-driven planning entry point decoupled from meal generation logic
- [x] Supported two operating modes:
      - User Mode: load persistent user profiles (interface prepared)
      - Visitor Mode: temporary user input without persistence  
- [x] Integrated a target calculation module to derive calorie and protein targets from user attributes  
- [x] Enabled goal-aware target generation via calculator logic (maintenance / fat loss / gain)
- [x] Fully decoupled user modeling, target computation, and meal planning flow
- [x] Implement persistent user_profile table in database (user_id, height, weight, age, sex, activity_level, goal)
- [x] Replace stubbed user loading logic with database-backed DAO layer
- [x] Support multi-user scenarios and profile switching
- [x] Store generated meal plans linked to user_id and date
- [x] Enable strategy selection to be driven by user preferences
- [x] Prepare user-linked data for explainability and evaluation phases


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

### Phase 6: Feedback Loop, Reproducibility & System Polish *(Planned)*

**Goal:**  
Evolve the project into a **reproducible experimental system** suitable for research and long-term extension.

**Planned Features**
- Add user weight log table (`user_log`)
  - Track weekly weight changes  
  - Adjust calorie targets using simple feedback rules  
- Ensure reproducible meal generation:
  - Support fixed random seeds  
  - Centralized configuration file for parameters  
- Modularize project structure:
  - Separate database access, planning logic, strategies, and evaluation  
- Improve usability and reproducibility:
  - `requirements.txt`  
  - `.env.example`  
  - Database initialization scripts  

---

## Long-Term Vision

This project serves as a foundation for future work in:

- Constraint-based optimization  
- Personalized recommendation systems  
- Explainable planning algorithms  
- Data-driven health and fitness applications  

---

## Summary

This project is not just a meal generator.  
It is a **data-driven, constraint-based, and extensible planning framework** that integrates:

- Structured SQL databases  
- Rule-based and strategy-based generation logic  
- User modeling and personalization  
- Explainability, evaluation, and reproducibility  

The system is designed to grow into a research-oriented platform suitable for graduate-level study and experimentation.
