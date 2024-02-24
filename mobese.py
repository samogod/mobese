from colorama import Fore, Back, Style, init
import colorama, sys, time
import base64
colorama.init(autoreset=True)
bred = Fore.RED + Style.BRIGHT
red = Fore.RED
bos = "\033[1;37m"
z = """
					Version 1.0.1
		[+] █████████████████████████████████████████████████████ [+]
					  Coded by github.com/samogod\n\n
"""#dont edit or change that lines and nvm this shitty cog file.
print("""
		███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗███████╗
		████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
		██╔████╔██║██║   ██║██████╔╝█████╗  ███████╗█████╗  
		██║╚██╔╝██║██║   ██║██╔══██╗██╔══╝  ╚════██║██╔══╝  
		██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████║███████╗
		╚═╝	 ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
													""")
for c in z:
	sys.stdout.write(f"{bred}{c}")
	sys.stdout.flush()
	time.sleep(0.02)
istturistik = {}
istsehir = {
	"1":"http://ibb-media1.ibb.gov.tr:1935/live/223.stream/playlist.m3u8",	#Mecidiyeköy
	"2":"http://ibb-media1.ibb.gov.tr:1935/live/344.stream/playlist.m3u8",	#FSM Köprüsü
	"3":"http://ibb-media4.ibb.gov.tr:1935/live/81.stream/playlist.m3u8",	#15 Temmuz Şehitler Köprüsü
	"4":"http://ibb-media4.ibb.gov.tr:1935/live/43.stream/playlist.m3u8",	#Beşiktaş
	"5":"http://ibb-media2.ibb.gov.tr:1935/live/711.stream/playlist.m3u8",	#Beykoz Çubuklu İskele
	"6":"http://ibb-media4.ibb.gov.tr:1935/live/58.stream/playlist.m3u8",	#Büyükdere addesi Maslak
	"7":"http://ibb-media1.ibb.gov.tr:1935/live/282.stream/playlist.m3u8",	#Sirkeci
	"8":"http://ibb-media4.ibb.gov.tr:1935/live/72.stream/playlist.m3u8",	#Avcılar Metrobüs
	"9":"http://ibb-media4.ibb.gov.tr:1935/live/39.stream/playlist.m3u8",	#Bayrampaşa Otogar Girişi
	"10":"http://ibb-media1.ibb.gov.tr:1935/live/201.stream/playlist.m3u8", #Kadıköy Rıhtım
	"11":"http://ibb-media1.ibb.gov.tr:1935/live/202.stream/playlist.m3u8", #Kağıthane
	"12":"http://ibb-media1.ibb.gov.tr:1935/live/289.stream/playlist.m3u8",	#Madenler Çamlık
	"13":"http://ibb-media2.ibb.gov.tr:1935/live/1021.stream/playlist.m3u8",#H.U Tuneli Beykoz
	"14":"http://ibb-media2.ibb.gov.tr:1935/live/593.stream/playlist.m3u8",	#İstoç Arka Yol
	"15":"http://ibb-media2.ibb.gov.tr:1935/live/1020.stream/playlist.m3u8",#HalilUlukurt Tüneli Riva Girişi
	"16":"http://ibb-media1.ibb.gov.tr:1935/live/304.stream/playlist.m3u8", #Tem Altınşehir
	"17":"http://ibb-media1.ibb.gov.tr:1935/live/302.stream/playlist.m3u8",	#Tem Akşamsettin
	"18":"http://ibb-media2.ibb.gov.tr:1935/live/362.stream/playlist.m3u8",	#Tem Kınalı
	"19":"http://ibb-media2.ibb.gov.tr:1935/live/391.stream/playlist.m3u8", #Tem Silivri 1
	"20":"http://ibb-media2.ibb.gov.tr:1935/live/389.stream/playlist.m3u8", #Tem Silivri 2
	"21":"http://ibb-media1.ibb.gov.tr:1935/live/312.stream/playlist.m3u8", #Tem Büyükçekmece 1
	"22":"http://ibb-media1.ibb.gov.tr:1935/live/313.stream/playlist.m3u8", #Tem Büyükçekmece 2
	"23":"http://ibb-media1.ibb.gov.tr:1935/live/314.stream/playlist.m3u8",	#Tem Büyükçekmece 3
	"24":"http://ibb-media1.ibb.gov.tr:1935/live/315.stream/playlist.m3u8", #Tem Büyükçekmece 4
	"25":"http://ibb-media2.ibb.gov.tr:1935/live/426.stream/playlist.m3u8", #Tem Emniyet Mah. Avrupa Yönü
	"26":"http://ibb-media2.ibb.gov.tr:1935/live/392.stream/playlist.m3u8", #Tem Tekstilkent Anadolu Yönü
	"28":"http://ibb-media1.ibb.gov.tr:1935/live/168.stream/playlist.m3u8",	#D100 Beylikdüzü
	"28":"http://ibb-media2.ibb.gov.tr:1935/live/648.stream/playlist.m3u8",	#Dünya Gazetesi
	"29":"http://ibb-media4.ibb.gov.tr:1935/live/13.stream/playlist.m3u8",	#Atatürk Havalimanı
	"30":"http://ibb-media1.ibb.gov.tr:1935/live/174.stream/playlist.m3u8", #Bahçe Taksim
	"31":"http://ibb-media4.ibb.gov.tr:1935/live/45.stream/playlist.m3u8",	#Eyüp Feshane
	"32":"http://ibb-media4.ibb.gov.tr:1935/live/78.stream/playlist.m3u8", 	#D100 Hadımköy
	"33":"http://ibb-media2.ibb.gov.tr:1935/live/610.stream/playlist.m3u8", #D100 Ambarlı
	"34":"http://ibb-media4.ibb.gov.tr:1935/live/66.stream/playlist.m3u8",	#D100 Acıbadem Köprüsü
	"35":"http://ibb-media2.ibb.gov.tr:1935/live/611.stream/playlist.m3u8", #D100 Avcılar Cihangir
	"36":"http://ibb-media2.ibb.gov.tr:1935/live/612.stream/playlist.m3u8", #D100 Avcılar Şükrübey
	"37":"http://ibb-media2.ibb.gov.tr:1935/live/631.stream/playlist.m3u8", #D100 Cevizli
	"38":"http://ibb-media4.ibb.gov.tr:1935/live/94.stream/playlist.m3u8",	#D100 Çobançeşme Yenibosna Yönü
	"39":"http://ibb-media4.ibb.gov.tr:1935/live/114.stream/playlist.m3u8",	#Harem ido
	"40":"http://ibb-media4.ibb.gov.tr:1935/live/112.stream/playlist.m3u8",	#D100 Haramidere
	"41":"http://ibb-media2.ibb.gov.tr:1935/live/535.stream/playlist.m3u8", #D100 Küçükçekmece
	"42":"http://ibb-media4.ibb.gov.tr:1935/live/136.stream/playlist.m3u8", #D100 Küçükyalı
	"43":"http://ibb-media1.ibb.gov.tr:1935/live/161.stream/playlist.m3u8",	#D100 Şirinevler
	"44":"http://ibb-media4.ibb.gov.tr:1935/live/99.stream/playlist.m3u8",	#D100 Florya
}
tkrdgsehir = {
	"1":"http://wowza.tekirdag.bel.tr:4443/sahil/sahil.stream/chunklist_w1321054680.m3u8"
}
konyaturistik = {
	"1":"http://konya.sehirkameralari.com/live/540eea6d7e9f3/playlist.m3u8?wowzasessionid=899384592&token=", #Büyükşehir Stadyumu
	"2":"http://konya.sehirkameralari.com/live/52f8ad56da5f9/playlist.m3u8?wowzasessionid=626528448&token=", #Mevlana Meydanı
	"3":"http://konya.sehirkameralari.com/live/56ab53773fc0b/playlist.m3u8?wowzasessionid=396600308&token=", #Zafer Meydanı Yer Saati
	"4":"http://konya.sehirkameralari.com/live/52f8ac7f0b9c8/playlist.m3u8?wowzasessionid=1203461556&token=", #Eski garaj
	"5":"http://konya.sehirkameralari.com/live/56ab52e122769/playlist.m3u8?wowzasessionid=1298953125&token=", #Alaaddin Caddesi 1
	"6":"http://konya.sehirkameralari.com/live/56a9e456dee18/playlist.m3u8?wowzasessionid=2018875179&token=", #Alaaddin Caddesi 2
	"7":"http://konya.sehirkameralari.com/live/5f106b8a0102b/playlist.m3u8?wowzasessionid=1658802253&token=", #Mevlana Caddesi
	"8":"http://konya.sehirkameralari.com/live/5902d8e46ae8a/playlist.m3u8?wowzasessionid=1605811501&token=", #Kılıçarslan Şehir Meydanı
	"9":"http://konya.sehirkameralari.com/live/52f8ab6152788/playlist.m3u8?wowzasessionid=460170994&token=", #Kültürpark
	"10":"http://konya.sehirkameralari.com/live/52f89fa816e2b/media_6282.ts?wowzasessionid=971554536&token=", #Kayalıpark
	"11":"http://konya.sehirkameralari.com/live/52f0d277cb6b1/playlist.m3u8?wowzasessionid=1149551718&token=", # Büyükşehir Belediyesi
	"12":"http://konya.sehirkameralari.com/live/57066620cdebc/playlist.m3u8?wowzasessionid=1326907534&token=", #İstiklal Harbi Şehitleri Abidesi
	"13":"http://konya.sehirkameralari.com/live/52f8ac0de0eb2/playlist.m3u8?wowzasessionid=930027864&token=", #Mevlana Kültür Merkezi
}
konyasehir = {
	"1":"http://konya.sehirkameralari.com/live/52f8ace7aaa21/media_30206.ts?wowzasessionid=632840095&token=", #Otogar Kavşağı
	"2":"http://konya.sehirkameralari.com/live/52f8ab98bd9de/playlist.m3u8?wowzasessionid=2016814857&token=", #Kule Kavşağı
	"3":"http://konya.sehirkameralari.com/live/52f8acce91ebc/playlist.m3u8?wowzasessionid=1475888472&token=",#Sarraflar Yeraltı Çarşısı
	"4":"http://konya.sehirkameralari.com/live/52f8ab33dccf7/playlist.m3u8?wowzasessionid=601929902&token=", #Yeni Meram
	"5":"http://konya.sehirkameralari.com/live/52f89f69e3378/playlist.m3u8?wowzasessionid=1123909904&token=", #İhsaniye Kavşağı
	"6":"http://konya.sehirkameralari.com/live/594b8e36e65d3/playlist.m3u8?wowzasessionid=1633186134&token=", #Kent Plaza Kavşağı
	"7":"http://konya.sehirkameralari.com/live/52f8abd1889b0/playlist.m3u8?wowzasessionid=17914461&token=", #Sille Kavşağı
	"8":"http://konya.sehirkameralari.com/live/594b8d6ec0d3d/playlist.m3u8?wowzasessionid=479067348&token=", #Kılıçarslan Gençlik M.
	"9":"http://konya.sehirkameralari.com/live/52f8ac9765db4/playlist.m3u8?wowzasessionid=1387174615&token=", #Mevlana-Üçler Kavşağı
	"10":"http://konya.sehirkameralari.com/live/52f8ac26649e2/playlist.m3u8?wowzasessionid=1453885599&token=",#Hükümet Meydanı
	"11":"http://konya.sehirkameralari.com/live/52f8ab7ae043e/playlist.m3u8?wowzasessionid=2127588498&token=", #Vatan Caddesi
	"12":"http://konya.sehirkameralari.com/live/594b8b7dbd75b/playlist.m3u8?wowzasessionid=736522265&token=", #Türk Yıldızları Parkı
	"13":"http://konya.sehirkameralari.com/live/594b8ece1bb48/playlist.m3u8?wowzasessionid=799760739&token=", #İnce Minareli Medrese
	"14":"http://konya.sehirkameralari.com/live/52f8ad3d32ad3/playlist.m3u8?wowzasessionid=264828849&token=", #Stadyum-Gar Kavşağı
	"15":"http://konya.sehirkameralari.com/live/52f8abe9177bb/playlist.m3u8?wowzasessionid=466675754&token=", #Belh Kavşağı
	"16":"http://konya.sehirkameralari.com/live/52f8acff68895/playlist.m3u8?wowzasessionid=1300243399&token=", #Mobilyacılar Kavşağı
	"17":"http://konya.sehirkameralari.com/live/594b8c7fc023a/playlist.m3u8?wowzasessionid=708332899&token=", #Galericiler Kavşağı
	"18":"http://konya.sehirkameralari.com/live/52f89f4776f81/playlist.m3u8?wowzasessionid=1034037292&token=", #Karatay Medresesi
	"19":"http://konya.sehirkameralari.com/live/594b78742e13d/playlist.m3u8?wowzasessionid=541030983&token=", #Bilim Merkezi
}
izmirtrstk = {}
izmirsehir = {
	"1":"http://izum-cams.izmir.bel.tr/mjpeg/cd91d30d-7166-4a4d-b419-c4dfa6462f25", #Bostanlı Köprü
	"2":"http://izum-cams.izmir.bel.tr/mjpeg/f10c44bd-eae8-476f-bd8d-8efeb12fd851?i=1400707704", #Bostanlı Cami
	"3":"http://izum-cams.izmir.bel.tr/mjpeg/7346fa3e-4c41-461b-a74f-43ac5532c6f6", #Şair Eşref Bulvarı
	"4":"http://izum-cams.izmir.bel.tr/mjpeg/e052b2e0-feaa-401c-b8c5-727379779d18", #Cumhuriyet Meydanı
	"5":"http://izum-cams.izmir.bel.tr/mjpeg/746fca9f-1c55-4b6e-9d58-cd2d1639f46a", #Tekel Meydanı
	"6":"http://izum-cams.izmir.bel.tr/mjpeg/604e7624-ba21-427a-a48b-1fa1966d7294", #Çankaya
	"7":"http://izum-cams.izmir.bel.tr/mjpeg/fd4be714-623d-4eec-bbd5-cfbaab17f0b5", #Varyant
	"8":"http://izum-cams.izmir.bel.tr/mjpeg/4f76ee9c-83fa-4d71-8ff9-4e09d88a4b7d", #Güzelyalı
	"9":"http://izum-cams.izmir.bel.tr/mjpeg/df463759-3be8-4630-8de1-de1f7185a38c?i=953576242", #Küçükyalı
	"10":"http://izum-cams.izmir.bel.tr/mjpeg/7ebee59d-6707-4112-8a5c-24e7f98e1507?i=419057700", #Karataş
	"11":"http://izum-cams.izmir.bel.tr/mjpeg/632d8d02-9282-490d-8003-ae79b7b5d984", #Göztepe
	"12":"http://izum-cams.izmir.bel.tr/mjpeg/d0656cf9-6c9c-45ea-a483-8cef7c20fe8e?i=1082247381", #Gaziemir Kipa Kavşağı
	"13":"http://izum-cams.izmir.bel.tr/mjpeg/5ff56631-ca03-41de-ba35-9069dfb6fb62", #Gaziemir Migros
	"14":"http://izum-cams.izmir.bel.tr/mjpeg/5eb3b40b-b795-4239-bd97-a5b6a9ae5aeb", #Marina Kavşağı
	"15":"http://izum-cams.izmir.bel.tr/mjpeg/9a14db8d-6490-4917-954d-bfec9beab556", #Mustafa Kemal Sahil Bulvarı
	"16":"http://izum-cams.izmir.bel.tr/mjpeg/1b4a6338-b0b3-435b-a26a-25222cf0be08", #Karya Evleri
	"17":"http://izum-cams.izmir.bel.tr/mjpeg/4b083fa2-dcf2-43c0-8888-bcfd5edb7a33", #Gündogdu Meydanı
	"18":"http://izum-cams.izmir.bel.tr/mjpeg/4e8211b9-f36e-4b7a-9a1c-8a89cff673c8", #Demirköprü
	"19":"http://izum-cams.izmir.bel.tr/mjpeg/4913387e-3324-4fc8-af70-f070cf71d857", #Kahramanlar Kapısı
	"20":"http://izum-cams.izmir.bel.tr/mjpeg/d5a3c713-6ef2-4cc2-b5d9-4713aecd7b94", #Buca Üçkuyular Meydanı
	"21":"http://izum-cams.izmir.bel.tr/mjpeg/e36a3682-e2bc-4a89-9794-699fbe3df145?i=1613072378", #Uçanyol
	"22":"http://izum-cams.izmir.bel.tr/mjpeg/7918e064-f02e-4a6f-aaf2-2775f9788436", #Alsancak Gar
	"23":"http://izum-cams.izmir.bel.tr/mjpeg/1bf4a0ed-5183-4d17-ba61-a999e041b6e7", #Karşıyaka Atatürk Anıtı
	"24":"http://izum-cams.izmir.bel.tr/mjpeg/efef7740-c174-421c-86a7-6f80bd2f851c", #Seyrek Köprü
	"25":"http://izum-cams.izmir.bel.tr/mjpeg/a5f1b361-48fa-42f5-ac43-86409bac9635", #Konak Pier
	"26":"http://izum-cams.izmir.bel.tr/mjpeg/b7427564-34dc-41de-99ef-16913badf564", #Konak Diş Hastanesi
	"27":"http://izum-cams.izmir.bel.tr/mjpeg/fe9c3733-3630-49c1-b833-b0e861a13f67", #Şirinyer Koşu Yolu
	"28":"http://izum-cams.izmir.bel.tr/mjpeg/84f481f3-8bf0-49c9-96bb-e6ec37989239?i=1551096267", #Vakıflar Kavşağı
	"29":"http://izum-cams.izmir.bel.tr/mjpeg/f987ad08-6086-4cf1-a0a5-a55b9396cba2", #Montrö Meydanı
	"30":"http://izmirmag.net/cctv/?id=01d9ca62-f179-4289-bf4a-df5c2344709a?i=666907915", #Yeşildere Caddesi
	"31":"http://izum-cams.izmir.bel.tr/mjpeg/9752f5bf-e862-4036-ad2d-cd0cc7b43de7", #Adnan Kahveci Köprüsü
	"32":"http://izum-cams.izmir.bel.tr/mjpeg/cbacd6aa-a79a-421f-8ce2-c44c6f3838d1", #İkiçeşmelik
	"33":"http://izum-cams.izmir.bel.tr/mjpeg/dc3b5dd0-ba26-40ca-9bc3-0d4dadea7480", #Meslek Fabrikası
	"34":"http://izum-cams.izmir.bel.tr/mjpeg/c2524620-685c-43b5-a95f-1eb33863afb9", #Yeni Girne Kavşağı
	"35":"http://izmirmag.net/cctv/?id=775699dc-4ed4-4e61-b216-cb8841f52482?i=194412069", #Şemikler
	"36":"http://izum-cams.izmir.bel.tr/mjpeg/a8933525-5c3b-4d22-87d3-18d70b1a04d4?i=1547874981", #Mavişehir Giriş
	"37":"http://izum-cams.izmir.bel.tr/mjpeg/584cfd94-98e5-4874-a582-e30a971624c3?i=1048618307", #Atakent Kavşağı
	"38":"http://izum-cams.izmir.bel.tr/mjpeg/3a581c91-3506-484c-8444-4ea06b14410f?i=590362489", #Çiğli İtfaiye
	"39":"http://izum-cams.izmir.bel.tr/mjpeg/6c1e39d5-5d85-47fd-b44c-6264d6c801dc", #Ekol Hastanesi
	"40":"http://izum-cams.izmir.bel.tr/mjpeg/9e143284-f992-4d67-950f-63a5a9cb8f71?i=1143072170", #Egekent
	"41":"http://izum-cams.izmir.bel.tr/mjpeg/1d54cb86-6dea-4c3d-8d57-9fd58e1ed4d1", #Ata Sanayi Girişi
	"42":"http://izum-cams.izmir.bel.tr/mjpeg/a3bf2d58-a528-4215-85da-29e85a94934e", #Serbest Bölge
	"43":"http://izum-cams.izmir.bel.tr/mjpeg/c84d2123-04b9-4d05-9a16-87e21067f06b", #Mürselpaşa Bulvarı
	"44":"http://izum-cams.izmir.bel.tr/mjpeg/f8554d81-c886-47a2-81b2-ff124c977b29", #Basmane Kavşağı
	"45":"http://izum-cams.izmir.bel.tr/mjpeg/e4294d19-08e0-4fb3-8031-96a33b2adaa1", #Karşıyaka Naldöken Köprüsü
	"46":"http://izum-cams.izmir.bel.tr/mjpeg/52af3693-cfef-4f7c-99bb-400e4d96630f", #Zübeyde Hanım Kavşağı
	"47":"http://izum-cams.izmir.bel.tr/mjpeg/dc6abc36-4a0b-4780-9e8b-4d67eb5ec60b", #Soğukkuyu Kavşağı
	"48":"http://izum-cams.izmir.bel.tr/mjpeg/bb72d507-0c47-43a5-b349-092587fc4c14", #İzmir Arena
	"49":"http://izum-cams.izmir.bel.tr/mjpeg/d39c792d-c2e1-4491-bc75-779a766d3824", #Bahçelerarası Köprü
	"50":"http://izum-cams.izmir.bel.tr/mjpeg/b377c86a-7ab0-4f9d-a463-46395f540cad?i=1980828252", #Balçova Kipa
	"51":"http://izum-cams.izmir.bel.tr/mjpeg/6e11455b-2c73-437f-868c-5fa50c63233a?i=957687056", #Maltepe Askeri Lisesi
	"52":"http://izum-cams.izmir.bel.tr/mjpeg/85afd98d-1c1e-4c4c-a766-52d1fe4230be?i=738451076", #Narlıdere Otoban
	"53":"http://izum-cams.izmir.bel.tr/mjpeg/5ad02030-cd32-4a98-8826-a97383799047", #Narlıdere Folkart
	"54":"http://izum-cams.izmir.bel.tr/mjpeg/eb1e7a1e-b9a9-469c-a478-6bea7a670f5d", #Ege-Park Kavşağı
	"55":"http://izum-cams.izmir.bel.tr/mjpeg/871a4fd2-7133-42ec-b6d1-126668a2655f", #Bahçelerarası
	"56":"http://izum-cams.izmir.bel.tr/mjpeg/f02deb0d-70f3-407d-a821-157462f4e44d?i=272180414", #Mirhatpaşa Endüstri Meslek
	"57":"http://izum-cams.izmir.bel.tr/mjpeg/c001270e-d775-4819-988d-0cd4a97eea38", #Fahrettin Altay Kavşağı
	"58":"http://izum-cams.izmir.bel.tr/mjpeg/b163641a-8814-421b-a7f9-2ac4ed2c51fc?i=1489590977", #Denizmen Kavşağı
	"59":"http://izum-cams.izmir.bel.tr/mjpeg/a4808057-b7a5-4b69-9d52-fba73f597703", #Hıfzısıhha Kavşağı
	"60":"http://izum-cams.izmir.bel.tr/mjpeg/2c8135ad-ed2e-4146-a975-f41dd61118ce", #İslam Enstitüsü
	"61":"http://izum-cams.izmir.bel.tr/mjpeg/fe66561e-c61f-4fae-bf4c-ccd30015374b?i=1436060600", #Yeşilyurt Kavşağı
	"62":"http://izum-cams.izmir.bel.tr/mjpeg/e4796815-f5f7-4e0e-8bdf-7fc8298e956f", #Üçyol Kavşağı
	"63":"http://izum-cams.izmir.bel.tr/mjpeg/4e23c106-5536-4560-931f-01ace531e506", #Gümrük Borsa
	"64":"http://izum-cams.izmir.bel.tr/mjpeg/50b6305c-10ae-4025-9ba2-3e734738ae9a", #Tınaztepe Kavşağı
	"65":"http://izum-cams.izmir.bel.tr/mjpeg/1bbfebc8-6e4b-419a-bfee-9598ae95b2df", #Çevikbir Meydanı
	"66":"http://izum-cams.izmir.bel.tr/mjpeg/336d42fe-4946-4669-b536-5e1b8fc4a267", #Köstence Köprüsü Kavsagi
	"67":"http://izum-cams.izmir.bel.tr/mjpeg/2bd7a5f0-9b83-44d7-9e0f-da3bed72fcd9", #Buca Heykel Kavşağı
	"68":"http://izum-cams.izmir.bel.tr/mjpeg/b2da00ad-3b25-4ccc-badd-c6bae49a2802", #Şirinyer Tapu
	"69":"http://izum-cams.izmir.bel.tr/mjpeg/e0bdc30c-9fec-4156-9e45-1aa83ad03db0?i=603496981", #Yeşillik Caddesi Buca Ayrımı
	"70":"http://izum-cams.izmir.bel.tr/mjpeg/524f77fc-7edc-4eba-be51-c9dbbd516cbf", #Eşrefpaşa
	"71":"http://izum-cams.izmir.bel.tr/mjpeg/2566972d-7fb8-43fc-ab6b-39eff65149fc?i=1256017117", #Melez Deltası
	"72":"http://izum-cams.izmir.bel.tr/mjpeg/b7ea8f3c-4ed5-43e6-9aa4-885a26fc25b1", #Bornova Hükümet Konağı
	"73":"http://izum-cams.izmir.bel.tr/mjpeg/282ac058-5097-4b44-bda8-47167c9786db", #Bornova Stadyum Kavsağı
	"74":"http://izum-cams.izmir.bel.tr/mjpeg/382fa8d3-ecca-438c-822e-f73ef86e6d67?i=1156232904", #Migros Kavsagi
	"75":"http://izum-cams.izmir.bel.tr/mjpeg/db8b5b15-4cbf-4be7-9806-0753b3a14b93", #Otogar Kavsagi
	"76":"http://izum-cams.izmir.bel.tr/mjpeg/54dceff0-9115-4eb8-b470-b15e93ed8ef8?i=938582999", #Esrefpasa Hastane Kavsagi
}

