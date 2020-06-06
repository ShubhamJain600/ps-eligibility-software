# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:01:43 2020

@author: Shubham Jain
"""
print ("Loading files, this may take few seconds")

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import os
import shutil
import ui, loadwin_ui


class MainWin(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()

		self.ui.ps1_btn_id.clicked.connect(self.ps1_chk_id)
		self.ui.ps2_btn_id.clicked.connect(self.ps2_chk_id)
		self.ui.ps1_btn_lst.clicked.connect(self.ps1_chk_lst)
		self.ui.ps2_btn_lst.clicked.connect(self.ps2_chk_lst)


	def ps1_chk_id(self):
		self.ui.result_text_space.clear()
		self.ui.right_list.clear()
		self.ui.left_list.clear()
		self.ui.student_result_label.clear()
		self.ui.right_list_label.clear()
		self.ui.left_list_label.clear()
		self.ui.file_input.clear()

		self.std_id = self.ui.std_id_input.text().upper()
		self.ui.student_result_label.setText(self.std_id)
		#Check whether the entered student id is proper format
		if(self.stdnt_id_check()==0):
			return

		#Check if the given id is registered or not
		if(self.list_stdnt_crs()==0):
			self.ui.result_text_space.appendPlainText("No student registered by the given ID.\n")
			return

		#List the courses successfully completed by student
		self.ui.student_result_label.setText(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
		self.ui.left_list_label.setText("Courses successfully completed by Student")
		self.ui.left_list.addItems(self.stdnt_crs['Course Code and Name'])

		#Lists the prereq for PS1 for the student
		self.list_prereq_ps1()
		self.ui.right_list_label.setText("Prerequisite for PS-I")
		self.ui.right_list.addItems(self.prereq_dataframe['Course Code and Name'])

		set_stdnt_crs_cid = set(self.stdnt_crs['Course ID'])
		set_prereq_dataframe_compcodes = set(self.prereq_dataframe['COMP CODES'])

		#Checking if student has already done PS-1
		if (21591 in set_stdnt_crs_cid):
			self.ui.result_text_space.appendPlainText("Student has already done PS - 1")

		#Checks whether student has successfully completed all the courses in prereq list
		elif (set_prereq_dataframe_compcodes.issubset(set_stdnt_crs_cid)):
			self.ui.result_text_space.appendPlainText(str.format("Student is eligible for PS-1"))

		else:
			self.ui.result_text_space.appendPlainText(str.format("Student is not eligible for PS-1"))


	def ps2_chk_id(self):
		self.ui.result_text_space.clear()
		self.ui.right_list.clear()
		self.ui.left_list.clear()
		self.ui.student_result_label.clear()
		self.ui.right_list_label.clear()
		self.ui.left_list_label.clear()
		self.ui.file_input.clear()

		self.std_id = self.ui.std_id_input.text().upper()
		self.ui.student_result_label.setText(self.std_id)
		#Check whether the entered student id is proper format
		if(self.stdnt_id_check()==0):
			return

		#Check if the given id is registered or not
		if(self.list_stdnt_crs()==0):
			self.ui.result_text_space.appendPlainText("No student registered by the given ID.\n")
			return

		#List the courses successfully completed by student
		self.ui.student_result_label.setText(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
		self.ui.left_list_label.setText("Courses successfully completed by Student")
		self.ui.left_list.addItems(self.stdnt_crs['Course Code and Name'])

		#Lists the prereq for PS1 for the student
		self.list_prereq_ps2()
		self.ui.right_list_label.setText("Prerequisite for PS-II")
		self.ui.right_list.addItems(self.prereq_dataframe['Course Code and Name'])

		set_stdnt_crs_cid = set(self.stdnt_crs['Course ID'])
		set_prereq_dataframe_compcodes = set(self.prereq_dataframe['COMP CODES'])

		#Checks whether student has successfully completed all the courses in prereq list
		if (set_prereq_dataframe_compcodes.issubset(set_stdnt_crs_cid)):
			self.ui.result_text_space.appendPlainText(str.format("Student is eligible for PS-2"))

		else:
			self.ui.result_text_space.appendPlainText(str.format("Student is not eligible for PS-2"))


	def ps1_chk_lst(self):
		self.ui.result_text_space.clear()
		self.ui.right_list.clear()
		self.ui.left_list.clear()
		self.ui.student_result_label.clear()
		self.ui.right_list_label.clear()
		self.ui.left_list_label.clear()
		self.ui.std_id_input.clear()

		input_file_name = self.ui.file_input.text()
		#Checking the type of file and opening the file
		try:
			if (input_file_name[-3:] == "txt"):
				input_file = pd.read_csv(input_file_name, header=None)

			elif (input_file_name[-3:] == "xls" or input_file_name[-4:] == "xlsx"):
				input_file = pd.read_excel(input_file_name, header=None)

			else:
				self.ui.result_text_space.appendPlainText("Enter file extension along with file name (only .txt, .xls, .xlsx)\n")
				return

		except FileNotFoundError:
		#Handle the exception if file not found in the same directory in which the software is running
			self.ui.result_text_space.appendPlainText("File not found. It must be present in the same folder where the software is present.\n")
			return

		self.ui.left_list_label.setText("List of students who are eligible for PS-I")
		self.ui.right_list_label.setText("List of students who are not eligible for PS-I")
		self.ui.student_result_label.setText("Reading list from file")
		self.ui.result_text_space.appendPlainText("Total no of entries in the list: " + str(len(input_file.index)) + "\n")

		eligible_stdnt_lst = []
		not_eligible_stdnt_lst = []
		for i in input_file.index:
			app.processEvents()
			self.std_id = input_file.iloc[i,0].upper()
			#Check whether the entered student id is proper format
			if(self.stdnt_id_check()==0):
				continue

			#Check if the given id is registered or not
			if(self.list_stdnt_crs()==0):
				self.ui.result_text_space.appendPlainText(self.std_id + ": No student registered by the given ID.\n")
				continue

			self.list_prereq_ps1()
			set_stdnt_crs_cid = set(self.stdnt_crs['Course ID'])
			set_prereq_dataframe_compcodes = set(self.prereq_dataframe['COMP CODES'])

			#Checks whether student has successfully completed all the courses in prereq list
			if (set_prereq_dataframe_compcodes.issubset(set_stdnt_crs_cid)):
				self.ui.left_list.addItem(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
				eligible_stdnt_lst.append([self.std_id, self.stdnt_crs.iloc[0,1]])

			else:
				self.ui.right_list.addItem(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
				not_eligible_stdnt_lst.append([self.std_id, self.stdnt_crs.iloc[0,1]])

		self.ui.result_text_space.appendPlainText("Done")

		#Writing results to file
		eligible_stdnt_df = pd.DataFrame(eligible_stdnt_lst, columns = ['ID', 'Name'])
		not_eligible_stdnt_df = pd.DataFrame(not_eligible_stdnt_lst, columns = ['ID', 'Name'])
		
		try:	
			with pd.ExcelWriter("Results_PS1.xls") as writer:
				eligible_stdnt_df.to_excel(writer, sheet_name = "Eligible", index =False)
				not_eligible_stdnt_df.to_excel(writer, sheet_name = "Not_Eligible", index =False)

			#Moving the result file one directory up
			file_path = os.getcwd()
			file_path = os.path.split(file_path)
			shutil.copy("Results_PS1.xls", file_path[0])
		except PermissionError:
			loadwin.label.setText("The results file was not saved because \nit was open in excel.\nClose the results file and try again.\n")
			q_widget.setWindowTitle("Error")
			q_widget.show()


	def ps2_chk_lst(self):
		self.ui.result_text_space.clear()
		self.ui.right_list.clear()
		self.ui.left_list.clear()
		self.ui.student_result_label.clear()
		self.ui.right_list_label.clear()
		self.ui.left_list_label.clear()
		self.ui.std_id_input.clear()

		input_file_name = self.ui.file_input.text()
		#Checking the type of file and opening the file
		try:
			if (input_file_name[-3:] == "txt"):
				input_file = pd.read_csv(input_file_name, header=None)

			elif (input_file_name[-3:] == "xls" or input_file_name[-4:] == "xlsx"):
				input_file = pd.read_excel(input_file_name, header=None)

			else:
				self.ui.result_text_space.appendPlainText("Enter file extension along with file name (only .txt, .xls, .xlsx)\n")
				return

		except FileNotFoundError:
		#Handle the exception if file not found in the same directory in which the software is running
			self.ui.result_text_space.appendPlainText("File not found. It must be present in the same folder where the software is present.\n")
			return

		self.ui.left_list_label.setText("List of students who are eligible for PS-II")
		self.ui.right_list_label.setText("List of students who are not eligible for PS-II")
		self.ui.student_result_label.setText("Reading list from file")
		self.ui.result_text_space.appendPlainText("Total no of entries in the list: " + str(len(input_file.index)) + "\n")

		eligible_stdnt_lst = []
		not_eligible_stdnt_lst = []
		for i in input_file.index:
			app.processEvents()
			self.std_id = input_file.iloc[i,0].upper()
			#Check whether the entered student id is proper format
			if(self.stdnt_id_check()==0):
				continue

			#Check if the given id is registered or not
			if(self.list_stdnt_crs()==0):
				self.ui.result_text_space.appendPlainText(self.std_id + ": No student registered by the given ID.\n")
				continue

			self.list_prereq_ps2()
			set_stdnt_crs_cid = set(self.stdnt_crs['Course ID'])
			set_prereq_dataframe_compcodes = set(self.prereq_dataframe['COMP CODES'])

			#Checks whether student has successfully completed all the courses in prereq list
			if (set_prereq_dataframe_compcodes.issubset(set_stdnt_crs_cid)):
				self.ui.left_list.addItem(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
				eligible_stdnt_lst.append([self.std_id, self.stdnt_crs.iloc[0,1]])

			else:
				self.ui.right_list.addItem(self.stdnt_crs.iloc[0,1] + " - " + self.std_id)
				not_eligible_stdnt_lst.append([self.std_id, self.stdnt_crs.iloc[0,1]])
			
		self.ui.result_text_space.appendPlainText("Done")

		#Writing Results to file
		eligible_stdnt_df = pd.DataFrame(eligible_stdnt_lst, columns = ['ID', 'Name'])
		not_eligible_stdnt_df = pd.DataFrame(not_eligible_stdnt_lst, columns = ['ID', 'Name'])
		
		try:	
			with pd.ExcelWriter("Results_PS2.xls") as writer:
				eligible_stdnt_df.to_excel(writer, sheet_name = "Eligible", index =False)
				not_eligible_stdnt_df.to_excel(writer, sheet_name = "Not_Eligible", index =False)

			#Moving the result file one directory up
			file_path = os.getcwd()
			file_path = os.path.split(file_path)
			shutil.copy("Results_PS2.xls", file_path[0])
		except PermissionError:
			loadwin.label.setText("The results file was not saved because \nit was open in excel.\nClose the results file and try again.\n")
			q_widget.setWindowTitle("Error")
			q_widget.show()

	#Check whether the entered student id is proper format
	def stdnt_id_check(self):
		#Check whether length is 13 characters
		if len(self.std_id)!=13:
			self.ui.result_text_space.appendPlainText(self.std_id + ": ID length not correct, please enter 13 characters.\n")
			return 0

		year = self.std_id[0:4]
		fbranch = self.std_id[4:6]
		sbranch = self.std_id[6:8]
		sid = self.std_id[8:12]
		
		#Check whether year is between 2010 and 2025
		try:
			iyear = int(year)
			if iyear not in list(range(2010,2025)):
				self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student year.\n")
				return 0

		except ValueError:
		#Handle the exception if first four characters are not digits
			self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student year.\n")
			return 0

		#Check whether first branch code is correct
		if fbranch not in ["A1", "A3", "A4", "A7", "A8", "AA", "B1","B2","B3","B4","B5"]:
			self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student branch.\n")
			return 0

		#Check whether second branch code is correct
		elif sbranch not in ["A1", "A3", "A4", "A7", "A8", "AA", "B1","B2","B3","B4","B5", "PS", "TS"]:
			self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student branch.\n")
			return 0

		#Check whether id is between 0000 and 2500
		try:
			isid = int(sid)
			if isid not in list(range(000,2500)):
				self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student 4 digit ID number.\n")
				return 0
		except ValueError:
		#Handle the exception if last four characters are not digits
			self.ui.result_text_space.appendPlainText(self.std_id + ": Invalid student 4 digit ID number.\n")
			return 0

		#Check whether last charactyer is G
		if (self.std_id[-1]!='G'):
			self.ui.result_text_space.appendPlainText(self.std_id + ": Last character in id is not G.\n")
			return 0


	#Lists the prereq for PS1 for the student
	def list_prereq_ps1(self):
		
		tag = self.std_id[4:6] + "CDC"
		self.prereq_dataframe = ps1_cdc[ps1_cdc['TAG'] == tag]
		self.prereq_dataframe['Course Code and Name'] = self.prereq_dataframe['Course Code'] + " - " + self.prereq_dataframe['Course Name']


	#Lists the prereq for PS2 for the student
	def list_prereq_ps2(self):
		
		tag = self.std_id[4:6] + "CDC"
		self.prereq_dataframe = ps2_cdc[ps2_cdc['TAG'] == tag]
		self.prereq_dataframe['Course Code and Name'] = self.prereq_dataframe['Course Code'] + " - " + self.prereq_dataframe['Course Name']

		#If dual degree student then add the prereq of second degree also
		if (self.std_id[6:8] not in ['PS', 'TS']):
			tag = self.std_id[6:8] + "CDC"
			self.prereq_dataframe_second = ps2_cdc[ps2_cdc['TAG'] == tag]
			self.prereq_dataframe_second['Course Code and Name'] = self.prereq_dataframe_second['Course Code'] + " - " + self.prereq_dataframe_second['Course Name']
			self.prereq_dataframe = pd.concat([self.prereq_dataframe, self.prereq_dataframe_second], ignore_index=True)
			self.prereq_dataframe.drop_duplicates(subset ="COMP CODES", keep = 'first', inplace = True)

		self.prereq_dataframe.sort_values(by=['Course Code'], inplace=True, ignore_index=True)


	#List the courses successfully completed by student
	def list_stdnt_crs(self):

		fsem_17_18_selected = file_df_list[0][file_df_list[0]['Campus ID']==self.std_id]
		ssem_17_18_selected = file_df_list[1][file_df_list[1]['Campus ID']==self.std_id]
		fsem_18_19_selected = file_df_list[2][file_df_list[2]['Campus ID']==self.std_id]
		ssem_18_19_selected = file_df_list[3][file_df_list[3]['Campus ID']==self.std_id]
		fsem_19_20_selected = file_df_list[4][file_df_list[4]['Campus ID']==self.std_id]
		ssem_19_20_selected = file_df_list[5][file_df_list[5]['Campus ID']==self.std_id]
		sterm_17_18_selected = file_df_list[6][file_df_list[6]['Campus ID']==self.std_id]
		sterm_18_19_selected = file_df_list[7][file_df_list[7]['Campus ID']==self.std_id]

		self.stdnt_crs = pd.concat([fsem_17_18_selected,ssem_17_18_selected,fsem_18_19_selected,ssem_18_19_selected,fsem_19_20_selected,ssem_19_20_selected,sterm_17_18_selected,sterm_18_19_selected], ignore_index=True)

		#Check if the given id is registered or not
		if (self.stdnt_crs.empty):
			return 0

		self.stdnt_crs.sort_values(by=['Subject', 'Catalog No.', 'Semester'], ascending=[True, True, False], inplace=True, ignore_index=True)
		#Remove duplicates and courses with NC, RC or W grades
		prev_CID = 0000
		prev_grd = 'A'
		for index in self.stdnt_crs.index:
			curr_CID = self.stdnt_crs.loc[index,"Course ID"]
			curr_grd = self.stdnt_crs.loc[index,"Course Grade"]
			if (curr_grd in ['NC','W', 'RC']):
				self.stdnt_crs.drop(index, inplace = True)
				if (curr_grd=='W' and prev_grd=='NC' and curr_CID==prev_CID):
					curr_grd = 'NC'
			elif (curr_CID==prev_CID):
				if (prev_grd == 'W'):
					continue
				else:
					self.stdnt_crs.drop(index, inplace = True)
			prev_CID = curr_CID
			prev_grd  = curr_grd
	
		#Add a new coloumn with course code and name together
		self.stdnt_crs['Course Code and Name'] = self.stdnt_crs['Subject'] + " " + self.stdnt_crs['Catalog No.'] + " - " + self.stdnt_crs['Descr']

if __name__ == '__main__':

	#Starting the initial Loading Window
	app = QApplication([])
	q_widget = QWidget()
	loadwin = loadwin_ui.Ui_LoadWin()
	loadwin.setupUi(q_widget)
	q_widget.show()
	app.processEvents()

	#Import all the semester registration and grade data
	file_df_list = []
	file_name_list = ["FIRST SEMESTER 2017-2018.xls", "SECOND SEMESTER 2017-2018.xls", "FIRST SEMESTER 2018-2019.xls", "SECOND SEMESTER 2018-2019.xls", "FIRST SEMESTER 2019-2020.xls", "SECOND SEMESTER 2019-2020.xls", "SUMMER TERM 2017-2018.xls", "SUMMER TERM 2018-2019.xls"]
	
	try:
		for i in file_name_list:
			file_df_list.append(pd.read_excel(i, skiprows = 1, usecols = [0,1,3,5,6,7,8,10,11]))

		i = "CDC courses.xls"
		ps1_cdc = pd.read_excel("CDC courses.xls", sheet_name = 'PS1_CDC', usecols=[0,1,2,3])
		ps2_cdc = pd.read_excel("CDC courses.xls", sheet_name = 'PS2_CDC', usecols=[0,1,2,3])

	except FileNotFoundError:
		loadwin.label.setText("File not found.\n" + i)
		sys.exit(app.exec_())

	#Starting the Main Window
	q_widget.hide()
	main_win = MainWin()
	sys.exit(app.exec_())