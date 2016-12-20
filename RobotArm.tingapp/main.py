import roboarm

import tingbot
import tingbot_gui as gui

arm = None

class MomentaryButton(gui.Button):
    def __init__(self, xy, size, align="topleft", parent=None, label="", on_press=None, on_release=None):
        super(MomentaryButton,self).__init__(xy,size,align,label=label)
        self.on_press = on_press
        self.on_release = on_release
        
    def on_touch(self, xy, action):
        if action=="down":
            if self.on_press:
                self.on_press()
            self.pressed = True
            self.update()
        if action=="up":
            if self.on_release:
                self.on_release()
            self.pressed=False
            self.update()
            

            
def make_buttons(arm):
    def light_on(value):
        if value:
            arm.led.on()
        else:
            arm.led.off()
    MomentaryButton(xy=(10,10),
                    size=(85,40),
                    label="Grip",
                    on_press=lambda: arm.grips.close(None),
                    on_release=lambda: arm.grips.stop())
    MomentaryButton(xy=(10,70),
                    size=(85,40),
                    label="Release",
                    on_press=lambda: arm.grips.open(None),
                    on_release=lambda: arm.grips.stop())

    MomentaryButton(xy=(115,10),
                    size=(85,40),
                    label="W Up",
                    on_press=lambda: arm.wrist.up(None),
                    on_release=lambda: arm.wrist.stop())
    MomentaryButton(xy=(115,70),
                    size=(85,40),
                    label="W Down",
                    on_press=lambda: arm.wrist.down(None),
                    on_release=lambda: arm.wrist.stop())

    MomentaryButton(xy=(220,10),
                    size=(85,40),
                    label="E Up",
                    on_press=lambda: arm.elbow.up(None),
                    on_release=lambda: arm.elbow.stop())
    MomentaryButton(xy=(220,70),
                    size=(85,40),
                    label="E Down",
                    on_press=lambda: arm.elbow.down(None),
                    on_release=lambda: arm.elbow.stop())

    MomentaryButton(xy=(10,130),
                    size=(85,40),
                    label="S Up",
                    on_press=lambda: arm.shoulder.up(None),
                    on_release=lambda: arm.shoulder.stop())
    MomentaryButton(xy=(10,190),
                    size=(85,40),
                    label="S Down",
                    on_press=lambda: arm.shoulder.down(None),
                    on_release=lambda: arm.shoulder.stop())

    MomentaryButton(xy=(115,130),
                    size=(85,40),
                    label="Left",
                    on_press=lambda: arm.base.rotate_clock(None),
                    on_release=lambda: arm.base.stop())
    MomentaryButton(xy=(115,190),
                    size=(85,40),
                    label="Right",
                    on_press=lambda: arm.base.rotate_counter(None),
                    on_release=lambda: arm.base.stop())

    gui.ToggleButton(xy=(220,130),
                    size=(85,100),
                    label="Light",
                    align="topleft",
                    callback=light_on)
def run_setup():
    global arm
    if arm is None:
        try:
            arm = roboarm.Arm()
        except Exception as e:
            print e
            gui.message_box(message="No arm found, please connect")
        else:
            make_buttons(arm)
            tingbot.screen.fill("black")
            gui.get_root_widget().update(downwards=True)
            
tingbot.run(run_setup)
