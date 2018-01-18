let item3: neopixel.Strip = null
let random3 = 0
let item2: neopixel.Strip = null
let random2 = 0
let item: neopixel.Strip = null
let random = 0
let mode = 0
let led_strip = 0
let led2 = 0
function blank()  {
    item.showColor(neopixel.rgb(0, 0, 0))
    item2.showColor(neopixel.rgb(0, 0, 0))
    item3.showColor(neopixel.rgb(0, 0, 0))
    item.show()
    item2.show()
    item3.show()
}
function _3stripe()  {
    blank()
    while (mode == 2) {
        for (let led2 = 0; led2 <= led_strip; led2++) {
            item.setPixelColor(led2, neopixel.colors(NeoPixelColors.Red))
            item.show()
            basic.pause(100)
            item.clear()
        }
        for (let led2 = 0; led2 <= led_strip; led2++) {
            item2.setPixelColor(led2, neopixel.colors(NeoPixelColors.Red))
            item2.show()
            basic.pause(100)
            item2.clear()
        }
        for (let led2 = 0; led2 <= led_strip; led2++) {
            item3.setPixelColor(led2, neopixel.colors(NeoPixelColors.Red))
            item3.show()
            basic.pause(100)
            item3.clear()
        }
    }
}
input.onButtonPressed(Button.A, () => {
    mode += 1
})
input.onButtonPressed(Button.B, () => {
    mode += -1
})
input.onButtonPressed(Button.AB, () => {
    mode = 0
})
function stars()  {
    random = Math.random(led_strip + 1)
    random2 = Math.random(led_strip + 1)
    random3 = Math.random(led_strip + 1)
    item.setPixelColor(random, neopixel.colors(NeoPixelColors.White))
    item.setPixelColor(random3 / 2, neopixel.colors(NeoPixelColors.White))
    item2.setPixelColor(random2, neopixel.colors(NeoPixelColors.White))
    item2.setPixelColor(random / 2, neopixel.colors(NeoPixelColors.White))
    item3.setPixelColor(random3, neopixel.colors(NeoPixelColors.White))
    item3.setPixelColor(random2 / 2, neopixel.colors(NeoPixelColors.White))
    item.show()
    item.clear()
    item2.show()
    item2.clear()
    item3.show()
    item3.clear()
    basic.pause(300)
}
function _3rainbow()  {
    item.showRainbow(1, 360)
    item2.showRainbow(1, 360)
    item3.showRainbow(1, 360)
    while (mode == 3) {
        item.rotate(1)
        item2.rotate(2)
        item3.rotate(3)
        item.show()
        item2.show()
        item3.show()
        basic.pause(100)
    }
}
led_strip = 24
item = neopixel.create(DigitalPin.P0, led_strip, NeoPixelMode.RGB)
item2 = neopixel.create(DigitalPin.P1, led_strip, NeoPixelMode.RGB)
item3 = neopixel.create(DigitalPin.P2, led_strip, NeoPixelMode.RGB)
led2 = 0
mode = 0
basic.forever(() => {
    while (mode == 0) {
        blank()
    }
    while (mode == 3) {
        _3rainbow()
    }
    while (mode == 2) {
        _3stripe()
    }
    while (mode == 1) {
        stars()
    }
})
