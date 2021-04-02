from kivy.animation import Animation
#from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from os.path import join
import requests

Base_url="http://127.0.0.1:8000/"


Window.size = (305, 488)

KV = """
<SignUp>:
    email:email
    password:password
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
            id:email
            hint_text: "Enter Your Email"
            pos_hint: {"top":0.55,'right':1.1,}
            # current_hint_text_color: 0, 0, 0, 1
            # color_mode: "custom"
            line_color_focus: 0, 0, 0, 1  
        MDTextField:
            id:password
            hint_text: "Enter Your Password"
            pos_hint: {"top":0.4,'right':1.1,}
            # current_hint_text_color: 0, 0, 0, 1
            password: True
            # color_mode: "custom"
            line_color_focus: 0, 0, 0, 1
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .2}
            # size_hint_x: .5
            on_press:root.getText()
        MDTextButton:
            text: "Forgot Password?"
            pos_hint: {"center_x": .5, "center_y": .1}
            custom_color: 0, 0, 0, 1
            on_press: app.change_Login()  
        MDTextButton:
            text: "Sign-Up"
            on_press: app.change_abhi()
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
            # size_hint_x: .5
<Abhi>:
    MDToolbar:
        md_bg_color: 1, 0, 0, 1
        title: "SignUp"
        pos_hint: {"top" : 1}
        elevation: 11
    MDCard:
        orientation: "vertical"
        size_hint: None,None
        size: 128,128
        pos_hint: {"center_x": .25,"center_y": .7}
        Image:
            source: "Doctor.PNG"
        Button:
            background_normal: ''
            background_color: (242/255, 247/255, 247/255, 1)
            size_hint: (1, .25)
            text: "Doctor" 
            on_press: app.change_Sign()  

    MDCard:
        orientation: "vertical"
        size_hint: None,None
        size: 128,128
        pos_hint: {"center_x": .72,"center_y": .7}
        Image:
            source: "Nurse.PNG"
        Button:
            background_normal: ''
            background_color: (242/255, 247/255, 247/255, 1)
            size_hint: (1, .25)
            text: "Nurse" 
            on_press: app.change_Sign()    
    MDCard:
        orientation: "vertical"
        size_hint: None,None
        size: 128,128
        pos_hint: {"center_x": .25,"center_y": .4}
        Image:
            source: "Patient.PNG"
        Button:
            background_normal: ''
            background_color: (242/255, 247/255, 247/255, 1)
            size_hint: (1, .25)
            text: "Patient"
            on_press: app.change_Sign() 
<Sign>:
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
            hint_text: "Enter Your User_id"
            pos_hint: {"top":0.7,'right':1.1,}
            current_hint_text_color: 0, 0, 0, 1
            color_mode: "custom"
            line_color_focus: 0, 0, 0, 1  
        MDTextField:
            hint_text: "Enter Your Password"
            pos_hint: {"top":0.55,'right':1.1,}
            current_hint_text_color: 0, 0, 0, 1
            password: True
            color_mode: "custom"
            line_color_focus: 0, 0, 0, 1
        MDTextField:
            hint_text: "Verify your Password"
            pos_hint: {"top":0.4,'right':1.1}
            current_hint_text_color: 0, 0, 0, 1
            password: True
            color_mode: "custom"
            line_color_focus: 0, 0, 0, 1
                
"""


class SignUp(Screen):
    
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def getText(self):
        print(self.email.text,self.password.text)
        email=str(self.email.text)
        password=str(self.password.text)
        r=requests.post(Base_url+"dj-rest-auth/login/",data={"username":"","email":email,"password":password})
        print(r)


class Login(Screen):
    pass

class  Abhi(Screen):
    pass

class Sign(Screen):
    pass


class LoginApp(MDApp):
    

    def build(self):
        Builder.load_string(KV)
      
        self.sm = ScreenManager()
        self.sm.add_widget(SignUp(name="signup"))
        self.sm.add_widget(Login(name="login"))
        self.sm.add_widget(Abhi(name="abhi"))
        self.sm.add_widget(Sign(name="sign"))
        # self.
        return self.sm

    def change_Login(self):
        self.sm.transition.direction = 'left'
        self.sm.current = "login"

    def change_register(self):
        self.sm.transition.direction = 'right'
        self.sm.current = "signup"

    def change_abhi(self):
        self.sm.transition.direction = 'left'
        self.sm.current = "abhi"    
    
    def change_Sign(self):
        self.sm.transition.direction = 'left'
        self.sm.current = "sign"

    
if __name__ == "__main__":
    app = LoginApp()
    app.run()
