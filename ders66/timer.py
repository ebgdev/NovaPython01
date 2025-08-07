# import time

# orgiginalTime = int(input("Enter duration for count down timer: "))
# print("\nCount Down Starting...")

# for duration in range(orgiginalTime,0,-1):
#     mins, seconds = (duration//60) , (duration%60)
#     print(f"\r{mins:02d}:{seconds:02d}", end='',flush=True)
#     time.sleep(1)

# print("\rTime is over.      ")  # overwrites the timer display

# ----------------------

# import time

# secondCounter = 20

# print("Countdown time is starting now!")
# for remaining in range(secondCounter, 0, -1):
#     tmin, tsec = divmod(remaining, 60)
#     print(f"\r{tmin:02d}:{tsec:02d}", end='',flush=True)
#     time.sleep(1)

# print("\rTime is over.      ")  # overwrites the timer display



# ----------------------


# import time

# secondCounter = 20  # Total countdown time in seconds
# bar_length = 30     # Length of the progress bar

# print("Countdown starting now!")

# for remaining in range(secondCounter, 0, -1):
#     tmin, tsec = divmod(remaining, 60)
    
#     # Calculate progress
#     elapsed = secondCounter - remaining
#     progress = int((elapsed / secondCounter) * bar_length)
#     bar = '#' * progress + '-' * (bar_length - progress)

#     # Print timer and progress bar on the same line
#     print(f"\r{tmin:02d}:{tsec:02d} |{bar}|", end='', flush=True)
#     time.sleep(1)

# # Final bar when time is over
# print(f"\r00:00 |{'#' * bar_length}| Time is over.     ")


# ----------------------


# import time

# secondCounter = 20  # total countdown duration in seconds
# bar_length = secondCounter  # bar will be exactly 20 characters long

# print("Countdown starting now!")

# for remaining in range(secondCounter, 0, -1):
#     tmin, tsec = divmod(remaining, 60)
    
#     # Calculate elapsed time and progress
#     elapsed = secondCounter - remaining
#     progress = int((elapsed / secondCounter) * bar_length)
#     bar = '#' * progress + '-' * (bar_length - progress)

#     # Print timer and bar on same line
#     print(f"\r{tmin:02d}:{tsec:02d} |{bar}|", end='', flush=True)
#     time.sleep(1)

# # Final display
# print(f"\r00:00 |{'#' * bar_length}| Time is over.     ")


