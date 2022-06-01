# Kütüphane yüklemeleri

import numpy as np
import time

# Uzay Yıldırım

print("")
print("")
print("   ___   __      __      _      ")
print("  / _ \  \ \    / /     (_)  ")
print(" | (_) |  \ \  / /__ _____ _ __")
print("  > _ <    \ \/ / _ \_  / | '__|")
print(" | (_) |    \  /  __// /| | |   ")
print("  \___/      \/ \___/___|_|_|   ")
print("")
print("")
print("[+][+][+][+][+][+][+][+][+][+]")
print("")

# Kod Başlangıcı

vezirler = 0

# Kullanıcı Ayarları
try:
	vezirInput = int(input("Tahta boyutu kaç olmalı? Girilebilecekler: 8 / 16 / 32 (Önerilen: 8) | "))
	if vezirInput == 8:
		vezirler = 8
	elif vezirInput == 16:
		vezirler = 16
	elif vezirInput == 32:
		print("NOT: 32 Seçtiniz - Henüz sadece n=27'ye kadar sonuç bulunabildi. İşlemin tamamlanması asırlar sürebilir.")
		vezirler = 32
	else:
		print("Geçersiz değer girildi. 8 olarak kabul ediliyor.")
		vezirler = 8
except:
    print("Geçersiz değer girildi. 8 olarak kabul ediliyor.")
    vezirler = 8

caprazlamaturuinput = str(input("Çaprazlama Türü (Tek Nokta/Çift Nokta) Girilebilecekler: 1 / 2 (Önerilen: 1 Tek) | "))
if caprazlamaturuinput == "1":
    caprazlamaturu = 1
elif caprazlamaturuinput == "2":
    caprazlamaturu = 2
else:
    print("Geçersiz değer girildi. 1 (Tek Nokta Çaprazlama) olarak kabul ediliyor.")
    caprazlamaturu = 1
mutasyonInput = str(input("Mutasyon kullanılsın mı? Girilebilecekler: e / h (Önerilen: e evet) | "))
if mutasyonInput == "e":
    mutasyonParametre = True
elif mutasyonInput == "h":
    mutasyonParametre = False
else:
    print("Geçersiz değer girildi. evet (True) olarak kabul ediliyor.")
    mutasyonParametre = True
    
try:
    maksInput = int(input("Maksimum kaç iterasyon yapılabilir? (Önerilen: 2000) | "))
except:
    print("Geçersiz değer girildi. 2000 olarak kabul ediliyor.")
    maksInput = 2000

populasyonSayisi = vezirler * 150 # Popülasyon sayısı parametrelere göre hesaplanır.
maksimumFitness = (vezirler * (vezirler - 1)) / 2 # Maksimum olabilecek Fitness değeri. (8 Vezir için 28)
mutasyonDegeri = 0.005 # Mutasyon yapılırken temel alınacak değer.
maksIterasyon = maksInput 
POPULASYON = None

print("[+][+][+][+][+][+][+]")
print("[+] BAŞLATILIYOR [+]")
print("[+][+][+][+][+][+][+]")

class tahta:
	def __init__(self):
		self.sira = None
		self.fitness = None
		self.survival = None
	def setSira(self, val):
		self.sira = val
	def setFitness(self, fitness):
		self.fitness = fitness
	def setSurvival(self, val):
		self.survival = val

def fitness(kromozom = None):
	cakisma = 0
	row_col_cakisma = abs(len(kromozom) - len(np.unique(kromozom)))
	cakisma += row_col_cakisma

	for i in range(len(kromozom)):
		for j in range(len(kromozom)):
			if ( i != j):
				dx = abs(i-j)
				dy = abs(kromozom[i] - kromozom[j])
				if(dx == dy):
					cakisma += 1
	return maksimumFitness - cakisma	

def kromozomOlustur():
	global vezirler
	init_distribution = np.arange(vezirler)
	np.random.shuffle(init_distribution)
	return init_distribution

def populasyonOlustur(populasyonBoyutu = 100):
	global POPULASYON
	print ("> İlk jenerasyon oluşturuluyor...")
	while True:
		POPULASYON = populasyonBoyutu
		populasyon = [tahta() for i in range(populasyonBoyutu)]
		for i in range(populasyonBoyutu):
			populasyon[i].setSira(kromozomOlustur())
			populasyon[i].setFitness(fitness(populasyon[i].sira))

		fitnessvals = [pos.fitness for pos in populasyon]
		maxfitnessvar = (maksimumFitness in fitnessvals) 
		if maxfitnessvar == False:
			break
	return populasyon


