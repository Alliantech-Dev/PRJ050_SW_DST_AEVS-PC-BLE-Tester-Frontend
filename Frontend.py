import tkinter as tk
#from tkinter import filedialog
from tkinter import ttk
import ctypes

from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import central
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import GetSystemStatus
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import GetSystemInfos
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import ReadListFiles
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import WriteAndUpdateConfig
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import StartRecording
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import StopRecording
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import DownloadFile
from Modules.PRJ050_SW_DST_AEVS_PC_BLE_Tester.AevsBleTester import DeleteFile
#from Backend.AevsBleTester import InitializeConnection


#InitializeConnection()

root = tk.Tk()
style = ttk.Style(root)
style.configure('test.TButton', font= 'calibri', background="red")
style.configure('test2.TButton', font= 'arial', background="blue")

#Functions
def insertText(windowText, text):
    windowText.config(state="normal")
    windowText.insert("end", text)
    windowText.insert("end", "\n")
    windowText.config(state="disabled")

def clearText(windowText):
    windowText.config(state="normal")
    windowText.delete("1.0", "end")
    windowText.config(state="disabled")

def DisplaySystemStatus(text, central):
    bError, bResp, sResp, measureStatus, stateOfChargeBattery, storageSizeInKBytes, freeStorageSizeInKB, frameCounter = GetSystemStatus(central)
    #insertText(text, "System error : " + str(bError))
    #insertText(text, "System responded : " + str(bResp))
    #insertText(text, "System response : " + str(sResp))
    insertText(text, "Measure Status : " + str(measureStatus))
    insertText(text, "State of the charge battery : " + str(stateOfChargeBattery))
    insertText(text, "Storage size in bytes : " + str(storageSizeInKBytes))
    insertText(text, "Free storage size in KB : " + str(freeStorageSizeInKB))
    insertText(text, "Frame counter : " + str(frameCounter))
    insertText(text, "****************************************")

def DisplaySystemInfos(text, central):
    bError, bResp, sResp, serialNumber, targetName, softwareVersion, channelsNumber, fullScale = GetSystemInfos(central)
    #insertText(text, "System error : " + str(bError))
    #insertText(text, "System responded : " + str(bResp))
    #insertText(text, "System response : " + str(sResp))
    insertText(text, "Serial number : " + serialNumber)
    insertText(text, "Target name : " + targetName)
    insertText(text, "Software version : " + softwareVersion)
    insertText(text, "Channels number : " + str(channelsNumber))
    insertText(text, "Full scale : " + str(fullScale))
    insertText(text, "****************************************")

def DisplayFileNames(text, central, wav_folder_path):
    bError, bResp, fileNumber, fileCount, fileName = ReadListFiles(central, wav_folder_path)
    insertText(text, "fileNumber : " + str(fileNumber))
    insertText(text, "fileCount : " + str(fileCount))
    insertText(text, "fileName : " + str(fileName))
    insertText(text, "****************************************")

def WriteConfig(text, central):
    WriteAndUpdateConfig(central)
    insertText(text, "Configuration updated")
    insertText(text, "****************************************")

def StartRecordingButton(text, central):
    # ToDo : Verify the function is working correctly
    StartRecording(central)
    insertText(text, "Recording started")
    insertText(text, "****************************************")

def StopRecordingButton(text, central):
    # ToDo : Verify the function is working correctly
    StopRecording(central)
    insertText(text, "Recording stopped")
    insertText(text, "****************************************")

def DownloadFileButton(text, central, downloadFilePath):
    # ToDo : Verify the function is working correctly (Problem : tries to download first file)
    DownloadFile(central, downloadFilePath)

    insertText(text, "File downloaded")
    insertText(text, "****************************************")

def DeleteFileButton(text, central, deleteFilePath):
    # ToDo : Verify the function is working correctly (Problem : tries to delete first file)
    DeleteFile(central, deleteFilePath)

    insertText(text, "File deleted")
    insertText(text, "****************************************")

"""
def chooseDirectory(text):
    path = filedialog.askdirectory()
    text.delete("1.0", "end")
    text.insert("1.0", path)

def chooseFile(text):
    path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    text.delete("1.0", "end")
    text.insert("1.0", path)
"""
#General configuration
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.title("AEVS Central Simulator")
root.state("zoomed")

