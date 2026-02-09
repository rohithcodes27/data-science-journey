-- Basic SQL Practice

-- 1. Select all records
SELECT * FROM employees;

-- 2. Select specific columns
SELECT name, department, salary
FROM employees;

-- 3. Filter using WHERE
SELECT name, salary
FROM employees
WHERE salary > 30000;

-- 4. Sort results
SELECT name, salary
FROM employees
ORDER BY salary DESC;

-- 5. Group and aggregate
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
