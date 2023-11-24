"""
CP1404 Practical - dynamic labels with Kivy
estimate: 30 min
actual: 40min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """initialise dynamic label app"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """"""
        super().__init__(**kwargs)
        self.species_to_diet = {"Tyranosaurus Rex": "Carnivore", "Oviraptor": "Omnivore", "Triceratops": "Herbivore"}

    def build(self):
        """ build app with dynamic lables"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """function to create dynamic lables"""
        for species in self.species_to_diet:
            temp_label_species = Label(text=species)
            temp_label_diet = Label(text=self.species_to_diet[species])
            self.root.ids.specieslabs.add_widget(temp_label_species)
            self.root.ids.dietlabs.add_widget(temp_label_diet)




DynamicLabelsApp().run()