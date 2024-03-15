# Raspberry-pi-ORB-Keyboard-Controlled-Robot-NL

SAMENVATTING:

     Dit is een raspberry Pi4/Zero W Robot(using parts from orb : https://openroboticplatform.com/ ) 
     bestuurt met Keyboard in  VNC Viewer:https://www.realvnc.com/en/connect/download/viewer/
     video link is here : 
     youtube: hKomt er zo aan
WAARSCHUWING!

deze project is bedoeld om te gebruiken met (openroboticsplatform) 3d printed onderdelen die je kan vinden in de  github repository Link : [https://github.com/Dawsatek22/Raspberry-pi-ORB-Keyboard-Controlled-Robot.](https://github.com/Dawsatek22/Raspberry-pi-ORB-Keyboard-Controlled-Robot-NL/tree/main) parts  en de : https://openroboticplatform.com/ (je kan ook meer onderdelen toevoegen hiervan) ik raad aan om heatsink (als je dat hebt ). ik ben het best een gemilde programeur troubleshooting is niet mijn  specialiteit maar alsjeblieft
comment als je hulp nodig hebt.

kijk eerst als je het project kunt veroorloven(mijn advies).

de python code kan vreemd uitzien (zie voor jezelf ik weet niet of het de  hardware of de software is ).

           AANGERADEN VAARDIGHEDEN:  
python programming ,kennis van gebruiken VNC viewer(ik gebruik voor dit project),3d printing, bouten schroeven,solderen (voor de dc motor en mogelijk raspberry Pi Zero/ZeroW header). Installern van de robot-hat Module meer info hier : https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/index.html .

3D PRINTED ONDERDELEN NODIG:
(PLA,PETG is optional) stl/3mf files zijn in  de github link : https://github.com/Dawsatek22/Raspberry-pi-ORB-Keyboard-Controlled-Robot/tree/main/stl Or the ORB (openroboticplatform) link is here : https://openroboticplatform.com/ 1X dt22-72-d22.2to4wheelerplate.stl 1X jordan-25-Pi_Zero_Holder.3mf 1X dt22-68-batteryHolder6V-12-2X_18650.stl https://openroboticplatform.com/part:68.

          OPTIONEEL:

          2x   nikodembartnik-11-tt_motor_wheel.3mf https://openroboticplatform.com/part:11.
          2x (als je  TPU Filament hebt) Two part wheel for TT motor 65mm https://openroboticplatform.com/part:46.

     DINGEN DIE JE NODIG HEBT:
#links zijn meer voor referentie. 
1x laptop/pc (ik gebruik Ubuntu Desktop LTS om de robot te besturen)

1x 16 GB of hoger micro sd card with raspberry Pi 4/Zero W compatable os geinstalleert(op dit momment  Raspberry PI os  aangeraden).

1x SunFounder Robot HAT Expansion Board Designed for Raspberry Pi (more info here : https://www.sunfounder.com/collections/expansion-boards/products/sunfounder-robot-hat-expansion-board-designed-for-raspberry-pi). 1x Raspberry Pi 4 or Zero W(depends on holder you using). 2x Yellow tt motor dc motors https://www.amazon.com/Aoicrie-Electric-Magnetic-Engine%EF%BC%8CDIY-Vibration/dp/B083BDW3FD/ref=sr_1_5?crid=349ZR0DUA9P8&dib=eyJ2IjoiMSJ9.uG6IbMpcZ6yn_IUI48RYAwYWpvm7KXne5uj6PJtAGCt2fbDAEp_Wsaa-UFRJ-gK1DtmKW8w3-U-3ukH2teve4dWQvwHxLJe5ZPPaBvWKiJnU4_eR_cIjRO7uszjvk_RF0hfkI980S0ZdR2aoHYL43bJ8puZkgoj_cZ61hUYsOddSFvt2E2NXGUfzPq5svUwOU1kJJHFAgbHMp5ZT5eUsv9KGoHponTXKksFrB_6vTqID0nIJ2QqBv0uQrh_gKeo5Lu-eYuff4SgMcUQwoIF43vsNngYxxwhjI_AdTFaVT1w.9H6kH1E6HZsgKn-DiH0ZUh5icqpNx20WqmCNqYLPLYo&dib_tag=se&keywords=yellow+dc+motor&qid=1710238445&sprefix=yellow+dc%2Caps%2C153&sr=8-5.

2x wielen https://www.tinytronics.nl/en/mechanics-and-actuators/parts/wheels/spare-wheel-auto-kit-diy. 
2x m2.5 *10+6 afstandhouder
2x 15mm of langer female XH2.54 cable(te solderen op  yellow tt motor).

M3 moer, afstandhouder of schroevendraaier for bouten (metal ones recommended) : 
4x M2.5 6mm. 4x M3 30mm. 6x M3 12

                     OPTIONEEL:
boor met m2.5 bit (voor het geval de m2.5 gaten van de raspberry Pi4/ZeroW houder te klein is geprint). usb c kabel(om op te laden als nodig is)
