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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add blog',7,'add_blog'),(26,'Can change blog',7,'change_blog'),(27,'Can delete blog',7,'delete_blog'),(28,'Can view blog',7,'view_blog'),(29,'Can add tag',8,'add_tag'),(30,'Can change tag',8,'change_tag'),(31,'Can delete tag',8,'delete_tag'),(32,'Can view tag',8,'view_tag'),(33,'Can add tour detail',9,'add_tourdetail'),(34,'Can change tour detail',9,'change_tourdetail'),(35,'Can delete tour detail',9,'delete_tourdetail'),(36,'Can view tour detail',9,'view_tourdetail'),(37,'Can add transport',10,'add_transport'),(38,'Can change transport',10,'change_transport'),(39,'Can delete transport',10,'delete_transport'),(40,'Can view transport',10,'view_transport'),(41,'Can add hotel',11,'add_hotel'),(42,'Can change hotel',11,'change_hotel'),(43,'Can delete hotel',11,'delete_hotel'),(44,'Can view hotel',11,'view_hotel'),(45,'Can add tour total',12,'add_tourtotal'),(46,'Can change tour total',12,'change_tourtotal'),(47,'Can delete tour total',12,'delete_tourtotal'),(48,'Can view tour total',12,'view_tourtotal'),(49,'Can add tour detail views',13,'add_tourdetailviews'),(50,'Can change tour detail views',13,'change_tourdetailviews'),(51,'Can delete tour detail views',13,'delete_tourdetailviews'),(52,'Can view tour detail views',13,'view_tourdetailviews'),(53,'Can add comment tour detail',14,'add_commenttourdetail'),(54,'Can change comment tour detail',14,'change_commenttourdetail'),(55,'Can delete comment tour detail',14,'delete_commenttourdetail'),(56,'Can view comment tour detail',14,'view_commenttourdetail'),(57,'Can add comment blog',15,'add_commentblog'),(58,'Can change comment blog',15,'change_commentblog'),(59,'Can delete comment blog',15,'delete_commentblog'),(60,'Can view comment blog',15,'view_commentblog'),(61,'Can add booking',16,'add_booking'),(62,'Can change booking',16,'change_booking'),(63,'Can delete booking',16,'delete_booking'),(64,'Can view booking',16,'view_booking'),(65,'Can add rating',17,'add_rating'),(66,'Can change rating',17,'change_rating'),(67,'Can delete rating',17,'delete_rating'),(68,'Can view rating',17,'view_rating'),(69,'Can add like',18,'add_like'),(70,'Can change like',18,'change_like'),(71,'Can delete like',18,'delete_like'),(72,'Can view like',18,'view_like'),(73,'Can add img detail',19,'add_imgdetail'),(74,'Can change img detail',19,'change_imgdetail'),(75,'Can delete img detail',19,'delete_imgdetail'),(76,'Can view img detail',19,'view_imgdetail'),(77,'Can add application',20,'add_application'),(78,'Can change application',20,'change_application'),(79,'Can delete application',20,'delete_application'),(80,'Can view application',20,'view_application'),(81,'Can add access token',21,'add_accesstoken'),(82,'Can change access token',21,'change_accesstoken'),(83,'Can delete access token',21,'delete_accesstoken'),(84,'Can view access token',21,'view_accesstoken'),(85,'Can add grant',22,'add_grant'),(86,'Can change grant',22,'change_grant'),(87,'Can delete grant',22,'delete_grant'),(88,'Can view grant',22,'view_grant'),(89,'Can add refresh token',23,'add_refreshtoken'),(90,'Can change refresh token',23,'change_refreshtoken'),(91,'Can delete refresh token',23,'delete_refreshtoken'),(92,'Can view refresh token',23,'view_refreshtoken'),(93,'Can add id token',24,'add_idtoken'),(94,'Can change id token',24,'change_idtoken'),(95,'Can delete id token',24,'delete_idtoken'),(96,'Can view id token',24,'view_idtoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_tours_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-10-13 05:50:43.176425','1','Nghia Hoang',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Address\", \"Phone\", \"Avatar\", \"Birthdate\", \"Active staff\"]}}]',6,1),(2,'2021-10-13 05:52:08.561373','2','Ngoc Thi',1,'[{\"added\": {}}]',6,1),(3,'2021-10-13 05:52:15.594343','2','Ngoc Thi',2,'[{\"changed\": {\"fields\": [\"Active staff\"]}}]',6,1),(4,'2021-10-13 05:52:39.046460','3','Huy Trịnh',1,'[{\"added\": {}}]',6,1),(5,'2021-10-13 05:53:23.054785','1','DaLat',1,'[{\"added\": {}}]',12,1),(6,'2021-10-13 05:53:39.431108','2','Phú Quốc',1,'[{\"added\": {}}]',12,1),(7,'2021-10-13 05:53:51.990040','1','Mountain',1,'[{\"added\": {}}]',8,1),(8,'2021-10-13 05:54:00.142453','2','Couple',1,'[{\"added\": {}}]',8,1),(9,'2021-10-13 05:54:06.873259','3','Beach',1,'[{\"added\": {}}]',8,1),(10,'2021-10-13 05:54:11.957415','4','Islands',1,'[{\"added\": {}}]',8,1),(11,'2021-10-13 06:23:14.119718','1','Dalat',3,'',9,1),(12,'2021-10-13 06:35:50.022347','2','Dalat',3,'',9,1),(13,'2021-10-13 07:19:35.824731','11','Booking object (11)',3,'',16,1),(14,'2021-10-13 07:20:20.308812','13','Booking object (13)',3,'',16,1),(15,'2021-10-13 07:24:52.020478','1','Nghia Hoang',2,'[{\"changed\": {\"fields\": [\"Point\"]}}]',6,1),(16,'2021-10-13 07:27:01.731510','15','Booking object (15)',3,'',16,1),(17,'2021-10-13 07:27:50.233381','17','Booking object (17)',3,'',16,1),(18,'2021-10-13 07:36:26.506242','18','Booking object (18)',3,'',16,1),(19,'2021-10-13 07:36:57.939013','19','Booking object (19)',3,'',16,1),(20,'2021-10-13 07:38:27.824285','20','Booking object (20)',3,'',16,1),(21,'2021-10-13 14:13:34.431414','7','ávấ DaLat',3,'',6,1),(22,'2021-10-13 14:13:34.434420','6','ávấ DaLat',3,'',6,1),(23,'2021-10-13 14:13:34.436434','5','ávấ DaLat',3,'',6,1),(24,'2021-10-13 14:13:34.438414','4','ávấ DaLat',3,'',6,1),(25,'2021-10-14 10:41:42.513932','1','Nghia Hoang',2,'[{\"changed\": {\"fields\": [\"Birthdate\"]}}]',6,1),(26,'2021-10-15 09:45:20.610630','10','Nghia Thi',1,'[{\"added\": {}}]',6,1),(27,'2021-10-15 09:48:43.448762','11','Ngoc Thi',1,'[{\"added\": {}}]',6,1),(28,'2021-10-15 09:49:57.387465','12','Nghia Thi',1,'[{\"added\": {}}]',6,1),(29,'2021-10-15 09:51:57.452165','13','Nghia Thi',1,'[{\"added\": {}}]',6,1),(30,'2021-10-15 10:03:01.083373','14','Nghia Thi',1,'[{\"added\": {}}]',6,1),(31,'2021-10-15 10:03:40.820284','15','Nghia Hoang',1,'[{\"added\": {}}]',6,1),(32,'2021-10-15 10:27:10.486419','1','Nghia Hoang',2,'[{\"changed\": {\"fields\": [\"Birthdate\"]}}]',6,1),(33,'2021-10-16 02:56:09.143059','2','Ngoc Thi',2,'[{\"changed\": {\"fields\": [\"Avatar\"]}}]',6,1),(34,'2021-10-16 03:05:03.411424','2','Ngoc Thi',2,'[{\"changed\": {\"fields\": [\"Avatar\"]}}]',6,1),(35,'2021-10-16 15:53:02.699345','1','DaLat',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}, {\"changed\": {\"name\": \"tour detail\", \"object\": \"Dalat\", \"fields\": [\"Time start\", \"Content\"]}}, {\"changed\": {\"name\": \"tour detail\", \"object\": \"Dalat2\", \"fields\": [\"Time start\", \"Content\"]}}]',12,1),(36,'2021-10-17 03:23:48.465054','4','VHL2',3,'',12,1),(37,'2021-10-17 03:29:29.008659','3','VHL',3,'',12,1),(38,'2021-10-17 03:29:29.012407','5','ABC',3,'',12,1),(39,'2021-10-17 08:05:00.950186','6','a',3,'',12,1),(40,'2021-10-17 08:05:00.950186','7','abc',3,'',12,1),(41,'2021-10-17 08:05:00.958193','8','DaLat2',3,'',12,1),(42,'2021-10-17 08:05:00.958193','9','DaLat3',3,'',12,1),(43,'2021-10-17 15:50:30.667238','10','abc',3,'',12,1),(44,'2021-10-17 15:50:30.671239','11','bád',3,'',12,1),(45,'2021-10-17 15:50:30.674247','12','Dalat2234',3,'',12,1),(46,'2021-10-17 15:50:30.676240','13','Dalat223',3,'',12,1),(47,'2021-10-17 15:56:08.443873','9','h',3,'',8,1),(48,'2021-10-17 15:56:08.448875','8','c',3,'',8,1),(49,'2021-10-17 15:56:08.450874','7','a',3,'',8,1),(50,'2021-10-17 15:56:08.453875','6','e',3,'',8,1),(51,'2021-10-17 15:56:08.456877','5','B',3,'',8,1),(52,'2021-10-17 16:04:08.631014','15','d',3,'',8,1),(53,'2021-10-17 16:04:08.635013','14','n',3,'',8,1),(54,'2021-10-17 16:04:08.636935','13','a',3,'',8,1),(55,'2021-10-17 16:04:08.637936','12','l',3,'',8,1),(56,'2021-10-17 16:04:08.640205','11','s',3,'',8,1),(57,'2021-10-17 16:04:08.643021','10','I',3,'',8,1),(58,'2021-10-17 16:05:33.692191','14','a',3,'',12,1),(59,'2021-10-17 16:05:33.694191','16','abác',3,'',12,1),(60,'2021-10-17 16:05:33.696456','17','VHL',3,'',12,1),(61,'2021-10-17 16:05:33.698459','18','aváav',3,'',12,1),(62,'2021-10-18 06:23:30.163227','19','ấvsa',3,'',12,1),(63,'2021-10-18 06:23:30.167209','20','â',3,'',12,1),(64,'2021-10-18 06:23:30.169223','21','av',3,'',12,1),(65,'2021-10-18 06:43:43.377038','1','DaLat',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',12,1),(66,'2021-10-18 06:44:49.699403','2','Phú Quốc3',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',12,1),(67,'2021-10-18 14:00:31.224516','1','DaLat giảm giá',1,'[{\"added\": {}}]',7,1),(68,'2021-10-19 05:46:58.332901','4','avá',3,'',7,1),(69,'2021-10-19 05:46:58.335892','3','Phú Quốc2',3,'',7,1),(70,'2021-10-19 05:46:58.337760','2','Phú Quốc2',3,'',7,1),(71,'2021-10-19 07:49:49.932311','7','áabad',3,'',7,1),(72,'2021-10-19 07:49:49.935331','6','á',3,'',7,1),(73,'2021-10-19 07:49:49.937351','5','ab',3,'',7,1),(74,'2021-10-19 08:21:58.734406','10','ầ',3,'',7,1),(75,'2021-10-19 08:21:58.737605','9','abav',3,'',7,1),(76,'2021-10-19 08:21:58.739535','8','SGAG',3,'',7,1),(77,'2021-10-19 10:37:05.062915','13','DL2',1,'[{\"added\": {}}]',9,1),(78,'2021-10-20 01:23:09.203350','1','Train',1,'[{\"added\": {}}]',10,1),(79,'2021-10-20 01:23:15.680925','2','Plan',1,'[{\"added\": {}}]',10,1),(80,'2021-10-20 01:23:24.470788','3','Coach',1,'[{\"added\": {}}]',10,1),(81,'2021-10-20 05:07:42.056343','4','Like object (4)',3,'',18,1),(82,'2021-10-20 05:07:42.060330','3','Like object (3)',3,'',18,1),(83,'2021-10-20 05:07:42.062456','1','Like object (1)',3,'',18,1),(84,'2021-10-20 05:07:52.113577','5','Like object (5)',3,'',18,1),(85,'2021-10-20 05:32:56.383444','14','abc',3,'',9,1),(86,'2021-10-20 05:33:09.904657','7','n',3,'',10,1),(87,'2021-10-20 05:33:09.907658','6','a',3,'',10,1),(88,'2021-10-20 05:33:09.909658','5','l',3,'',10,1),(89,'2021-10-20 05:33:09.911659','4','P',3,'',10,1),(90,'2021-10-20 05:33:15.429992','15','abc',3,'',9,1),(91,'2021-10-20 05:34:54.474673','16','abc',3,'',9,1),(92,'2021-10-20 05:36:42.720616','17','abc',3,'',9,1),(93,'2021-10-20 05:37:26.659823','18','abc',3,'',9,1),(94,'2021-10-20 05:38:19.919463','19','abc',3,'',9,1),(95,'2021-10-20 05:50:07.676085','11','n',3,'',10,1),(96,'2021-10-20 05:50:07.680077','10','a',3,'',10,1),(97,'2021-10-20 05:50:07.682078','9','l',3,'',10,1),(98,'2021-10-20 05:50:07.683078','8','P',3,'',10,1),(99,'2021-10-20 14:34:49.526239','21','Booking object (21)',3,'',16,1),(100,'2021-10-20 14:35:36.816835','1','Nghia Hoang2',2,'[{\"changed\": {\"fields\": [\"Point\"]}}]',6,1),(101,'2021-10-20 14:35:45.137421','36','Booking object (36)',3,'',16,1),(102,'2021-10-20 14:36:19.555136','38','Booking object (38)',3,'',16,1),(103,'2021-10-20 14:37:51.641953','39','Booking object (39)',3,'',16,1),(104,'2021-10-20 14:39:00.156683','40','Booking object (40)',3,'',16,1),(105,'2021-10-20 14:39:07.849782','1','Nghia Hoang2',2,'[{\"changed\": {\"fields\": [\"Point\"]}}]',6,1),(106,'2021-10-20 14:49:17.564040','41','Booking object (41)',3,'',16,1),(107,'2021-10-20 14:49:25.425396','1','Nghia Hoang2',2,'[{\"changed\": {\"fields\": [\"Point\"]}}]',6,1),(108,'2021-10-20 14:49:37.467836','9','Dalat',2,'[{\"changed\": {\"fields\": [\"Slot\"]}}]',9,1),(109,'2021-10-20 15:24:57.243254','42','Booking object (42)',3,'',16,1),(110,'2021-10-20 15:25:12.845947','9','Dalat',2,'[{\"changed\": {\"fields\": [\"Slot\"]}}]',9,1),(111,'2021-10-20 15:25:20.088284','1','Nghia Hoang2',2,'[{\"changed\": {\"fields\": [\"Point\"]}}]',6,1),(112,'2021-10-20 15:41:51.235582','43','Booking object (43)',3,'',16,1),(113,'2021-10-20 15:44:05.237633','44','Booking object (44)',3,'',16,1),(114,'2021-10-20 15:44:48.016000','45','Booking object (45)',3,'',16,1),(115,'2021-10-20 15:46:19.677930','46','Booking object (46)',3,'',16,1),(116,'2021-10-20 15:47:44.019776','47','Booking object (47)',3,'',16,1),(117,'2021-10-20 15:49:58.274321','48','Booking object (48)',3,'',16,1),(118,'2021-10-20 15:55:13.617086','49','Booking object (49)',3,'',16,1),(119,'2021-10-20 15:57:11.999981','50','Booking object (50)',3,'',16,1),(120,'2021-10-20 16:01:28.849520','51','Booking object (51)',3,'',16,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(21,'oauth2_provider','accesstoken'),(20,'oauth2_provider','application'),(22,'oauth2_provider','grant'),(24,'oauth2_provider','idtoken'),(23,'oauth2_provider','refreshtoken'),(5,'sessions','session'),(7,'tours','blog'),(16,'tours','booking'),(15,'tours','commentblog'),(14,'tours','commenttourdetail'),(11,'tours','hotel'),(19,'tours','imgdetail'),(18,'tours','like'),(17,'tours','rating'),(8,'tours','tag'),(9,'tours','tourdetail'),(13,'tours','tourdetailviews'),(12,'tours','tourtotal'),(10,'tours','transport'),(6,'tours','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-13 05:48:37.242879'),(2,'contenttypes','0002_remove_content_type_name','2021-10-13 05:48:37.318902'),(3,'auth','0001_initial','2021-10-13 05:48:37.563639'),(4,'auth','0002_alter_permission_name_max_length','2021-10-13 05:48:37.616651'),(5,'auth','0003_alter_user_email_max_length','2021-10-13 05:48:37.622652'),(6,'auth','0004_alter_user_username_opts','2021-10-13 05:48:37.628653'),(7,'auth','0005_alter_user_last_login_null','2021-10-13 05:48:37.633656'),(8,'auth','0006_require_contenttypes_0002','2021-10-13 05:48:37.637656'),(9,'auth','0007_alter_validators_add_error_messages','2021-10-13 05:48:37.643658'),(10,'auth','0008_alter_user_username_max_length','2021-10-13 05:48:37.650660'),(11,'auth','0009_alter_user_last_name_max_length','2021-10-13 05:48:37.656660'),(12,'auth','0010_alter_group_name_max_length','2021-10-13 05:48:37.670663'),(13,'auth','0011_update_proxy_permissions','2021-10-13 05:48:37.678667'),(14,'auth','0012_alter_user_first_name_max_length','2021-10-13 05:48:37.684667'),(15,'tours','0001_initial','2021-10-13 05:48:39.626183'),(16,'admin','0001_initial','2021-10-13 05:48:39.758275'),(17,'admin','0002_logentry_remove_auto_add','2021-10-13 05:48:39.769361'),(18,'admin','0003_logentry_add_action_flag_choices','2021-10-13 05:48:39.779365'),(19,'oauth2_provider','0001_initial','2021-10-13 05:48:40.583739'),(20,'oauth2_provider','0002_auto_20190406_1805','2021-10-13 05:48:40.708150'),(21,'oauth2_provider','0003_auto_20201211_1314','2021-10-13 05:48:40.764170'),(22,'oauth2_provider','0004_auto_20200902_2022','2021-10-13 05:48:41.253882'),(23,'sessions','0001_initial','2021-10-13 05:48:41.312664'),(24,'tours','0002_auto_20211013_1335','2021-10-13 06:35:04.473878'),(25,'tours','0003_alter_booking_unique_together','2021-10-13 07:13:24.819598'),(26,'tours','0004_alter_user_birthdate','2021-10-14 10:40:30.990300'),(27,'tours','0005_auto_20211016_0757','2021-10-16 00:57:40.312399'),(28,'tours','0006_blog_decription','2021-10-18 09:14:16.415254'),(29,'tours','0007_alter_like_type','2021-10-19 01:17:56.018687'),(30,'tours','0008_alter_blog_content','2021-10-19 05:40:53.679283'),(31,'tours','0009_alter_like_type','2021-10-20 03:20:40.310461');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('77bicr5t92zydei6d8bgioe1h1j3w7km','.eJxVjMsOwiAQRf-FtSEIHR4u3fcbmhkYpGogKe3K-O_apAvd3nPOfYkJt7VMW-dlmpO4iLM4_W6E8cF1B-mO9dZkbHVdZpK7Ig_a5dgSP6-H-3dQsJdvHZx3VjvLhBgMWG29JaV1BOABwHEOjOA9qEiUKQPkYGJgldxgMnvx_gDJ5DfP:1mbZKT:YGPC0YaV2VTjE2G22SXOxFq812Hsz1t3wRSauUwfP74','2021-10-30 02:21:45.626123');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint DEFAULT NULL,
  `id_token_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  UNIQUE KEY `id_token_id` (`id_token_id`),
  KEY `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_tours_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr` FOREIGN KEY (`id_token_id`) REFERENCES `oauth2_provider_idtoken` (`id`),
  CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_accesstoken` VALUES (1,'ycvgZyTOCbR9AtoGo2HUPgHh1hctl1','2021-10-13 15:51:23.436240','read write',1,1,'2021-10-13 05:51:23.436240','2021-10-13 05:51:23.436240',NULL,NULL),(2,'jNpgESQkzWgHOpPbUGlMHU2X8oGUl8','2021-10-13 19:55:56.647859','read write',1,1,'2021-10-13 09:55:56.648859','2021-10-13 09:55:56.648859',NULL,NULL),(3,'7qE86DzVIXgiGliFulCjaYNpeml8B9','2021-10-13 19:56:24.015660','read write',1,1,'2021-10-13 09:56:24.015660','2021-10-13 09:56:24.015660',NULL,NULL),(4,'Igy0V4BiCxieRkPoUKqcCCAZCm1jgA','2021-10-13 19:59:37.457882','read write',1,1,'2021-10-13 09:59:37.458882','2021-10-13 09:59:37.458882',NULL,NULL),(5,'vE7IhzUszN8vcFMJiQdaRKXHu77reX','2021-10-13 19:59:41.325162','read write',1,1,'2021-10-13 09:59:41.325162','2021-10-13 09:59:41.325162',NULL,NULL),(6,'61Oj6eAL6RnfFu9KRrksYbRC4HEoPr','2021-10-13 19:59:41.909080','read write',1,1,'2021-10-13 09:59:41.910066','2021-10-13 09:59:41.910066',NULL,NULL),(7,'QzP6lrdl0aoCYjWe8XG7N78ki9tWLP','2021-10-13 19:59:42.606240','read write',1,1,'2021-10-13 09:59:42.606240','2021-10-13 09:59:42.606240',NULL,NULL),(8,'dICAIgU7Lkn7dnNbintgehTS6xFfYl','2021-10-13 20:00:12.847841','read write',1,1,'2021-10-13 10:00:12.848841','2021-10-13 10:00:12.848841',NULL,NULL),(9,'3t94GE5srOzDCehtJOSFKF7vy3cwUR','2021-10-13 20:01:29.887267','read write',3,3,'2021-10-13 10:01:29.888270','2021-10-13 10:01:29.888270',NULL,NULL),(10,'dpIK5t8D2NhDvyXIgaQZG1EPqA9hZD','2021-10-13 20:01:52.113765','read write',1,2,'2021-10-13 10:01:52.114769','2021-10-13 10:01:52.114769',NULL,NULL),(11,'MIIY68UpWAfmKCbiGzzrzYfKHyAUNW','2021-10-13 20:33:30.992959','read write',1,2,'2021-10-13 10:33:30.992959','2021-10-13 10:33:30.992959',NULL,NULL),(12,'2mS47zD63HHfJCbRq8A1UfoIgQf2Dv','2021-10-13 20:34:29.993348','read write',1,2,'2021-10-13 10:34:29.993348','2021-10-13 10:34:29.993348',NULL,NULL),(13,'Uduiec58Hq1GqmAuCOmZwjOOryB6NB','2021-10-13 20:35:06.498744','read write',1,2,'2021-10-13 10:35:06.498744','2021-10-13 10:35:06.498744',NULL,NULL),(14,'TYhg00hC2Xe2p3LgvQQJ8RjxAa7FHJ','2021-10-13 20:37:01.051853','read write',1,2,'2021-10-13 10:37:01.052852','2021-10-13 10:37:01.052852',NULL,NULL),(15,'cVD8BkdyO27F1MeoavCa9WsPfdYbzg','2021-10-13 20:37:40.614633','read write',1,2,'2021-10-13 10:37:40.615647','2021-10-13 10:37:40.615647',NULL,NULL),(16,'QvDxwWGw0yvvK3s4SDWnkdILvd9FQ1','2021-10-13 20:48:36.942037','read write',1,1,'2021-10-13 10:48:36.943030','2021-10-13 10:48:36.943030',NULL,NULL),(17,'crC3lJPjpDwiUijWdmMRhcIjOjB7Vh','2021-10-13 22:46:11.879918','read write',1,1,'2021-10-13 12:46:11.879918','2021-10-13 12:46:11.879918',NULL,NULL),(18,'FakOguDRvbUNwzWv8hdU64EHNxufp5','2021-10-13 22:50:26.845893','read write',2,2,'2021-10-13 12:50:26.846891','2021-10-13 12:50:26.846891',NULL,NULL),(19,'SsqXWwdPvb40CZQMYoLzdGGCSAe1yf','2021-10-13 22:52:51.483705','read write',2,2,'2021-10-13 12:52:51.484705','2021-10-13 12:52:51.484705',NULL,NULL),(20,'SNjCNKnyDV9qiyk1qUUzKGiOM7Nwrx','2021-10-13 22:56:34.670081','read write',2,2,'2021-10-13 12:56:34.670081','2021-10-13 12:56:34.670081',NULL,NULL),(21,'8JHegVOf2VcTgsv1Cd9opoVBvUilt8','2021-10-13 23:50:02.410594','read write',2,1,'2021-10-13 13:50:02.411596','2021-10-13 13:50:02.411596',NULL,NULL),(22,'3kICT5x1hx2AJHf210jFvf66vGXPKN','2021-10-13 23:50:11.878027','read write',2,1,'2021-10-13 13:50:11.879027','2021-10-13 13:50:11.879027',NULL,NULL),(23,'n66IXQIIRpawkyjRGl73INXHvXHfBk','2021-10-14 00:27:39.802489','read write',2,1,'2021-10-13 14:27:39.802489','2021-10-13 14:27:39.802489',NULL,NULL),(24,'F6h2DvkOgmWIuPMdzHoBFyEwaZoBhZ','2021-10-14 00:30:30.766597','read write',2,1,'2021-10-13 14:30:30.766597','2021-10-13 14:30:30.766597',NULL,NULL),(25,'EiHfpCOYyk0qZSONLexfmLdCJfIW1i','2021-10-14 00:31:02.988308','read write',2,2,'2021-10-13 14:31:02.988308','2021-10-13 14:31:02.988308',NULL,NULL),(26,'0ifxEVbeGrvdidHUzwyqphzJRTVXPm','2021-10-14 00:38:26.234606','read write',2,1,'2021-10-13 14:38:26.234606','2021-10-13 14:38:26.234606',NULL,NULL),(27,'vpZJNBBGzDy5gbrEQPn3mJUT6wE4Ik','2021-10-14 00:39:13.254977','read write',2,2,'2021-10-13 14:39:13.254977','2021-10-13 14:39:13.254977',NULL,NULL),(28,'gELAY6pYISJrcm0Bzd4Ip0BZVqq5qL','2021-10-14 11:21:41.707730','read write',2,1,'2021-10-14 01:21:41.708732','2021-10-14 01:21:41.708732',NULL,NULL),(29,'lCnsNZamsgVrNZY0oUMWJQJGFgvKow','2021-10-14 11:55:42.937322','read write',1,1,'2021-10-14 01:55:42.938324','2021-10-14 01:55:42.938324',NULL,NULL),(30,'5xbQRUOC1E5UtRroTcPeLaMl6cXxJg','2021-10-14 21:22:33.909224','read write',2,1,'2021-10-14 11:22:33.909224','2021-10-14 11:22:33.909224',NULL,NULL),(31,'PSC4M6HYLI2S6mywWSZ3yKjX63JXTE','2021-10-14 21:39:57.860085','read write',2,1,'2021-10-14 11:39:57.860085','2021-10-14 11:39:57.860085',NULL,NULL),(32,'tZNIrhHz0g7t4OpgEMaskYS2Kmr3Ii','2021-10-14 21:42:47.962715','read write',2,1,'2021-10-14 11:42:47.963715','2021-10-14 11:42:47.963715',NULL,NULL),(33,'D3Q3t9Db7MWkCxCyiCL8L7ZsXiCPN1','2021-10-14 21:46:44.508929','read write',2,1,'2021-10-14 11:46:44.508929','2021-10-14 11:46:44.508929',NULL,NULL),(34,'hz8kOYxpRO2mCtHQVS8sfPtcFE7RlX','2021-10-14 21:49:45.474758','read write',2,1,'2021-10-14 11:49:45.475753','2021-10-14 11:49:45.475753',NULL,NULL),(35,'ZwSOyVaIlFAzcYN4I62O58aep5gns6','2021-10-15 11:27:15.701640','read write',2,1,'2021-10-15 01:27:15.702649','2021-10-15 01:27:15.702649',NULL,NULL),(36,'FOv7DY850PO9zH0qhKh7DC9JshyENL','2021-10-15 22:26:37.359635','read write',2,1,'2021-10-15 12:26:37.360622','2021-10-15 12:26:37.360622',NULL,NULL),(37,'pvmF9NxMt8omBXwNnHYzehhrRdC2tu','2021-10-16 00:18:48.832911','read write',2,1,'2021-10-15 14:18:48.832911','2021-10-15 14:18:48.832911',NULL,NULL),(38,'6ZPU0agg4j5l1yIooWGxE12RngwnQe','2021-10-16 00:21:13.925040','read write',2,1,'2021-10-15 14:21:13.925040','2021-10-15 14:21:13.925040',NULL,NULL),(39,'UrAnNHQivKnSjNRNDXcteaxNQcqJFK','2021-10-16 11:40:22.853395','read write',2,2,'2021-10-16 01:40:22.854395','2021-10-16 01:40:22.854395',NULL,NULL),(40,'JkVay1VJOoHMcGRNBdYlBkcFn7mpu1','2021-10-16 11:40:52.972232','read write',2,2,'2021-10-16 01:40:52.972232','2021-10-16 01:40:52.973231',NULL,NULL),(41,'EVYzUtcM0fj7se7JgfIICtgGoVkMDM','2021-10-16 11:56:31.286583','read write',2,1,'2021-10-16 01:56:31.286583','2021-10-16 01:56:31.286583',NULL,NULL),(42,'d5nYEyZt8mGxDH1RBRBryb1aBMk3fn','2021-10-16 12:54:46.731799','read write',2,2,'2021-10-16 02:54:46.732799','2021-10-16 02:54:46.732799',NULL,NULL),(43,'FIt9dduCeRUj5vDbO6KATmyXfIKV1t','2021-10-16 12:56:53.404027','read write',2,1,'2021-10-16 02:56:53.405027','2021-10-16 02:56:53.405027',NULL,NULL),(44,'jRjNs3mjY5ybPZBeXZp6nHX6WRdS5Q','2021-10-16 12:58:52.204550','read write',2,2,'2021-10-16 02:58:52.204550','2021-10-16 02:58:52.204550',NULL,NULL),(45,'2GkUoUWhSUFEJGtNGI2ToSKsjQOxkK','2021-10-16 13:01:51.596230','read write',2,1,'2021-10-16 03:01:51.596230','2021-10-16 03:01:51.596230',NULL,NULL),(46,'iyXP0rsxNB8p2tSzdpaHC3XwuaPynL','2021-10-16 13:04:42.145853','read write',2,1,'2021-10-16 03:04:42.146854','2021-10-16 03:04:42.146854',NULL,NULL),(47,'G5sA9Owds8H8hxz9nUqUNLHvnhV2Z1','2021-10-16 13:05:16.489747','read write',2,2,'2021-10-16 03:05:16.490749','2021-10-16 03:05:16.490749',NULL,NULL),(48,'J1O3hhK5uvBMcweOCrlzDGXBIVt0ML','2021-10-16 17:05:51.519649','read write',2,2,'2021-10-16 07:05:51.523651','2021-10-16 07:05:51.523651',NULL,NULL),(49,'dUBrroL0gndAnRgXDAl3nfabzjrjlM','2021-10-17 13:22:52.924486','read write',2,2,'2021-10-17 03:22:52.925487','2021-10-17 03:22:52.925487',NULL,NULL),(50,'XLdmGD4vPak2AV4O6AZ0CkVVht8y3y','2021-10-17 13:31:46.463727','read write',2,1,'2021-10-17 03:31:46.463727','2021-10-17 03:31:46.463727',NULL,NULL),(51,'p2Rbha93Q5zEzaGLzMNkKqHLumHek9','2021-10-19 15:39:57.415648','read write',2,1,'2021-10-19 05:39:57.415648','2021-10-19 05:39:57.415648',NULL,NULL),(52,'uQtxzlHdCBuqOvaIXwsVwhY7ZsrPvr','2021-10-19 15:45:21.537662','read write',2,1,'2021-10-19 05:45:21.537662','2021-10-19 05:45:21.537662',NULL,NULL),(53,'mh2SDCXZUYHQRnY1VyL9DltJgYIHqD','2021-10-19 18:42:24.545506','read write',2,1,'2021-10-19 08:42:24.545506','2021-10-19 08:42:24.545506',NULL,NULL),(54,'anO16x2HFoYGpB8Z1Flr1XROu4emhf','2021-10-20 11:43:57.822477','read write',2,1,'2021-10-20 01:43:57.823476','2021-10-20 01:43:57.823476',NULL,NULL),(55,'uGJ97vQnIKim4bnOXh53cJHi59GcoL','2021-10-20 15:29:05.522787','read write',2,1,'2021-10-20 05:29:05.523789','2021-10-20 05:29:05.523789',NULL,NULL),(56,'xz62CwRrORamlVgv9jSEprDfczhvAx','2021-10-21 01:23:16.341366','read write',2,2,'2021-10-20 15:23:16.342365','2021-10-20 15:23:16.342365',NULL,NULL),(57,'pi5CUDnH398YgoypNHaDuNL1gFqPM4','2021-10-21 01:23:56.733998','read write',2,1,'2021-10-20 15:23:56.734999','2021-10-20 15:23:56.734999',NULL,NULL),(58,'U2zUYQzScLNwXz1MnUknHMG0BirdQU','2021-10-21 01:45:10.971018','read write',2,1,'2021-10-20 15:45:10.971018','2021-10-20 15:45:10.971018',NULL,NULL);
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `redirect_uris` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_type` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `authorization_grant_type` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_secret` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `algorithm` varchar(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_user_id_79829054_fk_tours_user_id` (`user_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
INSERT INTO `oauth2_provider_application` VALUES (1,'c34istjDIrTUiZuJd27y8cTYmz77OudO3bKBvwJe','','confidential','password','doUebGLGbpOfm3z2UMgzfPo6xjvkDkagvbQS7zzCSPvYNw5KFpDfJJBSazCiLPcU0JQp85seAg4I40juUQWRR2E3W9Ydn6uSWyUgclMwQXj56q0V0trYWFyGioK39yo9','Nghia',1,0,'2021-10-13 05:51:16.501409','2021-10-13 05:51:16.501409',''),(2,'V1Xb5MRepyl5SIUkSNDvHdownLxPjMRC63caDbbH','','confidential','password','QuYWSyJmvAGX8BA3ID3IIJxyxZ3VqbD9MAT5kzuprq7lWUGNgCNHv8flObzdLWM9A1X5QYLqOvppUYvboCIqwqIqegw3kD0UyGgQHwMLWSS0PKvxTHejrsTLLA2qTfDO','DaLat',2,0,'2021-10-13 09:27:51.868648','2021-10-13 09:27:51.868648',''),(3,'xCVIdSq7ezzaWoCOMe0ZKrNxZDHLSEPrhv03F53T','','confidential','password','qlPZqxCJiJn9qnGG0duo6Yko7yWOJ800B5wvGuQS5l7gsnai7UdZCtRzUxfZAVcAfd6yU7AxRFpozTdZWOUBMuav4cYZn5Er5iZe40Foul5rOMp7iLqhgJZt8qmhNYWs','DaLat',3,0,'2021-10-13 09:31:26.580348','2021-10-13 09:31:26.580348','');
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `code_challenge` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `code_challenge_method` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nonce` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `claims` longtext COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_tours_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_idtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_idtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_idtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jti` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jti` (`jti`),
  KEY `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_idtoken_user_id_dd512b59_fk_tours_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_idtoken_user_id_dd512b59_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_idtoken`
--

LOCK TABLES `oauth2_provider_idtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `access_token_id` bigint DEFAULT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  KEY `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_tours_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_refreshtoken` VALUES (1,'rNRBfbc4oWFzxy1YhC2GhlxB1DpGAB',1,1,1,'2021-10-13 05:51:23.443242','2021-10-13 05:51:23.443242',NULL),(2,'VeyqL7lGapxur0P2UKUtI6yyM3rxJX',2,1,1,'2021-10-13 09:55:56.651860','2021-10-13 09:55:56.651860',NULL),(3,'6snm5JdAOkYEFzv6Nt3V1Vcbnd3of4',3,1,1,'2021-10-13 09:56:24.016660','2021-10-13 09:56:24.016660',NULL),(4,'d0NlI8X7OzeYhXuuxamtBI4J1Tnd1W',4,1,1,'2021-10-13 09:59:37.460882','2021-10-13 09:59:37.460882',NULL),(5,'paapZU1FrelUJij96OLOM5Lt0okWBn',5,1,1,'2021-10-13 09:59:41.328163','2021-10-13 09:59:41.328163',NULL),(6,'TgXILjtV9grzWwM7gzb5Uxpi28hllz',6,1,1,'2021-10-13 09:59:41.911067','2021-10-13 09:59:41.911067',NULL),(7,'gPva5iKnYPl3s4eMoJxeshwH8OTHd2',7,1,1,'2021-10-13 09:59:42.607326','2021-10-13 09:59:42.607326',NULL),(8,'OhPcRnD1RYsZFfZ95wPvJABNpnbbUr',8,1,1,'2021-10-13 10:00:12.848841','2021-10-13 10:00:12.849841',NULL),(9,'a7UhYk6WpiLnOd81NasVxcR6VpeNXD',9,3,3,'2021-10-13 10:01:29.890268','2021-10-13 10:01:29.890268',NULL),(10,'Cf0xTqbNngdpEleAk2ABqeatv79LMn',10,1,2,'2021-10-13 10:01:52.116758','2021-10-13 10:01:52.116758',NULL),(11,'M2n72stOFLDp2SWqDXaJUPeK5XuLuU',11,1,2,'2021-10-13 10:33:30.993958','2021-10-13 10:33:30.993958',NULL),(12,'n6XNy5TzGInZ4TVRJDKEmBoqFDnEN9',12,1,2,'2021-10-13 10:34:29.995336','2021-10-13 10:34:29.995336',NULL),(13,'YdjpRSGc09jvOGYiu0PadpbG53zdLr',13,1,2,'2021-10-13 10:35:06.500272','2021-10-13 10:35:06.500272',NULL),(14,'Gsx7vVnKQIVahozljHMHpRRIwbWslg',14,1,2,'2021-10-13 10:37:01.053853','2021-10-13 10:37:01.053853',NULL),(15,'9SHTw7QToMMLJ4teTK5gpHHzisEYCE',15,1,2,'2021-10-13 10:37:40.617632','2021-10-13 10:37:40.617632',NULL),(16,'r1Uim17qru5BXDsZIoJLLHbbJ6JMb0',16,1,1,'2021-10-13 10:48:36.946141','2021-10-13 10:48:36.946141',NULL),(17,'Xb0RVskCBwEauAMoSTkkrQjkvuWC56',17,1,1,'2021-10-13 12:46:11.881919','2021-10-13 12:46:11.881919',NULL),(18,'8wA5ctvg1aPt7Ir3mCm5jjseuvAbXg',18,2,2,'2021-10-13 12:50:26.848890','2021-10-13 12:50:26.848890',NULL),(19,'ttbsm45A4ZUyA7Z6XSEBq7gc3yvrSX',19,2,2,'2021-10-13 12:52:51.485712','2021-10-13 12:52:51.485712',NULL),(20,'LfeUyxbdk4WFiao2UERDUCy87Ln29q',20,2,2,'2021-10-13 12:56:34.672084','2021-10-13 12:56:34.672084',NULL),(21,'CnoMBbS8qfTftNOYT48dBb26RUwzi9',21,2,1,'2021-10-13 13:50:02.412506','2021-10-13 13:50:02.412506',NULL),(22,'KxROevogCfKmWOQ36ROOR9SiRODBPt',22,2,1,'2021-10-13 13:50:11.880027','2021-10-13 13:50:11.880027',NULL),(23,'FumAdE4IR118jfBImui1Yzwkesd9WS',23,2,1,'2021-10-13 14:27:39.805489','2021-10-13 14:27:39.805489',NULL),(24,'qbRPWV83UPkiZ4T05c05S1amOKvHqY',24,2,1,'2021-10-13 14:30:30.768597','2021-10-13 14:30:30.768597',NULL),(25,'XysGBg2OjiUvYEMq0fiDYeV9Pi03mZ',25,2,2,'2021-10-13 14:31:02.990310','2021-10-13 14:31:02.990310',NULL),(26,'XtcjxS3pDesFDba75Xz4VCdihGWwhu',26,2,1,'2021-10-13 14:38:26.236614','2021-10-13 14:38:26.236614',NULL),(27,'llt1SRJWQsIGfYiCwHl7gE1P1J1DdY',27,2,2,'2021-10-13 14:39:13.256977','2021-10-13 14:39:13.256977',NULL),(28,'7ITi2kBXtmCObWbBb05RUnnnKLQniO',28,2,1,'2021-10-14 01:21:41.711738','2021-10-14 01:21:41.711738',NULL),(29,'VSoRM6DT7OiVsx8rtMgJDWusdyjmKz',29,1,1,'2021-10-14 01:55:42.941325','2021-10-14 01:55:42.941325',NULL),(30,'zQiuPfR64wwtjbmkm7uh9BX8HNhjIn',30,2,1,'2021-10-14 11:22:33.912224','2021-10-14 11:22:33.912224',NULL),(31,'2x8FFDp9bCrTdGtwTz8vQuZUkhWpgP',31,2,1,'2021-10-14 11:39:57.862087','2021-10-14 11:39:57.862087',NULL),(32,'eWxCn66PkBwxurZzEOosIum1Wrtuzf',32,2,1,'2021-10-14 11:42:47.964513','2021-10-14 11:42:47.964513',NULL),(33,'hm8h5NZzfZxr63F0p7Dwk5rIqG8gdu',33,2,1,'2021-10-14 11:46:44.509938','2021-10-14 11:46:44.509938',NULL),(34,'A0jTWrVy2BcGHRlRT90AHKW55yzQLM',34,2,1,'2021-10-14 11:49:45.476738','2021-10-14 11:49:45.476738',NULL),(35,'nwESaa0OUj7Yy21J8XKan3uKaPqBeJ',35,2,1,'2021-10-15 01:27:15.706643','2021-10-15 01:27:15.706643',NULL),(36,'KFa77YrfrwUNStv5FJbcR1XmfOjIZl',36,2,1,'2021-10-15 12:26:37.362620','2021-10-15 12:26:37.362620',NULL),(37,'Im3Z7xm7sN5jD6fU5Eg553KDln9v5U',37,2,1,'2021-10-15 14:18:48.835905','2021-10-15 14:18:48.835905',NULL),(38,'4xwKNKPgGTXfsKF4FPR6XGBOeAO7ym',38,2,1,'2021-10-15 14:21:13.926048','2021-10-15 14:21:13.926048',NULL),(39,'obYE3BNv657huJhwcrhs4VBkgHlwAa',39,2,2,'2021-10-16 01:40:22.856311','2021-10-16 01:40:22.856311',NULL),(40,'Pt55Tc5UAlIgyqMRe7oNMPEfLrnKtm',40,2,2,'2021-10-16 01:40:52.974233','2021-10-16 01:40:52.974233',NULL),(41,'vamSQ29MaDariMB2nZYUjgFiwOsk4a',41,2,1,'2021-10-16 01:56:31.287582','2021-10-16 01:56:31.287582',NULL),(42,'wyjIuJ7uGSIwRXOUJ9InCZDs3VOksz',42,2,2,'2021-10-16 02:54:46.735803','2021-10-16 02:54:46.735803',NULL),(43,'FUN070Gnp8vXC6UqeYWwwl3RFz8YkE',43,2,1,'2021-10-16 02:56:53.406021','2021-10-16 02:56:53.406021',NULL),(44,'qjLhMTHpOReR4gGRnVtZoc07Da6PqH',44,2,2,'2021-10-16 02:58:52.205541','2021-10-16 02:58:52.205541',NULL),(45,'wYiojh8NeqRraB8FhfZIHOQoO2uQMl',45,2,1,'2021-10-16 03:01:51.598229','2021-10-16 03:01:51.598229',NULL),(46,'A6vCnN7AcjNKdhhDzb0cY1nS2xn7Tz',46,2,1,'2021-10-16 03:04:42.147908','2021-10-16 03:04:42.147908',NULL),(47,'V68ULhUKXn4cGimpWNrAdNaL9YNYLN',47,2,2,'2021-10-16 03:05:16.491751','2021-10-16 03:05:16.491751',NULL),(48,'TkfSU9cN198A5lX7aUgGqBDk988JAV',48,2,2,'2021-10-16 07:05:51.527652','2021-10-16 07:05:51.527652',NULL),(49,'SI310arpUjUPepXxDwzPtbVhve1EDc',49,2,2,'2021-10-17 03:22:52.928488','2021-10-17 03:22:52.928488',NULL),(50,'vDxDAvMmPYrKfNNBaGLnv07EuR2yjn',50,2,1,'2021-10-17 03:31:46.466728','2021-10-17 03:31:46.466728',NULL),(51,'s0cbTm2wWpubOZvxCFfb5shW6xnpVV',51,2,1,'2021-10-19 05:39:57.427651','2021-10-19 05:39:57.427651',NULL),(52,'8FJMIspvHfkvnzJaL3iLJQ63AohNMD',52,2,1,'2021-10-19 05:45:21.539521','2021-10-19 05:45:21.539521',NULL),(53,'Tj3ZGMrQAZIkuuBo1bLxyPC4kloeAR',53,2,1,'2021-10-19 08:42:24.548511','2021-10-19 08:42:24.548511',NULL),(54,'aWEGOK36ozHSnFeBKKKDQzvjUETeJ3',54,2,1,'2021-10-20 01:43:57.825474','2021-10-20 01:43:57.825474',NULL),(55,'QRHOyUUTcE9hpc2zgiNowDbGlo6ni2',55,2,1,'2021-10-20 05:29:05.526791','2021-10-20 05:29:05.526791',NULL),(56,'uL85RUKGHZqMGNb1ctRXjRiYFOuFzB',56,2,2,'2021-10-20 15:23:16.344623','2021-10-20 15:23:16.344623',NULL),(57,'mWvIgOX6wh8vEie1L6wHrLxB2Rd99W',57,2,1,'2021-10-20 15:23:56.736000','2021-10-20 15:23:56.736000',NULL),(58,'Eo7JqCPYcQu6q7kjikRpkNzssBx3FV',58,2,1,'2021-10-20 15:45:10.974018','2021-10-20 15:45:10.974018',NULL);
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_blog`
--

DROP TABLE IF EXISTS `tours_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_blog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `tour_detail_id` bigint DEFAULT NULL,
  `decription` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `tours_blog_tour_detail_id_14deb40c_fk_tours_tourdetail_id` (`tour_detail_id`),
  CONSTRAINT `tours_blog_tour_detail_id_14deb40c_fk_tours_tourdetail_id` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_blog`
--

LOCK TABLES `tours_blog` WRITE;
/*!40000 ALTER TABLE `tours_blog` DISABLE KEYS */;
INSERT INTO `tours_blog` VALUES (1,'DaLat giảm giá','static/blog/2021/10/dl-blog.jpg','2021-10-18 14:00:31.222516','2021-10-18 14:00:31.222516',1,'<p>&aacute;gsaga</p>',9,'ágágsa'),(16,'Phú Quốc','static/blog/2021/10/dl-packed.jpg','2021-10-19 10:26:45.956690','2021-10-19 10:42:19.665672',1,'null',12,'sdgds'),(18,'DaLat','static/blog/2021/10/sapa-packed_KHQZBHK.jpg','2021-10-19 10:37:48.607351','2021-10-19 10:37:48.607351',1,NULL,NULL,'ágágsa');
/*!40000 ALTER TABLE `tours_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_booking`
--

DROP TABLE IF EXISTS `tours_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `adult` int NOT NULL,
  `children` int NOT NULL,
  `status` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `room` int NOT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `total` int DEFAULT NULL,
  `customer_id` bigint DEFAULT NULL,
  `tour_detail_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_booking_tour_detail_id_customer_id_a1cc06b2_uniq` (`tour_detail_id`,`customer_id`),
  KEY `tours_booking_customer_id_30170ed0_fk_tours_user_id` (`customer_id`),
  CONSTRAINT `tours_booking_customer_id_30170ed0_fk_tours_user_id` FOREIGN KEY (`customer_id`) REFERENCES `tours_user` (`id`),
  CONSTRAINT `tours_booking_tour_detail_id_1d9b75b3_fk_tours_tourdetail_id` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_booking`
--

LOCK TABLES `tours_booking` WRITE;
/*!40000 ALTER TABLE `tours_booking` DISABLE KEYS */;
INSERT INTO `tours_booking` VALUES (52,NULL,1,1,'a',1,'2021-10-20 16:01:44.672902',3064500,1,9);
/*!40000 ALTER TABLE `tours_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_commentblog`
--

DROP TABLE IF EXISTS `tours_commentblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_commentblog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `blog_id` bigint NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tours_commentblog_blog_id_77fd4b22_fk_tours_blog_id` (`blog_id`),
  KEY `tours_commentblog_customer_id_954cd4ce_fk_tours_user_id` (`customer_id`),
  CONSTRAINT `tours_commentblog_blog_id_77fd4b22_fk_tours_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `tours_blog` (`id`),
  CONSTRAINT `tours_commentblog_customer_id_954cd4ce_fk_tours_user_id` FOREIGN KEY (`customer_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_commentblog`
--

LOCK TABLES `tours_commentblog` WRITE;
/*!40000 ALTER TABLE `tours_commentblog` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_commentblog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_commenttourdetail`
--

DROP TABLE IF EXISTS `tours_commenttourdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_commenttourdetail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  `tour_detail_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tours_commenttourdetail_customer_id_3e216170_fk_tours_user_id` (`customer_id`),
  KEY `tours_commenttourdet_tour_detail_id_b83e2d73_fk_tours_tou` (`tour_detail_id`),
  CONSTRAINT `tours_commenttourdet_tour_detail_id_b83e2d73_fk_tours_tou` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`),
  CONSTRAINT `tours_commenttourdetail_customer_id_3e216170_fk_tours_user_id` FOREIGN KEY (`customer_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_commenttourdetail`
--

LOCK TABLES `tours_commenttourdetail` WRITE;
/*!40000 ALTER TABLE `tours_commenttourdetail` DISABLE KEYS */;
INSERT INTO `tours_commenttourdetail` VALUES (1,'abc','2021-10-20 11:04:46.778013','2021-10-20 11:04:46.778013',1,1,9),(2,'abc','2021-10-20 11:04:48.367613','2021-10-20 11:04:48.367613',1,1,9),(3,'abc','2021-10-20 11:04:50.384248','2021-10-20 11:04:50.384248',1,1,9),(4,'Tốt','2021-10-20 11:05:09.263854','2021-10-20 11:05:09.263854',1,1,9),(5,'cdm','2021-10-20 15:23:44.017248','2021-10-20 15:23:44.017248',1,2,9);
/*!40000 ALTER TABLE `tours_commenttourdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_hotel`
--

DROP TABLE IF EXISTS `tours_hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_hotel` (
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `tour_detail_id` bigint NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`tour_detail_id`),
  CONSTRAINT `tours_hotel_tour_detail_id_519c5d1b_fk_tours_tourdetail_id` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_hotel`
--

LOCK TABLES `tours_hotel` WRITE;
/*!40000 ALTER TABLE `tours_hotel` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_imgdetail`
--

DROP TABLE IF EXISTS `tours_imgdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_imgdetail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tour_detail_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_imgdetail_image_tour_detail_id_5c2d91e5_uniq` (`image`,`tour_detail_id`),
  KEY `tours_imgdetail_tour_detail_id_a8797f21_fk_tours_tourdetail_id` (`tour_detail_id`),
  CONSTRAINT `tours_imgdetail_tour_detail_id_a8797f21_fk_tours_tourdetail_id` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_imgdetail`
--

LOCK TABLES `tours_imgdetail` WRITE;
/*!40000 ALTER TABLE `tours_imgdetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_imgdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_like`
--

DROP TABLE IF EXISTS `tours_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` smallint unsigned NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `blog_id` bigint NOT NULL,
  `creator_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_like_blog_id_creator_id_24e3d82c_uniq` (`blog_id`,`creator_id`),
  KEY `tours_like_creator_id_4f3071cd_fk_tours_user_id` (`creator_id`),
  CONSTRAINT `tours_like_blog_id_1238306c_fk_tours_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `tours_blog` (`id`),
  CONSTRAINT `tours_like_creator_id_4f3071cd_fk_tours_user_id` FOREIGN KEY (`creator_id`) REFERENCES `tours_user` (`id`),
  CONSTRAINT `tours_like_chk_1` CHECK ((`type` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_like`
--

LOCK TABLES `tours_like` WRITE;
/*!40000 ALTER TABLE `tours_like` DISABLE KEYS */;
INSERT INTO `tours_like` VALUES (6,2,'2021-10-20 05:07:57.231626','2021-10-20 05:08:01.096057',1,1);
/*!40000 ALTER TABLE `tours_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_rating`
--

DROP TABLE IF EXISTS `tours_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `rate` smallint unsigned NOT NULL,
  `creator_id` bigint NOT NULL,
  `tour_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_rating_tour_id_creator_id_64eb46a1_uniq` (`tour_id`,`creator_id`),
  KEY `tours_rating_creator_id_8a03693e_fk_tours_user_id` (`creator_id`),
  CONSTRAINT `tours_rating_creator_id_8a03693e_fk_tours_user_id` FOREIGN KEY (`creator_id`) REFERENCES `tours_user` (`id`),
  CONSTRAINT `tours_rating_tour_id_d7a8d329_fk_tours_tourdetail_id` FOREIGN KEY (`tour_id`) REFERENCES `tours_tourdetail` (`id`),
  CONSTRAINT `tours_rating_chk_1` CHECK ((`rate` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_rating`
--

LOCK TABLES `tours_rating` WRITE;
/*!40000 ALTER TABLE `tours_rating` DISABLE KEYS */;
INSERT INTO `tours_rating` VALUES (1,'2021-10-20 12:15:36.121110','2021-10-20 15:23:02.541887',4,1,9),(2,'2021-10-20 15:23:26.825763','2021-10-20 15:23:26.825763',2,2,9);
/*!40000 ALTER TABLE `tours_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_tag`
--

DROP TABLE IF EXISTS `tours_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tag`
--

LOCK TABLES `tours_tag` WRITE;
/*!40000 ALTER TABLE `tours_tag` DISABLE KEYS */;
INSERT INTO `tours_tag` VALUES (16,''),(3,'Beach'),(2,'Couple'),(4,'Islands'),(1,'Mountain');
/*!40000 ALTER TABLE `tours_tag` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourdetail`
--

LOCK TABLES `tours_tourdetail` WRITE;
/*!40000 ALTER TABLE `tours_tourdetail` DISABLE KEYS */;
INSERT INTO `tours_tourdetail` VALUES (9,'Dalat','static/2021/10/pq_oFgzsv2.jpg','2021-10-13 06:35:51.847783','2021-10-20 16:03:05.273611',1,22,'2021-10-16 15:52:48.000000',4,'<p>abc</p>',300000,1900000,3,1843000,1),(12,'Dalat3','static/2021/10/pq_JD28Ar3.jpg','2021-10-13 06:36:26.052045','2021-10-20 08:45:38.858120',1,40,'2021-10-16 15:52:00.000000',4,'<p>abc</p>',300000,1900000,3,1843000,1),(35,'2avá','static/2021/10/sapa-packed_XLD2j9K.jpg','2021-10-20 09:21:55.028641','2021-10-20 09:21:55.028641',1,40,'2021-10-28 19:21:00.000000',1,NULL,2,2,2,1,1);
/*!40000 ALTER TABLE `tours_tourdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_tourdetail_transport`
--

DROP TABLE IF EXISTS `tours_tourdetail_transport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tourdetail_transport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tourdetail_id` bigint NOT NULL,
  `transport_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_tourdetail_transpo_tourdetail_id_transport__1fd58b61_uniq` (`tourdetail_id`,`transport_id`),
  KEY `tours_tourdetail_tra_transport_id_312d5004_fk_tours_tra` (`transport_id`),
  CONSTRAINT `tours_tourdetail_tra_tourdetail_id_8a01915b_fk_tours_tou` FOREIGN KEY (`tourdetail_id`) REFERENCES `tours_tourdetail` (`id`),
  CONSTRAINT `tours_tourdetail_tra_transport_id_312d5004_fk_tours_tra` FOREIGN KEY (`transport_id`) REFERENCES `tours_transport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourdetail_transport`
--

LOCK TABLES `tours_tourdetail_transport` WRITE;
/*!40000 ALTER TABLE `tours_tourdetail_transport` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_tourdetail_transport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_tourdetailviews`
--

DROP TABLE IF EXISTS `tours_tourdetailviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tourdetailviews` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `views` int NOT NULL,
  `tour_detail_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tour_detail_id` (`tour_detail_id`),
  CONSTRAINT `tours_tourdetailview_tour_detail_id_af198f41_fk_tours_tou` FOREIGN KEY (`tour_detail_id`) REFERENCES `tours_tourdetail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourdetailviews`
--

LOCK TABLES `tours_tourdetailviews` WRITE;
/*!40000 ALTER TABLE `tours_tourdetailviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_tourdetailviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_tourtotal`
--

DROP TABLE IF EXISTS `tours_tourtotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tourtotal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_tourtotal_name_active_8b45be35_uniq` (`name`,`active`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourtotal`
--

LOCK TABLES `tours_tourtotal` WRITE;
/*!40000 ALTER TABLE `tours_tourtotal` DISABLE KEYS */;
INSERT INTO `tours_tourtotal` VALUES (1,'DaLat','static/2021/10/dl-blog.jpg','2021-10-13 05:53:23.051784','2021-10-18 06:43:43.372037',1,'avavá'),(2,'Phú Quốc','static/2021/10/vhl-packed_RQbovLR.jpg','2021-10-13 05:53:39.428093','2021-10-18 12:17:57.524556',1,'agfấaAVV'),(49,'VũngTào','static/2021/10/sapa-packed_WTrPWXZ.jpg','2021-10-18 12:41:37.228509','2021-10-18 13:59:16.391445',1,'ấccsa'),(70,'asa','static/2021/10/sp_HitrNYn.jpg','2021-10-19 05:44:04.429801','2021-10-19 05:44:04.438803',1,'ầ'),(71,'abc','static/2021/10/vt_GZkB7PL.jpg','2021-10-20 05:19:44.997864','2021-10-20 05:19:44.997864',1,'gấ');
/*!40000 ALTER TABLE `tours_tourtotal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_tourtotal_tags`
--

DROP TABLE IF EXISTS `tours_tourtotal_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_tourtotal_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tourtotal_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_tourtotal_tags_tourtotal_id_tag_id_0b918313_uniq` (`tourtotal_id`,`tag_id`),
  KEY `tours_tourtotal_tags_tag_id_f4796e7e_fk_tours_tag_id` (`tag_id`),
  CONSTRAINT `tours_tourtotal_tags_tag_id_f4796e7e_fk_tours_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `tours_tag` (`id`),
  CONSTRAINT `tours_tourtotal_tags_tourtotal_id_34f24b0c_fk_tours_tourtotal_id` FOREIGN KEY (`tourtotal_id`) REFERENCES `tours_tourtotal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_tourtotal_tags`
--

LOCK TABLES `tours_tourtotal_tags` WRITE;
/*!40000 ALTER TABLE `tours_tourtotal_tags` DISABLE KEYS */;
INSERT INTO `tours_tourtotal_tags` VALUES (1,1,1),(20,2,3),(33,49,2),(41,70,2);
/*!40000 ALTER TABLE `tours_tourtotal_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_transport`
--

DROP TABLE IF EXISTS `tours_transport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_transport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_transport`
--

LOCK TABLES `tours_transport` WRITE;
/*!40000 ALTER TABLE `tours_transport` DISABLE KEYS */;
INSERT INTO `tours_transport` VALUES (1,'Train',1),(2,'Plan',1),(3,'Coach',1),(12,'P',1),(13,'l',1),(14,'a',1),(15,'n',1);
/*!40000 ALTER TABLE `tours_transport` ENABLE KEYS */;
UNLOCK TABLES;

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
  `birthdate` date DEFAULT NULL,
  `active_staff` tinyint(1) NOT NULL,
  `point` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `tours_user_phone_username_45a80790_uniq` (`phone`,`username`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_user`
--

LOCK TABLES `tours_user` WRITE;
/*!40000 ALTER TABLE `tours_user` DISABLE KEYS */;
INSERT INTO `tours_user` VALUES (1,'pbkdf2_sha256$260000$syjkokGdFSoHfZWg8C6ClR$00SNZ7o5Z0mrcWJz+oV13/n5drw01DZpyJ/TvuGHvlk=','2021-10-16 02:21:45.000000',1,'admin','Hoang2','Nghia','nghiahoang10225@yahoo.com.vn',1,1,'2021-10-13 05:49:10.000000','371 nk','0358833453','static/user/2021/10/sapa-packed_gcW35M0.jpg','2000-11-21',0,26057),(2,'pbkdf2_sha256$260000$m1AptN3xUwbO5TEJ8Fh7lv$PdSLUWYsffzBUspAtwUWMgL2J6GmYdSabetJrZcUCig=','2021-10-13 12:48:48.000000',0,'staff','Thi','Ngoc','nghiahoang12345655@yahoo.com.vn',1,1,'2021-10-13 05:51:45.000000','371 Nguyễn Kiệm','0361231584','static/user/2021/10/sapa-packed_VQtC6G2.jpg','2000-11-06',1,0),(3,'pbkdf2_sha256$260000$m1AptN3xUwbO5TEJ8Fh7lv$PdSLUWYsffzBUspAtwUWMgL2J6GmYdSabetJrZcUCig=','2021-10-13 12:49:09.028926',0,'user','Trịnh','Huy','mr.tuan1749@gmail.com',1,1,'2021-10-13 05:52:17.000000','371 ngk','0361231584','static/user/2021/10/dl-blog.jpg','2021-10-05',0,0),(8,'pbkdf2_sha256$260000$fOOKGFnmK5v9Lejcl8hBqz$7mquUVcN7gmZ7bbpP1WRHQhbsQ1hQ9lf99EZGc+8Km8=',NULL,0,'abc123','DaLat','ávấ','nghiahoang12345655@yahoo.com.vn',0,1,'2021-10-13 14:14:26.370852','agá','0123456','static/user/2021/10/dl-packed_NgGxBNo.jpg',NULL,0,0),(16,'pbkdf2_sha256$260000$eCAe5VTbrQDsdHY1D99MJn$EbX0Pjd1IRdJG+M8XG5Gxzhwld2ShA6O/YohEycNv54=',NULL,0,'user123','Hoang','Nghia','1851050093nghia@ou.edu.vn',1,1,'2021-10-15 14:29:04.086249','371nk','0358833453','static/user/2021/10/sapa-packed_Pvl3mcy.jpg',NULL,1,0),(17,'pbkdf2_sha256$260000$h0NLtGyrlsQIHqaDSnhBWR$cECMhE1a92KhmF4QinYWUfFB+ruisL/U/7L6fuAzTd4=',NULL,0,'user1234','Hoang','Nghia','1851050093nghia@ou.edu.vn',1,1,'2021-10-15 14:30:27.712903','371nk','0358833453','static/user/2021/10/sapa-packed_p1HYbB4.jpg',NULL,1,0),(18,'pbkdf2_sha256$260000$VWqlGT5VybZ6mGWoCR2aQQ$SqUdWYGehkHmfH20JFLojI2UwCSZUX2RVQEOOBsl+nY=',NULL,0,'user12344','Hoang','Nghia','1851050093nghia@ou.edu.vn',1,1,'2021-10-15 14:30:40.456876','371nk','0358833453','static/user/2021/10/sapa-packed_5IWmoRU.jpg',NULL,1,0),(19,'pbkdf2_sha256$260000$p9GULFgf9oQtgxI1B0x4ZE$3o+pMjvVhrODaauPqpJpD6uDJStOJzw+kFSTkMz6CUA=',NULL,0,'admin2','abc','abc','nghia@gmai.com',1,1,'2021-10-17 03:32:16.112771','371nk','012356','',NULL,1,0),(20,'pbkdf2_sha256$260000$bjGMfDBQdRCRprrVLFP0nW$WHyPtlIOhFJICyvEJSo2zMF5ruEuEg42hTAhvAO/rzc=',NULL,0,'admin3','a','a','nghia@gmail.com',1,1,'2021-10-17 03:33:17.072567','123456','123','',NULL,1,0),(21,'pbkdf2_sha256$260000$l6dE144IXjIF306uIyTw7O$royVdT+iNn7Zp6+W6sNzDxCZI7+CBY9aaQVch1c33nA=',NULL,0,'admin4','a','a','nghia@gmail.com',1,1,'2021-10-17 03:33:45.748829','123','123','',NULL,1,0);
/*!40000 ALTER TABLE `tours_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_user_groups`
--

DROP TABLE IF EXISTS `tours_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_user_groups_user_id_group_id_76280a67_uniq` (`user_id`,`group_id`),
  KEY `tours_user_groups_group_id_2365fd14_fk_auth_group_id` (`group_id`),
  CONSTRAINT `tours_user_groups_group_id_2365fd14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `tours_user_groups_user_id_577fd1a7_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_user_groups`
--

LOCK TABLES `tours_user_groups` WRITE;
/*!40000 ALTER TABLE `tours_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours_user_user_permissions`
--

DROP TABLE IF EXISTS `tours_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tours_user_user_permissions_user_id_permission_id_9f30e23f_uniq` (`user_id`,`permission_id`),
  KEY `tours_user_user_perm_permission_id_cedf3ba3_fk_auth_perm` (`permission_id`),
  CONSTRAINT `tours_user_user_perm_permission_id_cedf3ba3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `tours_user_user_permissions_user_id_62eefd44_fk_tours_user_id` FOREIGN KEY (`user_id`) REFERENCES `tours_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours_user_user_permissions`
--

LOCK TABLES `tours_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `tours_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tours_user_user_permissions` ENABLE KEYS */;
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

-- Dump completed on 2021-10-20 23:04:51
