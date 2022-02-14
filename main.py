def onEvery_interval():
    basic.show_icon(IconNames.ANGRY)
    basic.show_string("AHOJ!")
    basic.show_arrow(ArrowNames.NORTH)
    pass
loops.every_interval(500, onEvery_interval)