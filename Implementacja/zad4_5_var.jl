x1 = parse(Float64, readline())
x2 = parse(Float64, readline())
x3 = parse(Float64, readline())
y1 = parse(Float64, readline())
y2 = parse(Float64, readline())
y3 = parse(Float64, readline())

ws1 = (y2 - y1) / (x2 - x1)
ws2 = (y3 - y2) / (x3 - x2)
ws3 = (ws2 - ws1) / (x3 - x1)

war = 0.25

wynik = y1 + (war - x1) * ws1 + (war - x1) * (war - x2) * ws3

println("Współczynniki:")
println(y1)
println(ws1)
println(ws3)
println("Wartość:")
println(wynik)
