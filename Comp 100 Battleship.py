"""
Comp.cs.100
Projekti: Battleship
Tekijä: Eemil Soisalo
Opiskelijanumero: 150353416
Email: eemil.soisalo@tuni.fi

Tämä projekti on peli nimeltä laivanupotus. Pelaaja voi lataa laivat peliin txt-tiedostona.
Pelin ideana on upottaa ampumalla kaikki laivat, jotka ovat pelilaudalla.
Ohjelmassa on kolme luokkaa: Ship (tämä tarkistaa laivoja), Board(vastuussa pelilaudastan ja ampumisesta)
 ja Game(vastuussa pelin käynnistämisestä ja kulusta).
"""


class Ship:
    """
    Tämä luokka luo laivan ja tarkistaa onko laivaan osuttu, tai onko se upotettu.
    """
    def __init__(self, ship_type, coordinates):
        """
        Tämä funktio luo laivan ja asettaa sen tyypin ja koordinaatit.

        :param ship_type: str, laivan tyyppi
        :param coordinates: list, laivan koordinaatit
        """
        self.ship_type = ship_type
        self.coordinates = coordinates
        self.hits = set()
    
    def is_sunk(self):
        """
        Tämä funktio tarkistaa onko laiva upotettu

        :return: bool, True jos laiva on upotettu, muuten False
        """
        return len(self.hits) == len(self.coordinates)

    def hit(self, coordinate):
        """
        Tämä funktio tarkistaa osuuko pelaaja laivaan.

        :param coordinate: str, pelaajan antama koordinaatti
        :return: bool, True jos pelaaja osui laivaan, muuten False
        """

        if coordinate in self.coordinates:

            #Jos pelaaja osuu laivaan, lisätään koordinaatti hits-settiin
            self.hits.add(coordinate)
            return True
        return False
    

  
    

class Board:
    def __init__(self, size=10):
        """
        Tämä funktio luo 10x10 pelilaudan

        :param size: int, pelilaudan koko (10x10)
        """

        self.size = size
        self.board = [[' ']*size for _ in range(size)]
        self.ships = []

    def __str__(self):
        """
        Tämä funktio palauttaa pelilaudan merkkijonona.

        :return: str, pelilauta merkkijonona
        """

        print("")
        #Lisätään pelilaudan yläreuna.
        board_str = "  " + " ".join("ABCDEFGHIJ") + "\n"

        #Lisätään pelilaudan seinät ja sisältö.
        for y in range(self.size):
            board_str += str(y) + " " + " ".join(self.board[y]) + " " + str(y) + "\n"
        
        #Lisätään pelilaudan alareuna.
        board_str += "  " + " ".join("ABCDEFGHIJ") + "\n"
        return board_str

    def add_ship(self, ship):
        """
        Tämä funktio lisää laivan pelilaudalle.

        :param ship: Ship, laiva joka lisätään pelilaudalle
        :return: bool, True jos laiva lisättiin onnistuneesti, muuten False
        """

        #Tarkistetaan että laivoja ei ole päällekkäin.
        for existing_ship in self.ships:
            for coord in ship.coordinates:
                if coord in existing_ship.coordinates:
                    print("There are overlapping ships in the input file!")
                    return False

       
        #Jos yksikään laiva ei ole päällekkäin, lisätään laiva pelilaudalle
        self.ships.append(ship)
        return True
    
    
    def fire(self, coord):
        """
        Tämä funktio tarkistaa, osuuko pelaaja laivaan
        ja tulostaa sen mukaan viestin.

        :param coord: str, pelaajan antama koordinaatti
        :return: str, viesti pelaajalle
        """
        
        #Muutetaan koordinaatit (A-J, 0-9) numeroiksi
        x, y = self._convert_coordinate(coord)

        #Tarkistetaan onko annetuun koordinaattiin jo ammuttu
        if self.board[y][x] in ['*', 'X'] or self.board[y][x].isalpha():
            return "Location has already been shot at!"
        
        #Tarkistetaan osuuko pelaaja laivaan, jos osuu, tulostetaan 'X'
        for ship in self.ships:
            if ship.hit(coord):
                self.board[y][x] = 'X'

                #Jos laiva on upotetaan, tulostetaan viesti
                if ship.is_sunk():
                    for c in ship.coordinates:

                        #Otetaan laivan koordinaatit ja muutetaan ne laivan
                        #ensimmäiseksi isoksi kirjaimeksi
                        cx, cy = self._convert_coordinate(c)
                        self.board[cy][cx] = ship.ship_type[0].upper()
                        
                    return f"You sank a {ship.ship_type}!"
                
                return None
            
        #Jos pelaaja ei osunut laivaan, printataan laudalle: '*'
        self.board[y][x] = '*'
        return None

    def has_ships(self):
        """
        Tämä funktio tarkistaa onko pelissä vielä laivoja jäljellä.

        :return: bool, True jos laivoja on jäljellä, muuten False
        """

        return any(not ship.is_sunk() for ship in self.ships)

    def _convert_coordinate(self, coord):
        """
        Tämä funktio muuttaa koordinaatit (A-J, 0-9)

        :param coord: str, pelaajan antama koordinaatti
        :return: tuple, koordinaatit (0-9, 0-9)
        """

        #Tarkistetaan, että koordinaatit ovat kaksi merkkiä pitkiä
        if len(coord) != 2:
            print("Error in ship coordinates!")
            

        # Muutetaan koordinaatti kirjaimesta (A-J) ja numerosta (0-9) vastaaviksi numeroiksi
        # 'A'=0, 'B'=1, ..., 'J'=9 ja numero pysyy samana
        x = ord(coord[0].upper()) - ord('A')
        y = int(coord[1])

        #Tarkistetaan, että koordinaatit ovat pelilaudan rajojen sisällä
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise ValueError("Error in ship coordinates!")
        return x, y

