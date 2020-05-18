# RubbishMaoGai
Auto generate database of questions based on known results for http://course.xmu.edu.cn/  
自动根据已做结果生成厦大course毛概课的题库  
**Note:** 只要是清华大学course系统，并且所在课程的在线测试结果有公布答案，都可以使用该脚本生成题库。

![亲测满分](https://github.com/F5Soft/RubbishMaoGai/blob/master/result.png?raw=true)  

## 如何使用题库?
1. 在Release里下载tiku.html，或者直接下载source code  
   https://github.com/F5Soft/RubbishMaoGai/releases
2. 用浏览器打开tiku.html
3. `Ctrl+F` 全文搜索
4. **全文搜索时，由于标点符号全半角、空格数量不匹配等问题，不建议复制整个标题搜索，可能会找不到结果！建议仅搜索题目标题的连续文字内容。**
5. **有的题目前面内容相同，但是后缀不同，注意搜索结果有多个的情况，以免看错！**

## 收集样本3569题，严格去重后共383题
![题库数量预测](https://github.com/F5Soft/RubbishMaoGai/blob/master/prediction.png?raw=true)

**说明题库的内容基本上都有了，仅有极小概率会漏题**  

`samples`: 原始测试网页  
`tiku.py`: 生成题库的脚本  
`tiku.html`: 当前生成的题库

## 如何提供题目?
1. 完成6次测试，不用做直接提交即可
1. 点击查看结果，进入含有答案的结果页面
3. 右键分别保存6个测试结果网页
4. 将网页结果打包发送至作者，或者放入samples文件夹内，并发起pull request

## 如何使用该脚本生成其他题库?
1. 操作同上，保存网页后，按照本仓库下samples文件夹的的结构，将测试结果放入samples文件夹
2. 在Python版本大于等于3.6.8的环境下运行`tiku.py`。在运行之前，确保已经安装了`matplotlib`。如果没有安装，可以通过如下命令安装
```bash
pip install matplotlib
```
3. 检查生成后的`tiku.html`。由于每个人提供的浏览器差异，可能会有其他Bug出现，欢迎提出。