'''giresuntrstk = {
	"1":"http://cdn-ipkamera.yayin.com.tr/giresunbel/kale/chunklist_w1828210775.m3u8", #Giresun Kalesi
}
giresunshr = {
	"1":"http://cdn-ipkamera.yayin.com.tr/giresunbel/cadde/chunklist_w1824418373.m3u8?anahtar=jO_dO3E3yYzbiItna_WVNw&sure=1629823114&ip=176.88.71.94jO_dO3E3yYzbiItna_WVNw&sure=1629823114&ip=176.88.71.94", #Gazi Caddesi
}'''

# Source: https://wowza.yayin.com.tr/playlist/marmarisbel/playlist_marmarisbel.json & https://www.marmaris.bel.tr/?Page=marmaris-canli-yayin
marmarishr = {
	"1":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/meydan/playlist.m3u8", #Gençlik Meydanı
	"2":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/yatlimani/playlist.m3u8", #Yat Limanı
	"3":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/uzunyali/playlist.m3u8", #Uzun Yalı
	"4":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/icmeler/playlist.m3u8", #İçmeler
	"5":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/ataturk/playlist.m3u8", #Atatürk Bulvarı
	"6":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/bozburun/playlist.m3u8", #Bozburun
	"7":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/kordon1/playlist.m3u8", #Kordon Caddesi 1
	"8":"http://cdn-ipkamera.yayin.com.tr/marmarisbel/kordon2/playlist.m3u8", #Kordon Caddesi 2
}

