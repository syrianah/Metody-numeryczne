using Printf

function newton(f::Function, fp::Function, x::Number;
                delta::Number=eps(1.0),
                epsilon::Number=eps(1.0),
                maxiter::Integer=100)
    fx = f(x)
    @printf("x0   = %30.26f, f(x0  ) = %30.26f\n", x, fx)
    for i in 1:maxiter
        if abs(fx) < epsilon
            return x
        end
        next = x - fx/fp(x)
        fx = f(next)
        @printf("x%-3d = %30.26f, f(x%-3d) = %30.26f\n", i, next, i, fx)
        if abs(next-x) < delta
            return x
        end
        x = next
    end
    error("Max iteration exceeded")
end

# Zadanie 7.6
f(x) = x^3 + x - 1
newton(f, 0, 1)
