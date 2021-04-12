import socket
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
import xml.etree.ElementTree as ET



class FloatLayout(FloatLayout):
    pass

class Window(App):
    IP = None
    PORT = None
    id = 1

    sos_number_1 = False
    sos_number_2 = False
    sos_number_3 = False
    sos_number_4 = False


    chandle_break_1 = False
    chandle_break_2 = False
    chandle_break_3 = False
    chandle_break_4 = False


    def checkbox1(self, checkbox, value):
        if value:
            self.sos_number_1 = True
        else:
            self.sos_number_1 = False

    def checkbox2(self, checkbox, value):
        if value:
            self.sos_number_2 = True

        else:
            self.sos_number_2 = False

    def checkbox3(self, checkbox, value):
        if value:
            self.sos_number_3 = True
        else:
            self.sos_number_3 = False

    def checkbox4(self, checkbox, value):
        if value:
            self.sos_number_4 = True
        else:
            self.sos_number_4 = False

    def checkbox5(self, checkbox, value):
        if value:
            self.chandle_break_1 = True
        else:
            self.chandle_break_1 = False

    def checkbox6(self, checkbox, value):
        if value:
            self.chandle_break_2 = True
        else:
            self.chandle_break_2 = False

    def checkbox7(self, checkbox, value):
        if value:
            self.chandle_break_3 = True
        else:
            self.chandle_break_3 = False

    def checkbox8(self, checkbox, value):
        if value:
            self.chandle_break_4 = True
        else:
            self.chandle_break_4 = False

    def sendNewFrame(self):
        self.IP = self.root.ids.input_ip.text
        self.PORT = int(self.root.ids.input_port.text)
        self.newFrame()
        self.id += 1


    def newFrame(self):
            wr_frame = ET.Element("Frame", type="request")
            command_name = ET.SubElement(wr_frame, "command", name="setButtonState", id=str(self.id))

            buttons = ET.SubElement(command_name, "buttons", type='Sos')
            if (self.sos_number_1):
                ET.SubElement(buttons, "dev", number="1", state='1')
            if (self.sos_number_2):
                ET.SubElement(buttons, "dev", number="2", state='1')
            if (self.sos_number_3):
                ET.SubElement(buttons, "dev", number="3", state='1')
            if (self.sos_number_4):
                ET.SubElement(buttons, "dev", number="4", state='1')

            buttons = ET.SubElement(command_name, "buttons", type='HandleBreak')
            if (self.chandle_break_1):
                ET.SubElement(buttons, "dev", number="1", state='1')
            if (self.chandle_break_2):
                ET.SubElement(buttons, "dev", number="2", state='1')
            if (self.chandle_break_3):
                ET.SubElement(buttons, "dev", number="3", state='1')
            if (self.chandle_break_4):
                ET.SubElement(buttons, "dev", number="4", state='1')

            tree = ET.ElementTree(wr_frame)
            tree.write('output.xml')
            xml_frame = ET.tostring(tree.getroot(), encoding='unicode')
            self.sendXMLFrame(xml_frame)

    def sendXMLFrame(self, xml_frame):
        print("XMl Frame in sendXMLFrame: ", xml_frame)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(xml_frame, encoding='utf-8'), (self.IP, self.PORT))

    def openFile(self):
        view = Builder.load_file("main.kv")
        return view

    def build(self):
        checkbox = CheckBox()
        checkbox.bind(active=self.checkbox1)
        checkbox.bind(active=self.checkbox2)
        checkbox.bind(active=self.checkbox3)
        checkbox.bind(active=self.checkbox4)
        checkbox.bind(active=self.checkbox5)
        checkbox.bind(active=self.checkbox6)
        checkbox.bind(active=self.checkbox7)
        checkbox.bind(active=self.checkbox8)
        view = self.openFile()
        return FloatLayout()


def main():
    Window().run()

if (__name__ == "__main__"):
    main()