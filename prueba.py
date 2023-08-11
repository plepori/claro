# PRUEBA DE CODIGO

from sys import path # usamos para importar modulos propios
path.append('C:\\Users\\EXT84085\\Desktop\\Python') # ruta del modulo que realizamos
from bs4 import BeautifulSoup


filename = 'C:\\Users\\EXT84085\\Desktop\\SCF para corroborar\\PLAN_CR00089_RC7_Amdocs\\SCF4.xml'  # Ruta del archivo
filename1 = 'C:\\Users\\EXT84085\\Desktop\\SCF para corroborar\\PLAN_CR00089_RC7_Amdocs\\SCF_3.xml'

class datos:
    def __init__(self, plan):
        self.plan = plan
        dic = {}
        self.dic = dic
        i = 0
        self.i = i
        flag = 1
        self.flag = flag
        port = {}
        self.port = port 
    

    def buscar_puerto(self,var):
        
        try:
            port = var.find("p",{"name":"connectorLabel"}).getText()
            state = var.find("p",{"name":"administrativeState"}).getText()
            speed = var.find("p",{"name":"speedAndDuplex"}).getText()
            self.port['PORT'+ str(self.i)] = port
            self.port['STATE' + str(self.i)] = state
            self.port['SPEED' + str(self.i)] = speed
        except: None 
        self.i +=1


    def puertos(self):
        self.i = 0
        [self.buscar_puerto(i) for i in self.plan.find_all(class_="com.nokia.srbts.tnl:ETHLK")]
        return self.port


    def clasificar(self,userlabel, vlannum, ip, mask):
        self.dic['TECNO'+ str(self.i)] = userlabel
        self.dic['VLAN' + str(self.i)] = vlannum
        self.dic['IP' + str(self.i)] = ip
        self.dic['MASK' + str(self.i)] = mask
        self.i +=1

    def data(self,var):
        ipno = var['distName'] + '/IPADDRESSV4-1'                               # SE ARMA LA RUTA CON IPADDRESS 4-1
        
        try:
            interfaceDN = var.find("p",{"name":"interfaceDN"}).getText()        # TRAE MRBTS-50149/TNLSVC-1/TNL-1/ETHSVC-1/ETHIF-1/VLANIF-1
        except:
            exit()

        vlanif = self.plan.find(distName=interfaceDN)                           # BUSCA interfaceDN EN EL PLAN
        ipno_v1 = self.plan.find(distName=ipno)                                 # GUARDA TODA LA INFO DE IPNO
        
        # Busco el userlabel
        try:
            userlabel = var.find("p",{"name":"userLabel"}).getText()
        except:
            try:
                userlabel = vlanif.find("p",{"name":"userLabel"}).getText()
            except:
                userlabel = 'N/A' 
                self.flag = 0

        try: 
            vlannum = vlanif.find("p",{"name":"vlanId"}).getText()              # num de vlan
        except:
            vlannum = 'N/A'

        try:
            ip = ipno_v1.find("p",{"name":"localIpAddr"}).getText()                 # extrae la ip
            mask = ipno_v1.find("p",{"name":"localIpPrefixLength"}).getText()       # extrae mask
        except:
            exit()
        
        self.clasificar(userlabel, vlannum, ip, mask)   

    def ipif(self):
        [self.data(i) for i in self.plan.find_all(class_="com.nokia.srbts.tnl:IPIF")]
        return self.dic


####################     INICIO     ####################

with open(filename,"r") as page:
	plan = BeautifulSoup(page,'xml',from_encoding='utf-8')

with open(filename1,"r") as page:
	plan2 = BeautifulSoup(page,'xml',from_encoding='utf-8')
        
scf = datos(plan)
info = scf.ipif()
'''
scf_2 = datos(plan2)
info2 = scf_2.ipif()
'''
#print(info)
#print(info2)