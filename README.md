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

------------
![Ferpes](https://user-images.githubusercontent.com/54080991/117893012-07278f80-b290-11eb-90a2-154fbd33ffcf.PNG)
------------
![Ferpes1](https://user-images.githubusercontent.com/54080991/117892731-a13b0800-b28f-11eb-9522-23a5d5518e00.png)
------------
![Ferpes2](https://user-images.githubusercontent.com/54080991/117892739-a4ce8f00-b28f-11eb-9cf7-ba05960bbf7d.png)
------------
![Ferpes3](https://user-images.githubusercontent.com/54080991/117892747-a7c97f80-b28f-11eb-8567-3ced121e9d7d.png)
------------
![Ferpes4](https://user-images.githubusercontent.com/54080991/117892756-aac47000-b28f-11eb-9413-67de692d383a.png)
------------
![Ferpes5](https://user-images.githubusercontent.com/54080991/117892762-adbf6080-b28f-11eb-9ff7-bac5bf0707d8.png)
------------
![Ferpes6](https://user-images.githubusercontent.com/54080991/117893072-1b6b8c80-b290-11eb-9175-7c4fef498dfd.png)
------------
![Ferpes7](https://user-images.githubusercontent.com/54080991/117893091-22929a80-b290-11eb-8104-512d453a73f8.png)

