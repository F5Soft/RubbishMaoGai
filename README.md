# RubbishMaoGai
Auto generate database of questions based on known results for http://course.xmu.edu.cn/  
自动根据已做结果生成厦大course毛概课的题库  

## 共收到1889题，去重后已有387题
**说明题库的内容基本上都有了，但不排除之后会有改动**  

`samples`: 原始测试网页  
`tiku.py`: 生成题库的脚本  
`tiku.html`: 当前生成的题库

## 如何提供题目?
1. 完成6次测试，不用做直接提交即可
1. 点击查看结果，进入含有答案的结果页面
3. 右键分别保存6个测试结果网页
4. 将网页结果打包发送至作者，或者放入samples文件夹内，并发起pull request

## 如何使用题库?
1. 在Release里下载tiku.html，或者直接下载这里的代码
2. 用浏览器打开tiku.html
3. `Ctrl+F` 全文搜索

## 题库基本生成后，将在release内发布
