%% 1
clear
clc
filename = 'fileExcel.xlsx';
T = readtable(filename);

leads = [string(T.x___(T.x____=="Руководитель"))]; %отбираем имена из строк, где роль - руководитель
workers = [string(T.x___(T.x____=="Исполнитель"))];

disp(leads); %вывод 
disp(workers);
Roles = ["Leads"; "Workers"];
People = [sprintf("%s; ",leads); sprintf("%s; ",workers)]; %форматируем данные в 2 строки, создаем массив

res = table(Roles, People);%таблица с двумя столбцами соответственно

writetable(res, 'outfile.xlsx');