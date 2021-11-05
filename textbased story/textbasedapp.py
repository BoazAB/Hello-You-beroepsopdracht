import time

def first():
    print('je hoort schieten niet ver weg, als je instinctief in de richting van de geluiden kijkt, zie je een menigte van paniekerige mensen op je afrennen.')
    print("Wat doe je?")
    print("A, ga kijken")
    print("B, verstop je")
    print("C, ren weg")
    choice1= input()
    if choice1 == "A":
        print("Je besluit je te gaan kijken, je probeert jezelf door de menigde te duwen,")
        print("maar al deze rennende mensen, het is moeilijk om je balans te bewaren, nadat iemand tegen je op botst verlies je je evenwicht en val je in de menigde.")
        print(" als je op de grond ligt wordt je vertrapt door de mensen, ze denken niet eens na over waar ze heen gaan, ze rennen gewoon, weg van het geluid.")
        print(" voordat je bewustzijn verliest voel je het gewicht van iemand die op je arm staat. Alles word zwart voor je ogen.")
        time.sleep(18)
        print()
        print("Je wordt wakker in een ziekenhuis bed, je krijgt van je dokter te horen dat je arm gebroken is en dat je die dus even rust moet geven")
        Arm = "broken"
        time.sleep(5)
        
    elif choice1 == "B":
        print("Je duikt snel een steegje in. Een menigte rent voorbij, in paniek.")
        print(" Ze lijken net een horde koeien, ze vertrappen alles op hun pad,")
        print("je ziet een man struikelen, hij verdwijnt in de menigte.")
        
    elif choice1 == "C":
        print("nadat je voor een seconde bevrooren stond, besluit je te rennen.")
        print("Je rent sneller dan je ooit heb gerent, weg van het geluid, ")
        print("je rent verder en verder naar een plek waar je veilig bent.")
        
    else:
        print("antwoord met 'A', 'B' of 'C' alsjeblieft.")
        time.sleep(3)
        first()
first()
print()
print("Hierna besluit je naar huis te gaan")
time.sleep(5)

