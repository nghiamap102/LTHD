-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: tourscsdl
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `tours_tourdetail`
--

DROP TABLE IF EXISTS `tours_tourdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tourdetail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `slot` int NOT NULL,
  `time_start` datetime(6) DEFAULT NULL,
  `duration` int NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `price_room` int DEFAULT NULL,
  `price_tour` int DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `total` int DEFAULT NULL,
  `tour_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_tourdetail_name_tour_id_3422a1f7_uniq` (`name`,`tour_id`),
  KEY `tours_tourdetail_tour_id_90feccd5_fk_tours_tourtotal_id` (`tour_id`),
  CONSTRAINT `tours_tourdetail_tour_id_90feccd5_fk_tours_tourtotal_id` FOREIGN KEY (`tour_id`) REFERENCES `tours_tourtotal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourdetail`
--

LOCK TABLES `tours_tourdetail` WRITE;
/*!40000 ALTER TABLE `tours_tourdetail` DISABLE KEYS */;
INSERT INTO `tours_tourdetail` VALUES (9,'Dalat','static/2021/10/pq_oFgzsv2.jpg','2021-10-13 06:35:51.847783','2021-10-13 07:38:32.508071',1,36,NULL,4,'abc',300000,1900000,3,1843000,1),(12,'Dalat2','static/2021/10/pq_JD28Ar3.jpg','2021-10-13 06:36:26.052045','2021-10-13 06:36:26.052045',1,40,NULL,4,'abc',300000,1900000,3,1843000,1);
/*!40000 ALTER TABLE `tours_tourdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'tourscsdl'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-14 19:06:13
