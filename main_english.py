import webbrowser
import time
import sys

time_start = float(time.time())
print("Clear your mind and think on a series...")

seasons = int(input("How many seasons does it have? "))
chapters = int(input("How many chapters does a season have? "))
mins_per_ch = int(input("How long is every chapter (in minutes)? "))
previously_duration = int(input("How long is the 'previously...' when a chapter starts (in seconds)? "))
intro_duration = int(input("How long is the series intro just before the chapter starts (in seconds)? "))
credits_length = int(input("How long are the final credits (in seconds)? "))
series_name = str(input("Oh, what is the series name? "))
times_watched = int(input("Last question: how many times did you watch the series? "))

wasted_time_hrs = round(float((mins_per_ch * chapters * seasons * times_watched) / 60), 2)
save_previous_mins = round(float(((previously_duration * chapters * seasons * times_watched) / 60)), 2)
save_intro_mins = round(float(((intro_duration * chapters * seasons * times_watched) / 60)), 2)
save_outro_mins = round(float(((credits_length * chapters * seasons * times_watched) / 60)), 2)
total_cha = round(int(seasons * chapters), 2)
total_savings = round(int(save_intro_mins + save_outro_mins + save_outro_mins), 2)
good_series_hrs = round(int((save_intro_mins + save_outro_mins + save_outro_mins) / wasted_time_hrs), 2)

if times_watched == 1:
   times_watched = str("once")
else:
   times_watched = str(f"{times_watched} times")

print(f"""
Congratulations, watching '{series_name}' completely {times_watched} you would waste {wasted_time_hrs} hours of your life, distributed in {seasons} seasons with a total of {total_cha} chapters!
Are you miserly? You can save {save_previous_mins} minutes skipping the 'previously...' summary when a chapter starts.
If you skip the intro of every chapter, you would recover another {save_intro_mins} minutes of you life time.
You could also save {save_outro_mins} minutes if you don't stare at the ending credits.

So, in conclusion:
- Watching '{series_name}' {times_watched} would cost you {wasted_time_hrs} irrecoverable hours of you life.
- Ignoring flourishes (summary, intro, credits) saves you {total_savings} minutes.
- The {good_series_hrs}% of '{series_name}' is worthless time (% is flourishes time / all series time)
""")
time_end = float(time.time())
time_final = round(float(time_end - time_start), 2) 
print(f"Also, did you notice that you just wasted another {time_final} seconds while doing this test?.")

kill = str(input("""To optinally share result on Twitter, enter T.
Enter any other key to finalize this program."""))
# Opens a Twitter window where you can tweet and comment you result.
if kill.lower() == "t":
    webbrowser.open(f"""https://twitter.com/intent/tweet?text=Hey, if I completely watch the '{series_name}' series {times_watched}, I would waste {wasted_time_hrs} hours of my life into it. Ignoring flourishes I could recover {total_savings} minutes! And I also wasted {time_final} seconds while discovering this!!""")
else:
    sys.exit()
