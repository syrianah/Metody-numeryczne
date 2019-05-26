using Printf
using LinearAlgebra


function richardson(A::AbstractMatrix, Q::AbstractMatrix, b::Array{Float64,1};
            delta::Number=eps(1.0),
            epsilon::Number=eps(1.0),
            maxiter::Integer=2)

    n = length(b)
    x = zeros(n)
    println(typeof(x))
    for i in 1:10
        y = x
        c = (Q - A) * x + b
        # c = Q * x
        x = inv(Q) * c
        println(i, x)
        # maxiter = maxiter + 1
        if norm(x - y, i) < epsilon
            println("convergence")
            break
        end
    end
end

A = [1.0 9 1; 4 1 -1; 1 -3 12]
Q = Matrix{Float64}(I, 3, 3)
b = [5.0; 3; 31;]

println(typeof(A))
println(typeof(Q))
println(typeof(b))

richardson(A, Q, b)

# n = length(b)
# x = zeros(n)
# println(x)
#
# X = (Q - A) * x + b
# x = X / Q
# println(x)
