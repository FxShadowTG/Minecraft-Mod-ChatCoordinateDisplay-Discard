# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
from math import floor
ServerSystem = serverApi.GetServerSystemCls()
factory = serverApi.GetEngineCompFactory()

class AddCommonModServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvent()
        print("加载监听ing")
        print("加载监听ok")

    def ListenEvent(self):
        #获取levelId
        self.levelId = serverApi.GetLevelId()
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChatEvent)

    def OnServerChatEvent(self,args):
        print("ok")
        
        compCreatePos = factory.CreatePos(args["playerId"])
        playerPos = compCreatePos.GetFootPos()
        
        x = int(floor(playerPos[0]))
        y = int(floor(playerPos[1]))
        z = int(floor(playerPos[2]))

        if '64' in str(x) or '64' in str(y) or '64' in str(z):
            args["username"] = "§8[" + "-" + "]" + "§r<"+ args["username"] + ">"
        else:
            args["username"] = "§8["+ str(x) + " " + str(y) + " " + str(z) +"]" + "§r<"+ args["username"] + ">"

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChatEvent)

    def Destroy(self):
        self.UnListenEvent()
