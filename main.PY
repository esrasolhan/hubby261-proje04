import cv2
from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.geometry("800x700")
pencere.title("Renk Tanıma")
pencere.configure(background="lavenderblush")
def tahmin():
    pencere.destroy()
    cap = cv2.VideoCapture(0)  # 0 olarak değiştirildi
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape
        # BGR'den HSV'ye dönüştürülüyor.(Gölge ve parlaklığın yaptığı renk değişiklikleri etkilenmemesi için.)
        cx = int(width / 2)
        cy = int(height / 2)
        # Ortadaki dairenin Webcam'in ortasında durması için konumu belirleniyor.

        # Pick pixel value
        pixel_center = hsv_frame[cy, cx] # Ortadaki dairenin koordinatları veriliyor.
        hue_value = pixel_center[0] # İlk baştaki renk değerinin 0 olduğu belirleniyor.

        color = "Undefined"
        if hue_value < 5:
            color = "KIRMIZI" #Eğer değer 5'ten küçükse "kırmızı"
        elif hue_value < 22:
            color = "TURUNCU" #Eğer değer 22'den küçükse "turuncu"
        elif hue_value < 33:
            color = "SARI"  #Eğer değer 33'ten küçükse "sarı"
        elif hue_value < 78:
            color = "YESİL" #Eğer değer 78'den küçükse "yeşil"
        elif hue_value < 131:
            color = "MAVi"  #Eğer değer 131'den küçükse "mavi"
        elif hue_value < 170:
            color = "MOR"   #Eğer değer 170'ten küçükse "mor"
        else:
            color = "KIRMIZI"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1) #Tahmini beyaz bir dikdörtgen içerisinde yazdırıyoruz.
        cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5) #Tahminle yakalanan rengin harflerini tahmin edilen renkle yazdırma
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    tahmin()

resim = ImageTk.PhotoImage(Image.open("welcome.PNG"))
lresim = Label(pencere,image=resim)
lresim.place(x=110,y=10)
lresim.pack()
anlatım= Label (pencere, text= "Uygulamanın amacı\nnesnelerin rengini tanımlamaktır!", font="Verdana 14 bold", fg="floral white", bg="PaleVioletRed1")
anlatım.place(x=200,y=200)
anlatım.pack()
anlatım1= Label(pencere, text= "Uygulama Nasıl Çalışır?\n 1-Pembe butona tıklamalısınız.\n2-Açılan WebCam'e renginin belirlenmesini istediğiniz nesneyi göstermelisiniz.\n3-Uygulamadan çıkmak için 'esc' tuşuna basmanız yeterlidir.",font= "Verdana 12", fg="floral white", bg="PaleVioletRed1")
anlatım1.pack()
pencere.resizable(width=False, height=False)
buton= Button(pencere, text="Uygulamaya geçmek için tıklayınız.", bg="PaleVioletRed1", fg= "floral white", command= tahmin)
buton.pack()
buton1= Button(pencere, text="Çıkmak için tıklayınız.", bg="black",fg="white",command=pencere.quit)
buton1.pack()

#Programdan esc tuşuyla çıkılması
pencere.mainloop()
cv2.destroyAllWindows()
