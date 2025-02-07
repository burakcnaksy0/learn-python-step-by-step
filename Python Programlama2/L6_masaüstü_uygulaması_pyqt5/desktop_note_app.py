import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QTextEdit, QPushButton, QTreeWidget,
                             QTreeWidgetItem, QInputDialog, QMessageBox, QFileDialog)
from PyQt6.QtCore import Qt
from datetime import datetime


class NotUygulamasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gelişmiş Not Uygulaması")
        self.setGeometry(100, 100, 1200, 800)

        # Veri dosyası yolu
        self.veri_dosyasi = "notlar.json"

        # Ana widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Ana layout
        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        # Sol panel - Kategoriler ve notlar ağacı
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Kategoriler ve Notlar")
        self.tree.setMinimumWidth(300)
        self.tree.itemClicked.connect(self.not_sec)
        layout.addWidget(self.tree)

        # Sağ panel
        sag_panel = QVBoxLayout()

        # Metin düzenleyici
        self.editor = QTextEdit()
        self.editor.setMinimumWidth(700)
        sag_panel.addWidget(self.editor)

        # Buton grubu
        buton_layout = QHBoxLayout()

        self.kaydet_btn = QPushButton("Kaydet")
        self.kaydet_btn.clicked.connect(self.notu_kaydet)
        buton_layout.addWidget(self.kaydet_btn)

        self.yeni_kategori_btn = QPushButton("Yeni Kategori")
        self.yeni_kategori_btn.clicked.connect(self.yeni_kategori_ekle)
        buton_layout.addWidget(self.yeni_kategori_btn)

        self.yeni_not_btn = QPushButton("Yeni Not")
        self.yeni_not_btn.clicked.connect(self.yeni_not_ekle)
        buton_layout.addWidget(self.yeni_not_btn)

        self.sil_btn = QPushButton("Sil")
        self.sil_btn.clicked.connect(self.secili_oge_sil)
        buton_layout.addWidget(self.sil_btn)

        sag_panel.addLayout(buton_layout)
        layout.addLayout(sag_panel)

        # Veri yapısı
        self.notlar = {}
        self.mevcut_not = None

        # Verileri yükle
        self.verileri_yukle()

        # Pencere kapatıldığında verileri kaydet
        self.closeEvent = self.kapatma_eventi

    def verileri_yukle(self):
        """Kaydedilmiş notları dosyadan yükler"""
        if os.path.exists(self.veri_dosyasi):
            try:
                with open(self.veri_dosyasi, 'r', encoding='utf-8') as f:
                    self.notlar = json.load(f)
                self.agaci_guncelle()
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Veriler yüklenirken hata oluştu: {str(e)}")
        else:
            # İlk çalıştırma - varsayılan kategoriyi oluştur
            self.notlar = {"Genel": {}}
            self.agaci_guncelle()

    def verileri_kaydet(self):
        """Notları dosyaya kaydeder"""
        try:
            with open(self.veri_dosyasi, 'w', encoding='utf-8') as f:
                json.dump(self.notlar, f, ensure_ascii=False, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Hata", f"Veriler kaydedilirken hata oluştu: {str(e)}")

    def agaci_guncelle(self):
        """Ağaç görünümünü günceller"""
        self.tree.clear()
        for kategori, notlar in self.notlar.items():
            kategori_item = QTreeWidgetItem(self.tree)
            kategori_item.setText(0, kategori)
            for baslik in notlar.keys():
                not_item = QTreeWidgetItem(kategori_item)
                not_item.setText(0, baslik)

    def yeni_kategori_ekle(self):
        kategori, ok = QInputDialog.getText(self, "Yeni Kategori", "Kategori adı:")
        if ok and kategori:
            if kategori not in self.notlar:
                self.notlar[kategori] = {}
                self.agaci_guncelle()
                self.verileri_kaydet()
            else:
                QMessageBox.warning(self, "Hata", "Bu kategori zaten mevcut!")

    def yeni_not_ekle(self):
        secili = self.tree.selectedItems()
        if not secili:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kategori seçin!")
            return

        kategori = secili[0].text(0)
        if kategori not in self.notlar:
            QMessageBox.warning(self, "Hata", "Geçersiz kategori!")
            return

        baslik, ok = QInputDialog.getText(self, "Yeni Not", "Not başlığı:")
        if ok and baslik:
            if baslik in self.notlar[kategori]:
                QMessageBox.warning(self, "Hata", "Bu başlıkta bir not zaten var!")
                return

            self.notlar[kategori][baslik] = {
                "icerik": "",
                "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.agaci_guncelle()
            self.verileri_kaydet()

    def not_sec(self, item):
        parent = item.parent()
        if parent:  # Bir not seçildi
            kategori = parent.text(0)
            baslik = item.text(0)
            self.mevcut_not = (kategori, baslik)
            self.editor.setText(self.notlar[kategori][baslik]["icerik"])
        else:  # Bir kategori seçildi
            self.mevcut_not = None
            self.editor.clear()

    def notu_kaydet(self):
        if not self.mevcut_not:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir not seçin!")
            return

        kategori, baslik = self.mevcut_not
        self.notlar[kategori][baslik]["icerik"] = self.editor.toPlainText()
        self.notlar[kategori][baslik]["tarih"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.verileri_kaydet()
        QMessageBox.information(self, "Başarılı", "Not kaydedildi!")

    def secili_oge_sil(self):
        secili = self.tree.selectedItems()
        if not secili:
            return

        item = secili[0]
        parent = item.parent()

        if parent:  # Not silme
            kategori = parent.text(0)
            baslik = item.text(0)
            del self.notlar[kategori][baslik]
            if self.mevcut_not and self.mevcut_not[1] == baslik:
                self.mevcut_not = None
                self.editor.clear()
        else:  # Kategori silme
            kategori = item.text(0)
            if kategori == "Genel":
                QMessageBox.warning(self, "Hata", "Genel kategori silinemez!")
                return
            del self.notlar[kategori]
            if self.mevcut_not and self.mevcut_not[0] == kategori:
                self.mevcut_not = None
                self.editor.clear()

        self.agaci_guncelle()
        self.verileri_kaydet()

    def kapatma_eventi(self, event):
        """Pencere kapatıldığında çağrılır"""
        self.verileri_kaydet()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotUygulamasi()
    window.show()
    sys.exit(app.exec())