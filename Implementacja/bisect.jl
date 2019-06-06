using Printf

function bisect(f::Function, a::Number, b::Number;
                delta::Number=eps(1.0),
                epsilon::Number=eps(1.0),
                maxiter::Integer=100)
  k = 0;
  fa = f(a);
  fb = f(b);
  @printf("a    = %30.26f, f(a   ) = %30.26f\n", a, fa)
  @printf("b    = %30.26f, f(b   ) = %30.26f\n", b, fb)
  if sign(fa) == sign(fb)
    error("MiÄdzy zadanymi wartoĹciami " *
      "niekoniecznie znajdziemy pierwiastek")
  end
  e = b - a;
  for i in 1:maxiter
    e = e/2;
    c = a + e;
    fc = f(c);
    @printf("x%-3d = %30.26f, f(x%-3d) = %30.26f\n", i, c, i, fc)
    if abs(fc) < epsilon || abs(e) < delta
      break
    end
    if sign(fc) != sign(fa)
      b = c;
      fb = fc;
    else
      a = c;
      fa = fc;
    end
  end
end


# Zadanie 7.6
# f(x) = x^3 + x - 1
# bisect(f, 0, 1)

# Zadanie 7.7
# f(x) = 1 / x - tan(x)
# halfpi = pi / 2
# bisect(f, 0, halfpi)

#Zadanie 4
f(x) = 11/x - 5
bisect(f, 2, 3)