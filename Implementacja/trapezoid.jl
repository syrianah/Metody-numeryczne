function trapezoid(f::Function, a::Number, b::Number,
                   n::Integer)
  h = (b - a)/n;
  result = 0
  for i in 0:(n-1)
    result += f(a+i*h) + f(a+(i+1)*h);
  end
  result *= h/2;
  print(result)
end

f(x) = sin(3x)
a=-2
b=2

trapezoid(f, a, b, 3)
