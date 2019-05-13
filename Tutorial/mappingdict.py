__mappingFXIDandESN__ = {
    "Port2": None,
    "Port3": None,
    "Port4": None,
    "Port5": None,
    "Port6": None,
}

esn = '123'
if esn in __mappingFXIDandESN__.values():
    print('重複ESN')
else:
    __mappingFXIDandESN__["Port2"] = esn
print(__mappingFXIDandESN__)

if esn in __mappingFXIDandESN__.values():
    print('重複ESN')
else:
    __mappingFXIDandESN__["Port3"] = esn
print(__mappingFXIDandESN__)

for port,esn in __mappingFXIDandESN__.items():
    print(int(port[4]),esn)