def howescap():
    print("Het kan niet langer zo door, je leven is in gevaar, dit land is te gevaarlijk. Je moet vluchten, alleen hoe?")
    print("A, Met de boot")
    print("B, met je paspoort over de grens")
    print("C, illegaal over de grens")
    choice2 = input()
    if choice2 == "A":
        print("Na een lange onconfertabele rit in een grote auto in het pikkedonker volgepropt en in een geheim compartmen kom je aan bij de zee.")
        print("Je ziet een klein bootje, waar je met heel veel mensen op moet, het ziet er naar uit dat het niet gaat passen.")
        time.sleep(10)

        def sit():
            print("Waar ga je zitten?")
            print("A, voorin.")
            print("B, achterin.")
            choicesitboat = input()
            if choicesitboat == "A" or "B":
                print("Na meerdere uren oncomfortabel op elkaar gelegen te hebben begint iedereen eindelijk een beetje te schuiven waardoor langzaam iedereen wat beter te zitten komt.")
                time.sleep(5)
            else:
                print("antwoord met 'A' of 'B' alsjeblieft.")
                time.sleep(5)
                sit()
            print("Waneer iedereen weer een beetje hoop krijgt en net op dat moment,")
            print("stopt de motor er mee, iedereen begint gelijk een beetje in paniek te schieten.")
            
            if choicesitboat == "B":
                def fix():
                    print("Wat doe je?")
                    print("A, probeer de motor te fixen.")
                    print("B, wacht tot iemand anders het fixt.")
                    boatmotor = input()
                    if boatmotor == "A":
                        print("ook al weet je niks van motors besluit je toch een poging the wagen,")
                        time.sleep(5)
                        print("nadat je een beetje aan de motor heb gezeten hoor je opeens 'KRAK', ")
                        time.sleep(5)
                        print("shit, de motor is kapot")
                        time.sleep(5)
                        print("zonder motor kom je niet ver,")
                        time.sleep(3)
                        print("je gaat dood, ")
                        time.sleep(3)
                        print("verloren op zee")
                        exit()    
                    elif boatmotor == "B":
                        print("Na een lange spannings volle wacht hoor je het geluid van een startende motor.")
                        print("Als je kijkt zie je dat iemand de motor heeft gemaakt.")
                        print("De boot is weer wat kalmer.")
                    else:  
                        print("antwoord met 'A' of 'B' alsjeblieft.")
                        fix()
                fix()    
            elif choicesitboat == "A": 
                print("Na een lange spannings volle wacht hoor je het geluid van een startende motor.")
                print("Als je kijkt zie je dat iemand de motor heeft gemaakt.")
                print("De boot is weer wat kalmer.")
                
            time.sleep(20)
            print("Na uren ongemakelijk te hebben gezeten komen jullie eindelijk aan, het vaste land.")
        sit()
        
    elif choice2 == "B":
        def naarduane():
            print("Je besluit langs te gaan, je heb namelijk gewoon een paspoort")
            time.sleep(5)
            print()
            print("Als je bij de douane aan komt verteld de bewaker dat je paspoort niet geldig is, dus je moet omkeren.")
            print("Wat doe je?")
            print("A, Bedenk een andere manier om te ontsnappen.")
            print("B, loop gewoon door, je wil weg, dus je mag weg.")
            choicegrens=input()
            if choicegrens == "A":
                print("Je loopt terug, je vind wel een andere manier om uit dit land te komen.")
                howescap()
            elif choicegrens == "B":
                print("Terweil je aan het doorlopen bent hoor je de man schreeuwen")
                print("'HÉ STOP'")
                print("Hij vraagt je te stoppen.")
                time.sleep(4)
                print()
                print("De man komt achter je aan, wat doe je?")
                print("A, geef jezelf over")
                print("B, REN")
                okkaren=input()
                if okkaren == "A":
                    print("De man arresteert je en neemt je mee naar de gevangenis.")
                    print("de gevangenis is zwaar en streng, na het een jaar uitgehouden te hebben ga je uiteindelijk toch dood in de gevangnis door slechte behandeling.")
                elif okkaren == "B":
                    print("BANG")
                    time.sleep(5)
                    print("Wat dacht je dat er ging gebeuren?")
        naarduane()
        
    elif choice2 == "C":
        def justgo():
            print("Je besluit illegaal paspoort over de grens te gaan, alleen hoe?")
            print("A, over de grens gesmokkelt worden.")
            print("B, gewoon langs de grens lopen.")
            hoelangsgrens = input()
            if hoelangsgrens == "A":
                print("je word in de achter kant van een pickup ge legd daarna wordt er een houte plank over je heen gelegd.")
                print("opeens begin je te bewegen na ongeveer een uur wordt de houte plank verwijderd.")
                time.sleep(5)
                print("je wordt overgezed naar een wit bestel busje.")
                print("en na zolang dat je niet eens weet hoe lang stoppen we opeens voor een lange periode.")
                print("je hoort de deuren open gaan en je ziet een blauw en wit licht.")
                time.sleep(5)
                print(" en daar staan de smokkelaars die je had ontmoet in handboeien naast politie")
                exit()
            elif hoelangsgrens == "B":
                print("Terweil je wacht tot het nacht is loop je langs de grens, kijkend of er een zwake plek is waar je er makkelijk door heen kan, ")
                time.sleep(5)
                print("en ja, je vind uiteindelijk een plek waar je in prensipe doorheen kan rammen met de auto, ") 
                print("ook vind je een zwak stuk in het hek waar je als je het met een tang een beetje vergroot doorheen zou kunnen kruipen.")
                print("Wat doe je?")
                print("A, Ram door het hek heen.")
                print("B, Kruip door het hek heen.")
                langshek = input()
                def hek():
                    if langshek == "A":
                        print("Zodra de nacht is gevallen rij je met je auto naar de grens.")
                        print(" Je ramt het hek, het hek is steviger dan je dacht. ")
                        print("Je hoord iemand schreeuwen, je bent gezien.")
                        print(" het is nu alles of niks je rijd achter uit nog een ram en het hek geeft wel in, je trapt op het gaspedaal en BANG.")
                        print(" je bent er door, je hoort een geluid dat je eerder ook hebt gehoord, een wapen dat gevuurt word.")
                        print("Je blijft op het gas drukken, snel weg, bijna ontsnapt bijna vrijheid.")
                        time.sleep(15)
                        print("Je bent ontsnapt uit Syrië, je heb je auto en je vrijheid.") 
                        print("nu alleen nog een baan vinden en dan kan je een nieuw leven opbouwen. Het is wel moeilijk om je oude leven achter te laten")
                    elif langshek == "B":
                        print("Je gaat snachts naar het hek, met een tang, als je dit gat nog een beetje vergroot zou je er doorheen passen.")
                        time.sleep(5)
                        print("Knip")
                        time.sleep(3)
                        print("Knip")
                        time.sleep(1)
                        print("Knip")
                        time.sleep(2)
                        print("Opeens hoor je een stem, :'HÉ STOP!'")
                        print("SHIT, je bent gezien")
                        time.sleep(5)
                        print()
                        def hekgat():
                            print("wat doe je?")
                            print("A, Kruip snel door het gat")
                            print("B, REN")
                            gespot =input()
                            if gespot == "A":
                                print("Het is iets te klein maar je kruipt snel door het gat")
                                time.sleep(5)
                                print("als je ongeveer halvewegen bent voel je opeens weerstand,")
                                print("SHIT, je shirt blijft hangen, je probeert je los te trekken")
                                print("Net op dat moment voel je je benen vast gegrepen worden")
                                print("je wordt naar de gevangenis gestuurd waar je na het anderhalf jaar uit te houden word vermoord.")
                                exit()
                            elif gespot =="B":
                                print("Je rent snel de bosjes in weg.")
                                print("Je hoort nog een paar keer het geluid van een geweerschot maar ja blijft rennen en rennen. ")
                                print("Uiteindelijk hoor je geen geluid meer, geen schoten, alleen maar het stromende bloed in je oren.") 
                                print("Na lang gerent te hebben ben je eindelijk thuis, je hebt wel voor meer dan een uur gerent, ")
                                print("Je bent uitgeput, je valt inslaap op je bed.")
                                time.sleep(10)
                                print("de volgende dag kom je om in een explosie, was je nu maar gevlucht.")
                            else:
                                print("antwoord met een 'A' of een 'B'")
                                hekgat()

                        hekgat()
                hek()    
        justgo()      
howescap()