"""
CP1404 Miles to kilometres with KIVY

estimate: 60min
actual: 30min
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.61


class MilestoKMApp(App):
    """ MilestoKMApp is a Kivy app that takes a miles input and converts to kilometers """
    def build(self):
        "build kivy app for conversion"
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_convert(self):
        """converts miles to km"""
        number = self.get_validated_miles()
        result = number * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        "function for handling increment"
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_convert()

    def get_validated_miles(self):
        """validates input and returns 0 if incorrect"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilestoKMApp().run()
