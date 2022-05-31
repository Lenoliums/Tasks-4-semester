a = 1 / 4;
b = 1 / 16;
m = 8;
n = 8;

s = 1000;

k = linspace(1, s, s);

t = linspace(-5, 5, s);


x = cos(t) - a .* cos(m * t) + b .* sin(n * t);
y = sin(t) + a .* sin(m * t) + b .* cos(n * t);
 
hold on;
title("12");
xlabel('x');
ylabel('y');
for i = 1:s
    plot(x ./ i, y ./ i);
end

a = 1 / 2;
b = 1 / 3;
m = 7;
n = 17;

s = 1000;

k = linspace(1, s, s);

t = linspace(-5, 5, s);


x = cos(t) + a .* cos(m * t) + b .* sin(n * t);
y = sin(t) + a .* sin(m * t) + b .* cos(n * t);
 
hold on;
title("11");
xlabel('x');
ylabel('y');
for i = 1:s
    plot(x ./ i, y ./ i);
end
