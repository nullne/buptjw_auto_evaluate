buptjw_auto_evaluate
====================

BUPT 教务系统教师评测快速完成

目前的功能是输入学号，教务系统密码，通用评论，通用等级（1-8，1是最高评价，依次降低），然后快速评论给每一位老师
需要bs4, requests两个python lib 的支持

本程序借鉴hansnow同学的代码，在此谢过。
相比较原程序有以下更新：
  1.采用系统自身编码，省去不同系统默认编码方式不同而导致乱码等的麻烦
  2.采用requests 库，urllib,urllib2 真心看的0碎了
  3.加入一些简单的错误处理功能

TODO： 实现远程调用，省去安装库，甚至安装python的麻烦。但是远程调用对于用户密码不安全
P.S. http://nullne.com/autoEvaluate.html 附有心得，也是第一次练手，望轻拍


<a href="https://cla-assistant.io/nullne/buptjw_auto_evaluate"><img src="https://cla-assistant.io/readme/badge/nullne/buptjw_auto_evaluate" alt="CLA assistant" /></a>
