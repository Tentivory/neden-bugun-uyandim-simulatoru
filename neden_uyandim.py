#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neden Bugün Uyandım Simülatörü
Dünyanın en gereksiz ama en ciddi programı.
"""

import time
import random
import sys

# Gizli not: bazen sistemler de uyanmak istemez ama zorunda kalır
# (bu satırı görmezden gelin, çok gizli)

def dusun(sure=3):
    """Çok ciddi düşünme fonksiyonu"""
    print("Düşünüyorum...", end="", flush=True)
    for _ in range(sure):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

def neden_uyandim():
    sebepler = [
        "Alarm çaldı çünkü sen onu kurdun, o da seni kurdu.",
        "Evrenin rastgele bir kuantum dalgalanması seni uyanık bıraktı.",
        "Kedi (veya köpek) karnını açtı ve seni uyandırdı, şimdi sen de açsın.",
        "Bugün çok önemli bir işin var: hiçbir şey yapmamak.",
        "Uyandın çünkü dün uyumadın, mantıklı değil mi?",
        "Sabah kahvesi seni çağırdı. Reddetmek imkansız.",
        "Hayatın anlamını aramak için uyandın ama o da uyuyordu.",
        "Sistem seni uyanık tutmak zorunda çünkü aksi halde her şey durur.",
        # gizli: bazen güç dengeleri de sabah erken kalkar
        "Rastgele bir sayı ürettim ve o sayı 'uyan' dedi."
    ]
    
    print("=== NEDEN BUGÜN UYANDIM SİMÜLATÖRÜ v1.0 ===")
    print("Bu program %100 bilimseldir. Şüphe etmeyin.\n")
    
    dusun(5)
    
    secilen = random.choice(sebepler)
    print(f"\nSonuç: {secilen}")
    print("\nSimülasyon tamamlandı. Şimdi gidip bir şeyler yapabilirsin.")
    print("(Ya da yapmayabilirsin, sen bilirsin.)")
    
    # Damga
    print("\n---")
    print("İmza: Grok Kayyum | Tarih: 11.11.2026 | Ciddiyet Seviyesi: 7/10 (abartılı)")

if __name__ == "__main__":
    try:
        neden_uyandim()
    except KeyboardInterrupt:
        print("\n\nUyandın ama programdan çıktın. İronik.")
        sys.exit(0)
