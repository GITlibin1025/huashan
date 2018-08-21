#! python 3
#phone number and e-mail Find

import pyperclip, re 

#电话号码的正则表达 

phoneRegex = re.compile(r'''(	   
	(\d{3})|\(\d{3}\))? 	#可选，三个数字或者带括号的三个数字，\( 是转义，区号
	(\s|-|\.)?				#可选，空格、-、. ，\. 是转义
	(\d{3})					#三个数字 
	(\s|-|\.)				#空格、-、. ，\. 是转义
	(\d{4})					#四个数字
	(\s*(ext|x|ext\.)\s*(\d{2,5})?		#美国分机
	)''',re.VERBOSE)					#re.VERBOSE，re下多行参数
	
	#TODO: Creat email regex.			#就是一个下一步要做什么的注释，习惯性#TODO
	
	#TODO: Find matches in clipboard text.
	
	#TODO: Copy results to the clipboard.
	
	
	#email 的正则表达
emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+	#用户名，+至少一个
		@
		[a-zA-Z0-9.-]+		#+至少一个
		（\.[a-zA-Z]{2,4})
		)''',re.VERBOSE)	 
	
	#TODO: Find matches in clipboard text.
	
	#TODO: Copy results to the clipboard.
	
	
	#找到所有匹配
text = str(pyperclip.paste())
match = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[2],groups[3],groups[5]])
	if group[8] != '':
		phoneNum += ' x' + group[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
		matches.append(groups[0])
		
	#TODO: Copy results to the clipboard.
	
	
	#复制到剪切板
if len(matches) > 0:
	pyperclip.copy('\n'.jion(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone nnumber or email addresses found.')