-- ===============================
-- Table: fruit
-- Description: Fruit products
-- ===============================
CREATE TABLE IF NOT EXISTS fruit (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT '单位：g',
  calorie INT COMMENT '单位：kcal',
  protein FLOAT COMMENT '单位：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  fruit (id, name, type, weight, calorie, protein)
VALUES
  ('F1', '180g-200g 苹果', '苹果', 180, 95, 0.5),
  ('F10', '一个橙子', '橙子', 200, 90, 1.7),
  ('F11', '100g 樱桃', '樱桃', 100, 50, 1),
  ('F12', '150g 樱桃', '樱桃', 150, 75, 1.5),
  ('F13', '100g 菠萝', '菠萝', 100, 50, 0.5),
  ('F14', '1个 奇异果', '奇异果', 100, 60, 1.2),
  ('F15', '2个 奇异果', '奇异果', 100, 120, 2.4),
  ('F2', '230g-250g 苹果', '苹果', 230, 120, 0.6),
  ('F3', '一根香蕉', '香蕉', 120, 105, 1.3),
  ('F4', '200g 哈密瓜', '哈密瓜', 200, 68, 1.6),
  ('F5', '180g-200g 梨', '梨', 180, 95, 0.6),
  ('F6', '230g-250g 梨', '梨', 230, 120, 0.8),
  ('F7', '100g 葡萄', '葡萄', 100, 69, 0.6),
  ('F8', '150g 葡萄', '葡萄', 150, 104, 0.9),
  ('F9', '200g 西瓜', '西瓜', 200, 60, 1.2);