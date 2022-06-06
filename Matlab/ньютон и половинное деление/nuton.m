%% правильный ньютон
clc;
clear
f1=figure;
fun = @(x) 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .* x) - 0.2).^2;
x = linspace(0, 7, 100);
y = 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .*x) - 0.2).^2;
hold on;
grid on;
xlim([0 7]);
ylim([-2 8]);
xlabel('x');
ylabel('y');
plot(x, y);
z = ginput(1);
x_left = z(1,1);
plot(x_left, fun(x_left), 'g*');

eps = 0.00001;
h = 1e-14;

fun_dif= @(x)(fun(x + h) - fun(x))/h;
x=-20:0.07:20;

x_n=x_left;
x_l=x_n;
x_r=x_n;
for iter = 1 : 1000
    x_n_x_fun =fun(x_n) - (x_n - x) .* fun_dif(x_n); 
    x_n = x_n - fun(x_n) / fun_dif(x_n);
    plot(x, x_n_x_fun, '--c', 'linewidth', 0.7);
    if x_n < x_l 
        x_l=x_n;
    end
    if x_n > x_r 
        x_r=x_n;
    end
    if abs(fun(x_n)) < eps 
        disp(iter);
        break;
    end
    plot(x_n, fun(x_n), 'b*');
    plot(x_n, 0, 'b.', 'MarkerSize', 15);
end
xlim([x_l-1 x_r+1])
x = x_l-1:0.07:x_r+1;
y = 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .*x) - 0.2).^2;
plot(x, y)
plot(x, x.*0, '--g', 'linewidth', 2);
plot(x_n, fun(x_n), 'r*');
f2=figure;
grid on;
hold on;
x = linspace(x_n-3, x_n+4, 100);
y = 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .*x) - 0.2).^2;
xlim([x_n-3 x_n+4])
plot(x, zeros(100), 'g--', 'linewidth', 2);
xlabel('x');
ylabel('y');
plot(x, y, 'k', x_n, fun(x_n), 'r*');
disp(x_n)
%% метод половинного деления
clc
clear
f3=figure;
fun = @(x) 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .* x) - 0.2).^2;
xlim([-7 7]);
ylim([-2 8]);
x = linspace(-7, 7, 100);
y = 1 + (1 + sin(x) - cos(x)).^2 - (sin(2 .* x) - cos(2 .*x) - 0.2).^2;

hold on
grid on
xlabel('x');
ylabel('y');
plot(x, x.*0, '--g', 'linewidth', 2);
plot(x, y);

z = ginput(2);
left = z(1,1);
right = z(2,1);
fun_meth(left,right, fun, 0);
%% метод половинного деления.2
clear
clc
f4=figure;
fun = @(x) sin(x)/x;

x = linspace(-10, 10, 100);
y = sin(x)./x;

hold on
grid on
xlabel('x');
ylabel('y');
plot(x, zeros(100), '--g', 'linewidth', 2);
plot(x, y);
z = ginput(2);
left = z(1,1);
right = z(2,1);
fun_meth(left,right, fun, 0);
%% ньютон 2
clc;
clear
f5=figure;
fun = @(x) sin(x)/x;
x = linspace(-10, 10, 100);
y = sin(x)./x;
hold on;
grid on;
xlim([-10 10]);
ylim([-1 1.5]);
xlabel('x');
ylabel('y');
plot(x, y);
z = ginput(1);
x_left = z(1,1);
plot(x_left, fun(x_left), 'g*');

eps = 0.00001;
h = 1e-14;
fun_dif= @(x)(fun(x + h) - fun(x))/h;
%x=-10:0.07:10;

x_n=x_left;
x_l=x_n;
x_r=x_n;
for iter = 1 : 1000
    x_n_x_fun =fun(x_n) - (x_n - x) .* fun_dif(x_n); 
    x_n = x_n - fun(x_n) / fun_dif(x_n);
    plot(x, x_n_x_fun, '--c', 'linewidth', 0.7);
    if x_n < x_l 
        x_l=x_n;
    end
    if x_n > x_r 
        x_r=x_n;
    end
    x = linspace(x_l-5, x_r+5, 100);
    if abs(fun(x_n)) < eps 
        disp(iter);
        break;
    end
    plot(x_n, fun(x_n), 'b*');
    plot(x_n, 0, 'b.', 'MarkerSize', 15);
end
xlim([x_l-5 x_r+5])
x = x_l-5:0.07:x_r+5;
y = sin(x)./x;
plot(x, y)
plot(x, x.*0, '--g', 'linewidth', 2);
plot(x_n, fun(x_n), 'r*');

f6=figure;
grid on;
hold on;
x = linspace(x_n-10, x_n+10, 100);
y = sin(x)./x;
xlim([x_n-10 x_n+10])
ylim([-1 1.5]);
plot(x, zeros(100), 'g--', 'linewidth', 2);
xlabel('x');
ylabel('y');
plot(x, y, 'k', x_n, fun(x_n), 'r*');
disp(x_n)
%%
function fun_meth(left,right, fun, k)
plot(left, fun(left), 'g*', right, fun(right), 'g*');
eps = 1e-14;
hold on
for iter = 1 : 1000
    mid = (left + right) / 2;
    if(abs(fun(mid)) < eps)
        plot(mid, fun(mid), 'r*');
        disp(iter+k);
        disp(mid);
        break;
    end
    plot(mid, fun(mid), 'b*');
    if fun(left) > 0 && fun(right) > 0 && fun(mid) > 0
        disp("Wrong point");
        break;
    end
    if fun(left) < 0 && fun(right) < 0 && fun(mid) < 0
        disp("Wrong point");
        break;
    end
    if fun(left) * fun(mid) > 0
        left = mid;
    end
    if fun(right) * fun(mid) > 0
        right = mid;
    end
    if fun(left) * fun(right) > 0 
        fun_meth(mid,right,fun, iter);
        right = mid;
    end
end
end