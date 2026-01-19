-- ===============================================================================
-- Table: user_weekly_plan
-- Description: Stores the current active weekly meal plan for each user.
--              Each plan represents a snapshot of a generated weekly meal plan
--              and is uniquely identified by user and plan date.
-- ================================================================================
CREATE TABLE IF NOT EXISTS user_weekly_plan (
	id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    plan_date DATE NOT NULL COMMENT 'The date when the weekly plan is generated',
    plan_json JSON NOT NULL COMMENT 'Serialized weekly meal plan snapshot',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),

    CONSTRAINT fk_user_weekly_plan_user
        FOREIGN KEY (user_id)
        REFERENCES user_profile(user_id)
        ON DELETE CASCADE,

    UNIQUE KEY uk_user_weekly_plan (user_id, plan_date)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;