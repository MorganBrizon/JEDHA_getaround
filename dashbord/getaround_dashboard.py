import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données nettoyées
delay_data_path = "get_around_delay_analysis.xlsx"
delay_data = pd.read_excel(delay_data_path)
delay_data = delay_data[(delay_data["delay_at_checkout_in_minutes"] >= 0) & (delay_data["delay_at_checkout_in_minutes"] <= 5000)]

overlapping_rentals = delay_data.dropna(subset=["time_delta_with_previous_rental_in_minutes"])

# Titre du Dashboard
st.title("📊 Dashboard GetAround - Analyse des Retards")

# Sélection du seuil de délai minimum
delay_threshold = st.slider("Sélectionnez un délai minimum entre deux locations (minutes)", 30, 180, 60, step=30)

affected_rentals = overlapping_rentals[
    overlapping_rentals["time_delta_with_previous_rental_in_minutes"] < delay_threshold
].shape[0]

st.write(f"### 🚗 Nombre de locations affectées avec un délai de {delay_threshold} min : {affected_rentals}")

# Affichage de la distribution des retards
st.write("### Distribution des retards à la restitution")
fig, ax = plt.subplots()
ax.hist(delay_data["delay_at_checkout_in_minutes"], bins=50, edgecolor='black', alpha=0.7)
ax.set_xlabel("Retard à la restitution (minutes)")
ax.set_ylabel("Nombre de locations")
ax.set_title("Distribution des retards à la restitution")
st.pyplot(fig)

st.write("📌 Ce dashboard vous permet d'explorer l'impact des retards et de simuler un délai minimum entre les locations.")
