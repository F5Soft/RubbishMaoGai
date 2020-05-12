"""
题库生成
Author: F5
Date: 2020-05-12
"""

import os

tiku = open("tiku.html", 'wt')
count = 0

for dirname in os.listdir("samples"):
    for filename in os.listdir("samples/" + dirname):
        if "_files" in filename:
            continue

        filename = dirname + '/' + filename
        f = open("samples/" + filename, 'rt', encoding='GBK')
        in_context = False

        for line in f.readlines():
            if "_content" in line:
                count += 1
                low = line.find('value="') + 7
                high = line.find('><iframe') - 1
                tiku.write("<h3>" + str(count) + ". " + line[low:high] + "</h3>")
            
            if "answer" in line and "sogoutip" not in line:
                low = line.find('answer') + 8
                tiku.write("<div>" + line[low:] + "</div>")

            if in_context and "</td>" in line:
                in_context = False
                tiku.write("</div>")

            if in_context:
                tiku.write(line)

            if "[参考答案]" in line:
                in_context = True
                tiku.write("<h5>参考答案</h5><div>")



        f.close()

tiku.close()