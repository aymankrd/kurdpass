import random
import arabic_reshaper
from bidi.algorithm import get_display
#Ayman Sabri #https://instagram.com/aym0k <==
print ("     _                    ___  _    ")
print ("    / \  _   _ _ __ ___  / _ \| | __")
print ("   / _ \| | | | '_ ` _ \| | | | |/ /")
print ("  / ___ \ |_| | | | | | | |_| |   < ")
print (" /_/   \_\__, |_| |_| |_|\___/|_|\_\Aym0k")
print ("         |___/                      ")
print ("\n")
text4 = "هـەر بژی کوردستان"
reshaped_text4 = arabic_reshaper.reshape(text4)    
bidi_text4 = get_display(reshaped_text4)       
text5 = "دانـەیا 1.0"
reshaped_text5= arabic_reshaper.reshape(text5)    
bidi_text5 = get_display(reshaped_text5)      
text8 = "درووستکرنا پاسسورەک سکیور کری"
reshaped_text8 = arabic_reshaper.reshape(text8)    
bidi_text8 = get_display(reshaped_text8)    
print ("                Aym0k              ")
print ("    " + bidi_text8 + "    ") 
print ("             " + bidi_text5 + "         ")  
print ("          " + bidi_text4 + "         ")   
print ("\n")
print ("L VS Code yan Sublime yan Brackets Taqi bka :)")
text = "ل بنی بنڤیسه پاسسورد چـەند پیت بن ؟"
reshaped_text = arabic_reshaper.reshape(text)    
bidi_text = get_display(reshaped_text)           
print (bidi_text)
#code mn
text44 = "ژمارە"
reshaped_text44 = arabic_reshaper.reshape(text44)    
bidi_text44 = get_display(reshaped_text44)  
ayman = input(bidi_text44 + " ==>  ")
drejahi = int(ayman)
print ("\n")
#karakter = "abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOQRSTUVWXWZ1234567890!@#$%^&*()_{}[]"
text1 = "             بنڤیسه كا پاسسورد ژ چ تشتی بن وەک پیت یان ژمارە یان رەمز ؟         "
reshaped_text1 = arabic_reshaper.reshape(text1)    
bidi_text1 = get_display(reshaped_text1)           
print (bidi_text1)
text6 = "                              بو نمونه وەک ڤـى - کوپی بکه                        "
reshaped_text6 = arabic_reshaper.reshape(text6)    
bidi_text6 = get_display(reshaped_text6)           
print (bidi_text6)
print ("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOQRSTUVWXWZ1234567890!@#$%^&*()_{}[]")
text444 = "بنڤیسه"
reshaped_text444 = arabic_reshaper.reshape(text444)    
bidi_text444 = get_display(reshaped_text444) 
kar = input(bidi_text444 + " ==>  ")
karakter = (kar)
lista_passworda = [random.choice(karakter) for i in range(drejahi)]
drostkrn = "".join(lista_passworda)
print ("\n")
text2 = "ئـەڤه پاسسوردێ تـەیه :)"
reshaped_text2 = arabic_reshaper.reshape(text2)    
bidi_text2 = get_display(reshaped_text2)           
print (bidi_text2)
text22 = "پاسسورد"
reshaped_text22 = arabic_reshaper.reshape(text22)    
bidi_text22 = get_display(reshaped_text22) 
print(bidi_text22 + " ==>  " + drostkrn)
input("")
