-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 (localhost)
SET @grants_1 = COALESCE((SELECT CONCAT('SHOW GRANTS FOR ''user_0d_1''@''', Host, '''') FROM mysql.user WHERE User = 'user_0d_1' ORDER BY Host = 'localhost' DESC LIMIT 1), 'SHOW GRANTS FOR ''user_0d_1''@''localhost''');
PREPARE stmt_1 FROM @grants_1;
EXECUTE stmt_1;
DEALLOCATE PREPARE stmt_1;
SET @grants_2 = COALESCE((SELECT CONCAT('SHOW GRANTS FOR ''user_0d_2''@''', Host, '''') FROM mysql.user WHERE User = 'user_0d_2' ORDER BY Host = 'localhost' DESC LIMIT 1), 'SHOW GRANTS FOR ''user_0d_2''@''localhost''');
PREPARE stmt_2 FROM @grants_2;
EXECUTE stmt_2;
DEALLOCATE PREPARE stmt_2;
