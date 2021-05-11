# Courses-Optimizer
## Introduction
The project tries to minimize and optimize the time (measured in semesters) that it takes to complete any university degree given as input.
This will be achieved by correctly assigning the necessary courses to receive the degree, prioritizing those that have more depth (measure created to prioritize).

## The Process
### Career Selection
The first step is to select which degree will be optimized. Currently you can choose between the five careers available at the Facultad de Ciencias Económicas de la Universidad de Buenos Aires (UBA-FCE). They are:

1. Actuario
1.1 en Administración
1.2 en Economía
3. Administración
4. Contador Público
5. Licenciatura en Economía
6. Sistemas


### Syllabus Load and Parsing
The input data (Syllabus) derived from the career selected will be load and parsed in a Pandas DataFrame.

The input data has the following structure:

| Course Code  | Course Name  | Weekly hours | Correlatives |
| :------------: |:---------------:| :-----:| :-----:|
| 250 | Microeconomía I | 4 |241-242 |
|...|...|...|...|
|755|Teoría Actuarial de los Seguros Patrimoniales|4|276-751-752|

- carga en dataframe
### Creation of Course Class
-  Course charging
