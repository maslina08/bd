CREATE TABLE `medals`.`athletes` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `nationality` VARCHAR(45) NULL,
  `sex` VARCHAR(45) NULL,
  `dob` VARCHAR(45) NULL,
  `height` DOUBLE NULL,
  `weight` DOUBLE NULL,
  `sport` VARCHAR(45) NULL,
  `gold` INT NULL,
  `silver` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `medals`.`countries` (
  `country` VARCHAR(45)  NULL,
  `code` VARCHAR(45)  NULL,
  `population` INT  NULL,
  `gpd_per_capita` VARCHAR(45)  NULL
  );


CREATE TABLE `medals`.`events` (
  `id` INT NOT NULL,
  `sport` VARCHAR(45) NULL,
  `discipline` VARCHAR(45) NULL,
  `name` VARCHAR(45) NULL,
  `sex` VARCHAR(45) NULL,
  `venues` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
