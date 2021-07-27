import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Simulation.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Simulation')

        # GroupBox안에 있는 RadioButton들을 연결합니다.
        # GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.
        self.groupBox_rad_park.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_africa.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_block.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_nh.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_building.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_mt.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_msb.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_trap.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad_zhang.clicked.connect(self.groupboxRadFunction)

        # # 촬영주체 radiobutton
        # self.groupBox_car_cam.clicked.connect(self.tabRadFunction)
        # self.groupBox_ped_cam.clicked.connect(self.tabRadFunction)
        # self.groupBox_drone_cam.clicked.connect(self.tabRadFunction)

    def groupboxRadFunction(self):
        if self.groupBox_rad_park.isChecked():
            print("groupBox_rad_park Chekced")
            self.env_path = '/home/aiffel-dj10/Downloads/AbandonedPark/LinuxNoEditor/AbandonedPark/Binaries/Linux/AbandonedPark'
        elif self.groupBox_rad_africa.isChecked():
            print("groupBox_rad_africa Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/Africa/LinuxNoEditor/Africa_001/Binaries/Linux/Africa_001'
        elif self.groupBox_rad_block.isChecked():
            print("groupBox_rad_block Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/Blocks/LinuxNoEditor/Blocks/Binaries/Linux/Blocks'
        elif self.groupBox_rad_nh.isChecked():
            print("groupBox_rad_nh Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/AirSimNH/LinuxNoEditor/AirSimNH/Binaries/Linux/AirSimNH'
        elif self.groupBox_rad_building.isChecked():
            print("groupBox_rad_building Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/Building99/LinuxNoEditor/Building_99/Binaries/Linux/Building_99'
        elif self.groupBox_rad_mt.isChecked():
            print("groupBox_rad_mt Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/LandscapeMountains/LinuxNoEditor/LandscapeMountains/Binaries/Linux/LandscapeMountains'
        elif self.groupBox_rad_msb.isChecked():
            print("groupBox_rad_msb Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/MSBuild2018/LinuxNoEditor/MSBuild2018/Binaries/Linux/MSBuild2018'
        elif self.groupBox_rad_trap.isChecked():
            print("groupBox_rad_trap Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/TrapCamera/LinuxNoEditor/TrapCam/Binaries/Linux/TrapCam'
        elif self.groupBox_rad_zhang.isChecked():
            print("groupBox_rad_zhang Checked")
            self.env_path = '/home/aiffel-dj10/Downloads/ZhangJiajie/LinuxNoEditor/ZhangJiajie/Binaries/Linux/ZhangJiajie'

    # def tabRadFunction(self):
    #     if self.groupBox_car_cam.isChecked():
    #         print("groupBox_car_cam Chekced")
    #         self.env_path = '/home/aiffel-dj10/Downloads/AbandonedPark/LinuxNoEditor/AbandonedPark/Binaries/Linux/AbandonedPark'
    #     elif self.groupBox_ped_cam.isChecked():
    #         print("groupBox_ped_cam Checked")
    #         self.env_path = '/home/aiffel-dj10/Downloads/Africa/LinuxNoEditor/Africa_001/Binaries/Linux/Africa_001'
    #     elif self.groupBox_drone_cam.isChecked():
    #         print("groupBox_drone_cam Checked")
    #         self.env_path = '/home/aiffel-dj10/Downloads/Blocks/LinuxNoEditor/Blocks/Binaries/Linux/Blocks'

        # 버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.button1Function)

    # btn_1이 눌리면 작동할 함수
    def button1Function(self):
        os.system(self.env_path)
        print("Sim2Data")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
