from flask import Flask
import serial

app = Flask(__name__)
#ser = serial.Serial('COM3', 128000)  # 根據你的Arduino設定串口

@app.route('/')
def index():
    return 'Arduino Server'

@app.route('/start')
def start():
    ser.write(b'start\n')  # 發送啟動指令
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)