# Get-copper-price
工作需要每天打开有色金属网取得相关数据进行计算成本，运行之后会在目录下面生成两个excel文件
代码贡献 来自 吾爱破解论坛@ciker_li 。  
用到库 requests ， BeautifulSoup 4 ，xlwt  
用pyinstall 命令可以打包；  
如果打包完成提示缺少模块，参考以下方法:  
1.设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.  
2.也可以使用多个-p参数来设置多个导入路径；   
然后我找到bs4模块所在的目录E:\python\clpicdownload\venv\Lib\site-packages，路径的查找的方法是:
用pycharm打开工程，菜单->setting->project->project Interpreter，把鼠标点到你想要包含的插件上，hint显示的就是所在目录

然后用pyinstaller -F -p E:\python\clpicdownload\venv\Lib\site-packages mypython.py这个命令打包，  
如果要包含多个目录，那就用分号隔开如：pyinstaller -F -p E:\python\clpicdownload\venv\Lib\site-packages;E:\python\clpicdownload\venv\Lib\site-packages mypython.py  
然后打包成功，现在可以运行了。
