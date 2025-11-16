from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from wifi_data_handler import save_wifi_info

class WifiScreen(BoxLayout):
    def submit(self):
        ssid = self.ids.ssid_input.text
        password = self.ids.password_input.text
        save_wifi_info(ssid, password)
        print(f"Saved: {ssid}")

class WifiSaverApp(App):
    def build(self):
        return WifiScreen()

if __name__ == '__main__':
    WifiSaverApp().run()