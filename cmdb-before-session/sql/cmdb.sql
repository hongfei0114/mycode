-- MySQL dump 10.13  Distrib 5.6.40, for macos10.13 (x86_64)
--
-- Host: localhost    Database: cmdb
-- ------------------------------------------------------
-- Server version	5.6.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app01_hosts`
--

DROP TABLE IF EXISTS `app01_hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_hosts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `host_pass` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=186 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_hosts`
--

LOCK TABLES `app01_hosts` WRITE;
/*!40000 ALTER TABLE `app01_hosts` DISABLE KEYS */;
INSERT INTO `app01_hosts` VALUES (21,'backend1','1'),(22,'backend2','2'),(23,'backend3','3'),(24,'backend4','4'),(25,'backend5','5'),(30,'ship2','2'),(31,'ship3','3'),(32,'ship4','4'),(33,'ship5','5'),(34,'ship6','6'),(35,'ship7','7'),(36,'ship8','8'),(37,'gaia1','1'),(38,'gaia2','2'),(39,'gaia3','3'),(40,'gaia4','4'),(41,'gaia5','5'),(42,'gaia6','6'),(43,'gaia7','7'),(44,'gaia8','8'),(45,'gaia1','1'),(46,'gaia2','2'),(47,'gaia3','3'),(48,'gaia4','4'),(49,'gaia5','5'),(50,'gaia6','6'),(51,'gaia7','7'),(52,'gaia8','8'),(53,'gaia10','10'),(54,'gaia11','11'),(55,'gaia12','12'),(56,'gaia13','13'),(57,'gaia14','14'),(58,'gaia15','15'),(59,'gaia16','16'),(60,'gaia17','17'),(61,'gaia18','18'),(62,'gaia19','19'),(63,'gaia20','20'),(64,'gaia21','21'),(65,'gaia22','22'),(66,'gaia23','23'),(67,'gaia24','24'),(68,'gaia25','25'),(69,'gaia26','26'),(70,'gaia27','27'),(71,'gaia28','28'),(72,'gaia29','29'),(73,'gaia30','30'),(74,'backend9','9'),(75,'backend10','10'),(76,'backend11','11'),(77,'backend12','12'),(78,'backend13','13'),(79,'backend14','14'),(80,'backend15','15'),(81,'backend16','16'),(82,'backend17','17'),(83,'backend18','18'),(84,'backend19','19'),(85,'backend20','20'),(86,'backend21','21'),(87,'backend22','22'),(88,'backend23','23'),(89,'backend24','24'),(90,'backend25','25'),(91,'backend26','26'),(92,'backend27','27'),(93,'backend28','28'),(94,'backend29','29'),(95,'backend30','30'),(96,'backend9','9'),(97,'backend10','10'),(98,'backend11','11'),(99,'backend12','12'),(100,'backend13','13'),(101,'backend14','14'),(102,'backend15','15'),(103,'backend16','16'),(104,'backend17','17'),(105,'backend18','18'),(106,'backend19','19'),(107,'backend20','20'),(108,'backend21','21'),(109,'backend22','22'),(110,'backend23','23'),(111,'backend24','24'),(112,'backend25','25'),(113,'backend26','26'),(114,'backend27','27'),(115,'backend28','28'),(116,'backend29','29'),(117,'backend30','30'),(118,'backend9','9'),(119,'backend10','10'),(120,'backend11','11'),(121,'backend12','12'),(122,'backend13','13'),(123,'backend14','14'),(124,'backend15','15'),(125,'backend16','16'),(126,'backend17','17'),(127,'backend18','18'),(128,'backend19','19'),(129,'backend20','20'),(130,'backend21','21'),(131,'backend22','22'),(132,'backend23','23'),(133,'backend24','24'),(134,'backend25','25'),(135,'backend26','26'),(136,'backend27','27'),(137,'backend28','28'),(138,'backend29','29'),(139,'backend30','30'),(140,'backend9','9'),(141,'backend10','10'),(142,'backend11','11'),(143,'backend12','12'),(144,'backend13','13'),(145,'backend14','14'),(146,'backend15','15'),(147,'backend16','16'),(148,'backend17','17'),(149,'backend18','18'),(150,'backend19','19'),(151,'backend20','20'),(152,'backend21','21'),(153,'backend22','22'),(154,'backend23','23'),(155,'backend24','24'),(156,'backend25','25'),(157,'backend26','26'),(158,'backend27','27'),(159,'backend28','28'),(160,'backend29','29'),(161,'backend30','30'),(162,'backend9','9'),(163,'backend10','10'),(164,'backend11','11'),(165,'backend12','12'),(166,'backend13','13'),(167,'backend14','14'),(168,'backend15','15'),(169,'backend16','16'),(170,'backend17','17'),(171,'backend18','18'),(172,'backend19','19'),(173,'backend20','20'),(174,'backend21','21'),(175,'backend22','22'),(176,'backend23','23'),(177,'backend24','24'),(178,'backend25','25'),(179,'backend26','26'),(180,'backend27','27'),(181,'backend28','28'),(182,'backend29','29'),(183,'backend30','30'),(184,'celery01',''),(185,'celery02','');
/*!40000 ALTER TABLE `app01_hosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_hosts_services`
--

DROP TABLE IF EXISTS `app01_hosts_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_hosts_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hosts_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_hosts_services_hosts_id_service_id_b0ddb65e_uniq` (`hosts_id`,`service_id`),
  KEY `app01_hosts_services_service_id_b8f741f8_fk_app01_service_id` (`service_id`),
  CONSTRAINT `app01_hosts_services_hosts_id_a5f55853_fk_app01_hosts_id` FOREIGN KEY (`hosts_id`) REFERENCES `app01_hosts` (`id`),
  CONSTRAINT `app01_hosts_services_service_id_b8f741f8_fk_app01_service_id` FOREIGN KEY (`service_id`) REFERENCES `app01_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_hosts_services`
--

LOCK TABLES `app01_hosts_services` WRITE;
/*!40000 ALTER TABLE `app01_hosts_services` DISABLE KEYS */;
INSERT INTO `app01_hosts_services` VALUES (2,21,1),(3,21,2),(4,22,1),(5,22,2),(11,22,7),(6,23,2),(12,23,7),(7,24,3),(8,25,1),(9,25,2),(10,25,3),(24,30,1),(22,30,2),(23,30,3),(25,30,7),(29,31,2),(31,31,3),(30,31,7),(13,36,8),(14,37,8),(16,55,10),(15,56,10),(18,184,2),(17,184,3),(20,185,1),(19,185,2),(21,185,3);
/*!40000 ALTER TABLE `app01_hosts_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_service`
--

DROP TABLE IF EXISTS `app01_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `Users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_service_Users_id_21f8e215_fk_app01_user_id` (`Users_id`),
  CONSTRAINT `app01_service_Users_id_21f8e215_fk_app01_user_id` FOREIGN KEY (`Users_id`) REFERENCES `app01_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_service`
