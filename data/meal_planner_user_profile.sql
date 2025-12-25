CREATE TABLE IF NOT EXISTS user_profile (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    height_cm INT NOT NULL,
    weight_kg DECIMAL(5, 2) NOT NULL,
    age INT NOT NULL,
    sex ENUM('female', 'male') NOT NULL,
    activity_level ENUM('low', 'light', 'moderate', 'high') NOT NULL,
    goal ENUM('maintain', 'lose', 'gain') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;