-- ============================
-- Table: dairy
-- Description: Dairy products
-- ============================
CREATE TABLE IF NOT EXISTS dairy (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT '单位：g',
  calorie INT COMMENT '单位：kcal',
  protein FLOAT COMMENT '单位：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  dairy (id, name, type, weight, calorie, protein)
VALUES
  ('D1', '100g 酸奶', '酸奶', 100, 61, 3.5),
  ('D2', '100g 果味酸奶', '酸奶', 100, 95, 3),
  ('D3', '100g 高蛋白酸奶', '酸奶', 100, 65, 9),
  ('D4', '250ml 脱脂牛奶', '牛奶', 250, 85, 8.5),
  ('D5', '30g 马苏里拉芝士', '芝士', 30, 85, 6.6),
  ('D6', '250ml 无糖豆奶', '豆奶', 250, 90, 7);