
class Math_Operation:
    def __init__(self):
        self.value1 = '1,3'
        self.value2 = '2,3'

    def get(self):
        print(f'value1: {self.value1}')
        print(f'value2: {self.value2}')


    def add(self):
        try:
            add = self.value1 + self.value2
            print(f'value 1 + value 2 = ', add)
            return add
        except:
            print('error')
    
        
    def check_data_type(self):
        print('Value 1:', type(self.value1))
        print('Value 2:', type(self.value2))

    def chuoi_dan_xen(self):
        maxDoDaiChuoi = max(len(self.value1), len(self.value2))
        chuoiDanXen = ""
  
        for i in range(maxDoDaiChuoi):
            if (i < len(self.value1)):
                 chuoiDanXen += self.value1[i]
            if (i < len(self.value2)):
                 chuoiDanXen += self.value2[i]
        return chuoiDanXen
    
    

mo = Math_Operation()
mo.add()
mo.check_data_type()
print(mo.chuoi_dan_xen())

        

        
