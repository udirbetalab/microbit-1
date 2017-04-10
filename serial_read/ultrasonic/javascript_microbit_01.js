let ping = 0
basic.forever(() => {
    ping = sonar.ping(
        DigitalPin.P0,
        DigitalPin.P1,
        PingUnit.Centimeters
    )
    serial.writeNumber(ping)
    basic.showNumber(ping)
})