--

LOCK TABLES `app01_service` WRITE;
/*!40000 ALTER TABLE `app01_service` DISABLE KEYS */;
INSERT INTO `app01_service` VALUES (1,'gaia',12),(2,'backend',13),(3,'ship',12),(7,'ascle',14),(8,'gm-face',15),(10,'hera',17);
/*!40000 ALTER TABLE `app01_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_user`
--

DROP TABLE IF EXISTS `app01_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_user`
--

LOCK TABLES `app01_user` WRITE;
/*!40000 ALTER TABLE `app01_user` DISABLE KEYS */;
INSERT INTO `app01_user` VALUES (12,'leishiyi','d91982741c0e8b4b94eea44ba248564c'),(13,'dalei','135247c659b765f5da666af6069857eb'),(14,'wangjing','488d2f55e9ed954a5d6dd5d6d47ed257'),(15,'lei','1cb84d995447154894a32d38d1a5129a'),(17,'雷十一','a9dfe49dd26ff21453d0895e52123b56'),(23,'admin','d138768d3b5eca407f0dd579c5ca3767');
/*!40000 ALTER TABLE `app01_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add service',8,'add_service'),(23,'Can change service',8,'change_service'),(24,'Can delete service',8,'delete_service'),(25,'Can add hosts',9,'add_hosts'),(26,'Can change hosts',9,'change_hosts'),(27,'Can delete hosts',9,'delete_hosts');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'app01','hosts'),(8,'app01','service'),(7,'app01','user'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-08-24 15:36:13.313781'),(2,'auth','0001_initial','2018-08-24 15:36:13.576365'),(3,'admin','0001_initial','2018-08-24 15:36:13.635282'),(4,'admin','0002_logentry_remove_auto_add','2018-08-24 15:36:13.660193'),(5,'contenttypes','0002_remove_content_type_name','2018-08-24 15:36:13.706328'),(6,'auth','0002_alter_permission_name_max_length','2018-08-24 15:36:13.724408'),(7,'auth','0003_alter_user_email_max_length','2018-08-24 15:36:13.746731'),(8,'auth','0004_alter_user_username_opts','2018-08-24 15:36:13.759366'),(9,'auth','0005_alter_user_last_login_null','2018-08-24 15:36:13.780782'),(10,'auth','0006_require_contenttypes_0002','2018-08-24 15:36:13.783431'),(11,'auth','0007_alter_validators_add_error_messages','2018-08-24 15:36:13.792758'),(12,'auth','0008_alter_user_username_max_length','2018-08-24 15:36:13.841599'),(13,'sessions','0001_initial','2018-08-24 15:36:13.868694'),(14,'app01','0001_initial','2018-08-24 15:37:11.373378'),(15,'app01','0002_auto_20180825_0244','2018-08-25 02:44:57.357679'),(16,'app01','0003_auto_20180825_0340','2018-08-25 03:40:56.649392'),(17,'app01','0004_auto_20180825_0343','2018-08-25 03:43:22.821221');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-25 22:37:10
