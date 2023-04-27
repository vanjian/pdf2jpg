import fitz
import os

dir_list = os.listdir()

def Process_dirlist():
    for i in dir_list:
        #print(i.find("pdf"))
        if((i.find("pdf")) == 0):
            dir_list.pop(dir_list.index(i))
        
def PDF2png(name):  
    index = 0
    docl = fitz.open(name)
    page_num = docl.page_count
    
    #处理文件名
    file_name = name.split(".pdf")[0]
    
    for i_page in range(page_num):
        page = docl[i_page]
        # 使用matrix参数来控制输出图像的精度
        matrix = fitz.Matrix(2, 2)  # 放大10倍
        pm = page.get_pixmap(matrix=matrix, colorspace="rgb")
        
        n_index = "_%d"  %index
        file_name_ = file_name + n_index + ".png"
        pm.save(file_name_)
        index+=1
        
if __name__ == "__main__":
    '''
    tmp_name = "44.深圳市应对气候变化标准体系框架构建研究.pdf"
    PDF2png(tmp_name)
    
    '''
    Process_dirlist()
    
    for i in dir_list:
        PDF2png(i)
        
        
        
    #PDF2png(dir_list[0])