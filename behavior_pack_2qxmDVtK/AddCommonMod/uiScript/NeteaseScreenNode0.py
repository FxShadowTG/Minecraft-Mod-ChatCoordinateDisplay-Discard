# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class NeteaseScreenNode0(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print("初始化UI的Init...")
		self.ListenForEvent(clientApi.GetEngineNamespace(),clientApi.GetEngineSystemName(),"UiInitFinished",self,self.Ui_Init)

	def Ui_Init(self,args):
		clientApi.RegisterUI("uiCourse", "uiCourse", "AddCommonMod.uiScript.uiCourse.uiCourse", "uiCourse.main")

	def Create(self):
		"""
		@description UI创建成功时调用
		"""
		print("UI创建成功...")
		pass

	def Destroy(self):
		"""
		@description UI销毁时调用
		"""
		self.UnListenForEvent(clientApi.GetEngineNamespace(),clientApi.GetEngineSystemName(),"UiInitFinished",self,self.Ui_Init)

		pass

	def OnActive(self):
		"""
		@description UI重新回到栈顶时调用
		"""
		pass

	def OnDeactive(self):
		"""
		@description 栈顶UI有其他UI入栈时调用
		"""
		pass
