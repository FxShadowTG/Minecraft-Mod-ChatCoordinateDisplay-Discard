# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi


@Mod.Binding(name="AddCommonMod", version="0.0.1")
class AddCommonMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def AddCommonModServerInit(self):
        serverApi.RegisterSystem("AddCommonMod","AddCommonModServerSystem","AddCommonMod.AddCommonModServerSystem.AddCommonModServerSystem")
        print("服务注册成功")

    @Mod.DestroyServer()
    def AddCommonModServerDestroy(self):
        print("服务销毁成功")

    @Mod.InitClient()
    def AddCommonModClientInit(self):
        clientApi.RegisterSystem("AddCommonMod","AddCommonModClientSystem","AddCommonMod.AddCommonModClientSystem.AddCommonModClientSystem")
        print("客户注册成功")

    @Mod.DestroyClient()
    def AddCommonModClientDestroy(self):
        print("客户销毁成功")
