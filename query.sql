# завдання 1 - визначити кількість спортсменів з різних країн
select nationality, count(*) as 'count of athletes' from athletes
group by nationality;

# завдання 2 - визначити залежність між національністю та кількістю золотих/срібних медалей
select nationality, sum(athletes.gold) as 'count of gold medals', sum(athletes.silver) as 'count of silver medals' from athletes
group by nationality;

# завдання 3 - визначити залежність між кількістю золотих/срібних та чоловіками/жінками за видами спорту
select sport, sex, sum(athletes.gold) as 'count of gold medals', sum(athletes.silver) as 'count of silver medals' from athletes
group by sport, sex