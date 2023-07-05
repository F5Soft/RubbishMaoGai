from bs4 import BeautifulSoup as bs
from argparse import ArgumentParser
import os
import html
import re

parser = ArgumentParser(description='根据传入的科目名生成对应的题库')
parser.add_argument('subject', type=str, help='科目名称拼音首字母  mg: 毛概 | sg: 史纲 | my: 马原')
args = parser.parse_args()


def unescape(raw: str):
    """
    转换十进制Unicode表示的字符
    """
    ans = html.unescape(raw)
    ans = ans.strip()
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
    subject_name = {
        "mg": "毛概",
        "sg": "史纲",
        "my": "马原"
    }

    prefix = "---\neditLink: false\n---\n# " + subject_name[subject] + "题库\n\n::: info\n全文搜索时，由于标点符号全半角、空格数量不匹配等问题，不建议复制整个标题搜索，可能会找不到结果！建议仅搜索题目标题的连续文字内容\n:::\n\n## 题目列表\n"

    questions = []
    question_count = 0
    total_count = 0

    data_path = subjects_path[subject]
    tiku_path = os.path.join("src/banks", subject+".md")

    if not os.path.exists("./src/banks"):
        os.mkdir("./src/banks")

    with open(tiku_path, 'wt', encoding="UTF-8", errors="replace") as tiku:
        tiku.write(prefix)
    
        for dirname in os.listdir(data_path):
            for filename in os.listdir(os.path.join(data_path, dirname)):
                if "_files" in filename:
                    continue
                
                filename = os.path.join(data_path, dirname, filename)
                soup = bs(open(filename, "r", encoding="GBK"), "html.parser")

                tables = soup.find_all("table", attrs={"class": "infotable"})
                for i in tables:
                    title = i.find("input", attrs={"name": re.compile("[0-9]*_content")})
                    if title:
                        title = unescape(title["value"])
                        if re.search(r'<.*?>(.*?)</.*?>', title):
                            title = re.search(r'<.*?>(.*?)</.*?>', title).group(1)
                        if title in questions:
                            total_count += 1
                            continue
                        else:
                            questions.append(title)
                            question_count += 1
                            total_count += 1
                            choices = i.find_all("input", attrs={"name": "answer"})
                            if choices:
                                choices = [j.next_sibling.replace("\n", "").strip() for j in choices]
                                answers = i.find_all("td", attrs={"colspan":"2", "class": "Fimg"})
                                if answers:
                                    answers = [k.strip() for k in [j.get_text(strip=False).split("\n") for j in answers if "[参考答案]" in j.text][0] if k.strip() != ""][1:]
                                    tiku.write(f"\n### {title}\n\n")
                                    for j in choices:
                                        if j in answers:
                                            tiku.write(f"- [x] {j}\n")
                                        else:
                                            tiku.write(f"- [ ] {j}\n")     

    with open("./src/banks/README.md", "a", encoding="utf8") as f:
        f.write(f"| [{subject_name[subject]}](/RubbishMaoGai/banks/{subject}.html) | {total_count} | {question_count} |\n")
    print(f"已生成{subject_name[subject]}题库，共{total_count}道题，去重后{question_count}道题")
    
            

if __name__ == "__main__":
    getSamplesInfo(args.subject)