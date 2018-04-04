
print('\n Please read the documentation of this script before using it')
print("\n Your Desktop files will moved to Documents Folder with particular folder name ")
k=input("\n Press enter to continue ;)")
import glob, os,pathlib
import sys

# print(sys.platform)
cwd = os.getcwd()
if(sys.platform=='win32'):
    slash='\\'
else:
    slash='/'
# print(cwd)

#os.chdir("/home/saurabh/Desktop")
#for file in glob.glob("*.csv"):
#    print(file)

filetypes={'audio':[".aif",".iff",".m3u",".m4a",".mid",".mp3",".mpa",".wav",".wma"],
     'video':[".3g2",".3gp",".asf",".avi",".flv",".m4v",".mov",".mp4",".mpg",".rm",".srt",".swf",".vob",".wmv"],
     'documents and text':[".doc",".docx",".odt",".rtf",".tex",".txt",".wks",".wps",".wpd"],
     'presentation':[".key",".odp",".pps",".ppt",".pptx"],
     'pdf':[".pdf"],'Data File':[".csv",".dat",".log"],
     'Spreadsheet':[".ods",".xlr",".xls",".xlsx"],
     'Compressed File':[".7z",".arj",".deb",".pkg",".rar",".rpm",".tar.gz",".z",".zip"],
     'Excecutable File':[".apk",".bat",".bin",".cgi",".pl",".com",".exe",".gadget",".jar",".py",".wsf"],
     'image':[".jpg",".jpeg",".png",".gif",".ico",".png",".tif",".tiff"],
     'Internet related':[".asp",".aspx",".cer",".cfm",".csr",".css",".htm",".html",".js",".jsp",".php",".rss",".xhtml"],
     # 'no extension':[""]
     }
#print(cpath[1])
if(sys.platform=='win32'): #use if else for ubuntu and windows separately
    cpath=cwd.split('\\')
    deskpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    #print(deskpath)
    docupath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
else:
    cpath=cwd.split('/')
    deskpath=os.path.join('/'+cpath[1]+'/'+cpath[2]+'/Desktop')
    docupath=os.path.join('/'+cpath[1]+'/'+cpath[2]+'/Documents')
# print(deskpath)
# print(docupath)
for folder, extensions in filetypes.items():
#        print(folder, ext)
    for ext in extensions:
        for files in os.listdir(deskpath):
            #print(files)
            if files.endswith(ext) or files.endswith(ext.upper()):
                if not os.path.islink(deskpath+slash+files):
                    #print(files)
                    #print(folder)
                    cfolder=os.path.join(docupath+slash+folder)
                    if not os.path.isdir(cfolder):
                        #print(os.path.join(docupath+'/'+files))
                        os.makedirs(cfolder)
                    if os.path.isfile(cfolder+slash+files):
                        print("We can't move this file,File name already exits--: ",files)
                    else:
                        os.rename(os.path.join(deskpath+slash+files),os.path.join(cfolder+slash+files))
print("\n Program Run Successfully")
k=input("\n Press enter to exit ;)")
