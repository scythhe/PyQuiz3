from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QComboBox, QPushButton, QCheckBox,
    QRadioButton, QMessageBox
)
import sys

class VacationPicker(QWidget):

    def find_destination(self):
        if not self.agreement.isChecked():
            QMessageBox.warning(self, "agree to the terms before continuing.")
            return

        continent = self.continent.currentText()
        budget = self.budget.currentText()
        climate = self.climate.currentText()

        if continent == "Europe" and budget == "Low" and climate == "Mild":
            place = "Portugal – Beautiful and budget-friendly!"
        elif continent == "Europe" and budget == "Medium" and climate == "Cold":
            place = "Switzerland – Breathtaking views and cool mountain air"
        elif continent == "Europe" and budget == "High" and climate == "Warm":
            place = "South of France – Classy, sunny, and luxurious"

        elif continent == "Asia" and budget == "Low" and climate == "Hot":
            place = "Thailand – Tropical paradise on a budget"
        elif continent == "Asia" and budget == "Medium" and climate == "Mild":
            place = "Japan – Culture, nature, and amazing food"
        elif continent == "Asia" and budget == "High" and climate == "Cold":
            place = "South Korea – Snowy slopes and high-tech cities"

        elif continent == "Africa" and budget == "Low" and climate == "Hot":
            place = "Morocco – Vibrant, historical, and sunny"
        elif continent == "Africa" and budget == "Medium" and climate == "Mild":
            place = "South Africa – A bit of everything: beaches, cities, and safaris"
        elif continent == "Africa" and budget == "High" and climate == "Hot":
            place = "Seychelles – Luxury island life"

        else:
            place = "Hmm... couldn't quite match that combo. Try different options."

        self.result.setText(f"Your ideal destination: {place}")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find Your Dream Vacation")
        self.setGeometry(500, 300, 400, 600)

        self.intro = QLabel("Pick a continent, budget, and climate, and we’ll help you choose a great vacation spot!")
        self.agreement = QCheckBox("I agree to the terms and conditions")
        
        self.gender_label = QLabel("Your gender (optional):")
        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female") 

        self.continent = QComboBox()
        self.continent.addItems(["Europe", "Asia", "Africa"])

        self.budget = QComboBox()
        self.budget.addItems(["Low", "Medium", "High"])

        self.climate = QComboBox()
        self.climate.addItems(["Hot", "Mild", "Cold", "Snow"]) 
        self.result = QLabel("Your ideal destination:")
        self.search_btn = QPushButton("Find My Vacation Spot")

        layout = QVBoxLayout()
        layout.addWidget(self.intro)
        layout.addWidget(self.agreement)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.male)
        layout.addWidget(self.female)
        layout.addWidget(self.robot)
        layout.addWidget(QLabel("Choose a continent:"))
        layout.addWidget(self.continent)
        layout.addWidget(QLabel("Select your budget:"))
        layout.addWidget(self.budget)
        layout.addWidget(QLabel("Preferred climate:"))
        layout.addWidget(self.climate)
        layout.addWidget(self.search_btn)
        layout.addWidget(self.result)

        self.search_btn.clicked.connect(self.find_destination)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = VacationPicker()
window.show()
sys.exit(app.exec_())

