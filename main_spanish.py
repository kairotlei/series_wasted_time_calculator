import webbrowser
import time
import sys

time_start = float(time.time())
print("Piensa en una serie...")

seasons = int(input("¿Cuántas temporadas tiene? "))
chapters = int(input("¿Cuántos capítulos hay en cada temporada? "))
mins_per_ch = int(input("¿Cuántos minutos dura, en total y sin decimales, cada capitulo? "))
previously_duration = int(input("¿Duración, en segundos y sin decimales, del 'anteriormente...' antes de cada capítulo? "))
intro_duration = int(input("¿Duración, en segundos, de la intro de cada capítulo? "))
credits_length = int(input("¿Cuánto duran los créditos finales? "))
series_name = str(input("Ah, ¿y cómo se llama la serie? "))
times_watched = int(input("Por último ¿cuántas veces has visto la serie? "))

wasted_time_hrs = round(float((mins_per_ch * chapters * seasons * times_watched) / 60), 2)
save_previous_mins = round(float(((previously_duration * chapters * seasons * times_watched) / 60)), 2)
save_intro_mins = round(float(((intro_duration * chapters * seasons * times_watched) / 60)), 2)
save_outro_mins = round(float(((credits_length * chapters * seasons * times_watched) / 60)), 2)
total_cha = round(int(seasons * chapters), 2)
total_savings = round(int(save_intro_mins + save_outro_mins + save_outro_mins), 2)
good_series_hrs = round(int((save_intro_mins + save_outro_mins + save_outro_mins) / wasted_time_hrs), 2)

if times_watched == 1:
   times_watched = str("una vez")
else:
   times_watched = str(f"{times_watched} veces")

print(f"""
¡Felicidades, al ver la serie '{series_name}' de principio a fin {times_watched} habrías perdido {wasted_time_hrs} horas de tu vida distribuídas en {seasons} temporadas con un total de {total_cha} capítulos!
Si te va el tacañismo, puedes ahorrarte {save_previous_mins} minutos saltándote el resumen de lo ocurrido anteriormente.
Y si te saltaras la misma intro de cada capítulo recuperarías {save_intro_mins} minutos de tu vida.
También podrías rescatar otros {save_outro_mins} minutos si ignoraras la palabrería que sale al final de cada capítulo.

En conclusión:
- Ver '{series_name}' {times_watched} te costará {wasted_time_hrs} horas de tu vida.
- Podrías recuperar {total_savings} minutos ignorando florituras.
- El {good_series_hrs}% de '{series_name}' es tiempo tirado a la basura (contenido no relevante en relación a contenido total)
""")
time_end = float(time.time())
time_final = round(float(time_end - time_start), 2) 
print(f"Por cierto, al hacer este test has perdido unos preciosos {time_final} segundos de tu vida.")


kill = str(input("""
Para, opcionalmente, compartir el resultado en Twitter, introduce T.
Introduce cualquier otra cosa para finalizar el programa."""))
# Abre una ventana de Twitter en donde poder tweetear y comentar el resultado
if kill.lower() == "t":
    webbrowser.open(f"""https://twitter.com/intent/tweet?text=Hey, si viera la serie '{series_name}' {times_watched} completamente, perderia {wasted_time_hrs} horas de mi vida en ella. Ignorando florituras podría recuperar {total_savings} minutos! ¡¡Y he desperdiciado {time_final} segundos en este test!!""")
else:
    sys.exit()
