using LinearAlgebra
using Printf

function suma(A::AbstractMatrix, x::Array{Float64,1};)
    n = length(A)
    m = length(x)
    for i in 1:3
        for j in 1:3
            temp = 0
            temp = temp + A[i][j] * x[j]
        end
    end
end

function jacobi(A::AbstractMatrix, b::Array{Float64,1};
            delta::Number=10^-10,
            epsilon::Number=1/2*10^-4,
            maxiter::Integer=100)

    # n = length(b)
    x = zeros(3)
    # println(typeof(x))
    for k in 1:maxiter
        y = x
        for i in 1:3
            sum = b[i]
            diag = A[i][i]
            if abs(diag) < epsilon
                println("diagonal element too small")
            end
            for j in 1:3
                if j != i
                    sum = sum - A[i][j] * y[j]
                end
            end
            x[i] = sum / diag
        end
        println(k, x)
        if norm(x - y) < epsilon
            println(k, x)
        end
    end
    print(x)
end


A = [1.0 9 1; 4 1 -1; 1 -3 12]
b = [5.0; 3; 31;]

jacobi(A, b)

# n = length(A)
# println(n)
# x = zeros(3)

# println(suma(A, x))
