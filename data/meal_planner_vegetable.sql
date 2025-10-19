CREATE DATABASE  IF NOT EXISTS `meal_planner` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `meal_planner`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: meal_planner
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vegetable`
--

DROP TABLE IF EXISTS `vegetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vegetable` (
  `id` char(5) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `weight` int DEFAULT NULL COMMENT '单位：g',
  `calorie` int DEFAULT NULL COMMENT '单位：kcal',
  `protein` float DEFAULT NULL COMMENT '单位：g',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vegetable`
--

LOCK TABLES `vegetable` WRITE;
/*!40000 ALTER TABLE `vegetable` DISABLE KEYS */;
INSERT INTO `vegetable` VALUES ('V1','300g 水煮/生吃圆生菜','圆生菜',300,45,3.6),('V10','200g 生青豆','青豆',200,248,16.8),('V11','200g 生黄瓜','黄瓜',200,30,1.4),('V12','300g 生黄瓜','黄瓜',300,45,2.1),('V13','200g 生油菜','油菜',200,42,3.2),('V14','200g 生白萝卜','白萝卜',200,36,1.2),('V15','100g 生洋葱','洋葱',100,40,1.1),('V16','200g 生生菜','生菜',200,30,2.4),('V17','200g 生胡萝卜','胡萝卜',200,66,1.6),('V18','200g 生西红柿','西红柿',200,44,2),('V2','500g 水煮/生吃圆生菜','圆生菜',500,75,6),('V3','300g 生芥蓝','芥蓝',300,105,9.6),('V4','300g 生西红柿','西红柿',300,66,3),('V5','200g 生白菜','白菜',200,34,2),('V6','300g 生白菜','白菜',300,51,3),('V7','150g 生西红柿','西红柿',150,33,1.5),('V8','150g 生芥蓝','芥蓝',150,52,4.8),('V9','150g 生青豆','青豆',150,186,12.6);
/*!40000 ALTER TABLE `vegetable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-18 22:19:12
