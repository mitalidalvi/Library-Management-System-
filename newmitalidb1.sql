-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: mitalidb1
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `Member` varchar(40) NOT NULL,
  `PRN_NO` varchar(45) NOT NULL,
  `ID` varchar(45) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `SurName` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `PostCode` varchar(45) DEFAULT NULL,
  `MobileNo` varchar(45) DEFAULT NULL,
  `BookID` varchar(45) DEFAULT NULL,
  `BookTitle` varchar(45) DEFAULT NULL,
  `AuthorName` varchar(45) DEFAULT NULL,
  `DateBorrowed` varchar(45) DEFAULT NULL,
  `DateDue` varchar(45) DEFAULT NULL,
  `LateReturnFine` varchar(45) DEFAULT NULL,
  `DateOverDue` varchar(45) DEFAULT NULL,
  `ActualPrice` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PRN_NO`,`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('','','','','','','','','','','','','','','',''),('Student','4456','65','Rutva','Jadhav','Thane','45879','9876543210','BKID2626','Secrete Rahasya','George MCcarthy','2022-04-01','2022-04-16','Rs.50','NO','Rs.590'),('Student','6784','34','Mitali','Dalvi','Dombivli','49053','1234567890','BKID6487','My Python','Paul Barry','2021-10-19','2021-11-03','Rs.50','NO','Rs.430'),('Lecturer','9845','25','Megha','Jadhav','Diva','28945','123456789','BKID2020','Python Tutorial','Guido van Rossum','2021-10-19','2021-11-03','Rs.50','NO','Rs.570');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `securityQ` varchar(45) DEFAULT NULL,
  `securityA` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('Darshana ','Rasal','5432167890','darshana@gmail.com','Your Favourite Subject','Hindi','321'),('Megha','Jadhav','6578329106','megha@gmail.com','Your Favourite Subject','History','0728'),('Megha','Jadhav','3421678432','megha12@gmail.com','Your Hobby','Dancing','12345'),('Megha','Jadhav','8765432190','megha123@gmail.com','Your Birth Place','Thane','1234'),('Mitali','Dalvi','0123456789','mitali@gmail.com','Your Birth Place','Mumbai','1234'),('Mitali','Dalvi','0123456789','mitali26@gmail.com','Your Hobby','Drawing','09876'),('Neha','Sawant','546783921','neha12@gmail.com','Your Hobby','Drawing','8809'),('Rutva','Jadhav','7654321890','rutva@gmail.com','Your Favourite Subject','Marathi','0001');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-03 21:31:23
