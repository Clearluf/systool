import json
import re
import sys
sys.path.append('..') #这条命令是用来添加上层目录的
from bean.cpu_info import cpu_info


with open(file="/proc/cpuinfo",mode="r",encoding="utf-8") as f:
    cores=0
    name = 'unknown'
    while(True):
        data=(f.readline())
        if(data):
            if re.match("^model name",data,re.IGNORECASE):
                name = data.split(":")[1].strip()
                cores += 1
        else:
            break
    my_cpu_info = cpu_info()
    # my_cpu_info.name = name
    # my_cpu_info.cores = cores
    a_cpu_info = cpu_info()
    print(json.dumps(my_cpu_info.__dict__))
    print(json.dumps(a_cpu_info.__dict__))
    