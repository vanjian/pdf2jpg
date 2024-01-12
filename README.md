# pdf2jpg
将pdf转成图片

直接运行，程序会自动将文件夹内的全部pdf文件转成图片

需要安装的库

pip install fitz

pip install pymupdf


闲来无事，随便玩玩

cmd直接pdf2jpg

````python
import fitz
doc = fitz.open(filename)
page = doc.load_page(0)
matrix = fitz.Matrix(2, 2)
pm = page.get_pixmap(matrix=matrix,colorspace="rgb")
pm.save(filename)
````
