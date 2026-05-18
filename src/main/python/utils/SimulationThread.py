# from PyQt5.QtCore import QThread, pyqtSignal

# class SimulationThread(QThread):
#     log = pyqtSignal(str)       # GUI me message bhejne ke liye
#     finished = pyqtSignal()     # Simulation complete hone par

#     def __init__(self, container, mode, mo_path=None):
#         super().__init__()
#         self.container = container
#         self.mode = mode
#         self.mo_path = mo_path

#     def run(self):
#         try:
#             # GUI free simulation function
#             self.container.simulate_non_gui(self.mode, self.mo_path)
#             self.log.emit("Simulation finished successfully")
#         except Exception as e:
#             self.log.emit(f"Simulation failed: {str(e)}")
#         finally:
#             self.finished.emit()
