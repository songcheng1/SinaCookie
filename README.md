
①录入account

方式一
前提：02_importer.py里为scan1
cmd运行importer.py，通过18459748505----astvar3647的格式输入账号和密码，然后该方法通过调用db.RedisClient类将账号存存储到reids（未设置db库，默认为0，type=hash,key="accounts:weibo"）
请输入账号密码组, 输入exit退出读入
18459748505----astvar3647

方式二
前提：02_importer.py里为scan2
这样的话会读取account_file中的账号，存储到redis
注意：格式都为 account----password；可以自行设置key值；hgetall accounts:weibo


②单独运行login/weibo/cookies.py即可通过redis中保存的账号密码生成cookie，所以如果我们更改了爬取的网站，就要相对的修改该文件


③录入完账号后即可运行run.py主程序，通过函数api启动falsk；通过generate_cookie、valid_cookie和valid_cookie对cookie进行判断保留有效的cookie；


③api为一个小的falsk网页，配置了一些路由  127.0.0.1:5005
/ 主页，显示 Welcome to Cookie Pool System
/<website>/random  随机获取该网站的一个cookie值    #website为在configs中配置的
/<website>/add/<username>/<password>   #添加账号
/<website>/count   #获取cookie个数


④cookie检验间隔时间在config中设置CYCLE=120秒

======================程序运行机制==================

①先配置账号密码文件01_account_file.txt

②导入文件中的账号密码到reids库accounts:weibo

③运行run.py文件
调用scheduler.py的run函数，运行三个函数
---api
详细信息查看api.py文件，运行在5005端口

---Scheduler.generate_cookie
运行生成cookie的WeiboCookiesGenerator函数，获取cookie保存到reids,在获取cookie的时候，有可能登入规则会变
所以需要特别注意

---Scheduler.valid_cookie
运行tester.py的WeiboValidTester函数，逐个验证，有效保留，无效删除
