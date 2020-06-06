# PS Eligibility Software

This software checks if any student of the institute is eligible for PS-1 or PS-2 (Practise School Programme of the college in which students work as internees in the Practice School stations or as members in a team working on mission-oriented time-bound research and development projects). I created this software as a project for the Academic Undergraduate Study Division (AUGSD) for my college, which is responsible for the registration of all the undergraduate students every semester. 

  * User can enter either one ID in the 'Enter Student ID' field or enter the name of a text/excel file in the 'Enter File Name' field containing a list of IDs. If a single ID is entered then a list of all the courses successfully completed by the student is displayed in the left box, and a list of courses required to be eligible for PS-1/Ps-2 is displayed on the right box.

  * If a name of file with list of students IDs is used then it displays all the students who are eligible in the left box and all the students who are not eligible on right box. The input file should contain only one student id per line and should be present inside the same directory as the .py file. An error message will be displayed if the file is not found. A 'Results_PS1/PS2.xls' will also be created with two worksheets - one which contains the list of eligible students and other with non-eligible students. The file will be created at two locations - at the cureent working directory and at parent of current working directory to make it easy for users to find the file. If any of these two excel file is open then an error will be displayed and the new results will not be saved in file.

  * The box just below the push buttons shows other information and error messages like number of IDs in the list, error if ID is not in a proper format or no student registered by the given ID, error if file not found, etc.

  * When the software is run, it will show a loading screen and load all the registration data of students in the background. It will throw an error if any data file is missing and the software won't start.

__Note:__ The software consider courses with no grade (i.e. courses currently being done by the student) as successfully completed.
