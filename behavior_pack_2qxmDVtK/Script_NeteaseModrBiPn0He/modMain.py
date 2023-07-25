# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModrBiPn0He", version="0.0.1")
class Script_NeteaseModrBiPn0He(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModrBiPn0HeServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModrBiPn0HeServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModrBiPn0HeClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModrBiPn0HeClientDestroy(self):
        pass
