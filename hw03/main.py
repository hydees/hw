str='我的电子邮件to.m@gmail.com.将什么发送到jerry123@163.com或者3123432@qq.com.若遇特殊情况打电话给182123445678.'
import re
ptn1=re.compile(r'[0-9a-z.]{0,19}@gmail\.com')
print(ptn1.search(str))
ptn2=re.compile(r'[0-9a-zA-Z_]{0,19}@163\.com')
print(ptn2.search(str,20))
ptn3=re.compile(r'[0-9a-zA-Z_]{0,19}@qq\.com')
print(ptn3.search(str,43))
ptn4=re.compile(r'\d+')
print(ptn4.search(str,59))
