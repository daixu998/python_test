#coding=utf-8
#

score = int(input("请输入一个0-100的整数:"))
if score>=85:
	print("您真优秀!")

if score<60:
	print("您需要加倍努力!")

if(score >= 60) and (score < 85):
	print("您的成绩还可以,仍需努力!")