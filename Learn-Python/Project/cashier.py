print("收银台程序")
goods = input("请输入商品名称：")
price = input("请输入商品价格：")
num = input("请输入商品数量：")
total = float(price) * int(num) * 0.9
alipay_total = total*0.95
print("购买的商品为：")
print(goods)
print("商品总价为：")
print(total)
print("使用支付宝支付：")
print(alipay_total)
