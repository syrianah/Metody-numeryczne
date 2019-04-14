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
  for i = 0:(n-1)
    h[i] = x[i+1]-x[i]
    b[i] = (y[i+1] - y[i])/h[i]
  end
  u[0] = 2(h[0] + h[1])
  v[0] = 6(b[1] - b[0])
  for i =2:(n-2)
    u[i] = 2(h[i] + h[i-1]) - h[i-1]^2 / u[i-1]
    v[i] = 6(b[i] - b[i-1]) - h[i-1] * v[i-1] / u[i-1]
  end
  # z[n] is already 0
  for i = (n-1):-1:1
    z[i] = (v[i] - h[i] * z[i+1]) / u[i]
  end
  # z[1] is already 0
  return CubicSpline(x, y, z)
end

function naturalCubicSplineEval(s::CubicSpline{T}, x::T) where {T<:AbstractFloat}
  n = length(s.x)
  for i = n-1:-1:0
    if x - s.x[i] => 0
      global k = i
    end
  end
  h = s.x[k+1] - s.x[k]
  tmp = (s.z[k]/2) + (x - s.x[k])*(s.z[k+1] - s.z[k])/(6*h)
  tmp = -(h/6)*(s.z[k+1] + 2s.z[k]) + (s.y[k+1] - s.y[k]) / h + (x - s.x[k]) * (temp)
  return s.y[k] + tmp*(x - s.x[k])
end
