from appJar import gui
import threading
app = gui("Cookie Clicker Clone", "800x500")
app.setBg("#b5b5b5")
app.addLabel("title", "Cookie Clicker Clone - 0 Cookie(s)")
app.setLabelBg("title", "#a0a0a0")
app.setLabelFont(25)

funds = 0

earning = 1

def update_header():
    global funds
    app.setLabel("title", "Cookie Clicker Clone - %s Cookie(s)" % funds)


def press(name):
    global earning
    global funds
    funds += earning
    update_header()

def upgrade(name):
    global funds
    global clicker_cost
    global earning
    if(funds-clicker_cost<0):
        app.warningBox("funds", "You do not have enough cookies!")
        return
    funds -= clicker_cost
    clicker_cost*=2
    earning+=1
    app.setButton("Upgrade", 'Upgrade your clicks for %s Cookies!' % clicker_cost)
    update_header()


passive_income = 0

def passive_income_generator():
    global passive_income
    global funds
    print("generating income")
    funds+=passive_income
    update_header()
    threading.Timer(1.0, passive_income_generator).start()



def grandma(name):
    global funds
    global grandma_cost
    global earning
    global passive_income
    if(funds-grandma_cost<0):
        app.warningBox("funds", "You do not have enough cookies!")
        return
    funds -= grandma_cost
    passive_income+=1
    grandma_cost = int(1.5 * grandma_cost)
    app.setButton("Grandma", 'Buy a grandma for %s cookies' % grandma_cost)
    update_header()


app.addButton("Get Cookies!", press)

clicker_cost = 5

app.addButton("Upgrade", upgrade)
app.setButton("Upgrade", 'Upgrade your clicks for %s Cookies!' % clicker_cost)

grandma_cost = 10
app.addButton("Grandma", grandma)
app.setButton("Grandma", 'Buy a grandma for %s cookies' % grandma_cost)

threading.Timer(1.0, passive_income_generator).start()

app.go()
