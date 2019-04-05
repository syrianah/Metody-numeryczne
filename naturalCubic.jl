struct CubicSpline{T<:AbstractFloat}
  x::Array{T,1}
  y::Array{T,1}
  z::Array{T,1}
end

function naturalCubicSplineInterpolation(x::Array{T}, y::Array{T}) where {T<:AbstractFloat}
  n = length(x)
  h = zeros(n-1)
  b = zeros(n-1)
  u = zeros(n-2)
  v = zeros(n-2)
  z = zeros(n)
  for i = 1:(n-1)
    h[i] = x[i+1]-x[i]
    b[i] = (y[i+1] - y[i])/h[i]
  end
  u[1] = 2(h[2] + h[1])
  v[1] = 6(b[2] - b[1])
  for i =2:(n-2)
    u[i] = 2(h[i+1] + h[i]) - h[i]^2/u[i-1]
    v[i] = 6(b[i+1] - b[i]) - h[i]v[i-1]/u[i-1]
  end
  # z[n] is already 0
  for i = (n-1):-1:2
    z[i] = (v[i-1] - h[i]z[i+1])/u[i-1]
  end
  # z[1] is already 0
  return CubicSpline(x, y, z)
end

function naturalCubicSplineEval(s::CubicSpline{T}, x::T) where {T<:AbstractFloat}
  n = length(s.x)
  for i = n-1:-1:1
    if x - s.x[i] == 0
      global k = i
    end
  end
  h = s.x[k+1] - s.x[k]
  tmp = (s.z[k]/2) + (x - s.x[k])*(s.z[k+1] - s.z[k])/(6h)
  tmp = -(h/6)*(s.z[k+1] + 2s.z[k]) + (s.y[k+1] - s.y[k])/h + tmp*(x - s.x[k])
  return s.y[k] + tmp*(x - s.x[k])
end