def ebeveynGet():	
	ebeveyn1, ebeveyn2 = None, None
    
	# Ebeveynler rastgele hayatta kalma olasılığına göre belirlenir.
	# Çözümü bulmak için Fitness değerini normalleştirmemiz gerekiyor.
	
	sum_fitness = np.sum([x.fitness for x in populasyon])
	for each in populasyon:
		each.survival = each.fitness/(sum_fitness*1.0)

	while True:
		ebeveyn1_random = np.random.rand()
		ebeveyn1_rn = [x for x in populasyon if x.survival <= ebeveyn1_random]
		try:
			t = np.random.randint(len(ebeveyn1_rn))
			ebeveyn1 = ebeveyn1_rn[t]
			break
		except:
			pass

	while True:
		ebeveyn2_random = np.random.rand()
		ebeveyn2_rn = [x for x in populasyon if x.survival <= ebeveyn2_random]
		try:
			t = np.random.randint(len(ebeveyn2_rn))
			ebeveyn2 = ebeveyn2_rn[t]
			if ebeveyn2 != ebeveyn1:
				break
			else:
				print ("< ! > Eşit ebeveynler, tekrar seçiliyor...")
				continue
		except:
			continue

	if ebeveyn1 is not None and ebeveyn2 is not None:
		return ebeveyn1, ebeveyn2, sum_fitness

def tekNokta_caprazla(ebeveyn1, ebeveyn2): # Tek Nokta Çaprazlaması
	n = len(ebeveyn1.sira)
	c = np.random.randint(n, size=1)
	cp = int(c)
	child = tahta()
	child.sira = []
	child.sira.extend(ebeveyn1.sira[0:cp])
	child.sira.extend(ebeveyn2.sira[cp:])
	child.setFitness(fitness(child.sira))	
	return child

def ciftNokta_caprazla(ebeveyn1, ebeveyn2): #  Çift Nokta Çaprazlaması
	n = len(ebeveyn1.sira)
	c1 = np.random.randint(0, n / 2, size=1)
	cp = int(c1)
	c2 = np.random.randint((n / 2) + 1, n, size=1)
	cp2 = int(c2)
	child = tahta()
	child.sira = []
	child.sira.extend(ebeveyn1.sira[0:cp])
	child.sira.extend(ebeveyn2.sira[cp:cp2])
	child.sira.extend(ebeveyn1.sira[cp2:])
	child.setFitness(fitness(child.sira))	
	return child

def mutate(child):
	"""	
	- Genetik teoriye göre çaprazlama durumu sırasında bir anormallik gerçekleştiğinde mutasyon meydana gelir.
	- Bir bilgisayar böyle bir anormalliği belirleyemediğinden böyle bir mutasyon geliştirme olasılığını kendimiz tanımlayabiliriz.
	"""
	if child.survival != None:
		if child.survival < mutasyonDegeri:
			c = np.random.randint(8)
			child.sira[c] = np.random.randint(8)
	return child

def GA(iterasyon):
	print ("[+] [+] [+] [+] " ,"Genetik Jenerasyon: >> #", int(iterasyon), " [+] [+] [+] [+] ")
	yeniPopulasyon = []
	for i in range(len(populasyon)):
		ebeveyn1, ebeveyn2, sum_fit = ebeveynGet()
		# print ("Oluşturulan ebeveynler: ", ebeveyn1, ebeveyn2)
		if caprazlamaturu == "1":
			child = tekNokta_caprazla(ebeveyn1, ebeveyn2)
		else:
			child = ciftNokta_caprazla(ebeveyn1, ebeveyn2)
		sum_fit += child.fitness
		child.survival = child.fitness/(sum_fit*1.0)
		if(mutasyonParametre):
			child = mutate(child)

		yeniPopulasyon.append(child)
	return yeniPopulasyon

def dur():
	fitnessvals = [pos.fitness for pos in populasyon]
	max_value = np.max(fitnessvals)
	print ("> Bu jenerasyonun en iyi Fitness değeri: ", max_value, " / ", maksimumFitness)
	print("________________________________________________________________________")
	if maksimumFitness in fitnessvals:
		print("Tamamlandı!")
		beep()
		return True
	if maksIterasyon == iterasyon:
		print("Maksimum iterasyon sayısına ulaşıldı. Timeout.")
		return True
	return False

def beep():
	print ("\a")

populasyon = populasyonOlustur(populasyonSayisi)
i = 1
print ("Popülasyon boyutu: ", len(populasyon))

iterasyon = 0;
while not dur():
	# En iyi pozisyon bulunana kadar iterasyonlara devam et.
	populasyon = GA(iterasyon)
	iterasyon +=1 

print (f"Toplam {iterasyon} iterasyon yapıldı.")
for each in populasyon:
	if each.fitness == maksimumFitness:
		print (each.sira)

time.sleep(4)

input("Çıkmak için Enter tuşuna basın...")