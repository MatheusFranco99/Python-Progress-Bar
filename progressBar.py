import math
import colorama



# this program is based on https://www.youtube.com/watch?v=x1eaT88vJUA

def progress_bar(progress, total, color = colorama.Fore.YELLOW):
    percent = int(100*(progress / float(total)))
    bar = chr(9608) * percent + '-' * (100-percent)
    if (progress == total):
        color = colorama.Fore.GREEN
    print(color + f"\r|{bar}| {percent:.2f}%", end='\r')


def main1():
    numbers = [x * 5 for x in range(0,4000,5)]
    results = []

    progress_bar(0,len(numbers))
    for i,x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i+1,len(numbers))
    print(colorama.Fore.RESET)






if __name__ == "__main__":
    main1()