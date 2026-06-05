from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests

class TradingApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.title = Label(text='BTC Live Price')
        self.price = Label(text='Loading...')

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.price)

        Clock.schedule_interval(self.update_price, 5)

        return self.layout

    def update_price(self, dt):
        try:
            data = requests.get(
                "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
                timeout=5
            ).json()

            self.price.text = f"BTC: ${data['price']}"

        except:
            self.price.text = "Connection Error"

if __name__ == "__main__":
    TradingApp().run()
