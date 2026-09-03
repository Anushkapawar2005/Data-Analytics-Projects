use hr_analytics;

select department, count(*) as Total_Employees, 
sum(case when Attrition='Yes' then 1 else 0 end) as Attrition_count ,
Round( sum(case when Attrition='Yes' then 1 else 0 end) *100.0 /count(*), 2) as Attrition_Rate
from clean_Employees group by department order by Attrition_Rate desc;


SELECT
    Job_Role,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Job_Role
ORDER BY Attrition_Rate DESC;


SELECT
    Overtime,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Overtime
ORDER BY Attrition_Rate DESC;


SELECT
    Age_Group,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Age_Group
ORDER BY Attrition_Rate DESC;


SELECT
    Salary_Band,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Salary_Band
ORDER BY Attrition_Rate DESC;


SELECT
    Experience_Level,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Experience_Level
ORDER BY Attrition_Rate DESC;


WITH department_stats AS (
    SELECT
        Department,
        COUNT(*) AS Total_Employees,
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) AS Attrition_Count
    FROM clean_employees
    GROUP BY Department
)

SELECT
    Department,
    Total_Employees,
    Attrition_Count,
    ROUND(
        Attrition_Count * 100.0 / Total_Employees,
        2
    ) AS Attrition_Rate
FROM department_stats
ORDER BY Attrition_Rate DESC;


SELECT
    Employee_ID,
    Department,
    Job_Role,
    Monthly_Income,
    RANK() OVER (
        PARTITION BY Department
        ORDER BY Monthly_Income DESC
    ) AS Salary_Rank
FROM clean_employees;


WITH ranked_employees AS (
    SELECT
        Employee_ID,
        Department,
        Job_Role,
        Monthly_Income,
        RANK() OVER (
            PARTITION BY Department
            ORDER BY Monthly_Income DESC
        ) AS Salary_Rank
    FROM clean_employees
)

SELECT *
FROM ranked_employees
WHERE Salary_Rank <= 3;



CREATE OR REPLACE VIEW vw_department_attrition AS
SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Department;

SELECT *
FROM vw_department_attrition;


CREATE OR REPLACE VIEW vw_jobrole_attrition AS
SELECT
    Job_Role,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count,
    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM clean_employees
GROUP BY Job_Role;

SELECT *
FROM vw_jobrole_attrition;



CREATE OR REPLACE VIEW vw_hr_summary AS
SELECT
    COUNT(*) AS Total_Employees,

    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Total_Attrition,

    ROUND(
        SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate,

    ROUND(AVG(Age), 2) AS Average_Age,

    ROUND(AVG(Monthly_Income), 2) AS Average_Monthly_Income,

    ROUND(AVG(Years_At_Company), 2) AS Average_Years_At_Company

FROM clean_employees;

SELECT *
FROM vw_hr_summary;