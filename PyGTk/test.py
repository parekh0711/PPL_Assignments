import gi
import math
PI = math.pi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import cairo


surface = None
global sze
sze=5
shape=False
def clear_surface():
    global surface
    cr = cairo.Context(surface)
    cr.set_source_rgb(1,1,1)
    cr.paint()
    del cr

def configure_event_cb(wid,evt):
    global surface

    if surface is not None:
        del surface
        surface = None

    win = wid.get_window()
    width = wid.get_allocated_width()
    height = wid.get_allocated_height()

    surface = win.create_similar_surface(
        cairo.CONTENT_COLOR,
        width,
        height)

    clear_surface()
    return True


def draw_cb(wid,cr):
    global surface

    cr.set_source_surface(surface,0,0)
    cr.paint()
    return False


def draw_brush(wid,x,y):
    global surface
    clr= col.get_current_rgba()
    cr = cairo.Context(surface)
    cr.set_source_rgb(clr.red,clr.green,clr.blue)
    cr.rectangle(x-3,y-3,sze,sze)
    cr.fill()
    del cr

    wid.queue_draw_area(x-3,y-3,sze,sze)

def draw_rectangle(wid,x,y):
    global surface
    clr= col.get_current_rgba()
    cr = cairo.Context(surface)
    cr.set_source_rgb(clr.red,clr.green,clr.blue)
    l=shape_length.get_value()
    b=shape_width.get_value()
    cr.rectangle(x-3,y-3,l,b)
    cr.set_line_width(sze)
    cr.stroke()
    del cr
    wid.queue_draw_area(x-3,y-3,l,b)

def draw_circle(wid,x,y):
    global surface
    clr= col.get_current_rgba()
    cr = cairo.Context(surface)
    cr.set_source_rgb(clr.red,clr.green,clr.blue)
    r=shape_radius.get_value()
    cr.arc(x-3,y-3,r,0,2*PI)
    cr.set_line_width(sze)
    cr.stroke()
    del cr
    wid.queue_draw_area(300,0,1100,800)

def draw_ellipse(wid,x,y):
    global surface
    clr= col.get_current_rgba()
    cr = cairo.Context(surface)
    cr.set_source_rgb(clr.red,clr.green,clr.blue)
    r=shape_radius.get_value()
    l=shape_length.get_value()
    b=shape_width.get_value()
    cr.translate(x+b/2,y+l/2)
    cr.scale(b/2,l/2)
    cr.arc(0,0,r, 0, 2*PI)
    cr.set_line_width(sze)
    cr.stroke()
    del cr
    wid.queue_draw_area(0,0,9000,9000)

def button_press_event_cb(wid,evt):
    global surface

    if surface is None:
        return False

    if evt.button == Gdk.BUTTON_PRIMARY:
        global shape
        if shape==True:
            if evt.x>50:
                if type_of_shape=="Rectangle":
                    draw_rectangle(wid,evt.x,evt.y)
                if type_of_shape=="Circle":
                    draw_circle(wid,evt.x,evt.y)
                if type_of_shape=="Ellipse":
                    draw_ellipse(wid,evt.x,evt.y)
                shape=False
        else :
            if evt.x>50:
                draw_brush(wid,evt.x,evt.y)
    elif evt.button == Gdk.BUTTON_SECONDARY:
        clear_surface()
        wid.queue_draw()

    return True


def motion_notify_event_cb(wid,evt):
    global surface

    if surface is None:
        return False

    if evt.state & Gdk.EventMask.BUTTON_PRESS_MASK:
        draw_brush(wid,evt.x,evt.y)

    return True


def close_window(wid):
    global surface
    if surface is not None:
        del surface
        surface = None
    Gtk.main_quit()

def on_increase_clicked(self):
    global sze
    sze+=1
    return

def on_decrease_clicked(self):
    global sze
    if sze>0:
        sze-=1
    return

def shape_click(self):
    global shape
    shape=True
    global type_of_shape
    type_of_shape=button3.get_active_text()
    return

def save_file(self):
    global surface
    filename=button5.get_text()
    surface.write_to_png(filename)


win = Gtk.Window()
win.set_title('P Paint')
win.connect('destroy',close_window)
win.set_border_width(8)

grid = Gtk.Grid()

col = Gtk.ColorSelection(has_palette=True) #Color Pallete

button1 = Gtk.Button(label="Width++")   #Width of brush
button2= Gtk.Button(label="Width--")

button3=Gtk.ComboBoxText()
button3.append("1","Rectangle")
button3.append("2","Ellipse")
button3.append("3","Circle")
button4=Gtk.Button(label="Ok")
button5=Gtk.Entry()
button6=Gtk.Button(label="Save")
button5.set_text("Enter file name with extn")

range=Gtk.Adjustment(lower=1,upper=1000,step_increment=1)
range2=Gtk.Adjustment(lower=1,upper=1000,step_increment=1)
range3=Gtk.Adjustment(lower=1,upper=750,step_increment=1)

shape_length=Gtk.SpinButton(adjustment=range)
shape_width=Gtk.SpinButton(adjustment=range2)
shape_radius=Gtk.SpinButton(adjustment=range3)

listb=Gtk.ListBox()
listb.set_selection_mode(Gtk.SelectionMode.NONE)

row = Gtk.ListBoxRow()
row2= Gtk.ListBoxRow()
row3= Gtk.ListBoxRow()

label1 = Gtk.Label(label="Length ")
label2 = Gtk.Label(label="Breadth")
label3 = Gtk.Label(label="Radius ")
hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)

hbox.add(label1)
hbox.add(shape_length)
hbox2.add(label2)
hbox2.add(shape_width)
hbox3.add(label3)
hbox3.add(shape_radius)

row.add(hbox)
row2.add(hbox2)
row3.add(hbox3)

listb.add(row)
listb.add(row2)
listb.add(row3)

win.add(grid)
da = Gtk.DrawingArea()
da.set_size_request(1300,800)
grid.attach(col,0,0,100,100)
grid.attach_next_to(da,col,Gtk.PositionType.RIGHT,1300,800)
grid.attach(button1,2,300,1,1)
grid.attach_next_to(button2,button1,Gtk.PositionType.RIGHT,1,1)
#
grid.attach(button3,2,330,1,1)
grid.attach(listb,2,335,7,7)
grid.attach(button4,2,350,1,1)
grid.attach(button5,2,500,10,10)
grid.attach_next_to(button6,button5,Gtk.PositionType.BOTTOM,1,1)
# grid.attach_next_to(listb,button3,Gtk.PositionType.BOTTOM,1,1)

da.connect('draw',draw_cb)
da.connect('configure-event',configure_event_cb)
button1.connect("clicked", on_increase_clicked)
button2.connect("clicked", on_decrease_clicked)
button4.connect("clicked", shape_click)
button6.connect("clicked", save_file)
da.connect('motion-notify-event',motion_notify_event_cb)
da.connect('button-press-event',button_press_event_cb)

da.set_events(da.get_events() | Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.POINTER_MOTION_MASK)

win.show_all()
Gtk.main()
