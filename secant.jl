using Printf

function secant(f::Function, a::Number, b::Number;
            delta::Number=eps(1.0),
            epsilon::Number=eps(1.0),
            maxiter::Integer=50)

    fa = f(a)
    fb = f(b)

    if abs(fa) > abs(fb)
        a = b
        fa = fb
    end
    println(0, a, fa)
    println(1, b, fb)
    for i in 2:maxiter
        if abs(fa) > abs(fb)
            a = b
            fa = fb
        end
        d = (b - a) / (fb - fa)
        b = a
        fb = fa
        d = d * fa
        if abs(d) < epsilon
            @printf("convergence")
        end
        a = a - d
        fa = f(a)
        println(i, a, fa)
    end
end

# Zadanie 7.6
f(x) = x^3 + x - 1
secant(f, 0, 1)