buttonFont = ('Arial', 15)
buttonPaddingX=20
buttonPaddingY=20

buttonColor = "#daebd9"
buttonDisconnectColor = "#f8d2d0"
buttonConnectColor = "#ddeafd"
buttonChangeColor = "#ccffcc"
logWindowColor = "#fff2cd"

textWriteCycleCntTitle = 'Write "Cycles Count"'
textWriteCycleCntPlaceholder = '1'
textWritePathFolderTitle = 'Write "Full Path To Folder"'
textWritePathWavTitle = 'Write "Full Path To WAV File"'
textWritePathWavPlaceholder = '.wav'

version = "1.0"

style = ttk.Style()
style.theme_use("clam")

#Buttons
buttonFrame = tk.Frame(root)

buttonFrame.grid_columnconfigure(0, weight=1)
buttonFrame.grid_columnconfigure(1, weight=1)
buttonFrame.grid_columnconfigure(2, weight=1)
buttonFrame.grid_rowconfigure(0, weight=1)
buttonFrame.grid_rowconfigure(1, weight=1)
buttonFrame.grid_rowconfigure(2, weight=1)
buttonFrame.grid_rowconfigure(3, weight=1)
buttonFrame.grid_rowconfigure(4, weight=1)
buttonFrame.grid_rowconfigure(5, weight=1)
buttonFrame.grid_rowconfigure(6, weight=1)
buttonFrame.grid_rowconfigure(7, weight=1)
buttonFrame.grid_rowconfigure(8, weight=1)

#Log Window (on la met au début car on en a besoin dans tous les boutons)
logWindowLabelFrame = tk.LabelFrame(buttonFrame, background=logWindowColor)

logWindowText = tk.Text(logWindowLabelFrame, height=10, font=buttonFont)
logWindowText.config(state=tk.DISABLED)
logWindowText.pack(padx=20, pady=20, fill="both")

logWindowLabelFrame.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=150)

