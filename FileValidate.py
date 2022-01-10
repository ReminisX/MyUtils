import hashlib
import os.path
from progress.bar import ShadyBar


# 验证文件完整性
class FileValidate:

    def __init__(self):
        self.bar = ShadyBar()

    def validateFile(self, pathA, pathB):
        # 判断路径是否存在
        if not os.path.exists(pathA):
            print("[{0}]文件或目录不存在".format(pathA))
        if not os.path.exists(pathB):
            print("[{0}]文件或目录不存在".format(pathB))
        # 若都是文件，则判断文件的md5码是否相同
        if os.path.isfile(pathA) and os.path.isfile(pathB):
            md5A = hashlib.md5()
            md5B = hashlib.md5()
            with open(pathA, 'rb+') as fileA:
                with open(pathB, 'rb+') as fileB:
                    data1 = fileA.read(4096)
                    data2 = fileB.read(4096)
                    if not data1:
                        md5A.update(data1)
                    if not data2:
                        md5B.update(data2)
            if md5A.hexdigest() != md5B.hexdigest():
                print("文件{0}与文件{1}内容不一致".format(pathA, pathB))
            # else:
            #     print("文件{0}与文件{1}校验完成".format(pathA, pathB))
        # 若都是目录，则递归调用该函数
        if os.path.isdir(pathA) and os.path.isdir(pathB):
            pathsA = []
            pathsB = []
            for path in os.listdir(pathA):
                pathsA.append(pathA + '\\' + path)
            for path in os.listdir(pathB):
                pathsB.append(pathB + '\\' + path)
            list.sort(pathsA)
            list.sort(pathsB)
            if len(pathsA) != len(pathsB):
                print("目录{0}与目录{1}文件数量不一致".format(pathA, pathB))
            else:
                for i in range(len(pathsA)):
                    self.validateFile(pathsA[i], pathsB[i])
        if (os.path.isdir(pathA) and os.path.isfile(pathB)) or (os.path.isdir(pathB) and os.path.isfile(pathA)):
            print("路径{0}和路径{1}目录文件不匹配".format(pathA, pathB))


if __name__ == '__main__':
    filevalidate = FileValidate()
    pathA = r"E:\尚硅谷Java学科全套教程（总207.77GB）"
    pathB = r"F:\尚硅谷Java学科全套教程（总207.77GB）"
    filevalidate.validateFile(pathA, pathB)
