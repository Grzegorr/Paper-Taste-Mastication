import time

#Load in repository of mixing moves
import CookingMoves.MixingMoves as MIX

#Load a script containing various ways to sample the salinity
import CookingMoves.SalinitySamplingMoves as SALINITY_SAMPLING

#Load a script containing various ways to sample the salinity
import CookingMoves.CameraControl as CAM

#Functions to save data
import DataHandling.SavingExperimentData as DATA


def test_mix_picture_measure(robot, SALT):

    MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
    salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=1)
    img = CAM.returnPanPicture(robot)
    DATA.nextEntrySave("Test2", 0, img, salt_data, "Hope it works!")

def first_actual_mixing(robot, SALT):
    n = 20  #no. of measurements
    m = 2   #mixes between measurement
    k = 1   #no. of attempts

    for attempt in range(k):
        for measurement in range(n):
            for mix in range(m):
                MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
            salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=1)
            img = CAM.returnPanPicture(robot)
            DATA.nextEntrySave("First_Actual_Mixing", attempt, img, salt_data, "Two zigzag mixes between any next measurement")

def first_egg_mixing(robot, SALT):
    n = 50  #no. of measurements
    m = 2   #mixes between measurement
    k = 2   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("First_Egg_Mixing", k, img, salt_data, "Two zigzag mixes between any next measurement, 6 Eggs")

def eggs_with_shakeoff(robot, SALT):
    n = 15  #no. of measurements
    m = 2   #mixes between measurement
    k = 1   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        salt_data = SALINITY_SAMPLING.mass_salinity_test_shakeoff(robot, SALT, r=0.08, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("Eggs_With_Shakeoff", k, img, salt_data, "Two zigzag mixes between any next measurement, 4 Eggs")

def eggs_with_brush(robot, SALT):
    n = 15  #no. of measurements
    m = 2   #mixes between measurement
    k = 1   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        time.sleep(5)
        salt_data = SALINITY_SAMPLING.mass_salinity_test_brush(robot, SALT, r=0.08, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("Eggs_With_Brush", k, img, salt_data, "Two zigzag mixes between any next measurement, 4 Eggs")


#This is just a variation of "eggs with brush", just the eggs are in room emperature at the start
def eggs_with_brush_room_temp(robot, SALT):
    n = 15  #no. of measurements
    m = 3   #mixes between measurement
    k = 1   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        time.sleep(5)
        salt_data = SALINITY_SAMPLING.mass_salinity_test_brush(robot, SALT, r=0.1, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("Eggs_With_Brush_room_temp", k, img, salt_data, "Three zigzag mixes between any next measurement, 4 Eggs, room temperature")

def brush_new_pan(robot, SALT):
    n = 15  #no. of measurements
    m = 5   #mixes between measurement
    k = 2   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        time.sleep(5)
        salt_data = SALINITY_SAMPLING.mass_salinity_test_brush(robot, SALT, r=0.1, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("Brush_New_Egg", k, img, salt_data, "Three zigzag mixes between any next measurement, 4 Eggs, room temperature. New pan used.")