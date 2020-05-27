

# 服务端执行:  python upload.py 8081
# 全量同步:    sh upload.sh 127.0.0.1:8081   服务端目录 本地目录
# 增量实时同步: sh upload.sh 127.0.0.1:8081   服务端目录 本地目录

root_dir=$3
dstdir=$2
host=$1

if [ $root_dir=='' ];then
    root_dir=`pwd`
fi

if [ $root_dir=='.' ];then
    root_dir=`pwd`
fi

if [ $root_dir=='./' ];then
    root_dir=`pwd`
fi

function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
            getdir $dir_or_file
        else
           localname=$dir_or_file
           dstname=${dir_or_file/$root_dir/$dstdir}  
           echo `date "+%Y-%m-%d %H:%M:%S"` $dir_or_file `curl -s -F "file=@$localname"   "http://$host/?name=$dstname"`
        fi
    done
}


getdir $root_dir $dstdir
fswatch -d $root_dir | while read localname
do
 if [ -f $localname ];then
    dstname=${localname/$root_dir/$dstdir};
    echo `date "+%Y-%m-%d %H:%M:%S"` $localname `curl -s -F "file=@$localname" "http://$host/?name=$dstname";`
 fi
done


