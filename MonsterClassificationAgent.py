class MonsterClassificationAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):


        negative_samples = {
            "size": [],
            "color": [],
            "covering": [],
            "foot-type": [],
            "leg-count": [],
            "arm-count": [],
            "eye-count": [],
            "horn-count": [],
            "lays-eggs": [],
            "has-wings": [],
            "has-gills": [],
            "has-tail": []
        }

        positive_samples = {
            "size": [],
            "color": [],
            "covering": [],
            "foot-type": [],
            "leg-count": [],
            "arm-count": [],
            "eye-count": [],
            "horn-count": [],
            "lays-eggs": [],
            "has-wings": [],
            "has-gills": [],
            "has-tail": []
        }

        #monster fict, is positive example
        for mon_dict, pos in samples:
            if pos is True:
                #import pdb; pdb.set_trace()
                for key, value in mon_dict.items():
                    curr_list = positive_samples.get(key)
                    if value not in curr_list:
                        #this list?
                        positive_samples[key].append(value)
        print(positive_samples)
        counter = 0
        for key in new_monster:
            if new_monster.get(key) in positive_samples.get(key):
                counter = counter + 1
        if counter >= 9:
            return True
        else:
            return False