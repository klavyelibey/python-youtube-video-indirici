
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import ComboBox
from pytube import YouTube

klasor_adi=""

root=Tk() 
#tkinter paketini root adı ile çağırmak için yapmamız gereken işlem. Root adı her hangi başka bir ifade alabilir.

root.title("Youtube Video İndirici") 
#Programımızın başlığını ifade edecek olan yazı

root.geometry("350x450")  
#yapmak istedimiz programın ekranda kaça kaç pikselde gözükmesini istiyorsak, bu ifade kullanılacak

root.columnconfigure(0,weight=1) 
#yazılacak olan kodların hepsinin ortalı şekilde ve alt alta gözükmesini istiyorsak kullanılacak ifade

#-----------------------------------------------------------------------------------------------------------------------

def dosya_konumu_ac_fonksiyonu():
    global klasor_adi
    klasor_adi=filedialog.askdirectory()

    if(len(klasor_adi)>1):
        dosya_konumu_hatasi.config(text=klasor_adi,bg="green")

    else:
        dosya_konumu_hatasi.grid()

def video_indirme_fonksiyonu():

    url=videonun_url_adresinin_girilecegi_kutu.get()
    #indir butonuna tıklandıktan sonra kullanıcının entry ile atatığımız kutuya girdiği ve sonradan
    # string türüne çevrilen url adresi alınıyor 

    comboboxtan_secilmis_video_cozunurlugu=videonun_indirilebilecek_cozunurluk_secenekleri_comboxu.get()
    #video indir butonuna tıklandığı zaman combobozdan kullanıcının seçtiği çözünürlük değerini
    #secilmiş değer olarak yeni bir değişkene atıyoruz

    #bu girilen ifadeler düzgün bir şekilde çalıştığı zaman aşağıdaki kod satırı devreye giriyor.
    if(len(url)>1):
        yt=YouTube(url)
        
        if(comboboxtan_secilmis_video_cozunurlugu==videonun_indirilebilecek_cozunurluk_secenekleri[0]):
            sec=yt.streams.filter(progressive=True).first()

        elif(comboboxtan_secilmis_video_cozunurlugu==videonun_indirilebilecek_cozunurluk_secenekleri[1]):
            sec=yt.streams.filter(progressive=True,file_extension="mp4").last()
        
        elif(comboboxtan_secilmis_video_cozunurlugu==videonun_indirilebilecek_cozunurluk_secenekleri[2]):
            sec=yt.streams.filter(only_audio=True).first()
        
        else:
            url_hata_mesaji.grid()

    sec.download(klasor_adi)
    url_hata_mesaji.config(text="İndirme Başlıyor...")







#-----------------------------------------------------------------------------------------------------------------------


#VİDEO LİNK GİR YAZISI

videonun_linkini_kutucuga_girin_yazisinin_degiskeni=Label(text="Video Linkini Kutucuğa Girin") 
#ekranda görülmesini istediğin uyarı

videonun_linkini_kutucuga_girin_yazisinin_degiskeni.grid() 
#grid komutu ile video_url_gir_yazisi içindeki text/metin ekrana çıkacak kutuda gözükür.


#-----------------------------------------------------------------------------------------------------------------------


#VİDEONUN LİNKİNİN GİRİLECEĞİ BOX

videonun_url_adresini_string_yap=StringVar() #hangi değişkeni string yapacağımızı anlattık.
#girilecek url içinde sayısal ve simgesel değerler olabileceği için "video_url_gir_basligi" değişkenine 
#girilecek url'yi  string yani metinsel ifadeye dönüştürecek komut.

videonun_url_adresinin_girilecegi_kutu=Entry(width=50,textvariable=videonun_url_adresini_string_yap)
#sağdan sola olacak şekilde
#videonun_url_adresini_string_yap=StringVar() ifadesi ile girilen değer tamamen metinsel ifadeye dönmüştü
#videonun_url_adresini_string_yap değişkenini textvariableye yani metin değeri olduğunu python'a anlattık
#width(genişlik) ifadesi ile kullanıcının url adresini girdiği yerin genişliğinin 50 piksel olduğunu anlattık
#(50piksel ifadesi program arayüzünde bu kutucuğun 50 piksel olarak gözükmesini istediğimiz anlama geliyor.Metin uzunluğu anlamına gelmiyor.)
#Bu parantez içindeki değerlerin hepsinin Entry ifadesi olduğunu belirttik. 
#işlem sağdan sola şekilde ilerliyor string_yağ ifadesini textvariable, width ifadesinin de 50 piksele eşit olduğu anlatıldı.
# Entry nin yani kutucuğun bu özellikleri kapsadığnı belirtip,onun solundaki ifade olan video_url_adresi değişkenine bunu aktardık.
# sonuç olarak biz video_url_adresi değişkenini işleme koyduğumuz vakit bu ifade; 50 piksel genişliğinde bir kutunun ve bu kutu içine
# girilecek olan ifadenin metinsel ifade olacağını anlattık

