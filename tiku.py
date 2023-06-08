import os, sys
import argparse
import html
import re

parser = argparse.ArgumentParser(description='根据传入的科目名生成对应的题库')
parser.add_argument('subject', type=str, help='科目名称拼音首字母  mg: 毛概 | sg: 史纲 | my: 马原')
args = parser.parse_args()

def unescape(raw: str):
    """
    转换十进制Unicode表示的字符
    """
    ans = raw.strip()
    ans = html.unescape(html.unescape(ans))
    ans = ans.replace("<p>", '').replace("</p>", '')
    ans = ans.replace("<br>", '').replace(' ', '').lstrip('>')
    # ans = ans.replace("（", '(').replace("）", ')')
    return ans



def getSamplesInfo(subject : str):
    subjects_path = {
        "mg": "samples/MaoGai",
        "sg": "samples/ShiGang",
        "my": "samples/MaYuan"
    }
    subjects_head = {
        "mg": "# 毛概题库\n\n",
        "sg": "# 史纲题库\n\n",
        "my": "# 马原题库\n\n"
    }

    prefix = subjects_head[subject] + "::: info\n全文搜索时，由于标点符号全半角、空格数量不匹配等问题，不建议复制整个标题搜索，可能会找不到结果！建议仅搜索题目标题的连续文字内容\n:::\n\n## 题目列表\n\n"

    questions = set()
    question_count = 0
    question_count_list = []
    total_count = 0
    total_count_list = []
    choices = []
    answers = []

    data_path = subjects_path[subject]
    tiku_path = os.path.join("src/banks", subject+".md")

    if not os.path.exists("./src/banks"):
        os.mkdir("./src/banks")

    with open(tiku_path, 'wt', encoding="utf8", errors="replace") as tiku:
        tiku.write(prefix)
    
        for dirname in os.listdir(data_path):
            for filename in os.listdir(os.path.join(data_path, dirname)):
                if "_files" in filename:
                    continue
                
                filename = os.path.join(data_path, dirname, filename)
                with open(filename, 'rt', encoding='GBK') as f:
                    in_context = False
                    in_answer_context = False

                    for line in f.readlines():
                        # 题目标题
                        if "_content" in line:
                            total_count += 1
                            low = line.find('value=') + 7
                            high = line.find('><iframe') - 1
                            contents = re.findall('[\u4e00-\u9fa5A-Za-z0-9（）\(\)《》“”"",\.，。：；]+', unescape(line[low:high]))
                            title = ''
                            for i in contents:
                                if i != '宋体' and i != '黑体' and i != '微软雅黑':
                                    title += i

                            if title not in questions:
                                in_context = True
                                questions.add(title)
                                question_count += 1
                                tiku.write("### " + title + " \n\n")

                            question_count_list.append(question_count)
                            total_count_list.append(total_count)

                        # 题目选项
                        if in_context and "answer" in line and "sogoutip" not in line:
                            low = line.find('answer') + 8
                            choices.append(unescape(line[low:]))

                        # 题目答案区域开始
                        if in_context and "[参考答案]" in line:
                            in_answer_context = True
                            continue
                        
                        # 题目答案选项内容（有多选情况）
                        if in_answer_context:
                            for i in re.findall('\S+', unescape(line)):
                                if i != "</td>" and i != "":
                                    answers.append(i)

                        # 题目答案区域结束
                        if in_answer_context and "</td>" in line:
                            in_context = False
                            in_answer_context = False
                            for i in choices:
                                if i in answers:
                                    tiku.write("- [x] " + i + "\n")
                                else:
                                    tiku.write("- [ ] " + i + "\n")
                            tiku.write("\n")
                            choices.clear()
                            answers.clear()

    print("去重后:", question_count)
    print("总计:", total_count)
            

if __name__ == "__main__":
    getSamplesInfo(args.subject)