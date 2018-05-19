#!/usr/bin/python2
import time
import webbrowser




print "Press 1 for string"
print "press 2 for image search"
print "press 3 for URL name"
print "press 4 for time and date"
print "press 5 for default browser"
print "press 6 for all network ip"
print "press 7 to get domain and owner name"
ch=raw_input()


if ch=='1':
   search_data=raw_input("enter data")
   new_data=search_data.strip()
   fi=new_data.split()
   for i in fi:
       webbrowser.open_new_tab("http://www.google.com/search?q="+i)
elif ch=="2":
   search_data=raw_input("enter data")
   new_data=search_data.strip()
   final_data=new_data.split()
   for i in final_data:
    webbrowser.open_new_tab("https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjxx5Spp4nbAhWKLY8KHQ2PAiIQ_AUIDCgD"%i)
elif ch=="3":   
   search_data=raw_input("enter data")
   new_data=search_data.strip()
   final_data=new_data.split()
   for i in final_data:   
elif ch=="4":
   print time.ctime()
elif ch=="5":
      webbrowser.open_new_tab("http:")
elif ch=="6":
   raw_input("Enter any statement ")
elif ch=="7":
   raw_input("Enter any statement ")
      webbrowser.open_new_tab("https://who.is/whois/%s"%a)
 
else:
   print "input"
