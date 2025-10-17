create database if not exists meal_planner
character set utf8mb4
collate utf8mb4_general_ci;

use meal_planner;

create table main
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table protein
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table vegetable
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table fruit
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table oil
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table dairy
(
id char(5) primary key,
name varchar(50),
calorie int,
protein int
);

create table meal_plan
(
id char(6) primary key,
date date,
meal_type enum('Lunch', 'Dinner'),
main_id char(5),
protein_id char(5),
vegetable_id char(5),
fruit_id char(5),
oil_id char(5),
dairy_id char(5),
total_calorie int,
total_protein int
);

-- 增加食品重量，并在 calorie 和 protein 列增加了单位注释。
alter table main
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

alter table protein
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

alter table vegetable
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

alter table fruit
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

alter table oil
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

alter table dairy
add column weight int comment '单位：g' after name,
modify column calorie int comment '单位：kcal',
modify column protein int comment '单位：g';

-- 将 protein 从 int 更改为 float
alter table main modify column protein float comment '单位：g';
alter table protein modify column protein float comment '单位：g';
alter table vegetable modify column protein float comment '单位：g';
alter table fruit modify column protein float comment '单位：g';
alter table oil modify column protein float comment '单位：g';
alter table dairy modify column protein float comment '单位：g';

-- 增加 seasoning table
create table seasoning
(
id char(5) primary key,
name varchar(20),
weight int comment '单位：g',
calorie int comment '单位：kcal',
protein float comment '单位：g'
);

alter table meal_plan
add column seasoning_id char(5) after oil_id;

-- 新增type列用于后期统计每周15-20种食物，seasoning 不算做统计。
alter table main add column type varchar(20) after name;
alter table protein add column type varchar(20) after name;
alter table vegetable add column type varchar(20) after name;
alter table fruit add column type varchar(20) after name;
alter table oil add column type varchar(20) after name;
alter table dairy add column type varchar(20) after name;

-- 在meal plan 里新增total type 的统计
alter table meal_plan add column total_type int;
describe meal_plan;