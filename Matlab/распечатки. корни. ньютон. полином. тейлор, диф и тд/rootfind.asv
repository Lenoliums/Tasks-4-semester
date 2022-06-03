%% 3 a
clear
x = -3:0.01:3; % интервал от -3 до 3 с шагом 0.01
f = sin(exp(x));
plot(x,f);
xlim([-3 3]); %ограничение оси графика

grid on %сетка
hold on
nears = [1 2 2.2 2.5 2.7 3];
for i = nears
    r = fzero('sin(exp(x))', i);
    plot(i, sin(exp(i)), 'b*');
    plot(r, sin(exp(r)), 'r*');
end
%% 3b
clear
x = 0:0.01:2*pi;
f = sin(x.*(x-1));
plot(x,f);
xlim([0 2*pi]);
grid on
hold on
nears = [1 2 3 3.5 4 4.5 5 5.2 5.5 5.9 6.1];
for i = nears
    r = fzero('sin(x*(x-1))', i);
    plot(i, sin(i*(i-1)), 'b*')
    plot(r, sin(r*(r-1)), 'r*');
end
%% 3e
clear
x = 0:0.01:4*pi;
f = x.*sin(x)-cos(x);
plot(x,f);
xlim([0,4*pi]);
grid on
hold on
nears = [1 3 6 9.5];
for i = nears
    r = fzero('x*sin(x)-cos(x)', i);
    plot(i, i*sin(i)-cos(i), 'g*')
    plot(r, r*sin(r)-cos(r), 'r*');
end

%% 4
clear
clc
syms x;
f = x^2 + 1==0;
disp(fzero('x^2+1', 0));
disp(solve(f));
%% 5
clc
syms x;
hold on
f = cos(x) - exp(0.001-x^2)==0;
r = -3:0.01:3;
y = cos(r) - exp(0.001-r.^2);
plot(r,y)
s=solve(f);
fr=fzero('cos(x)-exp(0.001-x^2)',1);
plot(fr,cos(fr) - exp(0.001-fr^2), 'r*');
grid on
disp(s);
disp(fr);

%% Ньютон b
%% Задача 1 b
clear
syms x
a = 1; % f(a) > 0
b = 2; % f(b) < 0
f = sin(x) / x;
fplot(f, [-2*pi 2*pi]); % график символьной функции
grid on
hold on

df = diff(f);
e = 1e-5; %
xk = (a + b) / 2;
yk = subs(f, x, xk); % символ. замена - вычисление симв. функц.
k = 0; % счетчик итераций
while abs(yk) > e
xnk = xk - subs(f, x, xk) / subs(df, x, xk);
xk = xnk;
yk = subs(f, x, xnk);
k = k + 1;
end
plot(xk, subs(f, x, xk), 'rO');
text(xk + 0.4, subs(f, x, xk), string(k) + ' iterations');

a = -4; b = -2;
xk = (a + b) / 2;
yk = subs(f, x, xk);
k = 0;
while abs(yk) > e
xnk = xk - subs(f, x, xk) / subs(df, x, xk);
xk = xnk;
yk = subs(f, x, xnk);
k = k + 1;
end
plot(xk, subs(f, x, xk), 'rO');
text(xk + 0.4, subs(f, x, xk), string(k) + ' iterations');


%% Полиномы
%% 1 
clear
clc
P = [1, 4, -2, -14, -3, -18];
x = linspace(-10,10,1000);
F = polyval(P,x);
plot(x,F)
grid on;
hold on;
a = roots(P);
disp(a);
for i = a
    plot(a(1),0., 'ro')
end
%% 1
clear
clc
syms x %сивольная функция для символьных вычислений
f = x^5 + 4*x^4 - 2*x^3 - 14*x^2 - 3*x - 18;
disp(factor(f))
%% 2.1 2.2 2.3
clc
clear
syms x
f_1 = x*exp(-x);
f_2 = tan(x)^(tan(2*x));
f_3 = atan(1/(1-x));
disp(limit(f_1, inf));
disp(limit(f_2, pi/4));
a = 0;
disp(limit(f_3, x, a, 'Right'));
%% 3 1,2,3
clear
clc
syms x
f_1 = atan(x)/2 - x/(2^(1+x^2)^2);
f_2 = 3*x^4 - 14*x^3 + 12*x^2 + 24*x + 6;
f_3 = (sin(3*x) - cos(3*x))^2;
disp(simplify(diff(f_1))); %сводит к более простому виду (выносит общие члены и тд)
disp(simplify(diff(f_2)));
disp(simplify(diff(f_3)));
%% 4
clear
syms x
f_1 = sqrt(1-x^2)/x^2;
f_2 = 1/sin(x)^3;
f_3 = (sin(2*x) + 1)^(1/7) * cos(2*x);
f_5 = 1/(1+x^2);
disp(int(f_1,x));
disp(int(f_2,x));
disp(int(f_3,x));
disp(int(f_5,x, 0, inf));
%% 5.1
clear
clc
syms k n;
f = symsum(1/(k^2), k, 1, n);
disp(limit(f, n, inf));
%% 6.1
clc
syms x;
f = exp(x);
a = 0;
n = 5;
disp(taylor(f, x, a, 'Order', n));
