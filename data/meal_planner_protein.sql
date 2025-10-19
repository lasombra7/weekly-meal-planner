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
-- Table structure for table `protein`
--

DROP TABLE IF EXISTS `protein`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `protein` (
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
-- Dumping data for table `protein`
--

LOCK TABLES `protein` WRITE;
/*!40000 ALTER TABLE `protein` DISABLE KEYS */;
INSERT INTO `protein` VALUES ('P1','200g 煮鸡胸+腿肉','鸡肉',200,345,56),('P10','3个鸡蛋','鸡蛋',150,210,18.9),('P11','50g 生猪肉末','猪肉',50,130,9),('P12','50g 煮熟的虾','虾',50,50,10.5),('P13','100g 煮熟的虾','虾',100,100,21),('P14','100g 生龙利鱼','龙利鱼',100,80,17),('P15','200g 生龙利鱼','龙利鱼',200,160,34),('P16','100g 生三文鱼','三文鱼',100,208,20),('P17','200g 生三文鱼','三文鱼',200,416,40),('P18','100g 生扇贝肉','扇贝',100,70,12),('P19','250ml 豆奶','豆奶',250,110,7),('P2','300g 煮鸡胸+腿肉','鸡肉',300,518,84),('P20','100g 金枪鱼罐头','金枪鱼',100,116,25),('P3','300g 豆腐','豆腐',300,240,27),('P4','200g 煮牛瘦肉','牛肉',200,380,60),('P5','300g 煮牛瘦肉','牛肉',300,570,75),('P6','150g 豆腐','豆腐',150,120,13.5),('P7','200g 豆腐','豆腐',200,160,18),('P8','1个鸡蛋','鸡蛋',50,70,6.3),('P9','2个鸡蛋','鸡蛋',100,140,12.6);
/*!40000 ALTER TABLE `protein` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-18 22:19:13
