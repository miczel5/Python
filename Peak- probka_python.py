## Imie i nazwisko: Michal Parciak
## Czas pracy nad zadaniem: 8h

class Peak:
    def __init__(self,lista):
        """Inicjalizacja obiektu"""
        self.lista = lista[:]
        self.n = len(self.lista) #wysokosc
        self.m = len(self.lista[0]) #szerokosc
        self.position = None 
        self.top = None; self.bot = None; self.left = None; self.right = None
    def ret_list(self):
        """zwraca liste"""
        return self.lista
    def ret_len_list(self):
        """zwraca rozmiar listy, wysokosc i dlugosc"""
        return (self.n,self.m)
    def ret_position_xy(self):
        "zwraca wspolrzedne tablicy wskaznika self.position"
        return self.position
    def ret_position(self,w1,w2):
        """Ustawia pozycje wskaznika ret_position przy pomocy zmiennych wejsciowych w1,w2"""
        self.position = [w1,w2] #wysokosc - w1, szerokosc - w2
        return self.position
    def ret_position_value(self):
        """Zwraca wartosc jaka kryje pod wspolrzednymi self.position"""
        if self.position != None:
            return self.lista[self.position[0]][self.position[1]] 
    def ret_top_value(self):
        """Zwraca wartosc jaka kryje pod wspolrzednymi self.top"""
        self.ret_top()
        if self.top != None:
            return self.lista[self.top[0]][self.top[1]] 
    def ret_bot_value(self):
        """Zwraca wartosc jaka kryje pod wspolrzednymi self.bot"""
        self.ret_bot()
        if self.bot != None:
            return self.lista[self.bot[0]][self.bot[1]] 
    def ret_left_value(self):
        """Zwraca wartosc jaka kryje pod wspolrzednymi self.left"""
        self.ret_left()
        if self.left != None:
            return self.lista[self.left[0]][self.left[1]] 
    def ret_right_value(self):
        """Zwraca wartosc jaka kryje pod wspolrzednymi self.right"""
        self.ret_right()
        if self.right != None:
            return self.lista[self.right[0]][self.right[1]] 
    def ret_top(self):
        """zwraca wspolrzedne punktu top"""
        self.top = None
        if self.position[0] - 1 > -1:
            self.top = [self.position[0] - 1,self.position[1]]
        return self.top
    def ret_bot(self):
        """zwraca wspolrzedne punktu bot"""
        self.bot = None
        if self.position[0] + 1 < self.n:
            self.bot = [self.position[0] + 1,self.position[1]]
        return self.bot
    def ret_left(self):
        """zwraca wspolrzedne punktu left"""
        self.left = None
        if self.position[1] - 1 > -1:
            self.left = [self.position[0],self.position[1]-1]
        return self.left
    def ret_right(self):
        self.right = None
        """zwraca wspolrzedne punktu right"""
        if self.position[1] + 1 < self.m:
            self.right = [self.position[0],self.position[1] + 1]
        return self.right
    def brute_force(self):
        """Szukanie wierzcholka metoda brute force"""
        self.ret_position(0,0)
        rozmiar_listy = self.ret_len_list()
        lista = self.ret_list()[:]
        for i in range(rozmiar_listy[0]): #wysokosc
            for j in range(rozmiar_listy[1]): #szerokosc
                self.ret_position(i,j)
                wsk = self.ret_position_value()
                t = self.ret_top_value(); b = self.ret_bot_value()
                r = self.ret_right_value(); l = self.ret_left_value()
                if wsk >= t and wsk >= b and wsk >= l and wsk >= r:
                    return wsk,self.ret_position(i,j)
    def gradient(self):
        """szukanie wierzcholka metoda gradient"""
        wsk = self.ret_position(0,0)
        rozmiar_listy = self.ret_len_list()
        lista = self.ret_list()[:]
        kierunek = self.ret_right()
        while True:
            while True:
                if self.ret_position_value() <  self.ret_right_value() and self.ret_position_value() != None:
                    self.ret_position(self.ret_right()[0],self.ret_right()[1])
                else:
                    break
            while True:
                if self.ret_position_value() <  self.ret_bot_value() and self.ret_position_value() != None:
                    self.ret_position(self.ret_bot()[0],self.ret_bot()[1])
                else:
                    break
            while True:
                if self.ret_position_value() <  self.ret_left_value() and self.ret_position_value() != None:
                    self.ret_position(self.ret_left()[0],self.ret_left()[1])
                else:
                    break
            while True:
                if self.ret_position_value() <  self.ret_top_value() and self.ret_position_value() != None:
                    self.ret_position(self.ret_top()[0],self.ret_top()[1])
                else:
                    break
            wsk = self.ret_position_value()
            t = self.ret_top_value(); b = self.ret_bot_value()
            r = self.ret_right_value(); l = self.ret_left_value()
            if wsk >= t and wsk >= b and wsk >= l and wsk >= r:
                return wsk,self.ret_position_xy()
                break    
    def dziel_i_rzadz(self):
        """szukanie wierzcholka metoda dziel i rzadz"""
        rozmiar_listy = [self.n, self.m] # wysokosc - 0 szerokosc - 1
        lista = self.ret_list()[:]
        rozmiar_listy[1] = rozmiar_listy[1] / 2
        self.ret_position(rozmiar_listy[0],rozmiar_listy[1])
        max_element = [0,0]
        while True:
            for i in range(self.n):
                self.ret_position(i,rozmiar_listy[1]) 
                if max_element[0] < self.ret_position_value():
                    max_element = [self.ret_position_value(),self.ret_position(i,rozmiar_listy[1])] # wartosc - 0 wspolrzedne - 1 
            self.ret_position(max_element[1][0],max_element[1][1])            
            if self.ret_position_value() > self.ret_left_value() and self.ret_position_value() > self.ret_right_value():
                print "ZNALEZIONO WIERZCHOLEK"
                return self.ret_position_value(),self.ret_position(max_element[1][0],max_element[1][1])
                break
            elif self.ret_left_value() > self.ret_right_value():
                rozmiar_listy[1]-=1
            elif self.ret_right_value() > self.ret_left_value():
                self.ret_position(self.ret_right()[0],self.ret_right()[1])
                rozmiar_listy[1]+=1
                
        
L = [[1,   2,  3,  4],
    [14, 15, 16,  5],
    [19,18 , 17,  6],
    [12,  9,  3,  7],
    [11, 10,  9,  8]]
tab = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
import random
for i in range(20):
    for j in range(20):
        tab[i].append(random.randint(1,100))
    print tab[i]        

lista = Peak(tab)
print lista.dziel_i_rzadz()
print lista.gradient()
print lista.brute_force()
