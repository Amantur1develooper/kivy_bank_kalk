from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ServiceCostCalculator(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.gender_label = Label(text='Выберите пол (1 - мужчина, 2 - женщина):')
        self.gender_input = TextInput()
        
        self.age_label = Label(text='Введите возраст:')
        self.age_input = TextInput()
        
        self.status_label = Label(text='Выберите статус (1 - гос-служащий, 2 - простой гражданин):')
        self.status_input = TextInput()
        
        self.price_label = Label(text='Введите цену:')
        self.price_input = TextInput()
        
        self.month_label = Label(text='Выберите срок услуги (3, 6, 9, 12 месяцев):')
        self.month_input = TextInput()
        
        self.spravka_label = Label(text='Есть ли медицинская справка с работы? (1 - да, 2 - нет):')
        self.spravka_input = TextInput()
        
        self.result_label = Label(text='')

        self.calculate_button = Button(text='Рассчитать')
        self.calculate_button.bind(on_press=self.calculate_cost)

        self.layout.add_widget(self.gender_label)
        self.layout.add_widget(self.gender_input)
        self.layout.add_widget(self.age_label)
        self.layout.add_widget(self.age_input)
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.status_input)
        self.layout.add_widget(self.price_label)
        self.layout.add_widget(self.price_input)
        self.layout.add_widget(self.month_label)
        self.layout.add_widget(self.month_input)
        self.layout.add_widget(self.spravka_label)
        self.layout.add_widget(self.spravka_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def calculate_cost(self, instance):
        gender = int(self.gender_input.text)
        age = int(self.age_input.text)
        status = int(self.status_input.text)
        price = int(self.price_input.text)
        month = int(self.month_input.text)
        spravka = int(self.spravka_input.text)
        one_month = 0

        if status == 1:
            if spravka == 1:
                if month == 3:
                    price += (price / 100) * 3.3
                    one_month = price / 3
                elif month == 6:
                    price += (price / 100) * 6.3
                    one_month = price / 6
                elif month == 9:
                    price += (price / 100) * 9.3
                    one_month = price / 9
                elif month == 12:
                    price += (price / 100) * 15.3
                    one_month = price / 12
            elif spravka == 2:
                price += (price / 100) * 29
                if month == 3:
                    price += (price / 100) * 3.3
                    one_month = price / 3
                elif month == 6:
                    price += (price / 100) * 6.3
                    one_month = price / 6
                elif month == 9:
                    price += (price / 100) * 9.3
                    one_month = price / 9
                elif month == 12:
                    price += (price / 100) * 15.3
                    one_month = price / 12

        if age >= 21 and age <= 23:
            one_month -= one_month * 0.2

        self.result_label.text = f'Основная сумма: {price}, в месяц: {one_month:.2f}'

if __name__ == '__main__':
    ServiceCostCalculator().run()