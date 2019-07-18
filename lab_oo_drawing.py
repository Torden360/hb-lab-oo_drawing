
In [1]: import cs1graphics as cg

In [2]: paper = cg.Canvas()

In [3]: paper.setBackgroundColor("skyBlue")

In [4]: paper.setWidth(800)

In [5]: paper.setHeight(600)

In [6]: paper.setTitle("My World in Blue")

In [7]: paper
Out[7]: <cs1graphics.Canvas at 0x7fc6e88a4828>

In [8]: sun = cg.Circle()

In [9]: paper.add(sun)

In [10]: sun.setFillColor('yellow')

In [11]: sun.setRadius(50)

In [12]: sun.moveTo(700,100)

In [13]: sunCenter = cg.Point(700, 100)

In [14]: sun2 = cg.Circle(50, sunCenter)

In [15]: sun2.setFillColor('purple')

In [16]: sun2.setFillColor('blue')

In [17]: sun2.setFillColor('purple')

In [18]: sun2.moveTo(600,150)

In [19]: sun.moveTo(600,150)

In [20]: paper.add(sun2)

In [21]: sun.moveTo(700,100)

In [22]: sun2 = cg.Circle(50, cg.Point(700, 100))

In [23]: paper.add(sun2)

In [24]: sun.moveTo(500,100)

In [25]: sun2.moveTo(200,100)

In [26]: facade = cg.Square(200, cg.Point(400,350))

In [27]: facade.setFillColor("white")

In [28]: paper.add(facade)

In [29]: chimney = cg.Rectangle(50,70,cg.Point(450,215))

In [30]: chimney.setFillColor("red")

In [31]: paper.add(chimney)

In [32]: tree = cg.Polygon(cg.Point(150,220),cg.Point(120,380),cg.Point(180,380)
    ...: )

In [33]: tree.setFillColor("darkGreen")

In [34]: paper.add(tree)

In [35]: subraySW = cg.Path(cg.Point(660,140), cg.Point(635,165))

In [36]: sunraySE.setBorderColor('yellow')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-36-118b18eb9539> in <module>()
----> 1 sunraySE.setBorderColor('yellow')

NameError: name 'sunraySE' is not defined

In [37]: sunraySW.setBorderColor('yellow')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-37-b6c6af0feda2> in <module>()
----> 1 sunraySW.setBorderColor('yellow')

NameError: name 'sunraySW' is not defined

In [38]: subraySE.setBorderColor('yellow')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-38-dddc4f9a6a42> in <module>()
----> 1 subraySE.setBorderColor('yellow')

NameError: name 'subraySE' is not defined

In [39]: subraySW.setBorderColor('yellow')

In [40]: subraySW.setBorderWidth(6)

In [41]: paper.add(subraySW)

In [42]: sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))

In [43]: sunraySE.setBorderColor('yellow')

In [44]: sunraySE.setBorderWidth(6)

In [45]: paper.add(sunraySE)

In [46]: sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765, 35)))
  File "<ipython-input-46-30a8f8bcacbb>", line 1
    sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765, 35)))
                                                           ^
SyntaxError: invalid syntax


In [47]: sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765, 35))

In [48]: sunrayNE.setBorderColor('yellow')

In [49]: sunrayNE.setBorderWidth(6)

In [50]: paper.add(sunrayNE)

In [51]: sunrayNW = cg.Path(cg.Point(660,60), cg.Point(635,35))

In [52]: sunrayNW.setBorderColor('yellow
  File "<ipython-input-52-d722d8b07d2c>", line 1
    sunrayNW.setBorderColor('yellow
                                   ^
SyntaxError: EOL while scanning string literal


In [53]: sunrayNW.setBorderColor('yellow')

In [54]: sunrayNW.setBorderWidth(6)

In [55]: paper.add(sunrayNW)

In [56]: chimney.getDepth()
Out[56]: 50

In [57]: grass = cg.Rectangle(800,300,cg.Point(400,450))

In [58]: grass.setFillColor("green")

In [59]: grass.setBorderColor("green")

In [60]: grass.setDepth(75)

In [61]: paper.add(grass)

In [62]: window = cg.Square(30, cg.Point(450,400))

In [63]: window.setFillColor("pink")

In [64]: window.setDepth(30)

In [65]: paper.add(window)

In [66]: sun.Point()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-66-1d88c0f6decd> in <module>()
----> 1 sun.Point()

AttributeError: 'Circle' object has no attribute 'Point'

In [67]: cg.Point(400,350)
Out[67]: <cs1graphics.Point at 0x7fc6e8114a90>

In [68]: window.moveTo(400,200)

In [69]: window.moveTo(300,300)

In [70]: window.moveTo(350,350)

In [71]: window.moveTo(350,300)

In [72]: roof = cg.Polygon(cg.Point(300,220),cg.Point(360,200),cg.Point(500,220)
    ...: )

In [73]: roof.FillColor("pink")
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-73-fdd7c7eba96e> in <module>()
----> 1 roof.FillColor("pink")

AttributeError: 'Polygon' object has no attribute 'FillColor'

In [74]: roof.setFillColor("pink")

In [75]: roof.setDepth(40)

In [76]: paper.add(roof)

In [77]: roof.moveTo(350,250)

In [78]: roof.moveTo(320,250)

In [79]: roof.moveTo(300,250)

In [80]: roof.moveTo((100,250),(200,50),(300,25))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-80-638cba3176cf> in <module>()
----> 1 roof.moveTo((100,250),(200,50),(300,25))

TypeError: moveTo() takes 3 positional arguments but 4 were given
