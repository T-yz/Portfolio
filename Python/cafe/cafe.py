'''
task is to make a menu and find out total stock value
'''
menulist = {
    "Apple" : {
    "stock":10,
    "price":0.80,
    },
    "Coffee" : {
    "stock":13,
    "price":1.50,
    },
    "Tea": {
    "stock":15,
    "price":1.50,
    }, 
    "Cookie" : {
    "stock":18,
    "price":1.30,
    }, 
    "Sandwich": {
    "stock":14,
    "price":2.50,
    },
}
#   nested directory containing items with stock and price 
total_stock = int()
total_stock_value = float()
item_stock_value = float()
#   variables set to contain correct data types
for i in menulist:
    total_stock += menulist[i]["stock"]
    item_stock_value = menulist[i]["stock"] * menulist[i]["price"]
    total_stock_value += item_stock_value
#   the above iterates through the list.
#   it then adds items stock to total_stock then multiplies item stock by price to find stock value
#   data is then transferred to total_stock_value as a addition but I reckon I could skip a step here and just add it directly
print(total_stock_value)
