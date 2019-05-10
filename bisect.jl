function bisect(f::Function, a::AbstractFloat, b::AbstractFloat;
                delta::AbstractFloat=eps(a), epsilon::AbstractFloat=eps(b),
                maxiter::Integer=100)
k = 0;
fa = f(a);
fb = f(b);
@printf("a      = %30.26f, f(a) = %30.26f\n", a, fa)
@printf("b      = %30.26f, f(b) = %30.26f\n", b, fb)
if sign(fa) == sign(fb)
error("Między zadanymi wartościami " * "niekoniecznie znajdziemy pierwiastek")
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