ordutrstk = {
	"1":"http://frn.rtsp.me/L4tcEnc8zhF83AGZ8WO6xw/1629897906/hls/CXyFwk23.m3u8", #Akyazı Sahil
	"2":"http://frn.rtsp.me/S5vpD-vqjiYaXG7qfJ1_0g/1629897937/hls/zpB1RgcD.m3u8", #Sahil Fatsa 2
	"3":"http://frn.rtsp.me/nIRZcejYONqRQ3HNoG4Qgw/1629897921/hls/tk4TH3TS.m3u8", #Sahil Fatsa 3
	"4":"http://frn.rtsp.me/EJDHfSyrxS8Dc6-KDMuVeg/1629898083/hls/oK2VQrHa.m3u8", #Atatürk Parkı Ünye
	"5":"http://frn.rtsp.me/c1wzh18AUoCrMLqHsF8nYw/1629898040/hls/XiWUS5Vq.m3u8", #Atatürk Parkı 2 | Ünye
}
ordusehir = {
	"1":"http://frn.rtsp.me/ZwXr_uPrGLSXJDuSPoUIZw/1629897877/hls/hBLSGWRI.m3u8", #İbrahim Fırtına Bulvarı 2
	"2":"http://frn.rtsp.me/DtrZYFjyf2mXiR15ohIOsw/1629897834/hls/Z80qG5MA.m3u8", #İbrahim Fırtına Bulvarı 3
	"3":"http://frn.rtsp.me/wQQZ8J0j9a7vc6CElKDdmw/1629897991/hls/kjapH2iE.m3u8", #Meydan Ulubey
	"4":"http://frn.rtsp.me/h0_SecMXZqPUawxeeKZqvA/1629897946/hls/DG6ayZs5.m3u8", #Meydan 2 Ulubey
	"5":"http://frn.rtsp.me/3FGovE2wrjg7zOGW6aqiww/1629898107/hls/IDHq7rg2.m3u8", #Kent Meydanı | Perşembe
	"6":"http://frn.rtsp.me/DNc2UJhxzle9hk5creuYCA/1629898355/hls/QrzIdHS6.m3u8", #Belediye Meydanı | Perşembe
	"7":"http://frn.rtsp.me/9DHWEhjKKsyhYE95rX0EfA/1629897516/hls/tdzdszeQ.m3u8", #Fidangör 1
	"8":"http://frn.rtsp.me/utogO3C1ln_oJ67rvjm5Gg/1629897528/hls/DRH7fSdk.m3u8", #Fidangör 2
	"9":"http://frn.rtsp.me/DHKYh23BnmokL2VvQZ3sSA/1629897540/hls/sYrd5ar2.m3u8", #Fidangör 3
	"10":"http://frn.rtsp.me/TVnTnOE6H7ca4PC3mJGWdQ/1629897547/hls/F56e9drS.m3u8", #Fidangör 4
	"11":"http://frn.rtsp.me/6CCuRQ5BvyMBVr2Q7Cav6g/1629897557/hls/ftG8bFK2.m3u8", #Fidangör 5
	"12":"http://frn.rtsp.me/O0ZugkaZeB50kfyyonxNNA/1629897567/hls/65nd2aN9.m3u8", #Fidangör 6
	"13":"http://frn.rtsp.me/RunM0rQg85LvDdJFA6IZww/1629897576/hls/h8NEi2B9.m3u8", #Fidangör 7
	"14":"http://frn.rtsp.me/cWap5lI6Aot_R7Cr17853g/1629897585/hls/3H3GEebn.m3u8", #Fidangör 8
	"15":"http://frn.rtsp.me/t_MkbBc8DofEWmpzKQfQsQ/1629897603/hls/i635a357.m3u8", #Fidangör 9
	"16":"http://frn.rtsp.me/t4zaijgkH1jHZReIWacRSw/1629897614/hls/fzDT25th.m3u8", #Fidangör 10
}

