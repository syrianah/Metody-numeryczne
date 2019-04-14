struct CubicSpline{T<:Number, U<:Number, V<:Number}
  x::Array{T,1}
  y::Array{U,1}
  z::Array{V,1}

  function CubicSpline(x::Array{T,1}, y::Array{U,1}, z0::W, zN::W) where {T<:Number, U<:Number, W<:Number}
    length(x) == length(y) || error("arrays must have the same length")
    n = length(x)
    V = typeof((x[1]*y[1])/one(x[1]))
    h = zeros(V, n-1)
    b = zeros(V, n-1)
    u = zeros(V, n-2)
    v = zeros(V, n-2)
    z = zeros(V, n)
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
    z[n] = zN
    for i = (n-1):-1:2
      z[i] = (v[i-1] - h[i]z[i+1])/u[i-1]
    end
    z[1] = z0
    new{T, U, V}(x, y, z)
  end

  function CubicSpline(x::Array{T,1}, y::Array{U,1}) where {T<:Number, U<:Number}
    CubicSpline(x, y, 0, 0)
  end
end

function cubicSplineEval(s::CubicSpline{T, U, V}, x::W) where {T<:Number, U<:Number, V<:Number, W<:Number}
  n = length(s.x)
  k = n-1
  while (k >= 1) && (x - s.x[k] < 0)
    k -= 1
  end
  h = s.x[k+1] - s.x[k]
  tmp = (s.z[k]/2) + (x - s.x[k])*(s.z[k+1] - s.z[k])/(6h)
  tmp = -(h/6)*(s.z[k+1] + 2s.z[k]) + (s.y[k+1] - s.y[k])/h + tmp*(x - s.x[k])
  return s.y[k] + tmp*(x - s.x[k])
end

(s::CubicSpline)(x) = cubicSplineEval(s, x)

function interpolateParametricCurve(txys::Array{Tuple{T,U,V}, 1}) where {T<:Number, U<:Number, V<:Number}
  ts = map(x->x[1], txys)
  xs = map(x->x[2], txys)
  ys = map(x->x[3], txys)
  (CubicSpline(ts,xs), CubicSpline(ts,ys))
end

function plotParametricCurve(txys::Array{Tuple{T,U,V}, 1}, n::Integer) where {T<:Number, U<:Number, V<:Number}
  xs = map(x->x[2], txys)
  ys = map(x->x[3], txys)
  plot(xs, ys, seriestype=:scatter)

  sx, sy = interpolateParametricCurve(txys)
  ts = map(x->x[1], txys)
  start = minimum(ts)
  finish = maximum(ts)
  ts=range(start, stop=finish, length=n)
  plot!(sx.(ts), sy.(ts))
end

function interpolateParametricCurve(ts::Array{T, 1}, x::Function, y::Function) where {T<:Number}
  xs = x.(ts)
  ys = y.(ts)
  (CubicSpline(ts,xs), CubicSpline(ts,ys))
end

function plotParametricCurve(ts::Array{T, 1}, x::Function, y::Function, n::Integer) where {T<:Number}
  plot(x.(ts), y.(ts), seriestype=:scatter)

  sx, sy = interpolateParametricCurve(ts, x, y)
  start = minimum(ts)
  finish = maximum(ts)
  ts=range(start, stop=finish, length=n)
  plot!(sx.(ts), sy.(ts))
end
