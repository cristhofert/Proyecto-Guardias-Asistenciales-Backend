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

-- Dumping data for table sggdb.administrator: ~17 rows (approximately)
DELETE FROM `administrator`;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` (`id`, `superadmin`) VALUES
	('12272724', 0),
	('26779188', 0),
	('30697443', 0),
	('37523742', 0),
	('40209579', 0),
	('45103885', 0),
	('49057888', 0),
	('53844853', 0),
	('56594974', 0),
	('59692727', 0),
	('64782951', 0),
	('72400460', 0),
	('77696777', 0),
	('88437665', 1),
	('95648031', 0),
	('95806392', 0),
	('98765431', 1);
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;

-- Dumping data for table sggdb.assignment: ~27 rows (approximately)
DELETE FROM `assignment`;
/*!40000 ALTER TABLE `assignment` DISABLE KEYS */;
INSERT INTO `assignment` (`id`, `guard_id`, `medical_doctor_id`, `assignment_date`, `institution_id`, `deleted`) VALUES
	(1, 1, '4562123', '2021-12-04 12:40:23', 1, 0),
	(2, 1, '1234562', '2021-12-04 12:40:23', 1, 0),
	(3, 2, '1234562', '2021-12-04 12:40:23', 1, 0),
	(4, 5, '39658892', '2021-12-04 15:46:55', 2, 0),
	(5, 11, '34536998', '2021-12-04 15:47:01', 2, 0),
	(6, 9, '40167997', '2021-12-04 15:47:08', 2, 0),
	(7, 6, '34536998', '2021-12-04 15:47:19', 2, 0),
	(8, 7, '98528581', '2021-12-04 15:47:28', 2, 0),
	(9, 10, '89277357', '2021-12-04 15:47:36', 2, 0),
	(10, 18, '57447572', '2021-12-04 15:47:43', 2, 0),
	(11, 24, '41444071', '2021-12-04 15:47:50', 2, 0),
	(12, 23, '34536998', '2021-12-04 15:47:57', 2, 0),
	(13, 22, '40167997', '2021-12-04 15:48:05', 2, 0),
	(14, 20, '15851951', '2021-12-04 15:48:12', 2, 0),
	(15, 16, '41444071', '2021-12-04 15:48:21', 2, 0),
	(16, 14, '15851951', '2021-12-04 15:48:28', 2, 0),
	(17, 12, '87575193', '2021-12-04 15:48:44', 2, 0),
	(18, 34, '87575193', '2021-12-04 15:48:49', 2, 0),
	(19, 32, '57447572', '2021-12-04 15:48:56', 2, 0),
	(20, 37, '41444071', '2021-12-04 15:49:03', 2, 0),
	(21, 42, '34536998', '2021-12-04 15:49:10', 2, 0),
	(22, 47, '34866238', '2021-12-04 15:49:18', 2, 0),
	(23, 52, '15851951', '2021-12-04 15:49:24', 2, 0),
	(24, 58, '39658892', '2021-12-04 15:49:31', 2, 0),
	(25, 25, '90810255', '2021-12-04 15:49:45', 2, 0),
	(26, 63, '95763255', '2021-12-04 15:49:56', 2, 0),
	(27, 54, '88203111', '2021-12-04 15:50:04', 2, 0);
/*!40000 ALTER TABLE `assignment` ENABLE KEYS */;

-- Dumping data for table sggdb.guard: ~64 rows (approximately)
DELETE FROM `guard`;
/*!40000 ALTER TABLE `guard` DISABLE KEYS */;
INSERT INTO `guard` (`id`, `created_at`, `updated_at`, `date`, `start_time`, `end_time`, `zone_id`, `lock`, `medical_doctor_id`, `subscription_id`, `group_id`, `institution_id`, `deleted`) VALUES
	(1, '2021-12-04 12:40:22', '2021-12-04 12:40:23', '2021-12-25', '08:00:00', '10:15:00', NULL, 0, '1234562', 1, 2, 1, 0),
	(2, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-25', '09:00:00', '11:15:00', NULL, 0, '1234562', 1, 2, 1, 0),
	(3, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-26', '10:00:00', '12:15:00', NULL, 0, NULL, 1, 2, 1, 0),
	(4, '2021-12-04 12:40:23', '2021-12-04 12:40:23', '2021-12-27', '08:11:00', '10:00:00', NULL, 0, '4562123', 2, 3, 1, 0),
	(5, '2021-12-04 15:45:55', '2021-12-04 15:46:55', '2021-12-06', '06:45:00', '15:51:00', 1, 1, '39658892', 3, 4, 2, 0),
	(6, '2021-12-04 15:45:55', '2021-12-04 15:47:19', '2021-12-06', '06:45:00', '15:51:00', 1, 1, '34536998', 3, 4, 2, 0),
	(7, '2021-12-04 15:45:55', '2021-12-04 15:47:28', '2021-12-06', '06:45:00', '15:51:00', 1, 1, '98528581', 3, 4, 2, 0),
	(8, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-06', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(9, '2021-12-04 15:45:55', '2021-12-04 15:47:08', '2021-12-06', '06:45:00', '15:51:00', 1, 1, '40167997', 3, 4, 2, 0),
	(10, '2021-12-04 15:45:55', '2021-12-04 15:47:36', '2021-12-13', '06:45:00', '15:51:00', 1, 1, '89277357', 3, 4, 2, 0),
	(11, '2021-12-04 15:45:55', '2021-12-04 15:47:01', '2021-12-13', '06:45:00', '15:51:00', 1, 1, '34536998', 3, 4, 2, 0),
	(12, '2021-12-04 15:45:55', '2021-12-04 15:48:44', '2021-12-13', '06:45:00', '15:51:00', 1, 1, '87575193', 3, 4, 2, 0),
	(13, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-13', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(14, '2021-12-04 15:45:55', '2021-12-04 15:48:28', '2021-12-13', '06:45:00', '15:51:00', 1, 1, '15851951', 3, 4, 2, 0),
	(15, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-20', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(16, '2021-12-04 15:45:55', '2021-12-04 15:48:21', '2021-12-20', '06:45:00', '15:51:00', 1, 1, '41444071', 3, 4, 2, 0),
	(17, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-20', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(18, '2021-12-04 15:45:55', '2021-12-04 15:47:43', '2021-12-20', '06:45:00', '15:51:00', 1, 1, '57447572', 3, 4, 2, 0),
	(19, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-20', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(20, '2021-12-04 15:45:55', '2021-12-04 15:48:12', '2021-12-27', '06:45:00', '15:51:00', 1, 1, '15851951', 3, 4, 2, 0),
	(21, '2021-12-04 15:45:55', '2021-12-04 15:45:55', '2021-12-27', '06:45:00', '15:51:00', 1, 0, NULL, 3, 4, 2, 0),
	(22, '2021-12-04 15:45:55', '2021-12-04 15:48:05', '2021-12-27', '06:45:00', '15:51:00', 1, 1, '40167997', 3, 4, 2, 0),
	(23, '2021-12-04 15:45:55', '2021-12-04 15:47:57', '2021-12-27', '06:45:00', '15:51:00', 1, 1, '34536998', 3, 4, 2, 0),
	(24, '2021-12-04 15:45:55', '2021-12-04 15:47:50', '2021-12-27', '06:45:00', '15:51:00', 1, 1, '41444071', 3, 4, 2, 0),
	(25, '2021-12-04 15:46:45', '2021-12-04 15:49:45', '2021-12-06', '10:45:00', '18:45:00', 1, 1, '90810255', 8, 5, 2, 0),
	(26, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-06', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(27, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-07', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(28, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-07', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(29, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-08', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(30, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-08', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(31, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-09', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(32, '2021-12-04 15:46:45', '2021-12-04 15:48:56', '2021-12-09', '10:45:00', '18:45:00', 1, 1, '57447572', 8, 5, 2, 0),
	(33, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-10', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(34, '2021-12-04 15:46:45', '2021-12-04 15:48:49', '2021-12-10', '10:45:00', '18:45:00', 1, 1, '87575193', 8, 5, 2, 0),
	(35, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-13', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(36, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-13', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(37, '2021-12-04 15:46:45', '2021-12-04 15:49:03', '2021-12-14', '10:45:00', '18:45:00', 1, 1, '41444071', 8, 5, 2, 0),
	(38, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-14', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(39, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-15', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(40, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-15', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(41, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-16', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(42, '2021-12-04 15:46:45', '2021-12-04 15:49:10', '2021-12-16', '10:45:00', '18:45:00', 1, 1, '34536998', 8, 5, 2, 0),
	(43, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-17', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(44, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-17', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(45, '2021-12-04 15:46:45', '2021-12-04 15:46:45', '2021-12-20', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(46, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-20', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(47, '2021-12-04 15:46:46', '2021-12-04 15:49:18', '2021-12-21', '10:45:00', '18:45:00', 1, 1, '34866238', 8, 5, 2, 0),
	(48, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-21', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(49, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-22', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(50, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-22', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(51, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-23', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(52, '2021-12-04 15:46:46', '2021-12-04 15:49:24', '2021-12-23', '10:45:00', '18:45:00', 1, 1, '15851951', 8, 5, 2, 0),
	(53, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-24', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(54, '2021-12-04 15:46:46', '2021-12-04 15:50:04', '2021-12-24', '10:45:00', '18:45:00', 1, 1, '88203111', 8, 5, 2, 0),
	(55, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-27', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(56, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-27', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(57, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-28', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(58, '2021-12-04 15:46:46', '2021-12-04 15:49:31', '2021-12-28', '10:45:00', '18:45:00', 1, 1, '39658892', 8, 5, 2, 0),
	(59, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-29', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(60, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-29', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(61, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-30', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(62, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-30', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(63, '2021-12-04 15:46:46', '2021-12-04 15:49:56', '2021-12-31', '10:45:00', '18:45:00', 1, 1, '95763255', 8, 5, 2, 0),
	(64, '2021-12-04 15:46:46', '2021-12-04 15:46:46', '2021-12-31', '10:45:00', '18:45:00', 1, 0, NULL, 8, 5, 2, 0),
	(65, '2021-12-04 16:11:34', '2021-12-04 16:11:34', '2021-12-28', '16:11:00', '12:11:00', 1, 0, NULL, 2, 6, 1, 0),
	(66, '2021-12-04 16:11:34', '2021-12-04 16:11:34', '2021-12-28', '16:11:00', '12:11:00', 1, 0, NULL, 2, 6, 1, 0),
	(67, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-11', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(68, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-11', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(69, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-11', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(70, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-11', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(71, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-11', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(72, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-18', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(73, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-18', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(74, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-18', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(75, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-18', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(76, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-18', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(77, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-25', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(78, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-25', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(79, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-25', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(80, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-25', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0),
	(81, '2021-12-04 16:12:57', '2021-12-04 16:12:57', '2021-12-25', '19:15:00', '14:15:00', 1, 0, NULL, 2, 7, 1, 0);
/*!40000 ALTER TABLE `guard` ENABLE KEYS */;

-- Dumping data for table sggdb.guards_group: ~5 rows (approximately)
DELETE FROM `guards_group`;
/*!40000 ALTER TABLE `guards_group` DISABLE KEYS */;
INSERT INTO `guards_group` (`id`, `institution_id`, `quantity`, `deleted`) VALUES
	(1, 1, 1, 0),
	(2, 1, 1, 0),
	(3, 1, 1, 0),
	(4, 2, 1, 0),
	(5, 2, 1, 0),
	(6, 1, 1, 0),
	(7, 1, 1, 0);
/*!40000 ALTER TABLE `guards_group` ENABLE KEYS */;

-- Dumping data for table sggdb.institutions: ~2 rows (approximately)
DELETE FROM `institutions`;
/*!40000 ALTER TABLE `institutions` DISABLE KEYS */;
INSERT INTO `institutions` (`id`, `deleted`) VALUES
	(1, 0),
	(2, 0);
/*!40000 ALTER TABLE `institutions` ENABLE KEYS */;

-- Dumping data for table sggdb.medical_doctor: ~20 rows (approximately)
DELETE FROM `medical_doctor`;
/*!40000 ALTER TABLE `medical_doctor` DISABLE KEYS */;
INSERT INTO `medical_doctor` (`id`, `speciality`, `phone`, `email`, `zone_id`) VALUES
	('1234562', 'md', '09785412', 'c@c.com', 1),
	('15851951', 'medicina general', '091128356', 'mgonzalez@mail.com', 1),
	('23654278', 'medicina general', '093228369', 'sacosta@mail.com', 2),
	('27801940', 'medicina general', '093228373', 'vayala@mail.com', 3),
	('27871032', 'medicina general', '093228302', 'ecedres@mail.com', 2),
	('34536998', 'medicina general', '095128365', 'mayala@mail.com', 1),
	('34866238', 'medicina general', '094128372', 'lceceres@mail.com', 1),
	('38974126', 'medicina general', '095228365', 'mrodriguez@mail.com', 2),
	('39658892', 'medicina general', '091128354', 'tmartinez@mail.com', 1),
	('40167997', 'medicina general', '095128367', 'snunez@mail.com', 1),
	('41444071', 'medicina general', '091128359', 'mgimenez@mail.com', 1),
	('41602291', 'medicina general', '091128355', 'tbenitez@mail.com', 1),
	('43433004', 'medicina general', '091128357', 'slopez@mail.com', 1),
	('44177853', 'medicina general', '091128353', 'mvera@mail.com', 1),
	('4562123', 'pedatria', '09748512', 'b@c.com', 1),
	('57447572', 'medicina general', '091128362', 'pgomez@mail.com', 1),
	('61836581', 'medicina general', '093128369', 'arodriguez@mail.com', 1),
	('62659542', 'medicina general', '09676589', 'anunez@mainl.com', 4),
	('62836582', 'medicina general', '093228369', 'arodriguez@mail.com', 2),
	('72581357', 'medicina general', '093228370', 'lrojas@mail.com', 2),
	('76434077', 'medicina general', '091128358', 'evillalba@mail.com', 1),
	('87575193', 'medicina general', '094128401', 'vacosta@mail.com', 1),
	('88203111', 'medicina general', '093128374', 'zortiz@mail.com', 1),
	('89277357', 'medicina general', '093128370', 'nrojas@mail.com', 1),
	('090017536', 'medicina general', '093228363', 'mbaez@mail.com', 2),
	('090810255', 'medicina general', '091128361', 'efernandez@mail.com', 1),
	('095763255', 'medicina general', '091128360', 'lduarte123', 1),
	('098484268', 'medicina general', '093228372', 'nortiz@mail.com', 2),
	('098528581', 'medicina general', '093128364', 'mbaez@mail.com', 1);
/*!40000 ALTER TABLE `medical_doctor` ENABLE KEYS */;

-- Dumping data for table sggdb.notifications: ~0 rows (approximately)
DELETE FROM `notifications`;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;

-- Dumping data for table sggdb.services: ~7 rows (approximately)
DELETE FROM `services`;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` (`id`, `name`, `code`, `institution_id`, `deleted`) VALUES
	(1, 'Puerta de Emergencia', 'PE1', 1, 0),
	(2, 'Puerta de Emergencia II', 'PE2', 1, 0),
	(3, 'Piso I', 'P1', 2, 0),
	(4, 'C.T.I.', 'CTI', 2, 0),
	(5, 'Hemergencia Sur', 'HS', 2, 0),
	(6, 'Hemergencia Norte', 'HN', 2, 0),
	(7, 'Piso II', 'P2', 2, 0);
