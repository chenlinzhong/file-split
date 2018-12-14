#coding=utf-8

import os
import tkFileDialog


def get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension



def select_file():
    return tkFileDialog.askopenfilename(title="选择文件",initialdir=os.getcwd())



#按大小切割
def split_by_size(fromfile,chunksize=1,todir=os.getcwd()):
    ochunksize=chunksize
    filepath, shotname, extension = get_filePath_fileName_fileExt(fromfile)
    chunksize = chunksize*1024*1000
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)
    partnum = 0
    inputfile = open(fromfile,'rb')#open the fromfile
    files=[]
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        partnum += 1
        filename = os.path.join(todir,('%s-bysize-%dM-%04d'%(shotname,ochunksize,partnum)))
        fileobj = open(filename,'wb')#make partfile
        fileobj.write(chunk)
        files.append(filename)
        fileobj.close()
    return files

#按行数分隔
def split_by_row(fromfile,line=100,dir=os.getcwd()):
    filepath, shotname, extension = get_filePath_fileName_fileExt(fromfile)
    files=[]
    with open(fromfile) as myfile:
        index = 0
        while True:
            index += 1
            try:
                new_file='%s-byline-%d-%04d' % (shotname,line,index)
                new_file = dir+'/'+new_file
                files.append(new_file)
                with open(new_file, 'w') as f:
                    for _ in xrange(line):
                        f.write(myfile.next())
            except StopIteration:
                break
    return files



if __name__=='__main__':
    print split_by_row('/Users/chenlinzhong/Downloads/fanxian.txt',20000)