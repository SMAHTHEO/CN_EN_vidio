
import os
from Engine import Trans
import json
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


def Transipy(file_name):

    # 终端显示
    print("[XMeng] 开始翻译 : " + file_name + ".ipy\n")

    file_name1 = file_name + ".ipynb"
    file_name2 = file_name + "_ZN.ipynb"

    def remove_dot_space_lines(text):
        # 定义要删除的字符集合
        chars_to_remove = set(['.', ' '])

        # 按行分割字符串
        lines = text.split('\n')

        # 删除只有句号和空格的行
        lines = [line for line in lines if not set(line) <= chars_to_remove]

        # 将修改后的内容连接成字符串并返回
        return '\n'.join(lines)

    # 读取ipynb文件，并循环处理所有的Markdown单元格
    with open(file_name1) as f:
        data = json.load(f)

    for cell in data['cells']:
        if cell['cell_type'] == 'markdown':
            # 获取原始Markdown文本内容
            source = cell['source']

            # 对原始Markdown内容进行翻译
            translated = Trans('\n'.join(source))

            # 删除空行
            translated_removenull = remove_dot_space_lines(translated)

            # 在原始Markdown下方添加翻译后的内容
            cell['source'] += ['\n\n---\n\n', translated]

    # 将修改后的数据写回到文件中

    with open(file_name2, 'w') as f:
        json.dump(data, f)
    print("[XMeng] -------- e n d --------\n")


def ipy():
    filenames = []
    for filename in os.listdir('.'):
        if ".ipynb" in filename:
            filenames.append(filename[:-6])
    print("[XMeng] 共计找到 " + str(len(filenames)) + " 个 ipy 文件\n\n")
    for filename in filenames:
        print("[XMeng] 开始翻译 : " + filename + ".ipy\n")
        Transipy(filename)
