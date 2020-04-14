# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:02:19 2020

@author: User
"""
from datetime import datetime
import pickle
import os
import random
os.system("clr")

#creating the class "variable type" "task" which is a struct more or less that has the type of task, name of task, date and shit like that
class TaskClass:
  def __init__(self, Type, Task, Deadline, MainGoal, NumberLeft, NumPerDay, Completed):
    self.Type = Type
    self.Task = Task
    self.Deadline = Deadline
    self.MainGoal = MainGoal
    self.NumberLeft = NumberLeft
    self.NumPerDay = NumPerDay
    self.Completed = Completed


listOfTasks = []
TaskDict = dict()
f=open("TaskTextFile.txt", "r")
contents = f.readlines()
try:
    for x in contents:
        line = x.split(" -- ")
        TaskType = line[0]
        TaskName = line[1]
        TaskDeadline = line[2]
        TaskMainGoal = line[3]
        TaskNumberLeft = line[4]
        TaskNumPerDay = line[5]
        TaskCompleted = line[6]
        listOfTasks.append(line[1])
        TaskDict[TaskName] = TaskClass(TaskType,TaskName,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay,TaskCompleted)
except:
    print("somthings askew in the text file probobly an empty line")
#Function to save the data so your gonna get all the data that ur passing thru and somehow save it to the fucken text file
#def SaveTask(Type, Task, DateAdd, Deadline, MainGoal, NumberLeft, NumPerDay):



#creating a lists of "task class type structs" that will allow us to continously add this new variable type to a ever changing list
def ReadSaveFile():
  global listOfTasks
  global TaskDict
  listOfTasks.clear()
  f=open("TaskTextFile.txt", "r")
  contents = f.readlines()
  try:
      for x in contents:
        line = x.split(" -- ")
        TaskType = line[0]
        TaskName = line[1]
        TaskDeadline = line[2]
        TaskMainGoal = line[3]
        TaskNumberLeft = line[4]
        TaskNumPerDay = line[5]
        TaskCompleted = line[6]
        listOfTasks.append(line[1])
        TaskDict[TaskName] = TaskClass(TaskType,TaskName,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay,TaskCompleted)

  except:
    print("your data is messed up some1 enterd some janky stuff as a task")

  f.close()



def AddTask(TaskType,TaskName,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay,TaskCompleted):
    gap = " -- "
    save = str(TaskType) + gap + str(TaskName)+ gap +str(TaskDeadline)+ gap +str(TaskMainGoal)+ gap +str(TaskNumberLeft)+ gap + str(TaskNumPerDay) + gap + str(TaskCompleted)

    CheckIfThere = []
    ItsDoubled = 0
    f=open("TaskTextFile.txt", "r")
    contents = f.readlines()

    try:
     for x in contents:
      line = x.split(" -- ")
      names = line[1]
      CheckIfThere.append(line[1])
    except:
        print("your data is messed up some1 enterd some janky stuff as a task")


    #print(ItsDoubled)
    #print("read the shit and put all the names in a list heres the list \n")
    #print(CheckIfThere)
    if TaskName in CheckIfThere:
        ItsDoubled = 1
    #print(ItsDoubled)
    if ItsDoubled == 0:
        f = open("TaskTextFile.txt", "a")
        f.write(save)
    f.close()
    ReadSaveFile()




def _print_layout(object):
  print(object.Type)
  print(" ")
  print(object.Task)
  print(" ")
  print(object.Deadline)
  print(" ")
  print(object.MainGoal)
  print(" ")
  print(object.NumberLeft)
  print(" ")
  print(object.NumPerDay)
  print(" ")
  print(object.TaskCompleted)


def print_customer(nameoftask):
    try:
        _print_layout(TaskDict[nameoftask])
    except:
        print("that object doesnt exists lol")




def CheckFirstTimeOfDay():
    f=open("Dates.txt", "r")
    contents = f.readlines()
    for x in contents:
        lastline = x
    f.close()
    #contents == list of variables with \n there
    #lastline is last line.
    todaylist = lastline.strip('\n')
    todaylist = todaylist.split("-")
    TodayYear = int(todaylist[0])
    TodayMonth = int(todaylist[1])
    TodayDay = int(todaylist[2])
    LastDateActive = datetime(TodayYear, TodayMonth, TodayDay)
    f.close()
    if LastDateActive.date() == datetime.today().date():
        print("youve been here today heres some extra stuff for you")
        retval = 0
    else:
        f=open("Dates.txt", "a")
        whatwrite = str(datetime.today().date())
        whatwrite = str("\n" + whatwrite)
        f.write(whatwrite)
        f.close()
        retval = 1
        print("first time here for the day i will update the files :)")
    return retval

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def CopyLines(LineList):
    TaskForDay = []
    AllTasks = []
    f=open("TaskTextFile.txt", "r")
    contents = f.readlines()
    f.close()
    try:
        for x in contents:
            line = x.split(" -- ")
            AllTasks.append(line[1])
    except:
        print("your data is messed up some1 enterd some janky stuff as a task")
    #print(AllTasks)
    #print(LineList)
    for x in LineList:
        TaskForDay.append(AllTasks[x])

    with open("TasksForTheDay.txt", "w") as filehandle:
        filehandle.truncate(0)
        for listitem in TaskForDay:
            filehandle.write('%s\n' % listitem)





def DefineDailyTasks(NumOfTasks):
    TasksGiven = []
    NumLine = file_len("TaskTextFile.txt")
    while NumOfTasks > 0:
        reset = 0
        i = random.randint(0,NumLine-1)
        if i in TasksGiven:
            reset = 1
        else:
            TasksGiven.append(i)

        if reset == 0:
            NumOfTasks -= 1

    CopyLines(TasksGiven)
    #print(TasksGiven)
    #use the list which gives all the tasks for the day and save them into a new txt file.

def PrintTasksForTheDay():
    f=open("TasksForTheDay.txt", "r")
    lines = f.readlines()
    for x in lines:
        print(x)


def FinishedATask(TheNameOfTheTask):
    global listOfTasks
    global TaskDict
    ReadSaveFile()
    object = TaskDict[TheNameOfTheTask]
    object.TaskCompleted = 1
    #_print_layout(object)
    with open("TaskTextFile.txt", "r") as f:
        lines = f.readlines()
    with open("TaskTextFile.txt", "w") as f:
        for line in lines:
            x = line.split(" -- ")
            if x[1] != TheNameOfTheTask:
                f.write(line)

    f = open("TaskTextFile.txt", "a")
    f.write("\n")
    f.close()

    AddTask(object.Type,TheNameOfTheTask,object.Deadline,object.MainGoal,object.NumberLeft,object.NumPerDay,1)

    #_print_layout(object)
    ReadSaveFile()





#print_customer("write script for mtg deck")
#ReadSaveFile()
#print_customer("learn 500 Greek words")
#AddTask("complete task","Do mtrn lab 2 prework","2020, 2, 22","2020, 2, 27","Uni 2020 T1","0","0")
#ReadSaveFile()
#print_customer("learn 500 Greek words")
#print_customer("nerd")
#print_customer("Do mtrn lab 2 prework")
#CheckFirstTimeOfDay()
i = CheckFirstTimeOfDay()
if i == 1:
    DefineDailyTasks(2)
else:
    choice = input("what would you like to do ? \n1) complete a task ? \n2)Look at the tasks for today again \n3)Add a task \n")
    choice = int(choice)
    if choice == 1:
        addingtask = input("what is the name of the task? \n")
        addingtask = str(addingtask)
        FinishedATask(addingtask)
    elif choice == 2:
        PrintTasksForTheDay()
    elif choice == 3:
        print("add your own task nerd lol nah ceebs doing this")
    else:
        print("chose a real number you nob head")






    #NumberInp = input("how many tasks n")
    #NumberInp = int(NumberInp)
    #DefineDailyTasks(NumberInp)
    #PrintTasksForTheDay()
