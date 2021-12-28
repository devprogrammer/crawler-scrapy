from api.helpers.spiders.custom.aixmarseillemetropole_spider import AixMarseilleParser
from api.helpers.spiders.custom.amiens_spider import AmiensParser
from api.helpers.spiders.custom.lille_spider import LilleSpider
from api.helpers.spiders.custom.ampmetropole_spider import AmpMetropoleSpider
from api.helpers.spiders.custom.besacon_spider import BesaconSpider
from api.helpers.spiders.custom.marseille_spider import MarseilleParser
from api.helpers.spiders.custom.cc_intercom_bernay_terres_de_normandie_spider import CCIntercomBernayTerresdeNormandieSpider
from api.helpers.spiders.custom.ca_sud_sainte_baume_spider import CASudSainteBaumeSpider
from api.helpers.spiders.custom.cc_bievre_isere_spider import CCBievreIsereSpider
from api.helpers.spiders.custom.ca_fougeres_agglomeration_spider import CAFougeresAgglomerationSpider
from api.helpers.spiders.custom.arles_spider import ArlesSpider
from api.helpers.spiders.custom.massy_spider import MassySpider
from api.helpers.spiders.custom.villeurbanne_spider import VilleurbanneSpider
from api.helpers.spiders.custom.ca_du_pays_de_montbeliard_spider import CAduPaysdeMontbeliardSpider
from api.helpers.spiders.custom.cu_du_grand_poitiers_spider import CUduGrandPoitiersSpider
from api.helpers.spiders.custom.narbonne_spider import NarbonneSpider
from api.helpers.spiders.custom.gennevilliers_spider import GennevilliersParser
from api.helpers.spiders.custom.brive_spider import BriveParser
from api.helpers.spiders.custom.brive_admin import BriveAdminParser
from api.helpers.spiders.custom.saint_spider import SaintParser
from api.helpers.spiders.custom.saint_admin import SaintAdminParser
from api.helpers.spiders.custom.vitrolles_spider import VitrollesParser
from api.helpers.spiders.custom.lesmureaux_spider import LesmureauxParser
from api.helpers.spiders.custom.lesmureaux_admin import LesmureauxAdminParser
from api.helpers.spiders.custom.ermont_spider import ErmontParser
from api.helpers.spiders.custom.ville_villiers_spider import VilleVilliersParser
from api.helpers.spiders.custom.miramas_spider import MiramasParser
from api.helpers.spiders.custom.henin_spider import HeninParser
from api.helpers.spiders.custom.lesulis_spider import LesulisParser
from api.helpers.spiders.custom.ccel_spider import CcelParser


custom_spiders = {
    "FRCOMM59350": LilleSpider,
    "FREPCI248000531": AmiensParser,
    "FRCOMM80021": AmiensParser,
    'FREPCI200054807': AixMarseilleParser,
    'FREPCI200054807': AmpMetropoleSpider,
    'FREPCI200054807': BesaconSpider,
    'FRCOMM13055': MarseilleParser,
    'FREPCI200072452': CAFougeresAgglomerationSpider,
    'FRCOMM13004': ArlesSpider,
    'FREPCI200066413': CCIntercomBernayTerresdeNormandieSpider,
    'FREPCI248300394': CASudSainteBaumeSpider,
    'FREPCI200059392': CCBievreIsereSpider,
    'FRCOMM91377': MassySpider,
    'FRCOMM69266': VilleurbanneSpider,
    'FREPCI200065647': CAduPaysdeMontbeliardSpider,
    'FREPCI200069854': CUduGrandPoitiersSpider,
    'FRCOMM11262': NarbonneSpider,
    'FRCOMM92036' : GennevilliersParser,
    'FRCOMM19031' : BriveParser,
    'FRCOMM19031_1' : BriveAdminParser,
    'FRCOMM22278' : SaintParser,
    'FRCOMM22278_1' : SaintAdminParser,
    'FRCOMM13117' : VitrollesParser,
    'FRCOMM78440' : LesmureauxParser,
    'FRCOMM78440_1' : LesmureauxAdminParser,
    'FRCOMM95219' : ErmontParser,
    'FRCOMM95680' : VilleVilliersParser,
    'FRCOMM13063' : MiramasParser,
    'FRCOMM62427' : HeninParser,
    'FRCOMM91692' : LesulisParser,
    'FREPCI246900575' : CcelParser,
}

