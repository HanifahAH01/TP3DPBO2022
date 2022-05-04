/*
Navicat MySQL Data Transfer

Source Server         : MyKomeksi
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : db_tp3dpbo

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2022-05-03 22:28:52
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `mahasiswa`
-- ----------------------------
DROP TABLE IF EXISTS `mahasiswa`;
CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nim` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jurusan` varchar(255) NOT NULL,
  `jenins_kelamin` varchar(255) NOT NULL,
  `Hobi` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of mahasiswa
-- ----------------------------
INSERT INTO `mahasiswa` VALUES ('1', '2000152', 'Hanifah', 'Sastra Mesin', 'Perempuan', 'Bernyanyi');
INSERT INTO `mahasiswa` VALUES ('2', '5210002', 'Humaira', 'Filsafat Meme', 'Perempuan', 'Main Game');
