#coding=utf-8
import Tkinter

import comm


class FindLocation(object):
    def __init__(self):
        self.split_file=None
        self.file_dir = None
        # 创建主窗口,用于容纳其它组件
        self.root = Tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("文件切割神器1.0版")
        self.max_batch=0;

        # 选择文件
        self.file_button = Tkinter.Button(self.root, command=self.select_file, text="选择文件")

        #文件路径
        self.file_path = Tkinter.Entry(self.root,width=30)

        self.s_type = 1

        self.r2 = Tkinter.Radiobutton(self.root, text='按文件行数分隔', variable='s_type', value=2,
                                      command=self.change_s_type2)
        self.r2_input = Tkinter.Entry(self.root, width=30)
        self.r2_input.insert(0, 10000)

        self.r1 = Tkinter.Radiobutton(self.root, text='按文件大小分隔,单位:M', variable='s_type', value=1,command=self.change_s_type1,state="active")
        self.r1_input = Tkinter.Entry(self.root,width=30)
        self.r1_input.insert(0,5)



        # 创建一个回显列表
        self.display_info = Tkinter.Listbox(self.root, width=100)

        # 创建一个查询结果的按钮
        self.result_button = Tkinter.Button(self.root, command=self.start_split, text="开始切割")


    def change_s_type1(self):
        self.s_type = 1

    def change_s_type2(self):
        self.s_type = 2

    def select_file(self):
        fname = comm.select_file()
        self.split_file=fname
        self.file_path.delete(0)
        self.file_path.insert(0,fname)

        filepath, shotname, extension = comm.get_filePath_fileName_fileExt(fname)
        self.file_dir = filepath


    def start_split(self):
        files=[]
        if self.s_type == 1:
            size=int(self.r1_input.get())
            files = comm.split_by_size(self.split_file,size,self.file_dir)
        if self.s_type == 2:
            row = int(self.r2_input.get())
            files = comm.split_by_row(self.split_file, row,self.file_dir)

        for m in range(self.max_batch):
             self.display_info.delete(0)

        j=0
        k=1
        for i in files:
            self.display_info.insert(j, i)
            j=j+1
            k=k+1
        if k>self.max_batch:
            self.max_batch=k
        self.display_info.insert(j, 'done')


    # 完成布局
    def gui_arrang(self):
        self.file_button.pack()
        self.file_path.pack()

        self.r1.pack()
        self.r1_input.pack()
        self.r2.pack()
        self.r2_input.pack()

        self.display_info.pack()
        self.result_button.pack()




def main():
    # 初始化对象
    FL = FindLocation()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    Tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()

