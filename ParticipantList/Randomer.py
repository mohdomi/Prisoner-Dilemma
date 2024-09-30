# Gives Random Output Always(Builton random inbuilt function of python.)
def randomer():
    import random
    Options = ["cooperate", "defect"]

    random.shuffle(Options)
    return Options[0]


    


if __name__=="__main__":
    print(randomer())