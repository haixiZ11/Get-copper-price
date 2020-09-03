# coding=utf-8
import requests
from bs4 import BeautifulSoup
import xlwt
import datetime
import os



def paqu(url, title):
	strhtml = requests.get(url)

	f = xlwt.Workbook()
	sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
	for col in range(7):
		sheet1.col(col).width = 256 * 20

	style = xlwt.XFStyle()  # 创建标题样式对象，初始化样式

	al = xlwt.Alignment()
	al.horz = 0x02  # 设置水平居中
	al.vert = 0x01  # 设置垂直居中
	style.alignment = al

	# 设置字体样式
	xfont = xlwt.Font()
	xfont.height = 20 * 16  # 设置字体高度（20是基数不变，18是字号用于调整大小）
	style.font = xfont

	today = datetime.date.today()
	title0 = '市场：' + title + '    日期：' + str(today)
	sheet1.write_merge(0, 0, 0, 6, title0, style)

	# 设置数据格式
	style2 = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
	xfont2 = xlwt.Font()
	xfont2.height = 20 * 12
	style2.font = xfont2
	style2.alignment = al

	soup = BeautifulSoup(strhtml.text, 'lxml')
	data = soup.select('body > table > tbody > tr')
	j = 1
	for item in data:
		souptd = BeautifulSoup(item.text, 'lxml')
		datatd = souptd.select('body > p')
		for itemtd in datatd:
			data3 = itemtd.text.split('\n')
			for i in range(len(data3)):
				sheet1.write(j, i, data3[i], style2)
			j += 1

	f.save(title + str("单价表") + '.xls')


def main():
	print('正在读取今日长江现货数据...')
	title = '长江现货'
	url = 'https://www.ccmn.cn/history_data/cjxh.html'
	paqu(url, title)
	print('长江现货数据保存完毕！  ')

	print(

	)

	print('正在读取今日上海有色数据...')
	title = '上海有色'
	url = 'https://www.ccmn.cn/history_data/wmxh.html'
	paqu(url, title)
	print('上海有色数据保存完毕！  ')


print('=======================')
print('=== YG  Zhao Hai Xi ===')
print('=======================')
print(

)

if __name__ == '__main__':
	main()

print(

)
os.system('pause')
