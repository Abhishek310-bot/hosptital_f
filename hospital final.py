from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (305, 488)

KV = """
<SignUp>:
    name: "first"
    Image:
        source: "Hospitals.PNG"
        opacity: .1
    MDToolbar:
        md_bg_color: 1, 0, 0, 1
        title: "Hospital App"
        pos_hint: {"top" : 1}
        elevation: 11
    MDFloatLayout:

        MDTextField:
            hint_text: "Enter Your Email"
            pos_hint: {"top":0.55,'right':1.1,}
            current_hint_text_color: 0, 0, 0, 1
            color_mode: "custom"
            line_color_focus: 0, 0, 0, 1  
        MDTextField:
            hint_text: "Enter Your Password"
            pos_hint: {"top":0.4,'right':1.1,}
            current_hint_text_color: 0, 0, 0, 1
            password: True
            color_mode: "custom"
            line_color_focus: 0, 0, 0, 1
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint_x: .5

        MDTextButton:
            text: "Forgot Password?"
            pos_hint: {"center_x": .5, "center_y": .1}
            custom_color: 0, 0, 0, 1
            on_press: app.change_Login()  
        MDTextButton:
            text: "Sign-Up"
            pos_hint: {"center_x": .82, "center_y": .1}
<Login>:
    name: 'second'
    Image:
        source: "Hospitals.PNG"
        opacity: .1
    MDToolbar:
        md_bg_color: 1, 0, 0, 1
        title: "Hospital App"
        pos_hint: {"top" : 1}
        elevation: 11
    MDFloatLayout

        MDTextField:
            hint_text: "Enter Your User_id"
            pos_hint: {"top":0.55,'right':1.1,}

            color_mode: "custom"


        MDRaisedButton:
            text: "Enter"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint_x: .5






"""


class SignUp(Screen):
    pass


class Login(Screen):
    pass


class LoginApp(MDApp):
    def build(self):
        images = Builder.load_string(image)
        return images

    def build(self):
        Builder.load_string(KV)
        self.sm = ScreenManager()
        self.sm.add_widget(SignUp(name="signup"))
        self.sm.add_widget(Login(name="login"))
        return self.sm

    def change_Login(self):
        self.sm.transition.direction = 'left'
        self.sm.current = "login"

    def change_register(self):
        self.sm.transition.direction = 'right'
        self.sm.current = "signup"


if __name__ == "__main__":
    app = LoginApp()
    app.run()
