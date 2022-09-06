-- Move DB, table and field to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE second_table MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci;