while True:
	try:
		print(f"{bred} Kamera Türünü Seç:\n[ 1 ]{bos} Turistik Kamera\n{bred}[ 2 ]{bos} Şehir-Trafik Kameraları\n ", end='')
		kameraturu = int(input())
	except ValueError:
		print(f"{Back.RED}[ - ]{bos} Kamera türü 1 veya 2 seçilmelidir.")
	if kameraturu >= 3:
		print(f"{Back.RED}[ - ]{bos} Kamera türü 1 veya 2 seçilmelidir.")
	elif kameraturu < 0:
		print(f"{Back.RED}[ - ]{bos} Kamera türü 1 veya 2 seçilmelidir.")
	else:
		break

while True:
	try:
		print(f"{bred}Şehir Seç:\n[ 1 ]{bos} İstanbul\n{bred}[ 2 ]{bos} İzmir\n{bred}[ 3 ]{bos} Tekirdağ\n{bred}[ 4 ]{bos} Konya\n{bred}[ 5 ]{bos} Ordu\n ", end='')
		sehirturu = int(input())
	except ValueError:
		print(f"{Back.RED}[ - ]{bos} Şehir 1 ile 5 aralığında sayı olmalıdır.")
	if sehirturu >= 6:
		print(f"{Back.RED}[ - ]{bos} Şehir 1 ile 5 aralığında seçilmelidir.")
	elif sehirturu <= 0:
		print(f"{Back.RED}[ - ]{bos} Şehir 1 ile 5 aralığında seçilmelidir.")
	else:
		break

