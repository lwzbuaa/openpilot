import time
from selfdrive.df import lib_main
ffi, libmpc = lib_main.get_libmpc()
libmpc.init_model()
start = time.time()
#for i in range(50):
model_output = libmpc.run_model(0.40300879, 0.32720165, 0.30036449, 0.2559415 , 0.29458129)
#print(time.time() - start)
print(model_output)