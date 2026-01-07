-- =============================
-- Table: main
-- Description: Main products
-- =============================
CREATE TABLE IF NOT EXISTS main (
  id CHAR(5) NOT NULL,
  name VARCHAR(50),
  type VARCHAR(20),
  weight INT COMMENT '单位：g',
  calorie INT COMMENT '单位：kcal',
  protein FLOAT COMMENT '单位：g',
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO
  main (id, name, type, weight, calorie, protein)
VALUES
  ('M1', '200g 米饭', '米饭', 200, 260, 5.2),
  ('M10', '2片全麦面包', '全麦面包', 60, 150, 6),
  ('M11', '4片全麦面包', '全麦面包', 120, 300, 12),
  ('M12', '辛拉面', '泡面', 120, 505, 10),
  ('M13', '乌龙面', '泡面', 110, 510, 9),
  ('M14', '乌冬面', '乌冬面', 200, 220, 6),
  ('M15', '150g 芋头', '芋头', 150, 135, 2.2),
  ('M16', '250g 芋头', '芋头', 250, 225, 3.8),
  ('M2', '300g 米饭', '米饭', 300, 390, 7.8),
  ('M3', '200g 红薯', '红薯', 200, 180, 2.6),
  ('M4', '300g 红薯', '红薯', 300, 270, 3.9),
  ('M5', '85g （干）山东拉面', '山东拉面', 85, 300, 10),
  ('M6', '170g （干）山东拉面', '山东拉面', 170, 600, 20),
  ('M7', '150g 玉米罐头', '玉米', 150, 135, 4.8),
  ('M8', '300g 玉米罐头', '玉米', 300, 270, 9.6),
  ('M9', '一根煮玉米', '玉米', 180, 160, 5.4);