# Redis配置
# REDIS_HOST = 'localhost'
REDIS_HOST = '106.12.8.109'
REDIS_PORT = 6379
REDIS_PASSWORD = 'lxh123'
REDIS_DB = 2

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'


# # 检测cookie是否有效
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}


# 访问如下地址，验证reids中的cookie是否有效，在tester.py中用到了
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}


# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5005


# 产生器和验证器循环周期
CYCLE = 120


# 下面三个设置成True,说明都后台运行
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
