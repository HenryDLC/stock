# http://baostock.com/baostock/index.php/A%E8%82%A1K%E7%BA%BF%E6%95%B0%E6%8D%AE
# https://blog.csdn.net/wolf1132/article/details/78787466
# https://blog.csdn.net/avenccssddnn/article/details/8628478
# https://blog.csdn.net/llingmiao/article/details/79941066

# wind https://www.jianshu.com/p/4a71f1e5db8f

import tushare as ts

pro = ts.pro_api('abb953ed857518585eb9ffe2e581934a213faea48fa73f288f320940')

data = ts.get_today_all()

print(data)