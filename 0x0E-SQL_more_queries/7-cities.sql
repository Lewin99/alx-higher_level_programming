-- got foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (`id` INT NOT NULL FOREIGN KEY,`name` VARCHAR(256));
