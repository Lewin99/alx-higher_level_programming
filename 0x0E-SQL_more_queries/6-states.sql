-- database and table with multiple constraints
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
ICREATE TABLE IF NOT EXISTS `states` (`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,`name` VARCHAR(256) NOT NULL);
