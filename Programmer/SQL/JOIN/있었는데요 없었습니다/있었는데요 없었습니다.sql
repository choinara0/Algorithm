--- JOIN 이용 (조인 조건 ON에 기술)
SELECT A_I.ANIMAL_ID, A_I.NAME
FROM ANIMAL_INS AS A_I JOIN ANIMAL_OUTS AS A_O
ON A_I.ANIMAL_ID = A_O.ANIMAL_ID
WHERE A_I.DATETIME > A_O.DATETIME
ORDER BY A_I.DATETIME

--- JOIN 이용 (조인 조건 WHERE에 기술)
SELECT A_I.ANIMAL_ID, A_I.NAME
FROM ANIMAL_INS AS A_I JOIN ANIMAL_OUTS AS A_O
WHERE A_I.ANIMAL_ID = A_O.ANIMAL_ID AND A_I.DATETIME > A_O.DATETIME
ORDER BY A_I.DATETIME

--- JOIN 이용 (조인 조건 using에 기술)

SELECT A_I.ANIMAL_ID, A_I.NAME
FROM ANIMAL_INS AS A_I JOIN ANIMAL_OUTS AS A_O USING(ANIMAL_ID)
WHERE A_I.DATETIME > A_O.DATETIME
ORDER BY A_I.DATETIME

--- IN 이용
SELECT A_I.ANIMAL_ID, A_I.NAME
FROM ANIMAL_INS AS A_I
WHERE A_I.ANIMAL_ID IN (
    SELECT A_O.ANIMAL_ID
    FROM ANIMAL_OUTS AS A_O
    WHERE A_I.ANIMAL_ID = A_O.ANIMAL_ID AND A_I.DATETIME > A_O.DATETIME
)
ORDER BY A_I.DATETIME