#1 turistik #2 şehir-trafik
#1 istanbul #2 izmir 3# tekirdag 4# Konya 5# Ordu

def secim():
	if(kameraturu == 1 and sehirturu == 1):
		return print(f"{Back.RED}[ - ]{bos} İstanbul-Turistik kameraları mevcut değil.")
	elif(kameraturu == 1 and sehirturu ==4):
		print(f"{bred}[ 1 ]{bos} Büyükşehir Stadyumu\n{bred}[ 2 ]{bos} Mevlana Meydanı\n{bred}[ 3 ]{bos} Zafer Meydanı Yer Saati\n{bred}[ 4 ]{bos} Eski Garaj\n{bred}[ 5 ]{bos} Alaaddin Caddesi 1\n{bred}[ 6 ]{bos} Alaaddin Caddesi 2\n{bred}[ 7 ]{bos} Mevlana Caddesi\n{bred}[ 8 ]{bos} Kılıçarslan Şehir Meydanı\n{bred}[ 9 ]{bos} Kültürpark\n{bred}[ 10 ]{bos} Kayalıpark\n{bred}[ 11 ]{bos} Büyükşehir Belediyesi\n{bred}[ 12 ]{bos} İstiklal Harbi Şehitleri Abidesi\n{bred}[ 13 ]{bos} Mevlana Kültür Merkezi")
		kambolge = str(input())
		secilenkamera = konyaturistik[kambolge]
		return secilenkamera
	elif(kameraturu == 2 and sehirturu == 1):
		print(f"{bred}[ 1 ]{bos} Mecidiyeköy\n{bred}[ 2 ]{bos} FSM Köprüsü\n{bred}[ 3 ]{bos} 15 Temmuz Şehitler Köprüsü\n{bred}[ 4 ]{bos} Beşiktaş\n{bred}[ 5 ]{bos} Beykoz Çubuklu İskele\n{bred}[ 6 ]{bos} Maslak | Büyükdere Caddesi\n{bred}[ 7 ]{bos} Sirkeci\n{bred}[ 8 ]{bos} Avcılar Metrobüs\n{bred}[ 9 ]{bos} Bayrampaşa Otogar Girişi\n{bred}[ 10 ]{bos} Kadıköy Rıhtım\n{bred}[ 11 ]{bos} Kağıthane\n{bred}[ 12 ]{bos} Madenler Çamlık\n{bred}[ 13 ]{bos} Halil Ulukurt Tüneli\n{bred}[ 14 ]{bos} Tem Altınşehir\n{bred}[ 15 ]{bos} Tem Akşamsettin\n{bred}[ 16 ]{bos} Tem Kınalı\n{bred}[ 17 ]{bos} Tem Silivri 1\n{bred}[ 18 ]{bos} Tem Silivri 2\n{bred}[ 19 ]{bos} Tem Büyükçekmece 1\n{bred}[ 20 ]{bos} Tem Büyükçekmece 2\n{bred}[ 21 ]{bos} Tem Büyükçekmece 3\n{bred}[ 22 ]{bos} Tem Büyükçekmece 4\n{bred}[ 23 ]{bos} Tem Emniyet Mahallesi | Avrupa Yönü\n{bred}[ 24 ]{bos} Tem Tekstilkent Anadolu Yönü\n{bred}[ 25 ]{bos} D100 Beylikdüzü\n{bred}[ 26 ]{bos} Dünya Gazetesi\n{bred}[ 27 ]{bos} Atatürk Havalimanı\n{bred}[ 28 ]{bos} Bahçe Taksim\n{bred}[ 29 ]{bos} D100 Eyüp Feshane\n{bred}[ 30 ]{bos} D100 Hadımköy\n{bred}[ 31 ]{bos} D100 Ambarlı\n{bred}[ 32 ]{bos} D100 Acıbadem Köprüsü\n{bred}[ 33 ]{bos} D100 Avcılar Cihangir\n{bred}[ 34 ]{bos} D100 Avcılar Şükrübey\n{bred}[ 35 ]{bos} D100 Cevizli\n{bred}[ 36 ]{bos} D100 Çobançeşme Yenibosna Yönü\n{bred}[ 37 ]{bos} Harem ido\n{bred}[ 38 ]{bos} D100 Haramidere\n{bred}[ 39 ]{bos} D100 Küçükçekmece\n{bred}[ 40 ]{bos} D100 Küçükyalı\n{bred}[ 41 ]{bos} D100 Şirinevler\n{bred}[ 42 ]{bos} D100 Florya")
		kambolge = str(input())
		secilenkamera = istsehir[kambolge]
		return secilenkamera
	elif(kameraturu ==2 and sehirturu == 3):
		print(f"{bred}[ 1 ]{bos} Tekirdağ Sahil")
		kambolge = str(input())
		secilenkamera = tkrdgsehir[kambolge]
		return secilenkamera
	elif(kameraturu == 2 and sehirturu == 4):
		print(f"{bred}[ 1 ]{bos} Otogar Kavşağı\n{bred}[ 2 ]{bos} Kule Kavşağı\n{bred}[ 3 ]{bos} Sarraflar Yeraltı Çarşısı\n{bred}[ 4 ]{bos} Yeni Meram\n{bred}[ 5 ]{bos} İhsaniye Kavşağı\n{bred}[ 6 ]{bos} Kentplaza Kavşağı\n{bred}[ 7 ]{bos} Sille Kavşağı\n{bred}[ 8 ]{bos} Kılıçarslan Gençlik M.\n{bred}[ 9 ]{bos} Mevlana-Üçler Kavşağı\n{bred}[ 10 ]{bos} Hükümet Meydanı\n{bred}[ 11 ]{bos} Vatan Caddesi\n{bred}[ 12 ]{bos} Türk Yıldızları Parkı\n{bred}[ 13 ]{bos} İnce Minareli Medrese\n{bred}[ 14 ]{bos} Stadyum-Gar Kavşağı\n{bred}[ 15 ]{bos} Belh Kavşağı\n{bred}[ 16 ]{bos} Mobilyacılar Kavşağı\n{bred}[ 17 ]{bos} Galericiler Kavşağı\n{bred}[ 18 ]{bos} Karatay Medresesi\n{bred}[ 19 ]{bos} Bilim Merkezi")
		kambolge = str(input())
		secilenkamera = konyasehir[kambolge]
		return secilenkamera
	elif (kameraturu == 1 and sehirturu == 2):
		print(f"{Back.RED}[ - ]{bos} İzmir-Turistik kameraları mevcut değil.")
	elif (kameraturu == 1 and sehirturu == 3):
		print(f"{Back.RED}[ - ]{bos} Tekirdağ-Turistik kameraları mevcut değil.")
	elif(kameraturu == 2 and sehirturu ==2): #ik this print really suck :x
		print(f"{bred}[ 1 ]{bos} Bostanlı Köprü\n{bred}[ 2 ]{bos} Bostanlı Cami\n{bred}[ 3 ]{bos} Şair Eşref Bulvarı\n{bred}[ 4 ]{bos} Cumhuriyet Meydanı\n{bred}[ 5 ]{bos} Tekel Meydanı\n{bred}[ 6 ]{bos} Çankaya\n{bred}[ 7 ]{bos} Varyant\n{bred}[ 8 ]{bos} Güzelyalı\n{bred}[ 9 ]{bos} Küçükyalı\n{bred}[ 10 ]{bos} Karataş\n{bred}[ 11 ]{bos} Göztepe\n{bred}[ 12 ]{bos} Gaziemir Migros\n{bred}[ 13 ]{bos} Gaziemir Kipa Kavşağı\n{bred}[ 14 ]{bos} Marina Kavşağı\n{bred}[ 15 ]{bos} Mustafa Kemal Sahil Bulvarı\n{bred}[ 16 ]{bos} Karya Evleri\n{bred}[ 17 ]{bos} Gündogdu Meydanı\n{bred}[ 18 ]{bos} Demirköprü\n{bred}[ 19 ]{bos} Kahramanlar Kapısı\n{bred}[ 20 ]{bos} Buca Üçkuyular Meydanı\n{bred}[ 21 ]{bos} Uçanyol\n{bred}[ 22 ]{bos} Alsancak Gar\n{bred}[ 23 ]{bos} Karşıyaka Atatürk Anıtı\n{bred}[ 24 ]{bos} Seyrek Köprü\n{bred}[ 25 ]{bos} Konak Pier\n{bred}[ 26 ]{bos} Konak Diş Hastanesi\n{bred}[ 27 ]{bos} Şirinyer Koşu Yolu\n{bred}[ 28 ]{bos} Vakıflar Kavşağı\n{bred}[ 29 ]{bos} Montrö Meydanı\n{bred}[ 30 ]{bos} Yeşildere Caddesi\n{bred}[ 31 ]{bos} Adnan Kahveci Köprüsü\n{bred}[ 32 ]{bos} İkiçeşmelik\n{bred}[ 33 ]{bos} Meslek Fabrikası\n{bred}[ 34 ]{bos} Yeni Girne Kavşağı\n{bred}[ 35 ]{bos} Şemikler\n{bred}[ 36 ]{bos} Mavişehir Giriş\n{bred}[ 37 ]{bos} Atakent Kavşağı\n{bred}[ 38 ]{bos} Çiğli İtfaiye\n{bred}[ 39 ]{bos} Ekol Hastanesi\n{bred}[ 40 ]{bos} Egekent\n{bred}[ 41 ]{bos} Ata Sanayi Girişi\n{bred}[ 42 ]{bos} Serbest Bölge\n{bred}[ 43 ]{bos} Mürselpaşa Bulvarı\n{bred}[ 44 ]{bos} Basmane Kavşağı\n{bred}[ 45 ]{bos} Karşıyaka Naldöken Köprüsü\n{bred}[ 46 ]{bos} Zübeyde Hanım Kavşağı\n{bred}[ 47 ]{bos} Soğukkuyu Kavşağı\n{bred}[ 48 ]{bos} İzmir Arena\n{bred}[ 49 ]{bos} Bahçelerarası Köprü\n{bred}[ 50 ]{bos} Balçova Kipa\n{bred}[ 51 ]{bos} Maltepe Askeri Lisesi\n{bred}[ 52 ]{bos} Narlıdere Otoban\n{bred}[ 53 ]{bos} Narlıdere Folkart\n{bred}[ 54 ]{bos} Ege-Park Kavşağı\n{bred}[ 55 ]{bos} Bahçelerarası\n{bred}[ 56 ]{bos} Mirhatpaşa Endüstri Meslek\n{bred}[ 57 ]{bos} Fahrettin Altay Kavşağı\n{bred}[ 58 ]{bos} Denizmen Kavşağı\n{bred}[ 59 ]{bos} Hıfzısıhha Kavşağı\n{bred}[ 60 ]{bos} İslam Enstitüsü\n{bred}[ 61 ]{bos} Yeşilyurt Kavşağı\n{bred}[ 62 ]{bos} Üçyol Kavşağı\n{bred}[ 63 ]{bos} Gümrük Borsa\n{bred}[ 64 ]{bos} Tınaztepe Kavşağı\n{bred}[ 65 ]{bos} Çevikbir Meydanı\n{bred}[ 66 ]{bos} Köstence Köprüsü Kavşağı\n{bred}[ 67 ]{bos} Buca Heykel Kavşağı\n{bred}[ 68 ]{bos} Şirinyer Tapu\n{bred}[ 69 ]{bos} Yeşillik Caddesi | Buca Ayrımı\n{bred}[ 70 ]{bos} Eşrefpaşa\n{bred}[ 71 ]{bos} Melez Deltası\n{bred}[ 72 ]{bos} Bornova Hükümet Konağı\n{bred}[ 73 ]{bos} Bornova Stadyum Kavşağı\n{bred}[ 74 ]{bos} Migros Kavşağı\n{bred}[ 75 ]{bos} Otogar Kavşağı")
		kambolge = str(input())
		secilenkamera = izmirsehir[kambolge]
		return secilenkamera
	elif(kameraturu == 1 and sehirturu == 5):
		print(f"{bred}[ 1 ]{bos} Akyazı Sahil\n{bred}[ 2 ]{bos} Sahil Fatsa 2\n{bred}[ 3 ]{bos} Sahil Fatsa 3\n{bred}[ 4 ]{bos} Atatürk Parkı")
		kambolge = str(input())
		secilenkamera = ordutrstk[kambolge]
		return secilenkamera
	elif(kameraturu == 2 and sehirturu == 5):
		print(f"{bred}[ 1 ]{bos} İbrahim Fırtına Bulvarı 2\n{bred}[ 2 ]{bos} İbrahim Fırtına Bulvarı 3\n{bred}[ 3 ]{bos} Meydan Ulubey\n{bred}[ 4 ]{bos} Meydan Ulubey 2\n{bred}[ 5 ]{bos} Kent Meydanı | Perşembe\n{bred}[ 6 ]{bos} Belediye Meydanı | Perşembe\n{bred}[ 7 ]{bos} Fidangör 1\n{bred}[ 8 ]{bos} Fidangör 2\n{bred}[ 9 ]{bos} Fidangör 3\n{bred}[ 10 ]{bos} Fidangör 4\n{bred}[ 11 ]{bos} Fidangör 5\n{bred}[ 12 ]{bos} Fidangör 6\n{bred}[ 13 ]{bos} Fidangör 7\n{bred}[ 14 ]{bos} Fidangör 8\n{bred}[ 15 ]{bos} Fidangör 9\n{bred}[ 16 ]{bos} Fidangör 10")
		kambolge = str(input())
		secilenkamera = ordusehir[kambolge]
		return secilenkamera

