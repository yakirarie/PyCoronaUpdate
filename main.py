from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
from PyQt5.QtGui import QPen
import sys
import requests
from corona_ui import Ui_Dialog


class MainApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = {}
        self.country_data = {}
        self.countries = []
        self.graph_buttons = {'confirmed': self.ui.confirmed_button, 'deaths': self.ui.deaths_button,
                              'recovered': self.ui.recovered_button, 'actives': self.ui.active_button}
        self.graph_colors = {'confirmed': Qt.black, 'deaths': Qt.red, 'recovered': Qt.green, 'actives': Qt.blue}
        self.current_country = 'Global'
        self.clicked_button = 'confirmed'
        self.get_data()

        self.ui.comboBox.currentIndexChanged.connect(self.country_pick)
        self.ui.confirmed_button.clicked.connect(lambda: self.display_chart(status='confirmed'))
        self.ui.deaths_button.clicked.connect(lambda: self.display_chart(status='deaths'))
        self.ui.recovered_button.clicked.connect(lambda: self.display_chart(status='recovered'))
        self.ui.active_button.clicked.connect(lambda: self.display_chart(status='actives'))
        self.resize(700, 700)

    def get_data(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        response = requests.get("https://api.covid19api.com/summary")
        while not response.ok:
            response = requests.get("https://api.covid19api.com/summary")
        self.data = response.json()
        self.populate_combo_box()
        self.country_pick()
        QApplication.restoreOverrideCursor()

    def get_data_country(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.get_data_country_status("confirmed")
        self.get_data_country_status("deaths")
        self.get_data_country_status("recovered")
        self.calc_country_actives()
        self.display_chart(self.clicked_button)
        QApplication.restoreOverrideCursor()

    def calc_country_actives(self):
        self.country_data['actives'] = []

        total_confirmed = [cases for cases in [report['Cases'] for report in self.country_data['confirmed']]]
        total_deaths = [cases for cases in [report['Cases'] for report in self.country_data['deaths']]]
        total_recovered = [cases for cases in [report['Cases'] for report in self.country_data['recovered']]]
        total_dates = [dates for dates in [report['Date'] for report in self.country_data['confirmed']]]

        for confirmed, deaths, recovered, date in zip(total_confirmed, total_deaths, total_recovered, total_dates):
            self.country_data['actives'].append({'Cases': int(confirmed) - int(deaths) - int(recovered), 'Date': date})

    def get_data_country_status(self, status):
        response = requests.get(
            "https://api.covid19api.com/dayone/country/" + self.current_country + "/status/" + status)
        while not response.ok:
            response = requests.get(
                "https://api.covid19api.com/dayone/country/" + self.current_country + "/status/" + status)
        self.country_data[status] = response.json()

    def get_date(self):
        return self.data['Date'].replace('T', ' ').replace('Z', '')

    def populate_combo_box(self):
        self.countries = [country_data['Country'] for country_data in self.data['Countries']]
        self.ui.comboBox.addItems(['Global'] + self.countries)

    def country_pick(self):
        self.current_country = self.ui.comboBox.currentText()
        if self.current_country:
            current_data = self.data['Global'] if self.current_country == 'Global' else self.data['Countries'][
                self.countries.index(self.current_country)]
            self.ui.total_confirmed_num.display(current_data['TotalConfirmed'])
            self.ui.total_deaths_num.display(current_data['TotalDeaths'])
            self.ui.total_recovered_num.display(current_data['TotalRecovered'])
            self.ui.total_active_num.display(
                current_data['TotalConfirmed'] - current_data['TotalDeaths'] - current_data['TotalRecovered'])

            self.ui.title.setText(self.current_country + ' Corona Status\n' + self.get_date())
            if self.current_country != 'Global':
                self.get_data_country()
                self.ui.graphicsView.show()
                self.ui.confirmed_button.show()
                self.ui.deaths_button.show()
                self.ui.recovered_button.show()
                self.ui.active_button.show()
            else:
                self.ui.graphicsView.hide()
                self.ui.confirmed_button.hide()
                self.ui.deaths_button.hide()
                self.ui.recovered_button.hide()
                self.ui.active_button.hide()

    def display_chart(self, status):
        for button_status, button in self.graph_buttons.items():
            if button_status == status:
                button.setEnabled(False)
                self.clicked_button = status
            else:
                button.setEnabled(True)

        chart = QChart()
        chart.setTitle(self.current_country + " Cases Graph")
        max_value = max([report['Cases'] for report in self.country_data['confirmed']])
        total_cases = [cases for cases in [report['Cases'] for report in self.country_data[status]]]
        total_dates = [dates for dates in [report['Date'] for report in self.country_data[status]]]
        months_data = {}
        for count, date in zip(total_cases, total_dates):
            if date[:7] in months_data:
                months_data[date[:7]] = int(count)
            else:
                months_data[date[:7]] = 0

        series = QLineSeries()
        series.setName(status.capitalize())
        series.setPen(QPen(self.graph_colors[status], 2))

        for i, count in enumerate(months_data.values()):
            current_set = QPointF(i, count)
            series.append(current_set)

        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(months_data.keys())
        axis_y = QValueAxis()
        axis_y.setRange(0, roundup(max_value))

        chart.setAxisX(axis_x)
        chart.setAxisY(axis_y)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        series.setPointLabelsVisible()
        series.setPointLabelsFormat("@yPoint")

        self.ui.graphicsView.setChart(chart)


def roundup(x):
    from math import ceil
    num_of_digits = len(str(x)) - 1
    return int(ceil(x / (10 ** num_of_digits))) * (10 ** num_of_digits) * 1.1


app = QApplication(sys.argv)
dialog = MainApp()
dialog.show()
sys.exit(app.exec_())
