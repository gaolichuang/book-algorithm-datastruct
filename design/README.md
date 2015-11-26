# VII.Design

Object-Oriented Design

##Question
##### 1.[G]贪吃蛇
##### 2.贪吃蛇AI
http://pyroc.at/blog/2013/04/26/snake-ai/
http://blog.csdn.net/fox64194167/article/details/19965069
##### 3.[G]如何提高后端server整体吞吐量
> backend server就1个， 100qps 的服务能力  
> 多个client访问， 如何提高backend server 服务吞吐

问题分析：
  -  server服务能力过载时该如何？
     - 如何告知client发送request减缓？
     - 多个client该服务哪个？
  -  server的服务能力没到阈值，或者说client的request过慢，该怎么办？