import ctypes
import os
CUR_PATH=os.path.dirname(__file__)
dllPath=os.path.join(CUR_PATH,"CreateDLL.dll")
print (dllPath)
#mydll=ctypes.cdll.LoadLibrary(dllPath)
#print mydll
pDll=ctypes.WinDLL(dllPath)
print (pDll)

pResutl= pDll.Add(1,4)
pResult2=pDll.substract(1,4)
print (pResutl)
print (pResult2)