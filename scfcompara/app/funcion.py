
class datos:
    def __init__(self, plan):
        self.plan = plan
        self.dic = {}
        self.i = 0
        self.flag = 1
        self.port = {}
        self.var_alarm = []
    
    def alarm(self,i):
        var = i.find("p",{"name":"descr"}).getText()
        self.var_alarm.append(var)

    def alarmas(self):
        [self.alarm(i) for i in self.plan.find_all(class_="com.nokia.srbts.eqm:EAC_IN")]
        return self.var_alarm

    def cellid(self):
        cid = self.plan.find("p",{"name":"btsName"}).getText()
        return cid 

    def calidad(self):
            qos = {}
            #a = self.plan.find_all(class_="com.nokia.srbts.tnl:L2SWI")
            qos['qos'] = self.plan.find("p",{"name":"l2QoSEnabled"}).getText()
            qos['l2'] = self.plan.find("p",{"name":"l2SwitchingEnabled"}).getText()
            return qos

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
            interfaceDN = "N/A"

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
            ip = "N/A"
        
        if (ip != "N/A") and (interfaceDN != "N/A"):
            self.clasificar(userlabel, vlannum, ip, mask)  
                    

    def ipif(self):
        [self.data(i) for i in self.plan.find_all(class_="com.nokia.srbts.tnl:IPIF")]
        return self.dic