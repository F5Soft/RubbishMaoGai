"""
题库生成
Author: F5
Date: 2020-05-12
"""

import os

tiku = open("tiku.html", 'wt')

questions = set()
question_count = 0
question_count_list = []
total_count = 0
total_count_list = []

for dirname in os.listdir("samples"):
    for filename in os.listdir("samples/" + dirname):
        if "_files" in filename:
            continue

        filename = dirname + '/' + filename
        f = open("samples/" + filename, 'rt', encoding='GBK')
        in_context = False
        in_answer_context = False

        for line in f.readlines():
            # 题目标题
            if "_content" in line:
                total_count += 1
                low = line.find('value="') + 7
                high = line.find('><iframe') - 1
                title = line[low:high]

                if title not in questions:
                    in_context = True
                    questions.add(title)
                    question_count += 1
                    tiku.write("<h3>" + str(question_count) + ". " + title + "</h3>")
    
                question_count_list.append(question_count)
                total_count_list.append(total_count)

            # 题目选项
            if in_context and "answer" in line and "sogoutip" not in line:
                low = line.find('answer') + 8
                tiku.write("<div>" + line[low:] + "</div>")

            # 题目答案区域结束
            if in_answer_context and "</td>" in line:
                in_context = False
                in_answer_context = False
                tiku.write("</div>")

            # 题目答案选项内容（有多选情况）
            if in_answer_context:
                tiku.write(line)

            # 题目答案区域开始
            if in_context and "[参考答案]" in line:
                in_answer_context = True
                tiku.write("<h5>参考答案</h5><div>")
        f.close()

tiku.close()
print(question_count)
print(total_count)

# 预测题库题目数量
import matplotlib.pyplot as plt
plt.plot(total_count_list, question_count_list)
plt.show()
