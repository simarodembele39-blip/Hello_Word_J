import matplotlib.pyplot as plt 
### Données standar de l'ensoleillement et de la température pour l'année 2025
# Irradiation solaire en (kWh/m²/j)
Mois=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Decembre']
Irradiation_globale=[5.25,5.91,6.51,6.75,6.67,5.9,5.28,5.19,5.35,5.45,5.42,5.11] 
# Température en °C
Temperature=[25.3,27.6,30.2,32.6,32.6,28.5,25.6,25.3,25.8,27.6,28.6,26.1]
### Tracé de la courbe
plt.ylim(0, 40)
plt.plot(Mois,Temperature,marker='o',label="Température(°C)")
plt.xlabel('Mois')
plt.ylabel('Température(°C)')
plt.title('Température quotidienne de la zone de Manantali pour l\'année 2025')
plt.legend()
plt.grid() 
for i in range(len(Mois)):
    plt.text(Mois[i],Temperature[i], str(Temperature[i]),ha='left',va='top',bbox=dict(facecolor='white'))
plt.show()
