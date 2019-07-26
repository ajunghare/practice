import enum
from sqlalchemy.types import Enum, Date

#marriage
class EnumGan(enum.Enum):
    Dev = 1
    Manushya = 2
    Rakshas = 3

class EnumNakshtra(enum.Enum):
    Ashwini = 1
    Adra = 2
    Anuradha = 3
    Bharani = 4
    Chitra = 5
    Dhanishta = 6
    Hasta = 7
    Jyeshta = 8
    Krittika = 9
    Moola = 10
    Magha = 11
    Mrigasira = 12
    Pushya = 13
    PurvaPhalguni = 14
    PurvaBharda = 15
    PurvaShadha = 16
    Punarvasu = 17
    Rohini = 18
    Swati = 19
    Revati = 20
    Shattarka = 21
    Shravan = 22
    UttaraPhalguni = 23
    UttaraBhadra = 24
    UttaraShadha = 25
    Vishakha = 26

class EnumCharan(enum.Enum):
    First = 1
    Second = 2
    Third = 3
    Fourth = 4

class EnumNadi(enum.Enum):
    Adhya = 1
    Madhya = 2
    Antya = 3

class EnumMangal(enum.Enum):
    Yes = 1
    No = 2
    Saumya = 3
    dont_care = 4

class EnumMaritialStatus(enum.Enum):
    Unmarried = 1
    Divorcee = 2
    Widower = 3

class EnumRashi(enum.Enum):
    Mesh = 1
    Vrushabh = 2
    Mithun = 3
    Kark = 4
    Sinha = 5
    Kanya = 6
    Tula = 7
    Vrishchik = 8
    Dhanu = 9
    Makar = 10
    Kumbh = 11
    Meen = 12

#personal

class EnumDiet(enum.Enum):
    veg = 1
    nonveg = 2

class EnumCaste(enum.Enum):
    Maratha_96K = 1
    Maratha_Deshmukh = 2
    Maratha = 3
    Kunbi = 4
    Tirale_Kunbi = 5
    other = 6

class EnumBloodGroup(enum.Enum):
    A_positive = 1
    B_positive = 2
    AB_positive = 3
    O_positive = 4
    A_negative = 5
    B_negative = 6
    AB_negative = 7
    O_negative = 8

class EnumComplexion(enum.Enum):
    Fair = 1
    Nimgora = 2
    Wheatish = 3
    Dark = 4