#Read Status Button
buttonReadStatus = tk.Button(buttonFrame, text="READ STATUS", font=buttonFont, background=buttonColor, command=lambda: DisplaySystemStatus(logWindowText, central))
buttonReadStatus.grid(row=0, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Read System Info Button
buttonReadSystemInfo = tk.Button(buttonFrame, text="READ SYSTEM\nINFORMATIONS", font=buttonFont, background=buttonColor, command=lambda: DisplaySystemInfos(logWindowText, central))
buttonReadSystemInfo.grid(row=0, column=1, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Write Config Button
buttonWriteConfig = tk.Button(buttonFrame, text="WRITE CONFIG", font=buttonFont, background=buttonColor, command=lambda: WriteConfig(logWindowText, central))
buttonWriteConfig.grid(row=0, column=2, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Start Recording Button
buttonStartRec = tk.Button(buttonFrame, text="START RECORDING", font=buttonFont, background=buttonColor, command=lambda: StartRecordingButton(logWindowText, central))
buttonStartRec.grid(row=1, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Write Cycles Count Text
writeCyclesCountLabelFrame = tk.LabelFrame(buttonFrame)

writeCyclesCountLabelText = tk.Label(writeCyclesCountLabelFrame, text=textWriteCycleCntTitle)
writeCyclesCountLabelText.pack()

textWriteCyclesCnt = tk.Text(writeCyclesCountLabelFrame, height=1, font=buttonFont)
textWriteCyclesCnt.insert("1.0", textWriteCycleCntPlaceholder)
textWriteCyclesCnt.pack(fill="both")

writeCyclesCountLabelFrame.grid(row=1, column=1, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Stop Recording Button
buttonStopRec = tk.Button(buttonFrame, text="STOP RECORDING", font=buttonFont, background=buttonColor, command=lambda: StopRecordingButton(logWindowText, central))
buttonStopRec.grid(row=1, column=2, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Write Path Folder Text
textWritePathFolderLabelFrame = tk.LabelFrame(buttonFrame)

textWritePathFolderLabelText = tk.Label(textWritePathFolderLabelFrame, text=textWritePathFolderTitle)
textWritePathFolderLabelText.pack()

textWritePathFolder = tk.Text(textWritePathFolderLabelFrame, height=1, font=buttonFont)
textWritePathFolder.pack(fill="both")

#buttonChooseDirectoryFiles = tk.Button(textWritePathFolderLabelFrame, text="Change Folder", command=lambda: chooseDirectory(textWritePathFolder), background=buttonChangeColor)
#buttonChooseDirectoryFiles.pack(fill="both")

textWritePathFolderLabelFrame.grid(row=2, column=1, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY, columnspan=2)

#Read List Button
buttonReadList = tk.Button(buttonFrame, text="READ LIST OF FILES IN\nMEMORY", font=buttonFont, background=buttonColor, command=lambda: DisplayFileNames(logWindowText, central, textWritePathFolder.get("1.0", "end")))
buttonReadList.grid(row=2, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Write Path WAV Text
textWritePathWavLabelFrame = tk.LabelFrame(buttonFrame)

textWritePathWavLabelText = tk.Label(textWritePathWavLabelFrame, text=textWritePathWavTitle)
textWritePathWavLabelText.pack()

textWritePathWav = tk.Text(textWritePathWavLabelFrame, height=1, font=buttonFont)
textWritePathWav.insert("1.0", textWritePathWavPlaceholder)
textWritePathWav.pack(fill="both")

#buttonChooseDirectoryWav1 = tk.Button(textWritePathWavLabelFrame, text="Change WAV File", command=lambda: chooseFile(textWritePathWav), background=buttonChangeColor)
#buttonChooseDirectoryWav1.pack(fill="both")

textWritePathWavLabelFrame.grid(row=3, column=1, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY, columnspan=2)

#Download Button
buttonDownload = tk.Button(buttonFrame, text="DOWNLOAD FILE", font=buttonFont, background=buttonColor, command=lambda: DownloadFileButton(logWindowText, central, textWritePathWav.get("1.0", "end")))
buttonDownload.grid(row=3, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Write Path WAV 2 Text
textWritePathWav2LabelFrame = tk.LabelFrame(buttonFrame)

textWritePathWav2LabelText = tk.Label(textWritePathWav2LabelFrame, text=textWritePathWavTitle)
textWritePathWav2LabelText.pack()

textWritePathWav2 = tk.Text(textWritePathWav2LabelFrame, height=1, font=buttonFont)
textWritePathWav2.insert("1.0", textWritePathWavPlaceholder)
textWritePathWav2.pack(fill="both")

#buttonChooseDirectoryWav2 = tk.Button(textWritePathWav2LabelFrame, text="Change WAV File", command=lambda: chooseFile(textWritePathWav2), background=buttonChangeColor)
#buttonChooseDirectoryWav2.pack(fill="both")

textWritePathWav2LabelFrame.grid(row=4, column=1, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY, columnspan=2)

#Delete Button
buttonDelete = tk.Button(buttonFrame, text="DELETE FILE", font=buttonFont, background=buttonColor, command=lambda: DeleteFileButton(logWindowText, central, textWritePathWav2.get("1.0", "end")))
buttonDelete.grid(row=4, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX, pady=buttonPaddingY)

#Label Log
labelLog = tk.Label(buttonFrame, text="Execution Log", font=buttonFont).grid(row=5, column=0, columnspan=3)


#Disconnect Button
buttonDisconnect = tk.Button(buttonFrame, text="DISCONNECT FROM BLE PERIPHERAL", font=buttonFont, background=buttonDisconnectColor, command=lambda : clearText(logWindowText))
buttonDisconnect.grid(row=7, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX*20, pady=buttonPaddingY, columnspan=3)

#Connect Button
buttonConnect = tk.Button(buttonFrame, text="CONNECT TO BLE PERIPHERAL", font=buttonFont, background=buttonConnectColor, command=lambda: insertText(logWindowText, "test"))
buttonConnect.grid(row=8, column=0, sticky = tk.W + tk.E, padx=buttonPaddingX*20, pady=buttonPaddingY, columnspan=3)

#Label Version
labelVersion = tk.Label(buttonFrame, text="v" + version, font=buttonFont).grid(row=9, column=0, columnspan=3)

buttonFrame.pack(fill="x")

root.mainloop()