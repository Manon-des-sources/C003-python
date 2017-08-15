一、python的变量名只是内存的标签<br>
如：<br>
```javascript
first  = "Mrs.Morvon"
second = first
```
此时的first 和second 分别指向了同一个内存单元，其中存放了一个字符串。<br>
而修改了second之后：<br>
```javascript
second = "Mrs.Tysick"
```
变量名second 就从"Mrs.Morvon"这个内存上被撕掉，转而贴到另一个内存(其中存放了另一个字符串"Mrs.Tysick")。<br>