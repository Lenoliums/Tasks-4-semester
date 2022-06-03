%% 9
clear
a = 1;
n = 5;
m = 2;
phi = linspace(0,2*m*pi, 1000);
x = (1+n/m).*cos(phi.*(n/m))-a*n/m.*cos(1+n/m).*phi;
y = (1+n/m).*sin(phi.*(n/m))-a*n/m.*sin(1+n/m).*phi;
plot(x, y)
xlabel('x');
ylabel('y');
title("Task 9");

%% 10
clear
a = 100;
b = 5;
n = 3;
m = 2;
phi0 = pi;
phi = linspace(-pi/2,pi/2, 1000);
x = a.*sin(n.*phi + phi0);
y = b.*sin(m.*phi);
plot(x, y)
xlabel('x');
ylabel('y');
title("Task 10");

%% 11
clear 
t = linspace(-5, 5, 1000);
a = 1/2; 
b = 1/3; 
m = 7; 
n = 17;
x = cos(t) + a*cos(m*t) + b*sin(n*t);
y = sin(t) + a*sin(m*t) + b*cos(n*t);
plot(x, y)
xlabel('x');
ylabel('y');
title("Task 11");

%% 12
t = linspace(-5, 5, 1000);
s = 10;
a = 1/4; b = 1/16; m = 8; n = 8;
x = cos(t) - a*cos(m*t) + b*sin(n*t);
y = sin(t) + a*sin(m*t) + b*cos(n*t);
for k = 1:s
    plot(x./k,y./k);
end
xlabel('x');
ylabel('y');
title("Task 12");

%%  14.1 лемниската Бернулли
t = linspace(-100,100,200/0.1);
a = 3;
x = a*(t+t.^3)./(t.^4 + 1);
y = a*(t-t.^3)./(t.^4 + 1); 
plot(x,y);
xlabel('x');
ylabel('y');
title("Task 14.1 лемниската Бернулли");
%% 14.2 Роза Гранди 
clear
phi = linspace(-2*pi,2*pi,1000);
a=1;
k = 5;
rho = a*sin(k*phi);
polarplot(phi, rho);
title("Task 14.2 Роза Гранди ");
%% 14.19 Нефроид
clear
phi = linspace(-2*pi,2*pi,1000);
r = 1;
x = 3*r*cos(phi) - r* cos(3*phi);
y = 3*r*sin(phi) - r* sin(3*phi);
plot(x,y);
title("Task 14.19 Нефроид");