import tushare as ts

pro = ts.pro_api('abb953ed857518585eb9ffe2e581934a213faea48fa73f288f320940')

data = pro.get_hist_data()