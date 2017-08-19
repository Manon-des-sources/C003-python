# 一、python的变量名只是内存的标签<br>
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
变量名second 就从"Mrs.Morvon"这个内存上被撕掉，转而贴到另一个内存(其中存放了另一个字符串"Mrs.Tysick")<br>
<br>
换句话说、给变量名second 赋予新值的过程是：<br>
先在内存中先创建这个新值<br>
再将second 移到/贴到这个内存上<br>
<br>
在下面这个过程中、second 也是从原来的内存移到新的内存：<br>
```javascript
second = 7
second = second + 1
```
过程中创建了一个新值(7 + 1 = 8)、并放在一个新的内存中，然后将second 移到这个新的内存位置<br>
<br>
如果一个内存没有任何标签(全被移走了)、这个内存就会被释放，我们不再能访问该内存中的内容了、python会自动清理这种内存<br>
只有贴有标签、有变量名的内存才是可访问的<br>