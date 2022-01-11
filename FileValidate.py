import hashlib
import os.path
from loguru import logger


# 验证文件完整性
class FileValidate:

    # 获取文件/目录大小
    def getFileSize(self, path):
        if os.path.isfile(path):
            folder_size = os.path.getsize(path)
            logger.info("当前文件大小为: {0}MB".format(folder_size/1024/1024))
            return folder_size
        menu_size = 0
        for parent, dirs, files in os.walk(path):
            for file in files:
                fullname = os.path.join(parent, file)
                file_size = os.path.getsize(fullname) / 1024 / 1024
                menu_size += file_size
        logger.info("当前文件大小为: {0}MB".format(menu_size))
        return menu_size

    # def validate(self, path_a, path_b):


    def validateFile(self, path_a, path_b):
        # 判断路径是否存在
        if not os.path.exists(path_a):
            logger.warning("[{0}]文件或目录不存在".format(path_a))
        if not os.path.exists(path_b):
            logger.warning("[{0}]文件或目录不存在".format(path_b))
        # 若都是文件，则判断文件的md5码是否相同
        if os.path.isfile(path_a) and os.path.isfile(path_b):
            md5A = hashlib.md5()
            md5B = hashlib.md5()
            with open(path_a, 'rb+') as fileA:
                with open(path_b, 'rb+') as fileB:
                    data1 = fileA.read(4096)
                    data2 = fileB.read(4096)
                    if not data1:
                        md5A.update(data1)
                    if not data2:
                        md5B.update(data2)
            if md5A.hexdigest() != md5B.hexdigest():
                logger.warning("文件{0}与文件{1}内容不一致".format(path_a, path_b))
            else:
                logger.info("文件{0}与文件{1}校验完成".format(path_a, path_b))
        # 若都是目录，则递归调用该函数
        if os.path.isdir(path_a) and os.path.isdir(path_b):
            paths_a = []
            paths_b = []
            for path in os.listdir(path_a):
                paths_a.append(path_a + '\\' + path)
            for path in os.listdir(path_b):
                paths_b.append(path_b + '\\' + path)
            list.sort(paths_a)
            list.sort(paths_b)
            if len(paths_a) != len(paths_b):
                logger.warning("目录{0}与目录{1}文件数量不一致".format(path_a, path_b))
            else:
                for i in range(len(paths_a)):
                    self.validateFile(paths_a[i], paths_b[i])
        if (os.path.isdir(path_a) and os.path.isfile(path_b)) or (os.path.isdir(path_b) and os.path.isfile(path_a)):
            logger.warning("路径{0}和路径{1}目录文件不匹配".format(path_a, path_b))


if __name__ == '__main__':
    filevalidate = FileValidate()
    path_a = r"D:\尚硅谷Java学科全套教程（总207.77GB）"
    path_b = r"F:\尚硅谷Java学科全套教程（总207.77GB）"
    filevalidate.getFileSize(path_b)
