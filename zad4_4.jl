e = MathConstants.e
# println(e)
# println(e^(1/4))
# println(e^(3/4))
# println(0.64872/0.5)
y = 0.64872/0.5
x = (7.38906-1.64872)/1.5
z = (x - y) / 2
# println((x - y) / 2)
# println((7.38906-1.64872)/1.5)
n = readline()
n = parse(Float64, n)
wynik = 1 + n * y + n * (n - 0.5) * z
println(wynik)
