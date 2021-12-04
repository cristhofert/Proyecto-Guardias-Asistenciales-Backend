-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping data for table sggdb.institutions: ~2 rows (approximately)
DELETE FROM `institutions`;
/*!40000 ALTER TABLE `institutions` DISABLE KEYS */;
INSERT INTO `institutions` (`id`, `deleted`) VALUES
	(1, 0),
	(2, 0);
/*!40000 ALTER TABLE `institutions` ENABLE KEYS */;
-- Dumping data for table sggdb.user: ~3 rows (approximately)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `password`, `type`, `institution_id`, `deleted`) VALUES
	('1234562', 'Cristhofer Travieso', '$2b$12$y5uR7qEiIg9P6YN5KavN6.KmAt3sPRS26JBcni61P62VAlXNir3eK', 'medical_doctor', 1, 0),
	('4562123', 'Travieso Cristhofer ', '$2b$12$bj5C5Vzjt3LexbwJnmUDIeT8iaZ1e/WpOCUeFR9vNIlQoSor4U146', 'medical_doctor', 1, 0),
	('98765431', 'Juan Perez', '$2b$12$A0tq/nQuH/K3VetvTtXqf.FGwjq.0qj/K6.sKXhlHksvU2c.MPGOe', 'administrator', 1, 0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
-- Dumping data for table sggdb.zone: ~1 rows (approximately)
DELETE FROM `zone`;
/*!40000 ALTER TABLE `zone` DISABLE KEYS */;
INSERT INTO `zone` (`id`, `name`, `geotag`, `longitude`, `latitude`, `institution_id`, `deleted`) VALUES
	(1, 'z1', '0', '0', '0', 1, 0);
/*!40000 ALTER TABLE `zone` ENABLE KEYS */;
-- Dumping data for table sggdb.administrator: ~1 rows (approximately)
DELETE FROM `administrator`;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` (`id`, `superadmin`) VALUES
	('98765431', 1);
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;

-- Dumping data for table sggdb.medical_doctor: ~2 rows (approximately)
DELETE FROM `medical_doctor`;
/*!40000 ALTER TABLE `medical_doctor` DISABLE KEYS */;
INSERT INTO `medical_doctor` (`id`, `speciality`, `phone`, `email`, `zone_id`) VALUES
	('1234562', 'md', '09785412', 'c@c.com', 1),
	('4562123', 'pedatria', '09748512', 'b@c.com', 1);
/*!40000 ALTER TABLE `medical_doctor` ENABLE KEYS */;



-- Dumping data for table sggdb.notifications: ~0 rows (approximately)
DELETE FROM `notifications`;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;

-- Dumping data for table sggdb.services: ~2 rows (approximately)
DELETE FROM `services`;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` (`id`, `name`, `code`, `institution_id`, `deleted`) VALUES
	(1, 'Puerta de Emergencia', 'PE1', 1, 0),
	(2, 'Puerta de Emergencia II', 'PE2', 1, 0);
/*!40000 ALTER TABLE `services` ENABLE KEYS */;

-- Dumping data for table sggdb.subscriptions: ~2 rows (approximately)
DELETE FROM `subscriptions`;
/*!40000 ALTER TABLE `subscriptions` DISABLE KEYS */;
INSERT INTO `subscriptions` (`id`, `type`, `service_id`, `institution_id`, `deleted`) VALUES
	(1, 'lista', 1, 1, 0),
	(2, 'lista', 2, 1, 0);
/*!40000 ALTER TABLE `subscriptions` ENABLE KEYS */;

-- Dumping data for table sggdb.subscription_medical_doctor_table: ~1 rows (approximately)
DELETE FROM `subscription_medical_doctor_table`;
/*!40000 ALTER TABLE `subscription_medical_doctor_table` DISABLE KEYS */;
INSERT INTO `subscription_medical_doctor_table` (`subscription_id`, `medical_doctor_id`) VALUES
	(1, '1234562');
/*!40000 ALTER TABLE `subscription_medical_doctor_table` ENABLE KEYS */;


-- Dumping data for table sggdb.guards_group: ~3 rows (approximately)
DELETE FROM `guards_group`;
/*!40000 ALTER TABLE `guards_group` DISABLE KEYS */;
INSERT INTO `guards_group` (`id`, `institution_id`, `quantity`, `deleted`) VALUES
	(1, 1, 1, 0),
	(2, 1, 1, 0),
	(3, 1, 1, 0);
/*!40000 ALTER TABLE `guards_group` ENABLE KEYS */;

-- Dumping data for table sggdb.guard: ~4 rows (approximately)
DELETE FROM `guard`;
/*!40000 ALTER TABLE `guard` DISABLE KEYS */;
INSERT INTO `guard` (`id`, `created_at`, `updated_at`, `date`, `start_time`, `end_time`, `zone_id`, `lock`, `medical_doctor_id`, `subscription_id`, `group_id`, `institution_id`, `deleted`) VALUES
	(1, '2021-12-04 12:40:22', '2021-12-04 12:40:23', '2021-12-25', '08:00:00', '10:15:00', NULL, 0, '1234562', 1, 2, 1, 0),
	(2, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-25', '09:00:00', '11:15:00', NULL, 0, '1234562', 1, 2, 1, 0),
	(3, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-26', '10:00:00', '12:15:00', NULL, 0, NULL, 1, 2, 1, 0),
	(4, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-27', '08:11:00', '10:00:00', NULL, 0, '4562123', 2, 3, 1, 0);
/*!40000 ALTER TABLE `guard` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
-- Dumping data for table sggdb.assignment: ~3 rows (approximately)
DELETE FROM `assignment`;
/*!40000 ALTER TABLE `assignment` DISABLE KEYS */;
INSERT INTO `assignment` (`id`, `guard_id`, `medical_doctor_id`, `assignment_date`, `institution_id`, `deleted`) VALUES
	(1, 1, '4562123', '2021-12-04 12:40:23', 1, 0),
	(2, 1, '1234562', '2021-12-04 12:40:23', 1, 0),
	(3, 2, '1234562', '2021-12-04 12:40:23', 1, 0);
/*!40000 ALTER TABLE `assignment` ENABLE KEYS */;
