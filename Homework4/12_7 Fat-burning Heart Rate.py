#Kaitlyn Sourignosack
#1824497

def get_age():

    age = int(input())

    if age not in range (18,76):
        raise ValueError ('Invalid Age.')
    else:
        return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        print ('Fat burning heart rate for a',age, 'year-old:',round (fat_burning_heart_rate(age),2),'bpm')

    except:
        print ('Invalid age.\nCould not calculate heart rate info.''\n')

