# Industrial Anomaly Detection with Autoencoder (MVTec AD - Bottle Class)

این پروژه یک سیستم کشف ناهنجاری تصویری است که با استفاده از **Autoencoder** یاد می‌گیرد ظاهر «سالم» یک شیء صنعتی (بطری) چگونه است، و سپس در زمان تست، **با تحلیل خطای بازسازی**، تصاویر معیوب را شناسایی می‌کند.

---

##  ویژگی‌ها

✅ استفاده از دیتاست صنعتی واقعی (MVTec AD)  
✅ آموزش فقط روی داده‌های سالم (semi-supervised)  
✅ پیاده‌سازی ساده با PyTorch  
✅ رابط کاربری تعاملی با Gradio  
✅ تشخیص ناهنجاری با خطای بازسازی (MSE)  
✅ قابل گسترش برای سایر کلاس‌ها (مثل capsule, metal, ...)

---

##  ساختار کلی پروژه

```bash
mvtec-anomaly/
├── data/                
├── src/                 
│   ├── autoencoder.py
│   └── dataset.py
├── outputs/            
│   └── best_model.pth
├── app/                 
└── README.md
└── 01_train_autoencoder.ipynb
