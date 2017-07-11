from appJar import gui

app = gui("Cookie Clicker Clone", "800x500")
app.setBg("#b5b5b5")
app.addLabel("title", "Cookie Clicker Clone - 0 Cookies")
app.setLabelBg("title", "#a0a0a0")
app.setLabelFont(25)

funds = 0

earning = 1

def press(name):
    global funds
    global earning
    funds += earning
    app.setLabel("title", "Cookie Clicker Clone - %s Cookie(s)" % funds)

def upgrade(name):
    global funds
    global cost
    global earning
    if(funds-cost<0):
        app.warningBox("funds", "You do not have enough cookies!")
        return
    funds -= cost
    cost*=2
    earning+=1
    app.setButton("Upgrade", 'Upgrade your clicks for %s Cookies!' % cost)
    app.setLabel("title", "Cookie Clicker Clone - %s Cookie(s)" % funds)




app.addButton("Get Cookies!", press)

cost = 5

app.addButton("Upgrade", upgrade)
app.setButton("Upgrade", 'Upgrade your clicks for %s Cookies!' % cost)
app.go()
