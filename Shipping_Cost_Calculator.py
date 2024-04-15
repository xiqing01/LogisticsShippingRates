# 运费计算器

## 输入包裹重量和运输方式
weight = float(input("输入包裹重量（公斤）："))
rate = float(input("输入每公斤运费："))

## 计算运费
shipping_cost = weight * rate

## 显示结果
print(f"运输费： {shipping_cost} USD")