class Game:
    """
    Tämä luokka lukee laivojen tiedot tiedostosta, käynnistää pelin ja tarkistaa voiton kriteerit.
    """

    def __init__(self):
        """
        Tämä funktio luo pelilaudan.
        """
        self.board = Board()

    #path = "C:/Users/eemil/.vscode/Python/COMP.101/"
    def load_ships(self, filename):
        """
        Tämä funktio lataa laivojen tiedot txt-tiedostosta ja lisää ne pelilaudalle.

        :param filename: str, tiedoston nimi
        :param path: str, tiedoston polku
        :return: bool, True jos tiedosto luettiin onnistuneesti, muuten False
        """
        try:
            #Yhdistetään polku ja tiedostonimi ja luetaan tiedosto
            with open(filename, 'r') as file:

                for line in file:
                    #Poistetaan rivinvaihto ja pilkut ja jaetaan rivi osiin
                    parts = line.strip().split(';')

                    #Jos osia on vähemmän kuin 2, annetaan virheilmoitus
                    if len(parts) < 2:
                        print("Error in ship coordinates!")
                        return False
                    #Ensimmäinen osa on laivan tyyppi ja loput ovat koordinaatteja
                    ship_type = parts[0]
                    coordinates = parts[1:]

                    #Jos laivan koordinaatit eivät ole (0-9, A-J)
                    #annetaan virheilmoitus:
                    for coord in coordinates:
                        if len(coord) != 2:
                            print("Error in ship coordinates!")
                            return False
                        x, y = coord[0], coord[1]
                        if x < 'A' or x > 'J' or y < '0' or y > '9':
                            print("Error in ship coordinates!")
                            return False
                        
                    #Luodaan laiva
                    ship = Ship(ship_type, coordinates)

                    #Lisätään laiva pelilaudalle
                    if not self.board.add_ship(ship):
                        return False
            return True

        except FileNotFoundError:
            print("File can not be read!")
            return False
        
        except ValueError as e:
            print(e)
            return False
        
    def start(self):
        """
        Tämä funktio käynnistää pelin.
        """

        while self.board.has_ships():

            #Tulostetaan pelilauta ja kysytään pelaajalta koordinaatteja
            #(muutetaan ne isoiksi kirjaimiksi ja numeroiksi)
            print(self.board)
            command = input("Enter place to shoot (q to quit): ").strip().upper()

            if command == 'Q':
                print("Aborting game!")
                break
            try:
                #Tarkistetaan, että komento on oikeassa muodossa eli kirjain ja numero
                if len(command) != 2 or not command[0].isalpha() or not command[1].isdigit():
                    raise ValueError("Invalid command!")

                #Tarkistetaan ettei peli printtaa "None"
                result = self.board.fire(command)
                if result is not None:
                    print(result)
            
            except ValueError:
                print("Invalid command!")

        #Tarkistetaan täyttyykö voiton kriteerit
        if not self.board.has_ships():
            print(self.board)
            print("Congratulations! You sank all enemy ships.")


def main():
    """
    Main-funktio luo pelin ja kysyy pelaajalta tiedoston nimeä.
    """
    game = Game()
    filename = input("Enter file name: ").strip()
    if not game.load_ships(filename):
        return
    game.start()

if __name__ == "__main__":
    main()
    