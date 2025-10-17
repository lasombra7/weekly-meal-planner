use meal_planner;

-- 输入几组用于测试的数据。
insert into main (id, name, weight, calorie, protein)
values
('M1', '200g 米饭', 200, 260, 5.2),
('M2', '300g 米饭', 300, 390, 7.8),
('M3', '200g 红薯', 200, 180, 2.6),
('M4', '300g 红薯', 300, 270, 3.9);

insert into protein (id, name, weight, calorie, protein)
values
('P1', '200g 煮鸡胸+腿肉', 200, 345, 56),
('P2', '300g 煮鸡胸+腿肉', 300, 518, 84),
('P3', '300g 豆腐', 300, 240, 27),
('P4', '200g 煮牛瘦肉', 200, 380, 60);

insert into vegetable (id, name, weight, calorie, protein)
values
('V1', '300g 水煮/生吃圆生菜', 300, 45, 3.6),
('V2', '500g 水煮/生吃圆生菜', 500, 75, 6),
('V3', '300g 生芥蓝', 300, 105, 9.6),
('V4', '300g 西红柿', 300, 66, 3);

insert into fruit (id, name, weight, calorie, protein)
values
('F1', '180g-200g 苹果', 180, 95, 0.5),
('F2', '230g-250g 苹果', 230, 120, 0.6),
('F3', '一根香蕉', 120, 105, 1.3),
('F4', '200g 哈密瓜', 200, 68, 1.6);

insert into oil (id, name, weight, calorie, protein)
values
('O1', '一勺食用油', 10, 90, 0),
('O2', '一勺橄榄油', 10, 90, 0);

insert into seasoning (id, name, weight, calorie, protein)
values
('S1', '一勺酱油', 16, 10, 1.5),
('S2', '一勺醋', 15, 3, 0),
('S3', '一勺蚝油', 15, 15, 0.3),
('S4', '一勺蒸鱼豉油', 16, 10, 1);

insert into dairy (id, name, weight, calorie, protein)
values
('D1', '100g 酸奶', 100, 61, 3.5),
('D2', '100g 果味酸奶', 100, 95, 3),
('D3', '100g 高蛋白酸奶', 100, 65, 9);

--  在type类里增加数据
update main set type = '米饭' where id in ('M1', 'M2');
update main set type = '红薯' where id in ('M3', 'M4');
update protein set type = '鸡肉' where id in ('P1', 'P2');
update protein set type = '豆腐' where id in ('P3');
update protein set type = '牛肉' where id in ('P4');
update vegetable set type = '圆生菜' where id in ('V1', 'V2');
update vegetable set type = '芥蓝' where id in ('V3');
update vegetable set type = '西红柿' where id in ('V4');
update fruit set type = '苹果' where id in ('F1', 'F2');
update fruit set type = '香蕉' where id in ('F3');
update fruit set type = '哈密瓜' where id in ('F4');
update oil set type = '油' where id in ('O1');
update oil set type = '橄榄油' where id in ('O2');
update dairy set type = '酸奶' where id in ('D1', 'D2', 'D3');
