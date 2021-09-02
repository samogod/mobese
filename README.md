<br />
<p align="center">
  <a href="https://github.com/samet-g/mobese">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Türkiye Mobese Görüntü Takip</h3>

  <p align="center">
    Türkiye Mobese görüntülerinde OPENCV ve Yolo ile takip sistemi
  <p align="center">
      Multiple Object Tracking System in Turkish Mobese with OPENCV and Yolo       
    <br />
    <a href="https://github.com/samet-g/mobese"><strong>Explore the docs » Projeyi keşfet</strong></a>
    <br />
    <a href="https://github.com/samet-g/mobese/releases/tag/v1.0.0"></a>
    <img src="https://img.shields.io/github/v/release/samet-g/mobese"></a>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html"></a>
      <img src="https://img.shields.io/badge/license-GPL3-_red.svg"></a>
    <a href="https://github.com/samet-g/mobese/releases/download/v1.0.0/mobese.exe"></a>
      <img src="https://img.shields.io/github/downloads/samet-g/mobese/total"></a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents / İçerik Bölümü</summary>
  <ol>
    <li>
      <a href="#about-the-project--proje-hakkında">About the Project / Proje Hakkında</a>
      <ul>
        <li><a href="#built-with--kullanılanlar">Built With / Kullanılanlar</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started--başlangıç">Getting Started / Başlangıç</a>
      <ul>
        <li><a href="#installation--kurulum">Installation / Kurulum</a></li>
      </ul>
    </li>
    <li><a href="#usage--kullanım">Usage / Kullanım</a></li>  
    <li><a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a></li>
    <li><a href="#contributing--katkı">Contributing / Katkı</a></li>
    <li><a href="#license--lisans">License / Lisans</a></li>
  </ol>
</details>

> If you are having any os compatiblity issue, let me know. I will try to fix as soon as possible so let's explore the docs.

> Herhangi bir işletim sistemi uyumsuzluğu varsa, bana bildirin. En kısa sürede düzeltmeye çalışacağım, hadi dökümanı inceleyelim.

## About the Project / Proje Hakkında
Currently this project have **171** cameras. | Projeye yüklü **171** canlı mobese görüntüsü vardır.


    İstanbul > 44 Canlı Yayın          |   İstanbul > 44 Live CCTV Footage
    İzmir > 76 Canlı Yayın             |   İzmir > 76 Live CCTV Footage
    Tekirdag > 1 Canlı Yayın           |   Tekirdag > 1 Live CCTV Footage
    Konya > 32 Canlı Yayın             |   Konya > 32 Live CCTV Footage
    Ordu > 21 Canlı Yayın              |   Ordu > 21 Live CCTV Footage


<div align='center'>
<img src="images/demo.gif" width="90%"/>
</div>

This project implements Turkish Mobese CCTV footages detection classifier using pretrained yolov4-tiny models. If you trust your computer performance you can download yolov4 models too. The yolov4 models are taken from the official yolov4 paper which was released in April 2020 and the yolov4 implementation is from darknet.  

Bu proje, önceden eğitilmiş yolov4-tiny modellerini kullanarak Türk Mobese Canlı CCTV görüntülerine algılama sınıflandırıcısını uygular. Bilgisayarınızın performansına güveniyorsanız yolov4 modellerinide indirebilirsiniz.
Yolov4 modelleri, Nisan 2020'de yayınlanan resmi yolov4 belgesinden alınmıştır ve Yolov4 uygulaması darknet'tendir.


### Built With / Kullanılanlar

* [Python-3.8.5](https://www.python.org/downloads/release/python-385/)
* [OpenCV](https://docs.opencv.org/4.5.3/)
* [yolov4](https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view) weights, cfg and coco.names.


## Getting Started / Başlangıç

To get a local copy up and running follow these simple steps.  

Kendi bilgisayarınızda çalıştırmak için bu basit adımları izleyin.

### Installation / Kurulum

1. Clone the repo | Projeyi indir.
   ```sh
   git clone https://github.com/samet-g/mobese.git
   ```
2. Install Python packages | Gerekli Python paketlerini yükle.
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage / Kullanım

* Run with Python or [**Download**](https://github.com/samet-g/mobese/releases/download/v1.0.0/mobese.exe) the `.exe` file. 
*   Python kullanarak çalıştır veya `.exe` dosyasını [**indir**](https://github.com/samet-g/mobese/releases/download/v1.0.0/mobese.exe)
   ```sh
   python3 main.py | just run .exe file
   ```

## Roadmap / Yol Haritası

See the [open issues](https://github.com/samet-g/mobese/issues) for a list of proposed features  
It should be good use cctv cameras in city with Shodan API or make GUI.  

Sorunlar için [açık sorunları](https://github.com/samet-g/mobese/issues) kontrol edin.  
Shodan API ile esnaf güvenlik kamerası kullanmak veya GUI yapmak iyi olur.

## Contributing / Katkı

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated** especially <a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a> check this to-do list.  

Katkılar, açık kaynak topluluğu için büyük nimettir özellikle <a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a> kısmındaki yapılacak-listesini kontrol edin.  

1. Fork the Project | Projeyi forkla.
2. Create your Feature Branch | Katkıda Bulun  
`git checkout -b feature/YeniOzellik`
3. Commit your Changes | Değişiklikleri Commitle  
`git commit -m 'Add some YeniOzellik'`
4. Push to the Branch | Değişikliğini Yolla  
`git push origin feature/YeniOzellik`
5. Open a Pull Request | Pull Request Aç

## License / Lisans

Distributed under the GNU License.  
See `LICENSE` for more information.

GNU Lisansı altında dağıtılmaktadır.  
Daha fazla bilgi için `LICENSE` bölümüne bakın.
