import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("計數與文字輸入應用")
        self.resize(400, 300)

        # 元件：標籤、計數按鈕、輸入框、顯示按鈕、清除按鈕
        self.label = QLabel("請輸入文字並點擊按鈕：", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("在這裡輸入...")
        self.display_button = QPushButton("顯示文字", self)
        self.clear_button = QPushButton("清除文字", self)
        self.counter_button = QPushButton("增加計數", self)

        # 計數器
        self.counter = 0

        # 設定佈局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.display_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.counter_button)
        self.setLayout(layout)

        # 事件連接
        self.display_button.clicked.connect(self.display_text)
        self.clear_button.clicked.connect(self.clear_text)
        self.counter_button.clicked.connect(self.increment_counter)

    def display_text(self):
        text = self.input_field.text()
        if text.strip():
            self.label.setText(f"您輸入了：{text}")
        else:
            QMessageBox.warning(self, "警告", "輸入欄位為空！")

    def clear_text(self):
        self.input_field.clear()
        self.label.setText("請輸入文字並點擊按鈕：")

    def increment_counter(self):
        self.counter += 1
        self.label.setText(f"計數已增加 {self.counter} 次！")

# 主程式入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterApp()
    window.show()
    sys.exit(app.exec())