/*!40000 ALTER TABLE `services` ENABLE KEYS */;

-- Dumping data for table sggdb.subscriptions: ~12 rows (approximately)
DELETE FROM `subscriptions`;
/*!40000 ALTER TABLE `subscriptions` DISABLE KEYS */;
INSERT INTO `subscriptions` (`id`, `type`, `service_id`, `institution_id`, `deleted`) VALUES
	(1, 'lista', 1, 1, 0),
	(2, 'lista', 2, 1, 0),
	(3, 'lista', 3, 2, 0),
	(4, 'dispersión', 3, 2, 0),
	(5, 'lista', 4, 2, 0),
	(6, 'dispersión', 4, 2, 0),
	(7, 'lista', 5, 2, 0),
	(8, 'dispersión', 5, 2, 0),
	(9, 'lista', 6, 2, 0),
	(10, 'dispersión', 6, 2, 0),
	(11, 'lista', 7, 2, 0),
	(12, 'dispersión', 7, 2, 0),
	(13, 'dispersión', 1, 1, 0),
	(14, 'dispersión', 2, 1, 0);
/*!40000 ALTER TABLE `subscriptions` ENABLE KEYS */;

-- Dumping data for table sggdb.subscription_medical_doctor_table: ~1 rows (approximately)
DELETE FROM `subscription_medical_doctor_table`;
/*!40000 ALTER TABLE `subscription_medical_doctor_table` DISABLE KEYS */;
INSERT INTO `subscription_medical_doctor_table` (`subscription_id`, `medical_doctor_id`) VALUES
	(1, '1234562'),
	(1, '62659542');
