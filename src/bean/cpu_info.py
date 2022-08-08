import re


class cpu_info:
    # 静态变量
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
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
                cls._instance.name = name
                cls._instance.cores = cores 
        return cls._instance
    
    @property    
    def name(self):
        return self.__name
    @property
    def cores(self):
        return self.__cores
            
    @name.setter
    def name(self,name: str):
        self.__name = name
    @cores.setter
    def cores(self,cores: int):
        self.__cores = cores
        
