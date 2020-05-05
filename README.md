# daily_health_report
**必须先使用浏览器（Chrome或其他支持网络调试的浏览器）** 手动打卡一次获取Cookie和表单数据。
<br />

1. 直接访问https://wxxy.csu.edu.cn/ncov/wap/default/save 跳转登录界面，登录成功后进入每日打卡。

2. **F12（Chrome浏览器）打开网络调试**，获取位置信息后提交打卡数据，点开包含 https://wxxy.csu.edu.cn/ncov/wap/default/save 的请求，复制`Request Header`中的 `Cookie`字段，和`Request PayLoad`中类似如下格式的数据：

```
jcjgqr=0&sffdypz=0&zybj=&dzjkmys=3&id=5048756&jcbhrq=&jcwhryfs=&tw=3&wjtw=&jhfjhbcc=&glksrq=&sfjcbh=0&created=1588475919&province=广东省
&gtjzzfjsj=&bztcyy=&date=20200503&dqszyqfxdj=3&szgjcs=&sfcxzysx=0&sfcyglq=0..........
```

3. 将`main.py`中的`cookie`设置为第2步中复制的`Cookie`.

4. 删除第2步复制的数据中的 `&date=20200503`和`&created=1588475919`,并将`main.py`中的`msg`设置为该值(替换`your_post_data`).

5. 一键打卡: 打开windows/linux命令行，运行 `python3 main.py` .

6. 定时打卡(以linux为例):
* 在命令行输入
```
crontab -e 
```
* 为了在每天的14：00 定时打卡，可以在文件末尾添加以下内容: 
```
0 0 14 * * python3 your_directory/main.py
```



enjoy！
