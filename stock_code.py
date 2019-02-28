# http://baostock.com/baostock/index.php/A%E8%82%A1K%E7%BA%BF%E6%95%B0%E6%8D%AE
# https://blog.csdn.net/wolf1132/article/details/78787466
# https://blog.csdn.net/avenccssddnn/article/details/8628478
# https://blog.csdn.net/llingmiao/article/details/79941066

# wind https://www.jianshu.com/p/4a71f1e5db8f

import tushare as ts

# pro = ts.pro_api('abb953ed857518585eb9ffe2e581934a213faea48fa73f288f320940')
import time

data = ts.get_realtime_quotes('sh')
price_one = float(data['price'])
print(data[['code','name','price', 'time']])
while True:
    time.sleep(5)
    data = ts.get_realtime_quotes('sh')
    price_two = float(data['price'])


    if price_two > price_one:
        print("涨{:.2%}".format((price_two - price_one) / price_one))
        price_one = price_two


    elif price_one > price_two:
        print("跌{:.2%}".format((price_one - price_two) / price_two))
        price_one = price_two

    elif price_two == price_one:
        pass
