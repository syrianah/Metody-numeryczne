using LinearAlgebra
using Printf

function jacobi(A::AbstractMatrix, b::Array{Float64,1};
            delta::Number=10^-10,
            epsilon::Number=1/2*10^-4,
            maxiter::Integer=100)

    n = length(b)
    x = zeros(n)
    println()
    diag = Diagonal(A)
    println(broadcast(abs, diag))
    println(diag[1][1], inv(diag))
    for k in 1:maxiter
        y = x
        for i in 1:n
            sum = b[i]
            # if broadcast(abs, diag) < epsilon
            #     println("diagonal element too small")
            # end
            for j in 1:n
                if j != i
                    @inbounds sum = sum - diag[i][j] * y[i]
                end
            end
            x[i] = \(sum, diag)
        end
        # println(k, x)
        # if norm(x - y) < epsilon
        #     println(k, x)
        # end
    end
    println(x)
end


A = [1.0 9 1; 4 1 -1; 1 -3 12]
b = [5.0, 3, 31,]

jacobi(A, b)

# n = length(A)
# println(n)
# x = zeros(3)

# println(suma(A, x))