videonun_url_adresinin_girilecegi_kutu.grid() 
#özelliklerini atadığımız kutucuğun ekranda görülmesini sağladık

#-----------------------------------------------------------------------------------------------------------------------


#VİDEONUN LİNK YAPIŞTIRILACAĞI KUTUYA DEĞER GİRİLMEDİĞİ ZAMAN ALINACAK UYARI VEYA HATA MESAJI

url_hata_mesaji=Label(text="Eksik Veya Yanlış URL Adresi",bg="red",fg="white") 
#Kutucuğa link girilmediği zaman bir hata veya uyarı vermek istediğimiz zaman bu kodu çalıştıracağız.


#-----------------------------------------------------------------------------------------------------------------------


#DOSYANIN VEYA VİDEONUN NEREYE KAYDOLMASI İSTENİYOR YAZISI

video_nereye_kaydolsun_ekran_yazisi=Label(text="Videonun Kaydedilmesini İstediğiniz Konumu Seçin")
#label dediğimiz özelliğe text değerini atadığımızı ve text değeri içinde ne yazmasını istediğimizi belirttik.
#sağdan sola olarak kodları okuduğumuz için.
#ekranda yazmasını istediğimiz yazı-->text olduğunu anlattık-->Label değerine bu özellikleri attık
#dosya_nereye_kaydolsun_ekran_yazisi değişkeni çağırıldığı zaman bunun label olduğunu ve ekranda text değeri olarak
#Videonun Kaydedilmesini İstediğiniz Konumu Seçin      ifadesini yazdırmak istediğimizi anlattık.

video_nereye_kaydolsun_ekran_yazisi.grid()
#ekrana sabitledik

video_nereye_kaydolacak_butonu=Button(text="Kaydetme Konumunu Seç",bg="red",command=dosya_konumu_ac_fonksiyonu)
#buton yaptık ve bunun textinde "videoyu kaydet" yazmasını , renginin ise kırmızı olmasını istedik
#command özelliği ise butona tıklandığı zaman ne yapılması istendiğini ifade eder
#biz burada butona tıklandığı zaman dosya_konumunu_ac_fonksiyonunu devreye sokmasını istedik
#bu butona tıklamadan belirtilen fonksiyon asla devreye girmez
#lakin command yani tıklama özelliği haricindeki buton özellikleri aktiftir
#yani buton rengi üzerindeki yazı vs gibi 

video_nereye_kaydolacak_butonu.grid() 
#butonu ekrana sabitledik.

dosya_konumu_hatasi=Label(text="Dosya Konumu Hatası",bg="red",fg="white")
#dosya konumunda bir hata olursa veya kullanıcı dosya konumunu seçmezse ekranda gözükecek hata veya uyarı


#-----------------------------------------------------------------------------------------------------------------------


#VİDEONUN ÇÖZÜNÜRLÜĞÜ İLE İLGİLİ

videonun_indirilebilecek_cozunurluk_secenekleri=["1080p","720p","MP3"]
videonun_indirilebilecek_cozunurluk_secenekleri_comboxu=ttk.Combobox(values=videonun_indirilebilecek_cozunurluk_secenekleri)
videonun_indirilebilecek_cozunurluk_secenekleri_comboxu.grid()
#video indirilmek istenirken, hangi çözünürlükte video indirmek istediğini kullanıcıya sormak istiyoruz.
# videonun_indirilebilecek_cozunurluk_secenekleri değişkeni içine altertif seçenekleri ekledik (bu değerler arttırılabilir)
# bu değerleri combobox içine attık, ardından ifadeyi ComboBox values yani değerleri olarak bildirdik
# bildirilen değer videonun_indirilebilecek_cozunurluk_secenekleri_comboxu'a atandı
# bu seenek ekrana grid ifadesi ile sabitlendi


#-----------------------------------------------------------------------------------------------------------------------

#VİDEONUN İNDİR BUTONU İLE İLGİLİ

indirme_butonu=Button(text="Videoyu İndir",bg="red",command=video_indirme_fonksiyonu)
indirme_butonu.grid()



root.mainloop()
