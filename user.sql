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
-- Table structure for table `tours_user`
--

DROP TABLE IF EXISTS `tours_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `address` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(12) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avatar` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthdate` datetime(6) DEFAULT NULL,
  `active_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_user`
--

LOCK TABLES `tours_user` WRITE;
/*!40000 ALTER TABLE `tours_user` DISABLE KEYS */;
INSERT INTO `tours_user` VALUES (1,'pbkdf2_sha256$260000$cjf5Qx06SEursdaCvPxIw1$OzcgpzXtLk5AHpC0oOvm7O6FJZI1Ll6KE9MV+PzdVAQ=','2021-10-09 05:47:38.000000',1,'admin','Hoang','Nghia','1851050093nghia@ou.edu.vn',1,1,'2021-10-09 04:48:38.000000','371 Nguyễn Kiệm','0358833453','static/user/2021/10/pq-packed.jpg','2021-10-05 06:00:00.000000',1),(6,'pbkdf2_sha256$260000$z8debBuQOFg1EawHICwM0g$HQTktqfCiZWMFzryAF1CpqRo63TRGOfla0DIFECIw18=','2021-10-09 05:46:34.000000',0,'user','Trịnh','Huy','mr.tuan1749@gmail.com',1,1,'2021-10-09 05:16:53.000000','371 Nguyễn Kiệm','0368921284','static/user/2021/10/pq-packed_ePt8O4z.jpg','2021-10-05 06:00:00.000000',0),(8,'pbkdf2_sha256$260000$X5tCwJKlki8zRRdchThdiX$DDWv2XP6vavEOznqC/ZP86ws7IPt4t1mHrgIC0IvSUY=','2021-10-09 05:45:54.000000',0,'staff','','','',1,1,'2021-10-09 05:34:35.000000','371 Nguyễn Kiệm','0358833453','static/user/2021/10/dl-blog.jpg','2021-10-05 06:00:00.000000',1);
/*!40000 ALTER TABLE `tours_user` ENABLE KEYS */;
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

-- Dump completed on 2021-10-09 13:41:43
