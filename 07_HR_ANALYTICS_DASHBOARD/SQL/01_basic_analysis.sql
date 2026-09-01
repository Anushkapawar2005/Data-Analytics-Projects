use hr_analytics;
show tables;
SELECT COUNT(*) as Total_Employees FROM clean_employees;

select Attrition, count(*) from clean_employees group by attrition;

select round(sum(case when attrition='Yes' then 1 else 0 end) * 100.0 / count(*) ,2) as Attrition_Rate from clean_employees;

select department, count(*) as Employee_count from clean_employees group by department order by employee_count desc;

select round(Avg(Monthly_Income), 2) as Average_monthly_income from clean_employees;

SELECT
    Department,
    ROUND(AVG(Monthly_Income), 2) AS Average_Salary
FROM clean_employees
GROUP BY Department
ORDER BY Average_Salary DESC;

select gender, count(*) as employee_count from clean_employees group by gender order by employee_count desc;

select gender, count(*) as total_count, sum(case when attrition='yes' then 1 else 0 end) as attrition_count
from clean_employees group by gender;

SELECT
    Overtime,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count
FROM clean_employees
GROUP BY Overtime;

select job_role, count(*) as employee_count from clean_employees group by job_role order by employee_count;


SELECT
    Job_Role,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count
FROM clean_employees
GROUP BY Job_Role
ORDER BY Attrition_Count DESC;

SELECT
    Experience_Level,
    COUNT(*) AS Employee_Count
FROM clean_employees
GROUP BY Experience_Level
ORDER BY Employee_Count DESC;

SELECT
    Salary_Band,
    COUNT(*) AS Employee_Count
FROM clean_employees
GROUP BY Salary_Band
ORDER BY Employee_Count DESC;

SELECT
    Salary_Band,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count
FROM clean_employees
GROUP BY Salary_Band
ORDER BY Attrition_Count DESC;

SELECT
    Performance_Rating,
    COUNT(*) AS Employee_Count
FROM clean_employees
GROUP BY Performance_Rating
ORDER BY Performance_Rating DESC;

SELECT
    Job_Satisfaction,
    COUNT(*) AS Employee_Count
FROM clean_employees
GROUP BY Job_Satisfaction
ORDER BY Job_Satisfaction;