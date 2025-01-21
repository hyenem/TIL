USE `ssafy_corporation`;

-- 카타시안 곱
SELECT empno, ename, job
FROM emp;

SELECT deptno, dname
FROM dept;

SELECT empno, ename, job, emp.deptno, dname
FROM emp, dept;

SELECT empno, ename, job, emp.deptno, dname
FROM emp, dept
WHERE emp.deptno=dept.deptno;

-- 7788번인 사원의 정보를 가지고 와보자(부서이름까지)
SELECT ename, job, deptno
FROM emp
WHERE empno=7788;

SELECT dname
FROM dept
WHERE deptno = 20;

SELECT empno, ename, job, emp.deptno, dname
FROM emp, dept
WHERE emp.deptno = dept.deptno
AND empno = 7788;

-- INNER JOIN 키워드 사용
SELECT empno, ename, job, deptno, dname
FROM emp
INNER JOIN dept
USING (deptno)
WHERE empno=7788;

-- OUTER JOIN
INSERT INTO emp
VALUES (7777, "양싸피", "MANAGER", 7839, "2022-09-13", 5000, NULL, NULL);

-- 왼쪽 테이블 기준
SELECT ename, emp.deptno, dname
FROM emp LEFT OUTER JOIN dept
ON emp.deptno = dept.deptno;

-- 오른쪽 테이블 기준
SELECT ename, emp.deptno, dname
FROM emp RIGHT OUTER JOIN dept
ON emp.deptno = dept.deptno;


-- 셀프 조인
SELECT e1.empno, e1.ename, e1.mgr, e2.ename AS mgrName
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno;

SELECT e1.empno, e1.ename, e1.mgr, e2.ename AS mgrName
FROM emp e1 INNER JOIN emp e2
ON e1.mgr = e2.empno;

-- KING 이등장하질 않아,,,
SELECT e1.empno, e1.ename, e1.mgr, e2.ename AS mgrName
FROM emp e1 LEFT OUTER JOIN emp e2
ON e1.mgr = e2.empno;

-- 비 동등 조인(Non-Equi JOIN)
SELECT e.empno, e.ename, e.sal, sg.grade
FROM emp e, salgrade sg
WHERE e.sal >= sg.LOSAL AND e.sal <= sg.HISAL
ORDER BY sg.grade DESC, e.sal DESC;

SELECT e.empno, e.ename, e.sal, sg.grade
FROM emp e, salgrade sg
WHERE e.sal BETWEEN sg.LOSAL AND sg.HISAL
ORDER BY sg.grade DESC, e.sal DESC;