/*!40000 ALTER TABLE `subscription_medical_doctor_table` ENABLE KEYS */;

-- Dumping data for table sggdb.user: ~37 rows (approximately)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `password`, `type`, `institution_id`, `deleted`) VALUES
	('12272724', 'Claudia Mendez', '$2b$12$ODBTDj2GLtOArie20QIaVOGbfJ1fpUyVQ0YNrta4gJalF7IrYqlLq', 'administrator', 1, 0),
	('1234562', 'Cristhofer Travieso', '$2b$12$y5uR7qEiIg9P6YN5KavN6.KmAt3sPRS26JBcni61P62VAlXNir3eK', 'medical_doctor', 1, 0),
	('15851951', 'Mateo González', '$2b$12$MKmczBsungoMCiUF.etLQO84lZAGqq6iwYkzjTY90YKginvb00Kim', 'medical_doctor', 2, 0),
	('23654278', 'Santiago Acosta', '$2b$12$k9WZLR48AFnnmZuuoD.ADOoFif13d.ysXoCH6Slm4Ui.iZJEHPD7.', 'medical_doctor', 1, 0),
	('26779188', 'Isabel Castillo', '$2b$12$zcR9aswwO59XcArXPf8EP.v/ISi7jrg/IF9dBvtsfNNOAFVBHxS.a', 'administrator', 2, 0),
	('27801940', 'Valentina Ayala', '$2b$12$2Q/vBCrjOdnqIRh6IUId4utyq8vHmsP1BBU3kHCXi2zP0rIQL/jpa', 'medical_doctor', 1, 0),
	('27871032', 'Emilia Cáceres', '$2b$12$gS6DM.E9cl5GlnKry7gpuev04hyV1h21S/m1s5NKbKUSPMoxN3Ddy', 'medical_doctor', 1, 0),
	('30697443', 'Carlos Ferreira', '$2b$12$E3eu5qg4wmCqg51PcZSdsu.ZJC31X3MtgJyYulyDvRgzyQW7yU5wi', 'administrator', 2, 0),
	('34536998', 'Manuel Ayala', '$2b$12$c8IUulCFdFonvVO0OdNUpuXXxkc2IaHz7EtuigqCo0xsOuIGv0e92', 'medical_doctor', 2, 0),
	('34866238', 'Luis Cáceres', '$2b$12$388/C3l.KezKvTCon3oTCeyYwGJAY2F3j.75G4Oy70OWb1UGU8H9q', 'medical_doctor', 2, 0),
	('37523742', 'Nahuel Mendoza', '$2b$12$e3X5DRZ0aLEGGX3SjQpIGu.x0yVR7IRUV2YP1pPuPJGW8SSEcJHuO', 'administrator', 1, 0),
	('38974126', 'Miguel Rodríguez', '$2b$12$3WeMhgCT0rgeSRkwR8l.ce47fbxLxD3aCorPa2R062/Y.nQP1fNH6', 'medical_doctor', 1, 0),
	('39658892', 'Thiago Martínez', '$2b$12$E1BNu1ofQLJawvb3tdKOeuoN0hmWI/fnb1Br75WjE8bY88fLUQMTK', 'medical_doctor', 2, 0),
	('40167997', 'Santiago Núñez', '$2b$12$RO4UIDlb2nZrnk6jr1rXgOBAGNAYgSRDTN9xncb9SXBqGZ3EG5uyK', 'medical_doctor', 2, 0),
	('40209579', 'Maria Sellanez', '$2b$12$6gNOIvJY9RTlH2h/whR9qeKH1ybbjgkPqtNOfBskOVLyDOyOU/65a', 'administrator', 1, 0),
	('41444071', 'Martina Giménez', '$2b$12$vsq1nvZQP/Rr6zUI.8sqdODBNp5k5zuS.hZBimuJETKsBVLj0.1yW', 'medical_doctor', 2, 0),
	('41602291', 'Tomás Benítez', '$2b$12$t.Bv6gRSfll5b1P7CRbc8eaGptQEDHm6X0nLpu/VkUPUL6QtVFg0q', 'medical_doctor', 2, 0),
	('43433004', 'Sofía López', '$2b$12$tBgU20jYKrI5FyWkmoGQKO8tXuiufkgQS7e697syxPDZDUqFGcPMK', 'medical_doctor', 2, 0),
	('44177853', 'María Vera', '$2b$12$UHp4ksb9JEKgK2H5YC7T..yHtYGDVghcPCdsLjvU.wRJbdMQ.AYXa', 'medical_doctor', 2, 0),
	('45103885', 'Jose Perez', '$2b$12$BFMi2DAko7JWkrMgX2Bmy.aJLsObbd2ui0h.iOMNfz3ThgW9Qcdqq', 'administrator', 1, 0),
	('45621231', 'Travieso Cristhofer ', '$2b$12$bj5C5Vzjt3LexbwJnmUDIeT8iaZ1e/WpOCUeFR9vNIlQoSor4U146', 'medical_doctor', 1, 0),
	('49057888', 'Marta Hernadez', '$2b$12$boPfeNzUz9hxE0BERGMqOOky1lHPQL1t5UjozRaKCa5yLvXl/Ku8i', 'administrator', 1, 0),
	('53844853', 'Nahuel Galeano', '$2b$12$z8NmcyAKmx9z6ZNmerGhnO8pO50.E8RHM6wdmsuapNVCIkKJ2rFUy', 'administrator', 2, 0),
	('56594974', 'Luciano Olivera', '$2b$12$7eCEoFb3CONE5QpJCy9zqOjdF/3QZTQ.CIsEt1yd1nsBA4YSB0AP6', 'administrator', 2, 0),
	('57447572', 'Paula Gómez', '$2b$12$XfhjlbvYmzHv/3fVdFptYuE1l.ggUvFB0OPQ4bvAx4CYi9iHm.vRm', 'medical_doctor', 2, 0),
	('59692727', 'David Cardozo', '$2b$12$cFOLQIuI.dqWqlXmRDZXLuL33aE7MEpGMC71YtPe.FHPgRAJi9djK', 'administrator', 2, 0),
	('61836581', 'Alberto Rodríguez', '$2b$12$nQlrr/jNy6NALMgQo8Zqeu/bbDvl5NwkM4EkZPmoTCQ5BTA5Ubpq6', 'medical_doctor', 2, 0),
	('62659542', 'Alberto Núñez', '$2b$12$2Nk.Da4opaDdxLfx93EBkOilt/0vvfp0aWwBVbbHFZkcOXnOr2Y4G', 'medical_doctor', 1, 0),
	('62836582', 'Alberto Rodríguez', '$2b$12$/fkOh3ChTXyj2CZZtb1i6umzmZuH4KSRsg6h6gbc228AutHebPEnW', 'medical_doctor', 1, 0),
	('64782951', 'Juan Gomez', '$2b$12$koKMtdd07eVhSJGWn0IxReGINZM1jVlR8css4XLy8sb5QCnHs/nFi', 'administrator', 1, 0),
	('72400460', 'Vanesa Ortiz', '$2b$12$i4gbK2D0kfJ5erPbjTSXfeHTPsCE8Sm4fxIfMOJ9rLI0oY0vC3ecK', 'administrator', 2, 0),
	('72581357', 'Luis Rojas', '$2b$12$Ip0iHR84h5RGLuQSJLd8V.UuvH2jHwTGVWBez7P3/yTxCmncuGV7q', 'medical_doctor', 1, 0),
	('76434077', 'Elena Villalba', '$2b$12$m0dH5AMM00kb0eFImlDZGOBqvt8cu/ajsrAcQIUe9yRoG1./QeJdO', 'medical_doctor', 2, 0),
	('77696777', 'Ana Gonzalez', '$2b$12$d0q84ui6rNvjYEfoHZuBjuO6fHnrWsgbmZilmowefPCHGKmii0F8S', 'administrator', 1, 0),
	('87575193', 'Valentina Acosta', '$2b$12$Ywmm8KpkyDg0u.rZTxKo2.DHCB9Bqr.Z2d6J1gt92Yw6.imXoSlz2', 'medical_doctor', 2, 0),
	('88203111', 'Zoe Ortiz', '$2b$12$vPEt17WXukZ.mgeTJtl8Eu3dPCh2303X11yKzJGYDEFq1ZzGiWDIW', 'medical_doctor', 2, 0),
	('88437665', 'Ana Gomez', '$2b$12$3a025FROGReYlLK3EPjfH.PxYiU6/I5oJnh9QeDfCAmneMvnhMRCG', 'administrator', 2, 0),
	('89277357', 'Nicolas Rojas', '$2b$12$Q1w.eLYaAeQ1ulJNhq57y.HAjrGX4FZmM2UYGoNA2zcLTvaJFlEi2', 'medical_doctor', 2, 0),
	('90017536', 'Miguel Báez', '$2b$12$WskJhzLRXEMisQimjTlLleeMz3jMZswS/cAdt05xxYaad6706p2iG', 'medical_doctor', 1, 0),
	('90810255', 'Emilia Fernández', '$2b$12$dkYGLca88NGhtvhFt1JjQuc58PdnVd4eT96WNCNU7xk4uwDsR8gdK', 'medical_doctor', 2, 0),
	('95648031', 'Pedro gutierrez', '$2b$12$yqmTHOlT5x6b.BzbKIWsyu/on1lgap2mrv8gY1UxldHkgI6qTikPy', 'administrator', 1, 0),
	('95763255', 'Lucía Duarte', '$2b$12$1IyOZ4tg14rFwKgnuCesv.Ip3Sq0aF9PKtTk/qlot4SZjsbFM6Gnu', 'medical_doctor', 2, 0),
	('95806392', 'Antonela Rojas', '$2b$12$48EA/4yfMrQqFf52mnDbDebhNZMsJa0Wrmrf0hMVBpUl7ttuWSwU2', 'administrator', 2, 0),
	('98484268', 'Nicolas Ortiz', '$2b$12$Omu6OaZBRMbOjL2/kp2fnuZzJx5AkjEwAUTIYaD9hEYYZJA4gst2.', 'medical_doctor', 1, 0),
	('98528581', 'Miguel Báez', '$2b$12$9DkvuvaaoYqSpqBmYtIb4uLGGbz30F9dfs6sBJdjKCSeXaUH19s.K', 'medical_doctor', 2, 0),
	('98765431', 'Juan Perez', '$2b$12$A0tq/nQuH/K3VetvTtXqf.FGwjq.0qj/K6.sKXhlHksvU2c.MPGOe', 'administrator', 1, 0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

-- Dumping data for table sggdb.zone: ~3 rows (approximately)
DELETE FROM `zone`;
/*!40000 ALTER TABLE `zone` DISABLE KEYS */;
INSERT INTO `zone` (`id`, `name`, `geotag`, `longitude`, `latitude`, `institution_id`, `deleted`) VALUES
	(1, 'z1', '0', '0', '0', 1, 0),
	(2, 'Centro', 'a', '645342312', '12324354', 2, 0),
	(3, 'Posito', 'geotag', '3156697089', '335590445', 2, 0),
	(4, 'Prado', '', '', '', 1, 0),
	(5, 'Aguada', '', '', '', 1, 0);
/*!40000 ALTER TABLE `zone` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
