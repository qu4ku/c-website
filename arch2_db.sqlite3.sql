BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `title` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`	varchar ( 100 ) NOT NULL,
	`slug`	varchar ( 50 ) NOT NULL UNIQUE
);
INSERT INTO `title` VALUES (1,'Bitcoin','Bitcoin');
INSERT INTO `title` VALUES (2,'Blockchain','Blockchain');
INSERT INTO `title` VALUES (3,'Cyberpunk','cyberpunk');
INSERT INTO `title` VALUES (4,'Fiat','fiat');
CREATE TABLE IF NOT EXISTS `posts_categories` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`post_id`	integer NOT NULL,
	`category_id`	integer NOT NULL,
	FOREIGN KEY(`post_id`) REFERENCES `posts`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`category_id`) REFERENCES `title`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `posts_categories` VALUES (7,11,3);
INSERT INTO `posts_categories` VALUES (8,12,1);
INSERT INTO `posts_categories` VALUES (9,12,2);
INSERT INTO `posts_categories` VALUES (10,13,1);
INSERT INTO `posts_categories` VALUES (11,13,3);
INSERT INTO `posts_categories` VALUES (12,12,4);
INSERT INTO `posts_categories` VALUES (13,11,1);
INSERT INTO `posts_categories` VALUES (14,11,2);
INSERT INTO `posts_categories` VALUES (15,14,2);
INSERT INTO `posts_categories` VALUES (16,14,3);
CREATE TABLE IF NOT EXISTS `posts` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`slug`	varchar ( 200 ) NOT NULL,
	`url`	varchar ( 250 ) NOT NULL,
	`description`	text,
	`tease`	text NOT NULL,
	`status`	integer NOT NULL,
	`publish`	datetime NOT NULL,
	`created`	datetime NOT NULL,
	`modified`	datetime NOT NULL,
	`original_author`	varchar ( 250 ) NOT NULL,
	`original_author_handle`	varchar ( 250 ) NOT NULL,
	`original_author_url`	varchar ( 250 ) NOT NULL,
	`author_id`	integer,
	`difficulty_level_id`	integer NOT NULL,
	`post_type_id`	integer NOT NULL,
	`seo_text`	text,
	`set_number`	varchar ( 2 ) NOT NULL,
	`thumb_image`	varchar ( 100 ) NOT NULL,
	`active`	integer NOT NULL,
	`title`	varchar ( 280 ) NOT NULL,
	FOREIGN KEY(`difficulty_level_id`) REFERENCES `pages_difficultylevel`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`post_type_id`) REFERENCES `pages_posttype`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`author_id`) REFERENCES `auth_user`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `posts` VALUES (11,'cyberpunk','https://twitter.com/andrestaltz/status/970297316631568384','','',1,'2018-03-04 16:06:37','2018-03-04 16:08:04.657680','2018-03-12 19:26:50.841708','André Staltz','@andrestaltz','https://twitter.com/andrestaltz',NULL,3,1,'','33','',1,'I believe we are currently living the short period that preceeds a full cyberpunk-esque setting.  Common themes from 3 seminal Cyberpunk novels are starting to be seen in real life');
INSERT INTO `posts` VALUES (12,'crypto-is-hareder','https://bitcoinschannel.com/cryptocurrency-is-harder-to-launder-than-fiat-currency/','Bitcoin is a tool for terrorists and money launderers. At least that’s what your elected officials believe. When western leaders are pressed for their thoughts on cryptocurrency, that’s invariably the first sound bite to leave their lips, followed, occasionally, by a begrudging acknowledgement that “the underlying blockchain technology has potential”.','',1,'2018-03-04 16:18:17','2018-03-04 16:20:23.802817','2018-03-12 19:26:26.579250','','','',NULL,3,2,'','23','',1,'Cryptocurrency Is Harder to Launder Than Fiat Currency');
INSERT INTO `posts` VALUES (13,'dag','https://www.youtube.com/watch?v=lfgMnbb5JeM','','',1,'2018-03-04 16:20:50','2018-03-04 16:21:43.156688','2018-03-04 16:22:44.921311','','','',NULL,2,3,'','13','thumbs/vid-temp-img.png',1,'Bitcoin Q&A: Directed acyclic graphs (DAGs) and IOTA');
INSERT INTO `posts` VALUES (14,'getting-applications','https://a16z.com/2017/09/14/networks-protocols-labs-tokens/','','',1,'2018-03-13 16:18:15','2018-03-13 16:19:33.683147','2018-03-13 16:19:33.683165','','','',NULL,2,4,'','14','',1,'Getting applications into people’s hands');
CREATE TABLE IF NOT EXISTS `pages_posttype` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`post_type`	integer NOT NULL
);
INSERT INTO `pages_posttype` VALUES (1,1);
INSERT INTO `pages_posttype` VALUES (2,0);
INSERT INTO `pages_posttype` VALUES (3,2);
INSERT INTO `pages_posttype` VALUES (4,3);
CREATE TABLE IF NOT EXISTS `pages_link` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`ip`	varchar ( 50 ),
	`url`	varchar ( 250 ) NOT NULL
);
CREATE TABLE IF NOT EXISTS `pages_difficultylevel` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`dificulty_level`	integer NOT NULL
);
INSERT INTO `pages_difficultylevel` VALUES (1,0);
INSERT INTO `pages_difficultylevel` VALUES (2,2);
INSERT INTO `pages_difficultylevel` VALUES (3,1);
CREATE TABLE IF NOT EXISTS `django_session` (
	`session_key`	varchar ( 40 ) NOT NULL,
	`session_data`	text NOT NULL,
	`expire_date`	datetime NOT NULL,
	PRIMARY KEY(`session_key`)
);
INSERT INTO `django_session` VALUES ('b3ih7nxap90073galpi4m8ylisxpo01m','YjRjMTZkYjcxZGYwYThiNTAwOTk5OWI2ZThjMGU0ZjM3ZTk1MDYxMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OWM5ZGM3ZmYxMWFmYjJiNWYxMGZkNzZjNGYwMGQ5MTJlN2U2NDk3In0=','2018-03-18 15:42:24.809796');
CREATE TABLE IF NOT EXISTS `django_migrations` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app`	varchar ( 255 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	`applied`	datetime NOT NULL
);
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-02-23 20:05:23.228182');
INSERT INTO `django_migrations` VALUES (2,'auth','0001_initial','2018-02-23 20:05:23.266096');
INSERT INTO `django_migrations` VALUES (3,'admin','0001_initial','2018-02-23 20:05:23.277539');
INSERT INTO `django_migrations` VALUES (4,'admin','0002_logentry_remove_auto_add','2018-02-23 20:05:23.288256');
INSERT INTO `django_migrations` VALUES (5,'contenttypes','0002_remove_content_type_name','2018-02-23 20:05:23.307193');
INSERT INTO `django_migrations` VALUES (6,'auth','0002_alter_permission_name_max_length','2018-02-23 20:05:23.316517');
INSERT INTO `django_migrations` VALUES (7,'auth','0003_alter_user_email_max_length','2018-02-23 20:05:23.331295');
INSERT INTO `django_migrations` VALUES (8,'auth','0004_alter_user_username_opts','2018-02-23 20:05:23.346687');
INSERT INTO `django_migrations` VALUES (9,'auth','0005_alter_user_last_login_null','2018-02-23 20:05:23.358940');
INSERT INTO `django_migrations` VALUES (10,'auth','0006_require_contenttypes_0002','2018-02-23 20:05:23.362027');
INSERT INTO `django_migrations` VALUES (11,'auth','0007_alter_validators_add_error_messages','2018-02-23 20:05:23.374311');
INSERT INTO `django_migrations` VALUES (12,'auth','0008_alter_user_username_max_length','2018-02-23 20:05:23.386581');
INSERT INTO `django_migrations` VALUES (13,'auth','0009_alter_user_last_name_max_length','2018-02-23 20:05:23.398836');
INSERT INTO `django_migrations` VALUES (14,'pages','0001_initial','2018-02-23 20:05:23.434714');
INSERT INTO `django_migrations` VALUES (15,'sessions','0001_initial','2018-02-23 20:05:23.438731');
INSERT INTO `django_migrations` VALUES (16,'pages','0002_auto_20180225_1514','2018-02-25 15:14:46.862980');
INSERT INTO `django_migrations` VALUES (17,'pages','0003_auto_20180225_1947','2018-02-25 19:47:27.978865');
INSERT INTO `django_migrations` VALUES (18,'pages','0004_auto_20180225_1953','2018-02-25 19:54:11.544952');
INSERT INTO `django_migrations` VALUES (19,'pages','0005_auto_20180306_2334','2018-03-06 23:34:32.108777');
INSERT INTO `django_migrations` VALUES (20,'pages','0006_auto_20180313_1617','2018-03-13 16:17:35.296621');
CREATE TABLE IF NOT EXISTS `django_content_type` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app_label`	varchar ( 100 ) NOT NULL,
	`model`	varchar ( 100 ) NOT NULL
);
INSERT INTO `django_content_type` VALUES (1,'admin','logentry');
INSERT INTO `django_content_type` VALUES (2,'auth','permission');
INSERT INTO `django_content_type` VALUES (3,'auth','group');
INSERT INTO `django_content_type` VALUES (4,'auth','user');
INSERT INTO `django_content_type` VALUES (5,'contenttypes','contenttype');
INSERT INTO `django_content_type` VALUES (6,'sessions','session');
INSERT INTO `django_content_type` VALUES (7,'pages','category');
INSERT INTO `django_content_type` VALUES (8,'pages','difficultylevel');
INSERT INTO `django_content_type` VALUES (9,'pages','post');
INSERT INTO `django_content_type` VALUES (10,'pages','posttype');
INSERT INTO `django_content_type` VALUES (11,'pages','link');
CREATE TABLE IF NOT EXISTS `django_admin_log` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`object_id`	text,
	`object_repr`	varchar ( 200 ) NOT NULL,
	`action_flag`	smallint unsigned NOT NULL,
	`change_message`	text NOT NULL,
	`content_type_id`	integer,
	`user_id`	integer NOT NULL,
	`action_time`	datetime NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `django_admin_log` VALUES (1,'1','Bitcoin',1,'[{"added": {}}]',7,1,'2018-02-25 15:17:11.998741');
INSERT INTO `django_admin_log` VALUES (2,'1','Beginner',1,'[{"added": {}}]',8,1,'2018-02-25 15:17:20.994109');
INSERT INTO `django_admin_log` VALUES (3,'1','Twitter',1,'[{"added": {}}]',10,1,'2018-02-25 15:17:28.891473');
INSERT INTO `django_admin_log` VALUES (4,'1','How Newsweek Collapsed',1,'[{"added": {}}]',9,1,'2018-02-25 15:19:00.481112');
INSERT INTO `django_admin_log` VALUES (5,'1','How Newsweek Collapsed',2,'[{"changed": {"fields": ["status"]}}]',9,1,'2018-02-25 15:19:29.006784');
INSERT INTO `django_admin_log` VALUES (6,'1','How Newsweek Collapsed',2,'[{"changed": {"fields": ["author"]}}]',9,1,'2018-02-25 18:09:44.113704');
INSERT INTO `django_admin_log` VALUES (7,'2','Blockchain',1,'[{"added": {}}]',7,1,'2018-02-25 19:45:37.260999');
INSERT INTO `django_admin_log` VALUES (8,'2','Advanced',1,'[{"added": {}}]',8,1,'2018-02-25 19:45:46.798142');
INSERT INTO `django_admin_log` VALUES (9,'2','Article',1,'[{"added": {}}]',10,1,'2018-02-25 19:45:53.455534');
INSERT INTO `django_admin_log` VALUES (10,'2','The Costs Of Camouflaging Autism',1,'[{"added": {}}]',9,1,'2018-02-25 19:46:10.743842');
INSERT INTO `django_admin_log` VALUES (11,'2','The Costs Of Camouflaging Autism',2,'[{"changed": {"fields": ["publish"]}}]',9,1,'2018-02-25 19:57:54.774223');
INSERT INTO `django_admin_log` VALUES (12,'4','some',2,'[{"changed": {"fields": ["status"]}}]',9,1,'2018-02-26 21:32:05.081068');
INSERT INTO `django_admin_log` VALUES (13,'3','Intermediate',1,'[{"added": {}}]',8,1,'2018-02-27 15:20:10.946983');
INSERT INTO `django_admin_log` VALUES (14,'3','Video',1,'[{"added": {}}]',10,1,'2018-02-27 15:20:23.807740');
INSERT INTO `django_admin_log` VALUES (15,'7','Why you should NEVER Day Trade',3,'',9,1,'2018-02-27 15:27:42.027947');
INSERT INTO `django_admin_log` VALUES (16,'8','Why you should NEVER Day Trade',2,'[{"changed": {"fields": ["status", "thumb_image"]}}]',9,1,'2018-02-27 15:28:09.462139');
INSERT INTO `django_admin_log` VALUES (17,'10','video test',1,'[{"added": {}}]',9,1,'2018-03-04 15:44:10.753371');
INSERT INTO `django_admin_log` VALUES (18,'10','video test',3,'',9,1,'2018-03-04 16:03:58.518891');
INSERT INTO `django_admin_log` VALUES (19,'2','The Costs Of Camouflaging Autism',3,'',9,1,'2018-03-04 16:03:58.536057');
INSERT INTO `django_admin_log` VALUES (20,'9','new one',3,'',9,1,'2018-03-04 16:03:58.552438');
INSERT INTO `django_admin_log` VALUES (21,'8','Why you should NEVER Day Trade',3,'',9,1,'2018-03-04 16:03:58.567079');
INSERT INTO `django_admin_log` VALUES (22,'6','some title',3,'',9,1,'2018-03-04 16:03:58.582021');
INSERT INTO `django_admin_log` VALUES (23,'5','second one',3,'',9,1,'2018-03-04 16:03:58.597135');
INSERT INTO `django_admin_log` VALUES (24,'3','In China’s Hinterlands, Workers Mine Bitcoin for a Digital Fortune',3,'',9,1,'2018-03-04 16:03:58.614435');
INSERT INTO `django_admin_log` VALUES (25,'1','How Newsweek Collapsed',3,'',9,1,'2018-03-04 16:03:58.629877');
INSERT INTO `django_admin_log` VALUES (26,'3','Cyberpunk',1,'[{"added": {}}]',7,1,'2018-03-04 16:07:19.952631');
INSERT INTO `django_admin_log` VALUES (27,'11','I believe we are currently living the short period that preceeds a full cyberpunk-esque setting.  Common themes from 3 seminal Cyberpunk novels are starting to be seen in real life',1,'[{"added": {}}]',9,1,'2018-03-04 16:08:04.699743');
INSERT INTO `django_admin_log` VALUES (28,'11','I believe we are currently living the short period that preceeds a full cyberpunk-esque setting.  Common themes from 3 seminal Cyberpunk novels are starting to be seen in real life',2,'[{"changed": {"fields": ["set_number"]}}]',9,1,'2018-03-04 16:18:14.022042');
INSERT INTO `django_admin_log` VALUES (29,'12','Cryptocurrency Is Harder to Launder Than Fiat Currency',1,'[{"added": {}}]',9,1,'2018-03-04 16:20:23.843003');
INSERT INTO `django_admin_log` VALUES (30,'13','Bitcoin Q&A: Directed acyclic graphs (DAGs) and IOTA',1,'[{"added": {}}]',9,1,'2018-03-04 16:21:43.210355');
INSERT INTO `django_admin_log` VALUES (31,'13','Bitcoin Q&A: Directed acyclic graphs (DAGs) and IOTA',2,'[{"changed": {"fields": ["set_number"]}}]',9,1,'2018-03-04 16:22:44.939323');
INSERT INTO `django_admin_log` VALUES (32,'12','Cryptocurrency Is Harder to Launder Than Fiat Currency',2,'[{"changed": {"fields": ["set_number"]}}]',9,1,'2018-03-04 16:23:05.897948');
INSERT INTO `django_admin_log` VALUES (33,'4','Fiat',1,'[{"added": {}}]',7,1,'2018-03-12 19:26:20.638917');
INSERT INTO `django_admin_log` VALUES (34,'12','Cryptocurrency Is Harder to Launder Than Fiat Currency',2,'[{"changed": {"fields": ["categories"]}}]',9,1,'2018-03-12 19:26:26.619379');
INSERT INTO `django_admin_log` VALUES (35,'11','I believe we are currently living the short period that preceeds a full cyberpunk-esque setting.  Common themes from 3 seminal Cyberpunk novels are starting to be seen in real life',2,'[{"changed": {"fields": ["categories"]}}]',9,1,'2018-03-12 19:26:50.877197');
INSERT INTO `django_admin_log` VALUES (36,'4','Podcast',1,'[{"added": {}}]',10,1,'2018-03-13 16:17:52.489168');
INSERT INTO `django_admin_log` VALUES (37,'14','Getting applications into people’s hands',1,'[{"added": {}}]',9,1,'2018-03-13 16:19:33.715912');
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`) DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`group_id`	integer NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`) DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS `auth_user` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`password`	varchar ( 128 ) NOT NULL,
	`last_login`	datetime,
	`is_superuser`	bool NOT NULL,
	`username`	varchar ( 150 ) NOT NULL UNIQUE,
	`first_name`	varchar ( 30 ) NOT NULL,
	`email`	varchar ( 254 ) NOT NULL,
	`is_staff`	bool NOT NULL,
	`is_active`	bool NOT NULL,
	`date_joined`	datetime NOT NULL,
	`last_name`	varchar ( 150 ) NOT NULL
);
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$z2cRiBTIeD4o$BuJFBJDm5YvkqhY/nCffp6XcfaXJIPPG7B26XklJBqU=','2018-03-04 15:42:24.789493',1,'admin','','',1,1,'2018-02-23 20:06:36.471086','');
CREATE TABLE IF NOT EXISTS `auth_permission` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`content_type_id`	integer NOT NULL,
	`codename`	varchar ( 100 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO `auth_permission` VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO `auth_permission` VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO `auth_permission` VALUES (4,2,'add_permission','Can add permission');
INSERT INTO `auth_permission` VALUES (5,2,'change_permission','Can change permission');
INSERT INTO `auth_permission` VALUES (6,2,'delete_permission','Can delete permission');
INSERT INTO `auth_permission` VALUES (7,3,'add_group','Can add group');
INSERT INTO `auth_permission` VALUES (8,3,'change_group','Can change group');
INSERT INTO `auth_permission` VALUES (9,3,'delete_group','Can delete group');
INSERT INTO `auth_permission` VALUES (10,4,'add_user','Can add user');
INSERT INTO `auth_permission` VALUES (11,4,'change_user','Can change user');
INSERT INTO `auth_permission` VALUES (12,4,'delete_user','Can delete user');
INSERT INTO `auth_permission` VALUES (13,5,'add_contenttype','Can add content type');
INSERT INTO `auth_permission` VALUES (14,5,'change_contenttype','Can change content type');
INSERT INTO `auth_permission` VALUES (15,5,'delete_contenttype','Can delete content type');
INSERT INTO `auth_permission` VALUES (16,6,'add_session','Can add session');
INSERT INTO `auth_permission` VALUES (17,6,'change_session','Can change session');
INSERT INTO `auth_permission` VALUES (18,6,'delete_session','Can delete session');
INSERT INTO `auth_permission` VALUES (19,7,'add_category','Can add category');
INSERT INTO `auth_permission` VALUES (20,7,'change_category','Can change category');
INSERT INTO `auth_permission` VALUES (21,7,'delete_category','Can delete category');
INSERT INTO `auth_permission` VALUES (22,8,'add_difficultylevel','Can add difficulty level');
INSERT INTO `auth_permission` VALUES (23,8,'change_difficultylevel','Can change difficulty level');
INSERT INTO `auth_permission` VALUES (24,8,'delete_difficultylevel','Can delete difficulty level');
INSERT INTO `auth_permission` VALUES (25,9,'add_post','Can add post');
INSERT INTO `auth_permission` VALUES (26,9,'change_post','Can change post');
INSERT INTO `auth_permission` VALUES (27,9,'delete_post','Can delete post');
INSERT INTO `auth_permission` VALUES (28,10,'add_posttype','Can add post type');
INSERT INTO `auth_permission` VALUES (29,10,'change_posttype','Can change post type');
INSERT INTO `auth_permission` VALUES (30,10,'delete_posttype','Can delete post type');
INSERT INTO `auth_permission` VALUES (31,11,'add_link','Can add link');
INSERT INTO `auth_permission` VALUES (32,11,'change_link','Can change link');
INSERT INTO `auth_permission` VALUES (33,11,'delete_link','Can delete link');
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`group_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`) DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS `auth_group` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 80 ) NOT NULL UNIQUE
);
CREATE INDEX IF NOT EXISTS `posts_slug_f697e400` ON `posts` (
	`slug`
);
CREATE INDEX IF NOT EXISTS `posts_post_type_id_43165ea1` ON `posts` (
	`post_type_id`
);
CREATE INDEX IF NOT EXISTS `posts_difficulty_level_id_7dd9dc9c` ON `posts` (
	`difficulty_level_id`
);
CREATE UNIQUE INDEX IF NOT EXISTS `posts_categories_post_id_category_id_310be74c_uniq` ON `posts_categories` (
	`post_id`,
	`category_id`
);
CREATE INDEX IF NOT EXISTS `posts_categories_post_id_99568311` ON `posts_categories` (
	`post_id`
);
CREATE INDEX IF NOT EXISTS `posts_categories_category_id_706646cf` ON `posts_categories` (
	`category_id`
);
CREATE INDEX IF NOT EXISTS `posts_author_id_099b8aca` ON `posts` (
	`author_id`
);
CREATE INDEX IF NOT EXISTS `django_session_expire_date_a5c62663` ON `django_session` (
	`expire_date`
);
CREATE UNIQUE INDEX IF NOT EXISTS `django_content_type_app_label_model_76bd3d3b_uniq` ON `django_content_type` (
	`app_label`,
	`model`
);
CREATE INDEX IF NOT EXISTS `django_admin_log_user_id_c564eba6` ON `django_admin_log` (
	`user_id`
);
CREATE INDEX IF NOT EXISTS `django_admin_log_content_type_id_c4bce8eb` ON `django_admin_log` (
	`content_type_id`
);
CREATE UNIQUE INDEX IF NOT EXISTS `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` ON `auth_user_user_permissions` (
	`user_id`,
	`permission_id`
);
CREATE INDEX IF NOT EXISTS `auth_user_user_permissions_user_id_a95ead1b` ON `auth_user_user_permissions` (
	`user_id`
);
CREATE INDEX IF NOT EXISTS `auth_user_user_permissions_permission_id_1fbb5f2c` ON `auth_user_user_permissions` (
	`permission_id`
);
CREATE UNIQUE INDEX IF NOT EXISTS `auth_user_groups_user_id_group_id_94350c0c_uniq` ON `auth_user_groups` (
	`user_id`,
	`group_id`
);
CREATE INDEX IF NOT EXISTS `auth_user_groups_user_id_6a12ed8b` ON `auth_user_groups` (
	`user_id`
);
CREATE INDEX IF NOT EXISTS `auth_user_groups_group_id_97559544` ON `auth_user_groups` (
	`group_id`
);
CREATE UNIQUE INDEX IF NOT EXISTS `auth_permission_content_type_id_codename_01ab375a_uniq` ON `auth_permission` (
	`content_type_id`,
	`codename`
);
CREATE INDEX IF NOT EXISTS `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (
	`content_type_id`
);
CREATE INDEX IF NOT EXISTS `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (
	`permission_id`
);
CREATE UNIQUE INDEX IF NOT EXISTS `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `auth_group_permissions` (
	`group_id`,
	`permission_id`
);
CREATE INDEX IF NOT EXISTS `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (
	`group_id`
);
COMMIT;
