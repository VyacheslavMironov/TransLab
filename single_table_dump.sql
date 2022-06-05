-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: trans_lab_db
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `car_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model_car` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `year_car` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `volume_engine` double(8,2) NOT NULL,
  PRIMARY KEY (`car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,'Ford','Aerostar','1986',3.00),(2,'Ford','Aerostar','1987',3.00),(3,'Ford','Aerostar','1988',3.00),(4,'Ford','Aerostar','1989',3.00),(5,'Ford','Aerostar','1990',3.00),(6,'Ford','Aerostar','1990',4.00),(7,'Ford','Aerostar','1991',3.00),(8,'Ford','Aerostar','1991',4.00),(9,'Ford','Aerostar','1992',3.00),(10,'Ford','Aerostar','1992',4.00),(11,'Ford','Aerostar','1993',3.00),(12,'Ford','Aerostar','1993',4.00),(13,'Ford','Aerostar','1994',3.00),(14,'Ford','Aerostar','1994',4.00),(15,'Ford','Aerostar','1995',3.00),(16,'Ford','Aerostar','1995',4.00),(17,'Ford','Aerostar','1996',3.00),(18,'Ford','Aerostar','1996',4.00),(19,'Ford','Aerostar','1997',3.00),(20,'Ford','Aerostar','1997',4.00),(21,'Ford','Prode','1989',2.20),(22,'Ford','Prode','1990',2.20),(23,'Ford','Prode','1990',3.00),(24,'Ford','Prode','1991',2.20),(25,'Ford','Prode','1991',3.00),(26,'Ford','Prode','1992',2.20),(27,'Ford','Prode','1992',3.00),(28,'Ford','Prode','1993',2.00),(29,'Ford','Prode','1993',2.50),(30,'Ford','Prode','1994',2.00),(31,'Ford','Prode','1994',2.50),(32,'Ford','Prode','1995',2.00),(33,'Ford','Prode','1995',2.50),(34,'Ford','Prode','1996',2.00),(35,'Ford','Prode','1996',2.50),(36,'Ford','Prode','1997',2.00),(37,'Ford','Prode','1997',2.50),(38,'Lincoln','Zephyr','2006',3.00),(39,'Lincoln','MKS','2009',3.70),(40,'Lincoln','MKS','2010',3.50),(41,'Lincoln','MKS','2010',3.70),(42,'Lincoln','MKS','2011',3.50),(43,'Lincoln','MKS','2011',3.70),(44,'Lincoln','MKS','2012',3.50),(45,'Lincoln','MKS','2012',3.70),(46,'Lincoln','MKS','2013',3.50),(47,'Lincoln','MKS','2013',3.70),(48,'Lincoln','MKS','2014',3.50),(49,'Lincoln','MKS','2014',3.70),(50,'Lincoln','MKS','2015',3.50),(51,'Lincoln','MKS','2015',3.70),(52,'Lincoln','MKS','2016',3.50),(53,'Lincoln','MKS','2016',3.70);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-29 10:07:26
