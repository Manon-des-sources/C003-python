# 一、while 循环如何工作
## 1、range()不能用在while 循环
* 因为while 循环不是迭代器，而是条件判断  
* 所以每次调用rang() 时都会得到其中的第一个元素、而不会迭代  
* 可以使用break 和continue 语句  
