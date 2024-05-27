
import os
from Engine import Trans, Trans_deepl


# 为文件内字母开头的行进行翻译
def Transvtt(file):

    Chr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
           "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    str = ""
    with open(file+".vtt", "r") as f:
        line = f.readline()
        while line != "":
            if line[0] in Chr:
                lineCN = Trans_deepl(line)
                str += (lineCN)
            str += (line)
            line = f.readline()
    with open(file+".vtt", "w") as f:
        f.write(str)


def rename(Lecture):
    i = 0
    for filename in os.listdir('.'):
        if filename.startswith('ffff') or filename.startswith("0000"):
            # 获取文件创建时间
            ctime = os.path.getctime(filename)
            # 根据创建时间构造新文件名
            new_filename = f'{ctime}.txt'
            i += 1
            # 重命名文件
            os.rename(filename, f"Lec{Lecture}Vidio{i}.mp4")
            print(
                f'[XMeng] 已重命名文件: {filename} -> {f"Lec{Lecture}Vidio{i}.mp4"}')
    print("[XMeng] 成功 rename " + str(i) + " 个 .mp4 文件\n")
    i = 0
    for filename in os.listdir('.'):
        if ".vtt" in filename:
            # 获取文件创建时间
            ctime = os.path.getctime(filename)
            # 根据创建时间构造新文件名
            new_filename = f'{ctime}.txt'
            i += 1
            # 重命名文件
            os.rename(filename, f"Lec{Lecture}Vidio{i}.vtt")
            print(
                f'[XMeng] 已重命名文件: {filename} -> {f"Lec{Lecture}Vidio{i}.vtt"}')
    print("[XMeng] 成功 rename " + str(i) + " 个 .vtt 文件\n")


def vtt():
    filenames = []
    for filename in os.listdir('.'):
        if ".vtt" in filename:
            filenames.append(filename[:-4])
    print("[XMeng] 共计找到 " + str(len(filenames)) + " 个 vtt 文件")
    for filename in filenames:
        print("[XMeng] 开始翻译 : " + filename + ".vtt")
        Transvtt(filename)
    print("[XMeng] 幸不辱命, 一切顺利！")
